#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import struct
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from sprite_catalog import ObjectSpriteCatalog
from script_catalog import ScriptCatalog

ROM_BASE = 0x08000000
HEADER_SIZE = 0x1C
LAYOUT_SIZE = 0x18
TILESET_SIZE = 0x18
PRIMARY_PALETTE_BANKS = 6
SECONDARY_PALETTE_BANKS = 7
PRIMARY_TILE_FALLBACK = 512
SECONDARY_TILE_FALLBACK = 512
MAX_DIMENSION = 512

# Friendly names for the first outdoors group, matching vanilla Emerald.
# Other groups fall back to Bank.Map labels unless an external names JSON is supplied.
GROUP0_NAMES = [
    "PetalburgCity", "SlateportCity", "MauvilleCity", "RustboroCity", "FortreeCity",
    "LilycoveCity", "MossdeepCity", "SootopolisCity", "EverGrandeCity", "LittlerootTown",
    "OldaleTown", "DewfordTown", "LavaridgeTown", "FallarborTown", "VerdanturfTown",
    "PacifidlogTown", "Route101", "Route102", "Route103", "Route104", "Route105",
    "Route106", "Route107", "Route108", "Route109", "Route110", "Route111", "Route112",
    "Route113", "Route114", "Route115", "Route116", "Route117", "Route118", "Route119",
    "Route120", "Route121", "Route122", "Route123", "Route124", "Route125", "Route126",
    "Route127", "Route128", "Route129", "Route130", "Route131", "Route132", "Route133",
    "Route134", "Underwater_Route124", "Underwater_Route126", "Underwater_Route127",
    "Underwater_Route128", "Underwater_Route129", "Underwater_Route105", "Underwater_Route125",
]

GROUP_LABELS = [
    "TownsAndRoutes", "IndoorLittleroot", "IndoorOldale", "IndoorDewford", "IndoorLavaridge",
    "IndoorFallarbor", "IndoorVerdanturf", "IndoorPacifidlog", "IndoorPetalburg", "IndoorSlateport",
    "IndoorMauville", "IndoorRustboro", "IndoorFortree", "IndoorLilycove", "IndoorMossdeep",
    "IndoorSootopolis", "IndoorEverGrande", "IndoorRoute104", "IndoorRoute111", "IndoorRoute112",
    "IndoorRoute114", "IndoorRoute116", "IndoorRoute117", "IndoorRoute121", "Dungeons",
    "IndoorDynamic", "SpecialArea", "IndoorRoute104Prototype", "IndoorRoute109", "IndoorRoute110",
    "IndoorRoute113", "IndoorRoute123", "IndoorRoute119", "IndoorRoute124",
]

# Gen III English character mapping used by map/location names in Emerald-derived ROMs.
_GEN3_TEXT = {0x00: " "}
for _i, _c in enumerate("0123456789"):
    _GEN3_TEXT[0xA1 + _i] = _c
_GEN3_TEXT.update({
    0xAB: "!", 0xAC: "?", 0xAD: ".", 0xAE: "-", 0xAF: "·", 0xB0: "…",
    0xB1: "“", 0xB2: "”", 0xB3: "‘", 0xB4: "’", 0xB5: "♂", 0xB6: "♀",
    0xB7: "¥", 0xB8: ",", 0xB9: "×", 0xBA: "/", 0xF0: ":",
})
for _i, _c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    _GEN3_TEXT[0xBB + _i] = _c
for _i, _c in enumerate("abcdefghijklmnopqrstuvwxyz"):
    _GEN3_TEXT[0xD5 + _i] = _c


def u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]


def u16(data: bytes, off: int) -> int:
    return struct.unpack_from("<H", data, off)[0]


def gba_to_offset(ptr: int, rom_size: int) -> Optional[int]:
    if ROM_BASE <= ptr < ROM_BASE + rom_size:
        return ptr - ROM_BASE
    return None


def offset_to_gba(off: int) -> int:
    return ROM_BASE + off


def sanitize_name(name: str) -> str:
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip())
    return name.strip("_") or "map"


def ptr_hex(off: Optional[int]) -> Optional[str]:
    return None if off is None else f"0x{offset_to_gba(off):08X}"


@dataclass
class TilesetInfo:
    offset: int
    is_compressed: int
    is_secondary: int
    tiles_offset: int
    palettes_offset: int
    metatiles_offset: int
    attributes_offset: int
    callback_raw: int

    @property
    def gba(self) -> int:
        return offset_to_gba(self.offset)


@dataclass
class LayoutInfo:
    offset: int
    width: int
    height: int
    border_offset: int
    blockdata_offset: int
    primary_tileset_offset: int
    secondary_tileset_offset: int

    @property
    def gba(self) -> int:
        return offset_to_gba(self.offset)


@dataclass
class MapInfo:
    group: int
    number: int
    name: str
    header_offset: int
    layout_offset: int
    width: int
    height: int
    primary_tileset_offset: int
    secondary_tileset_offset: int
    region_map_section_id: int
    map_type: int
    weather: int
    music: int
    layout_id: int

    @property
    def id(self) -> str:
        return f"{self.group}.{self.number}"


class RomScanner:
    def __init__(self, path: Path, names_path: Optional[Path] = None):
        self.path = Path(path)
        self.data = self.path.read_bytes()
        self.size = len(self.data)
        if self.size < 0xC0:
            raise ValueError("File is too small to be a GBA ROM")
        self.game_code = self.data[0xAC:0xB0].decode("ascii", "replace")
        self.title = self.data[0xA0:0xAC].rstrip(b"\0").decode("ascii", "replace")
        self.sha256 = hashlib.sha256(self.data).hexdigest()
        self._tileset_cache: Dict[int, Optional[TilesetInfo]] = {}
        self._layout_cache: Dict[int, Optional[LayoutInfo]] = {}
        self._header_cache: Dict[int, Optional[dict]] = {}
        self.external_names: Dict[Tuple[int, int], str] = {}
        self.names = self._load_names(names_path)
        self.map_pointer_run: Optional[Tuple[int, int, int]] = None
        self.master_table_offset: Optional[int] = None
        self.group_starts: List[int] = []
        self.group_counts: List[int] = []
        self.maps: List[MapInfo] = []
        self.map_index: Dict[Tuple[int, int], MapInfo] = {}
        self.region_map_table_offset: Optional[int] = None
        self.region_map_names: Dict[int, str] = {}

    def _load_names(self, names_path: Optional[Path]) -> Dict[Tuple[int, int], str]:
        names: Dict[Tuple[int, int], str] = {}
        for i, name in enumerate(GROUP0_NAMES):
            names[(0, i)] = name
        if not names_path:
            return names
        obj = json.loads(Path(names_path).read_text(encoding="utf-8"))
        if "group_order" in obj:
            order = obj["group_order"]
            for g, key in enumerate(order):
                for m, name in enumerate(obj.get(key, [])):
                    names[(g, m)] = name
                    self.external_names[(g, m)] = name
        else:
            for key, value in obj.items():
                m = re.fullmatch(r"(\d+)\.(\d+)", str(key))
                if m:
                    key_tuple = (int(m.group(1)), int(m.group(2)))
                    names[key_tuple] = str(value)
                    self.external_names[key_tuple] = str(value)
        return names

    def decode_gen3_text(self, off: int, max_len: int = 48) -> Optional[str]:
        if off < 0 or off >= self.size:
            return None
        chars: List[str] = []
        for i in range(max_len):
            pos = off + i
            if pos >= self.size:
                return None
            b = self.data[pos]
            if b == 0xFF:
                text = "".join(chars).strip()
                return text if text else None
            ch = _GEN3_TEXT.get(b)
            if ch is None:
                # Location names should be simple display text. Reject control-code
                # streams so random ROM pointers do not masquerade as names.
                return None
            chars.append(ch)
        return None

    def _parse_region_entry(self, off: int) -> Optional[Tuple[str, Tuple[int, int, int, int]]]:
        if off < 0 or off + 8 > self.size:
            return None
        name_off = gba_to_offset(u32(self.data, off), self.size)
        if name_off is None:
            return None
        text = self.decode_gen3_text(int(name_off))
        if not text or len(text) < 2:
            return None
        x, y, width, height = self.data[off + 4:off + 8]
        # Region-map entries are normally tiny rectangles. Keep this permissive
        # enough for hacks while rejecting arbitrary pointer tables.
        if width == 0 or height == 0 or width > 32 or height > 32:
            return None
        return text, (x, y, width, height)

    def discover_region_map_names(self, max_section_id: int) -> Dict[int, str]:
        if max_section_id < 0:
            return {}

        # Find plausible RegionMapLocation records: name pointer followed by
        # x/y/width/height. Candidate table starts are scored across every map
        # section id actually needed by this ROM. This avoids hardcoding the
        # vanilla table address and works when hacks relocate or extend it.
        plausible: List[int] = []
        for off in range(0, self.size - 7, 4):
            if self._parse_region_entry(off) is not None:
                plausible.append(off)
        plausible_set = set(plausible)
        starts = [off for off in plausible if (off - 8) not in plausible_set]

        best_base: Optional[int] = None
        best_score = -1
        best_names: Dict[int, str] = {}
        for base in starts:
            # A real table should resolve a large fraction of 0..max_section_id.
            # Random candidate runs collapse quickly under this scoring pass.
            names: Dict[int, str] = {}
            score = 0
            for section_id in range(max_section_id + 1):
                parsed = self._parse_region_entry(base + section_id * 8)
                if parsed is not None:
                    names[section_id] = parsed[0]
                    score += 1
            if score > best_score:
                best_score = score
                best_base = base
                best_names = names

        minimum = max(16, int((max_section_id + 1) * 0.55))
        if best_base is None or best_score < minimum:
            return {}
        self.region_map_table_offset = best_base
        self.region_map_names = best_names
        return best_names

    def parse_tileset(self, off: int) -> Optional[TilesetInfo]:
        if off in self._tileset_cache:
            return self._tileset_cache[off]
        if off < 0 or off + TILESET_SIZE > self.size:
            self._tileset_cache[off] = None
            return None
        comp = self.data[off]
        secondary = self.data[off + 1]
        if comp not in (0, 1) or secondary not in (0, 1):
            self._tileset_cache[off] = None
            return None
        vals = struct.unpack_from("<5I", self.data, off + 4)
        ptrs = [gba_to_offset(v, self.size) if v else None for v in vals]
        if any(v is None for v in ptrs[:4]):
            self._tileset_cache[off] = None
            return None
        callback_raw = vals[4]
        if callback_raw:
            cb_base = callback_raw & ~1
            if not (ROM_BASE <= cb_base < ROM_BASE + self.size):
                self._tileset_cache[off] = None
                return None
        out = TilesetInfo(
            offset=off,
            is_compressed=comp,
            is_secondary=secondary,
            tiles_offset=int(ptrs[0]),
            palettes_offset=int(ptrs[1]),
            metatiles_offset=int(ptrs[2]),
            attributes_offset=int(ptrs[3]),
            callback_raw=callback_raw,
        )
        self._tileset_cache[off] = out
        return out

    def parse_layout(self, off: int) -> Optional[LayoutInfo]:
        if off in self._layout_cache:
            return self._layout_cache[off]
        if off < 0 or off + LAYOUT_SIZE > self.size:
            self._layout_cache[off] = None
            return None
        width, height, border_ptr, map_ptr, primary_ptr, secondary_ptr = struct.unpack_from("<6I", self.data, off)
        if not (1 <= width <= MAX_DIMENSION and 1 <= height <= MAX_DIMENSION):
            self._layout_cache[off] = None
            return None
        border_off = gba_to_offset(border_ptr, self.size)
        map_off = gba_to_offset(map_ptr, self.size)
        primary_off = gba_to_offset(primary_ptr, self.size)
        secondary_off = gba_to_offset(secondary_ptr, self.size)
        if None in (border_off, map_off, primary_off, secondary_off):
            self._layout_cache[off] = None
            return None
        if int(map_off) + width * height * 2 > self.size:
            self._layout_cache[off] = None
            return None
        if not self.parse_tileset(int(primary_off)) or not self.parse_tileset(int(secondary_off)):
            self._layout_cache[off] = None
            return None
        out = LayoutInfo(
            offset=off,
            width=width,
            height=height,
            border_offset=int(border_off),
            blockdata_offset=int(map_off),
            primary_tileset_offset=int(primary_off),
            secondary_tileset_offset=int(secondary_off),
        )
        self._layout_cache[off] = out
        return out

    def parse_header(self, off: int) -> Optional[dict]:
        if off in self._header_cache:
            return self._header_cache[off]
        if off < 0 or off + HEADER_SIZE > self.size:
            self._header_cache[off] = None
            return None
        layout_ptr, events_ptr, scripts_ptr, connections_ptr = struct.unpack_from("<4I", self.data, off)
        layout_off = gba_to_offset(layout_ptr, self.size)
        if layout_off is None:
            self._header_cache[off] = None
            return None
        layout = self.parse_layout(layout_off)
        if layout is None:
            self._header_cache[off] = None
            return None
        for ptr in (events_ptr, scripts_ptr, connections_ptr):
            if ptr and gba_to_offset(ptr, self.size) is None:
                self._header_cache[off] = None
                return None
        music = u16(self.data, off + 16)
        layout_id = u16(self.data, off + 18)
        region_map_section_id = self.data[off + 20]
        cave = self.data[off + 21]
        weather = self.data[off + 22]
        map_type = self.data[off + 23]
        flags = self.data[off + 26]
        battle_type = self.data[off + 27]
        out = {
            "offset": off,
            "layout": layout,
            "events_offset": gba_to_offset(events_ptr, self.size) if events_ptr else None,
            "scripts_offset": gba_to_offset(scripts_ptr, self.size) if scripts_ptr else None,
            "connections_offset": gba_to_offset(connections_ptr, self.size) if connections_ptr else None,
            "music": music,
            "layout_id": layout_id,
            "region_map_section_id": region_map_section_id,
            "cave": cave,
            "weather": weather,
            "map_type": map_type,
            "allow_cycling": bool(flags & 0x01),
            "allow_escaping": bool(flags & 0x02),
            "allow_running": bool(flags & 0x04),
            "show_map_name": bool((flags >> 3) & 0x1F),
            "battle_type": battle_type,
        }
        self._header_cache[off] = out
        return out

    @staticmethod
    def _contiguous_runs(values: List[int]) -> List[Tuple[int, int, int]]:
        if not values:
            return []
        values = sorted(set(values))
        runs: List[Tuple[int, int, int]] = []
        start = prev = values[0]
        for v in values[1:]:
            if v == prev + 4:
                prev = v
            else:
                runs.append((start, prev, (prev - start) // 4 + 1))
                start = prev = v
        runs.append((start, prev, (prev - start) // 4 + 1))
        return runs

    def discover(self) -> List[MapInfo]:
        # Scan aligned words for ROM pointers. For each pointer target, test whether it is a plausible MapHeader.
        header_pointer_sources: List[int] = []
        for src in range(0, self.size - 3, 4):
            ptr = u32(self.data, src)
            target = gba_to_offset(ptr, self.size)
            if target is None:
                continue
            if self.parse_header(target) is not None:
                header_pointer_sources.append(src)

        runs = self._contiguous_runs(header_pointer_sources)
        if not runs:
            raise RuntimeError("Could not discover a contiguous map-header pointer table")
        # The real gMapGroups child arrays form the longest contiguous run in tested Emerald-derived ROMs.
        run_start, run_end, run_count = max(runs, key=lambda r: r[2])
        if run_count < 50:
            raise RuntimeError(f"Best map-header pointer run is too small ({run_count} entries)")
        self.map_pointer_run = (run_start, run_end, run_count)

        # Locate the master group table: a contiguous sequence of pointers into the child pointer run.
        min_ptr = offset_to_gba(run_start)
        max_ptr = offset_to_gba(run_end)
        master_sources: List[int] = []
        for src in range(0, self.size - 3, 4):
            ptr = u32(self.data, src)
            if min_ptr <= ptr <= max_ptr and (ptr - min_ptr) % 4 == 0:
                master_sources.append(src)
        master_runs = self._contiguous_runs(master_sources)
        master_runs = [r for r in master_runs if 2 <= r[2] <= 256]
        if not master_runs:
            raise RuntimeError("Could not discover the master map-group pointer table")

        # Emerald has 34 vanilla groups, but hacks may append additional group arrays
        # elsewhere in the ROM.  Use the vanilla-shaped run only as an anchor, then
        # extend the master table while following entries continue to point to valid
        # arrays of MapHeader pointers.  This is important for hacks such as Hyper
        # Emerald, whose groups 34-37 are relocated far away from the vanilla child
        # pointer run.
        exact = [r for r in master_runs if r[2] == 34]
        mstart, mend, mcount = (exact[0] if exact else max(master_runs, key=lambda r: r[2]))
        self.master_table_offset = mstart

        def scan_group_count(start: int, cap: int = 1024) -> int:
            count = 0
            for n in range(cap):
                pos = start + n * 4
                if pos < 0 or pos + 4 > self.size:
                    break
                header_off = gba_to_offset(u32(self.data, pos), self.size)
                if header_off is None or self.parse_header(header_off) is None:
                    break
                count += 1
            return count

        # Extend beyond the anchor run.  A candidate group pointer is accepted only
        # if it leads to at least one consecutively-valid MapHeader pointer.
        group_starts: List[int] = []
        for i in range(mcount):
            target = gba_to_offset(u32(self.data, mstart + i * 4), self.size)
            if target is None:
                raise RuntimeError("Master map-group table contains invalid pointers")
            group_starts.append(int(target))

        for i in range(mcount, 256):
            pos = mstart + i * 4
            if pos + 4 > self.size:
                break
            target = gba_to_offset(u32(self.data, pos), self.size)
            if target is None or target % 4 != 0:
                break
            if scan_group_count(int(target)) < 1:
                break
            group_starts.append(int(target))

        self.group_starts = group_starts

        # For vanilla groups the next child-array pointer usually gives an exact
        # byte span.  Relocated/extended groups may be non-monotonic or separated by
        # unrelated ROM data, so validate the inferred span and otherwise scan until
        # the first non-MapHeader pointer.
        self.group_counts = []
        for i, start in enumerate(self.group_starts):
            count = 0
            if i + 1 < len(self.group_starts):
                end = self.group_starts[i + 1]
                diff = end - start
                if 0 < diff <= 0x4000 and diff % 4 == 0:
                    candidate = diff // 4
                    if candidate <= 1024:
                        valid = True
                        for n in range(candidate):
                            header_off = gba_to_offset(u32(self.data, start + n * 4), self.size)
                            if header_off is None or self.parse_header(header_off) is None:
                                valid = False
                                break
                        if valid:
                            count = candidate
            if count == 0:
                count = scan_group_count(start)
            if count < 1:
                raise RuntimeError(f"Could not determine map count for group {i}")
            self.group_counts.append(count)

        pending: List[Tuple[int, int, int, dict, LayoutInfo]] = []
        max_section_id = -1
        for group, (start, count) in enumerate(zip(self.group_starts, self.group_counts)):
            for number in range(count):
                ptr = u32(self.data, start + number * 4)
                header_off = gba_to_offset(ptr, self.size)
                if header_off is None:
                    continue
                header = self.parse_header(header_off)
                if not header:
                    continue
                layout: LayoutInfo = header["layout"]
                max_section_id = max(max_section_id, header["region_map_section_id"])
                pending.append((group, number, header_off, header, layout))

        region_names = self.discover_region_map_names(max_section_id)

        maps: List[MapInfo] = []
        for group, number, header_off, header, layout in pending:
            # Explicit --names metadata wins. Otherwise use the same ROM-resident
            # RegionMapSection display name that Advance Map can resolve. Legacy
            # group-0 names remain a final fallback if no table can be found.
            explicit = self.external_names.get((group, number))
            region_name = region_names.get(header["region_map_section_id"])
            if explicit:
                name = explicit
            elif region_name:
                name = region_name
            else:
                name = self.names.get((group, number), f"Map_{group:02d}_{number:02d}")
            maps.append(MapInfo(
                group=group,
                number=number,
                name=name,
                header_offset=header_off,
                layout_offset=layout.offset,
                width=layout.width,
                height=layout.height,
                primary_tileset_offset=layout.primary_tileset_offset,
                secondary_tileset_offset=layout.secondary_tileset_offset,
                region_map_section_id=header["region_map_section_id"],
                map_type=header["map_type"],
                weather=header["weather"],
                music=header["music"],
                layout_id=header["layout_id"],
            ))
        self.maps = maps
        self.map_index = {(m.group, m.number): m for m in maps}
        return maps

    def parse_connections(self, header_off: int) -> List[dict]:
        header = self.parse_header(header_off)
        if not header or header.get("connections_offset") is None:
            return []
        off = int(header["connections_offset"])
        if off < 0 or off + 8 > self.size:
            return []
        count, list_ptr = struct.unpack_from("<iI", self.data, off)
        list_off = gba_to_offset(list_ptr, self.size) if list_ptr else None
        if count <= 0:
            return []
        if count > 128 or list_off is None:
            return []
        direction_names = {1: "down", 2: "up", 3: "left", 4: "right", 5: "dive", 6: "emerge"}
        out: List[dict] = []
        for i in range(count):
            rec = int(list_off) + i * 12
            if rec < 0 or rec + 12 > self.size:
                break
            direction = self.data[rec]
            offset = struct.unpack_from("<i", self.data, rec + 4)[0]
            target_group = self.data[rec + 8]
            target_map = self.data[rec + 9]
            target = self.map_index.get((target_group, target_map))
            out.append({
                "direction_id": direction,
                "direction": direction_names.get(direction, f"unknown_{direction}"),
                "offset": offset,
                "target_group": target_group,
                "target_map": target_map,
                "target_id": f"{target_group}.{target_map}",
                "target_name": target.name if target else None,
                "record_pointer": ptr_hex(rec),
            })
        return out

    def parse_warps(self, header_off: int) -> Tuple[List[dict], dict]:
        header = self.parse_header(header_off)
        if not header or header.get("events_offset") is None:
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}
        off = int(header["events_offset"])
        if off < 0 or off + 20 > self.size:
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}
        object_count, warp_count, coord_count, bg_count = self.data[off:off + 4]
        object_ptr, warp_ptr, coord_ptr, bg_ptr = struct.unpack_from("<4I", self.data, off + 4)
        counts = {"object": object_count, "warp": warp_count, "coord": coord_count, "bg": bg_count}
        warp_off = gba_to_offset(warp_ptr, self.size) if warp_ptr else None
        if warp_count == 0 or warp_off is None or warp_count > 128:
            return [], counts
        out: List[dict] = []
        for i in range(warp_count):
            rec = int(warp_off) + i * 8
            if rec < 0 or rec + 8 > self.size:
                break
            x, y = struct.unpack_from("<hh", self.data, rec)
            elevation = self.data[rec + 4]
            dest_warp_id = self.data[rec + 5]
            target_map = self.data[rec + 6]
            target_group = self.data[rec + 7]
            layout: LayoutInfo = header["layout"]
            # MapEvents in a few heavily modified hack maps may use custom data.
            # Reject records that cannot be physical warp coordinates rather than
            # emitting garbage events into the destination project.
            if x < 0 or y < 0 or x >= layout.width or y >= layout.height or elevation > 15:
                continue
            target = self.map_index.get((target_group, target_map))
            dynamic_target = (target_group == 0x7F and target_map == 0x7F)
            out.append({
                "index": i,
                "x": x,
                "y": y,
                "elevation": elevation,
                "dest_warp_id": dest_warp_id,
                "target_group": target_group,
                "target_map": target_map,
                "target_id": f"{target_group}.{target_map}",
                "target_name": target.name if target else None,
                "dynamic_target": dynamic_target,
                "record_pointer": ptr_hex(rec),
            })
        return out, counts

    def parse_npcs(self, header_off: int) -> Tuple[List[dict], dict]:
        header = self.parse_header(header_off)
        if not header or header.get("events_offset") is None:
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}
        off = int(header["events_offset"])
        if off < 0 or off + 20 > self.size:
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}
        object_count, warp_count, coord_count, bg_count = self.data[off:off + 4]
        object_ptr, warp_ptr, coord_ptr, bg_ptr = struct.unpack_from("<4I", self.data, off + 4)
        counts = {"object": object_count, "warp": warp_count, "coord": coord_count, "bg": bg_count}
        object_off = gba_to_offset(object_ptr, self.size) if object_ptr else None
        if object_count == 0 or object_off is None or object_count > 64:
            return [], counts
        out: List[dict] = []
        for i in range(object_count):
            rec = int(object_off) + i * 24
            if rec < 0 or rec + 24 > self.size:
                break
            local_id = self.data[rec]
            graphics_id = self.data[rec + 1]
            kind = self.data[rec + 2]
            x, y = struct.unpack_from("<hh", self.data, rec + 4)
            elevation = self.data[rec + 8]
            movement_type = self.data[rec + 9]
            movement_ranges = u16(self.data, rec + 10)
            trainer_type = u16(self.data, rec + 12)
            trainer_sight_or_berry_tree_id = u16(self.data, rec + 14)
            script_raw = u32(self.data, rec + 16)
            flag_id = u16(self.data, rec + 20)
            out.append({
                "index": i,
                "local_id": local_id,
                "graphics_id": graphics_id,
                "kind": kind,
                "x": x,
                "y": y,
                "elevation": elevation,
                "movement_type": movement_type,
                "movement_range_x": movement_ranges & 0xF,
                "movement_range_y": (movement_ranges >> 4) & 0xF,
                "trainer_type": trainer_type,
                "trainer_sight_or_berry_tree_id": trainer_sight_or_berry_tree_id,
                "script_pointer": f"0x{script_raw:08X}" if script_raw else None,
                "script_pointer_raw": script_raw if script_raw else None,
                "script_offset": gba_to_offset(script_raw, self.size) if script_raw else None,
                "flag_id": flag_id,
                "record_pointer": ptr_hex(rec),
            })
        return out, counts

    def parse_coord_events(self, header_off: int) -> Tuple[List[dict], dict]:
        header = self.parse_header(header_off)
        if not header or header.get("events_offset") is None:
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}
        off = int(header["events_offset"])
        if off < 0 or off + 20 > self.size:
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}
        object_count, warp_count, coord_count, bg_count = self.data[off:off + 4]
        object_ptr, warp_ptr, coord_ptr, bg_ptr = struct.unpack_from("<4I", self.data, off + 4)
        counts = {"object": object_count, "warp": warp_count, "coord": coord_count, "bg": bg_count}
        coord_off = gba_to_offset(coord_ptr, self.size) if coord_ptr else None
        if coord_count == 0 or coord_off is None or coord_count > 128:
            return [], counts
        layout: LayoutInfo = header["layout"]
        out: List[dict] = []
        for i in range(coord_count):
            # Emerald CoordEvent is 16 bytes: x/y, elevation, pad, var, value,
            # two-byte pad, script pointer. See asm/macros/map.inc.
            rec = int(coord_off) + i * 16
            if rec < 0 or rec + 16 > self.size:
                break
            x, y = struct.unpack_from("<HH", self.data, rec)
            elevation = self.data[rec + 4]
            var = u16(self.data, rec + 6)
            value = u16(self.data, rec + 8)
            script_raw = u32(self.data, rec + 12)
            if x >= layout.width or y >= layout.height or elevation > 15:
                continue
            out.append({
                "index": i,
                "x": x,
                "y": y,
                "elevation": elevation,
                "var": var,
                "value": value,
                "weather_event": script_raw == 0,
                "script_pointer": f"0x{script_raw:08X}" if script_raw else None,
                "script_pointer_raw": script_raw if script_raw else None,
                "script_offset": gba_to_offset(script_raw, self.size) if script_raw else None,
                "record_pointer": ptr_hex(rec),
            })
        return out, counts

    def parse_bg_events(self, header_off: int) -> Tuple[List[dict], dict]:
        header = self.parse_header(header_off)
        if not header or header.get("events_offset") is None:
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}
        off = int(header["events_offset"])
        if off < 0 or off + 20 > self.size:
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}
        object_count, warp_count, coord_count, bg_count = self.data[off:off + 4]
        object_ptr, warp_ptr, coord_ptr, bg_ptr = struct.unpack_from("<4I", self.data, off + 4)
        counts = {"object": object_count, "warp": warp_count, "coord": coord_count, "bg": bg_count}
        bg_off = gba_to_offset(bg_ptr, self.size) if bg_ptr else None
        if bg_count == 0 or bg_off is None or bg_count > 128:
            return [], counts
        layout: LayoutInfo = header["layout"]
        out: List[dict] = []
        facing_names = {0: "any", 1: "north", 2: "south", 3: "east", 4: "west"}
        for i in range(bg_count):
            # Emerald BgEvent is 12 bytes. kind 0..4 stores a script pointer,
            # kind 7 stores hidden item/flag data, kind 8 stores a secret-base id.
            rec = int(bg_off) + i * 12
            if rec < 0 or rec + 12 > self.size:
                break
            x, y = struct.unpack_from("<HH", self.data, rec)
            elevation = self.data[rec + 4]
            kind = self.data[rec + 5]
            raw_arg = u32(self.data, rec + 8)
            if x >= layout.width or y >= layout.height or elevation > 15:
                continue
            item = {
                "index": i,
                "x": x,
                "y": y,
                "elevation": elevation,
                "kind": kind,
                "record_pointer": ptr_hex(rec),
            }
            if kind in facing_names:
                item.update({
                    "type": "sign",
                    "player_facing": facing_names[kind],
                    "script_pointer": f"0x{raw_arg:08X}" if raw_arg else None,
                    "script_pointer_raw": raw_arg if raw_arg else None,
                    "script_offset": gba_to_offset(raw_arg, self.size) if raw_arg else None,
                })
            elif kind == 7:
                item.update({
                    "type": "hidden_item",
                    "item_id": raw_arg & 0xFFFF,
                    "hidden_item_flag_offset": (raw_arg >> 16) & 0xFFFF,
                })
            elif kind == 8:
                item.update({"type": "secret_base", "secret_base_id": raw_arg})
            else:
                item.update({"type": "unknown", "raw_arg": f"0x{raw_arg:08X}"})
            out.append(item)
        return out, counts

    def parse_map_scripts(self, header_off: int) -> dict:
        header = self.parse_header(header_off)
        scripts_off = header.get("scripts_offset") if header else None
        if scripts_off is None:
            return {"table_pointer": None, "entries": [], "status": "none"}
        off = int(scripts_off)
        if off < 0 or off >= self.size:
            return {"table_pointer": ptr_hex(off), "entries": [], "status": "invalid"}
        type_names = {
            1: "on_load", 2: "on_frame_table", 3: "on_transition",
            4: "on_warp_into_map_table", 5: "on_resume",
            6: "on_dive_warp", 7: "on_return_to_field",
        }
        entries: List[dict] = []
        status = "parsed"
        for i in range(32):
            rec = off + i * 5
            if rec >= self.size:
                status = "truncated"
                break
            script_type = self.data[rec]
            if script_type == 0:
                break
            if rec + 5 > self.size:
                status = "truncated"
                break
            raw_ptr = u32(self.data, rec + 1)
            target_off = gba_to_offset(raw_ptr, self.size) if raw_ptr else None
            item = {
                "index": i,
                "type": script_type,
                "type_name": type_names.get(script_type, f"unknown_{script_type}"),
                "record_pointer": ptr_hex(rec),
                "script_pointer": f"0x{raw_ptr:08X}" if raw_ptr else None,
                "script_pointer_raw": raw_ptr if raw_ptr else None,
                "script_offset": target_off,
            }
            # ON_FRAME_TABLE and ON_WARP_INTO_MAP_TABLE point at 8-byte
            # conditional tables: u16 var, u16 compare, u32 script; terminal u16 0.
            if script_type in (2, 4) and target_off is not None:
                conditions: List[dict] = []
                pos = int(target_off)
                for j in range(256):
                    if pos + 2 > self.size:
                        break
                    var = u16(self.data, pos)
                    if var == 0:
                        break
                    if pos + 8 > self.size:
                        break
                    compare = u16(self.data, pos + 2)
                    cond_ptr = u32(self.data, pos + 4)
                    conditions.append({
                        "index": j,
                        "var": var,
                        "compare": compare,
                        "script_pointer": f"0x{cond_ptr:08X}" if cond_ptr else None,
                        "script_pointer_raw": cond_ptr if cond_ptr else None,
                        "script_offset": gba_to_offset(cond_ptr, self.size) if cond_ptr else None,
                        "record_pointer": ptr_hex(pos),
                    })
                    pos += 8
                item["conditions"] = conditions
                item["script_pointer_is_condition_table"] = True
            entries.append(item)
        else:
            status = "entry_limit_reached"
        return {"table_pointer": ptr_hex(off), "table_offset": off, "entries": entries, "status": status}

    def get_map(self, group: int, number: int) -> MapInfo:
        for m in self.maps:
            if m.group == group and m.number == number:
                return m
        raise KeyError(f"Map {group}.{number} not found")

    def diagnostics(self) -> dict:
        return {
            "rom": {
                "path": str(self.path),
                "title": self.title,
                "game_code": self.game_code,
                "size": self.size,
                "sha256": self.sha256,
            },
            "map_pointer_run": None if not self.map_pointer_run else {
                "start_offset": self.map_pointer_run[0],
                "end_offset": self.map_pointer_run[1],
                "count": self.map_pointer_run[2],
            },
            "master_table_offset": self.master_table_offset,
            "group_count": len(self.group_counts),
            "group_counts": self.group_counts,
            "map_count": len(self.maps),
            "region_map_table_offset": self.region_map_table_offset,
            "region_map_name_count": len(self.region_map_names),
        }


class Extractor:
    def __init__(self, scanner: RomScanner, out_dir: Path):
        self.s = scanner
        self.out = Path(out_dir)
        self.tileset_manifest: Dict[str, dict] = {}
        self.sprite_manifest: Dict[str, dict] = {}
        self.script_catalog: Optional[ScriptCatalog] = None
        self.script_diagnostics: Dict[str, object] = {}
        self.warnings: List[str] = []
        self.tileset_decode_modes: Dict[int, str] = {}

    def lz77_decompress(self, off: int, require_type_byte: bool = False) -> bytes:
        """Decode the GBA BIOS LZ stream layout used by Emerald graphics.

        The usual file marker is 0x10, but the BIOS routine consumes the 24-bit
        decompressed size from header bytes 1..3 and then decodes the same token
        stream from byte 4. Some production ROM data intentionally carries a
        different byte 0 while remaining a structurally valid BIOS LZ stream.
        Validate the token stream itself instead of rejecting it solely on byte 0.
        """
        d = self.s.data
        if off + 4 > len(d):
            raise ValueError(f"Truncated GBA LZ header at 0x{off:X}")
        if require_type_byte and d[off] != 0x10:
            raise ValueError(f"No canonical GBA LZ77 0x10 header at 0x{off:X}")
        out_size = d[off + 1] | (d[off + 2] << 8) | (d[off + 3] << 16)
        if not (1 <= out_size <= 0x400000):
            raise ValueError(f"Implausible GBA LZ output size {out_size} at 0x{off:X}")
        src = off + 4
        out = bytearray()
        while len(out) < out_size:
            if src >= len(d):
                raise ValueError("LZ77 stream ended unexpectedly")
            flags = d[src]
            src += 1
            for bit in range(7, -1, -1):
                if len(out) >= out_size:
                    break
                if not (flags & (1 << bit)):
                    if src >= len(d):
                        raise ValueError("LZ77 literal past EOF")
                    out.append(d[src])
                    src += 1
                else:
                    if src + 1 >= len(d):
                        raise ValueError("LZ77 backref past EOF")
                    b1, b2 = d[src], d[src + 1]
                    src += 2
                    length = (b1 >> 4) + 3
                    disp = ((b1 & 0x0F) << 8) | b2
                    copy_pos = len(out) - disp - 1
                    if copy_pos < 0:
                        raise ValueError("Invalid LZ77 displacement")
                    for _ in range(length):
                        out.append(out[copy_pos])
                        copy_pos += 1
                        if len(out) >= out_size:
                            break
        return bytes(out)

    def read_tiles(self, t: TilesetInfo, primary: bool) -> bytes:
        tile_count = PRIMARY_TILE_FALLBACK if primary else SECONDARY_TILE_FALLBACK
        if t.is_compressed:
            try:
                tiles = self.lz77_decompress(t.tiles_offset)
                header_byte = self.s.data[t.tiles_offset]
                mode = "gba_lz77" if header_byte == 0x10 else f"gba_lz77_bios_compatible_header_0x{header_byte:02X}"
                # Tile graphics are 32-byte units. A few hand-authored streams in
                # hacks advertise a byte count that ends mid-tile. Advance Map and
                # the engine effectively leave the missing tail transparent, so
                # normalize only that partial final tile. Do not pad complete 504-
                # tile secondary banks to 512, because their true size is useful.
                if len(tiles) % 32:
                    pad = 32 - (len(tiles) % 32)
                    tiles += bytes(pad)
                    mode += f"_padded_{pad}_byte"
                self.tileset_decode_modes[t.offset] = mode
                return tiles
            except ValueError as exc:
                # Preserve a raw window rather than aborting the entire batch.
                # This path is now reserved for genuinely non-BIOS-LZ streams.
                self.tileset_decode_modes[t.offset] = "raw_fallback_after_lz_validation_failure"
                self.warnings.append(
                    f"Tileset {ptr_hex(t.offset)} has compressed=1 but tiles at "
                    f"{ptr_hex(t.tiles_offset)} are not a valid BIOS-compatible LZ stream ({exc}); "
                    f"preserved {tile_count * 32} raw bytes as a fallback."
                )
                return self.s.data[t.tiles_offset:t.tiles_offset + tile_count * 32]
        self.tileset_decode_modes[t.offset] = "raw_uncompressed"
        return self.s.data[t.tiles_offset:t.tiles_offset + tile_count * 32]

    def metatile_count(self, t: TilesetInfo, primary: bool) -> int:
        diff = t.attributes_offset - t.metatiles_offset
        if diff > 0 and diff % 16 == 0:
            count = diff // 16
            if 1 <= count <= 1024:
                return count
        fallback = 512
        self.warnings.append(
            f"Could not infer metatile count for tileset {ptr_hex(t.offset)}; using fallback {fallback}."
        )
        return fallback

    @staticmethod
    def bgr555_to_rgb(word: int) -> Tuple[int, int, int]:
        r5 = word & 0x1F
        g5 = (word >> 5) & 0x1F
        b5 = (word >> 10) & 0x1F
        # Expand 5-bit to 8-bit with bit replication.
        return ((r5 << 3) | (r5 >> 2), (g5 << 3) | (g5 >> 2), (b5 << 3) | (b5 >> 2))

    def read_palette_bank(self, offset: int) -> List[Tuple[int, int, int]]:
        colors = []
        for i in range(16):
            word = u16(self.s.data, offset + i * 2)
            colors.append(self.bgr555_to_rgb(word))
        return colors

    @staticmethod
    def write_jasc(path: Path, colors: List[Tuple[int, int, int]]) -> None:
        text = ["JASC-PAL", "0100", str(len(colors))]
        text += [f"{r} {g} {b}" for r, g, b in colors]
        path.write_text("\n".join(text) + "\n", encoding="ascii")

    def write_tiles_png(self, path: Path, tiles: bytes, colors: List[Tuple[int, int, int]]) -> None:
        try:
            from PIL import Image
        except Exception:
            self.warnings.append("Pillow is not installed; tiles.png was skipped.")
            return
        tile_count = len(tiles) // 32
        cols = 16
        rows = max(1, (tile_count + cols - 1) // cols)
        img = Image.new("P", (cols * 8, rows * 8), 0)
        palette = []
        for r, g, b in colors[:16]:
            palette.extend([r, g, b])
        palette.extend([0] * (768 - len(palette)))
        img.putpalette(palette)
        px = img.load()
        for t in range(tile_count):
            base = t * 32
            tx = (t % cols) * 8
            ty = (t // cols) * 8
            for y in range(8):
                for x_pair in range(4):
                    b = tiles[base + y * 4 + x_pair]
                    px[tx + x_pair * 2, ty + y] = b & 0x0F
                    px[tx + x_pair * 2 + 1, ty + y] = (b >> 4) & 0x0F
        img.save(path)

    def extract_tileset(self, tileset_off: int, primary: bool) -> str:
        role = "primary" if primary else "secondary"
        key = f"{role}_{offset_to_gba(tileset_off):08X}"
        if key in self.tileset_manifest:
            return key
        t = self.s.parse_tileset(tileset_off)
        if not t:
            raise RuntimeError(f"Invalid tileset at {ptr_hex(tileset_off)}")
        folder = self.out / "tilesets" / key
        (folder / "palettes").mkdir(parents=True, exist_ok=True)

        tiles = self.read_tiles(t, primary)
        (folder / "tiles.4bpp").write_bytes(tiles)

        palette_count = PRIMARY_PALETTE_BANKS if primary else SECONDARY_PALETTE_BANKS
        palette_start_slot = 0 if primary else PRIMARY_PALETTE_BANKS
        palette_banks = []
        for i in range(palette_count):
            slot = palette_start_slot + i
            # Tileset::palettes points at the full 13-bank map palette table for
            # both primary and secondary tilesets. The engine loads secondary
            # palettes starting at NUM_PALS_IN_PRIMARY (slot 6), so the source
            # offset must use the destination slot, not a zero-based secondary
            # index. v0.3 incorrectly read slots 0..6 for secondary tilesets.
            colors = self.read_palette_bank(t.palettes_offset + slot * 32)
            pal_path = folder / "palettes" / f"{slot:02d}.pal"
            self.write_jasc(pal_path, colors)
            palette_banks.append({"slot": slot, "path": str(pal_path.relative_to(self.out))})

        # Indexed preview/import image. Pixel indices are the important payload; palette 0/6 is only display color.
        first_colors = self.read_palette_bank(t.palettes_offset + palette_start_slot * 32)
        self.write_tiles_png(folder / "tiles.png", tiles, first_colors)

        count = self.metatile_count(t, primary)
        defs_len = count * 16
        attrs_len = count * 2
        defs = self.s.data[t.metatiles_offset:t.metatiles_offset + defs_len]
        attrs = self.s.data[t.attributes_offset:t.attributes_offset + attrs_len]
        (folder / "metatiles.bin").write_bytes(defs)
        (folder / "metatile_attributes.bin").write_bytes(attrs)
        bvd = struct.pack("<I", count) + defs + attrs + b"RSE "
        (folder / "metatiles.bvd").write_bytes(bvd)

        meta = {
            "id": key,
            "role": role,
            "tileset_struct": ptr_hex(t.offset),
            "is_compressed": bool(t.is_compressed),
            "compression_mode": self.tileset_decode_modes.get(t.offset, "unknown"),
            "compression_header_byte": self.s.data[t.tiles_offset] if t.is_compressed else None,
            "tiles_pointer": ptr_hex(t.tiles_offset),
            "palette_pointer": ptr_hex(t.palettes_offset),
            "metatiles_pointer": ptr_hex(t.metatiles_offset),
            "attributes_pointer": ptr_hex(t.attributes_offset),
            "callback": f"0x{t.callback_raw:08X}" if t.callback_raw else None,
            "tile_count": len(tiles) // 32,
            "metatile_count": count,
            "palette_banks": palette_banks,
            "sha256": {
                "tiles_4bpp": hashlib.sha256(tiles).hexdigest(),
                "metatiles_bvd": hashlib.sha256(bvd).hexdigest(),
            },
        }
        (folder / "tileset.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        self.tileset_manifest[key] = meta
        return key

    def make_am195_visual_map(self, layout: LayoutInfo) -> bytes:
        # Visual-only AM1.95 container accepted by the custom Porymap bridge.
        # The compatibility .map remains visual-only; NPCs/connections live in package JSON.
        border_width = 2
        border_height = 2
        border_bytes = self.s.data[layout.border_offset:layout.border_offset + border_width * border_height * 2]
        block_bytes = self.s.data[layout.blockdata_offset:layout.blockdata_offset + layout.width * layout.height * 2]
        header = bytearray(52)
        struct.pack_into("<I", header, 0x00, layout.width)
        struct.pack_into("<I", header, 0x04, layout.height)
        # These numeric IDs are placeholders. The package manifest carries authoritative tileset identities.
        struct.pack_into("<I", header, 0x08, 0)
        struct.pack_into("<I", header, 0x0C, 1)
        header[0x10] = border_width
        header[0x11] = border_height
        header[0x14:0x18] = self.s.game_code.encode("ascii", "replace")[:4].ljust(4, b" ")
        struct.pack_into("<I", header, 0x18, 52)
        struct.pack_into("<I", header, 0x1C, 0)
        struct.pack_into("<I", header, 0x20, 0)
        struct.pack_into("<I", header, 0x24, 0)
        return bytes(header) + border_bytes + block_bytes

    def extract_map(self, m: MapInfo) -> dict:
        header = self.s.parse_header(m.header_offset)
        if not header:
            raise RuntimeError(f"Cannot parse map header {m.id}")
        layout: LayoutInfo = header["layout"]
        primary_key = self.extract_tileset(layout.primary_tileset_offset, True)
        secondary_key = self.extract_tileset(layout.secondary_tileset_offset, False)

        name = sanitize_name(m.name)
        folder = self.out / "maps" / f"{m.group:02d}.{m.number:02d}_{name}"
        folder.mkdir(parents=True, exist_ok=True)
        visual = self.make_am195_visual_map(layout)
        (folder / f"{m.group}.{m.number}_{name}.map").write_bytes(visual)

        border = self.s.data[layout.border_offset:layout.border_offset + 8]
        blockdata = self.s.data[layout.blockdata_offset:layout.blockdata_offset + layout.width * layout.height * 2]
        (folder / "border.bin").write_bytes(border)
        (folder / "blockdata.bin").write_bytes(blockdata)

        connections = self.s.parse_connections(m.header_offset)
        warps, warp_counts = self.s.parse_warps(m.header_offset)
        npcs, event_counts = self.s.parse_npcs(m.header_offset)
        coord_events, coord_counts = self.s.parse_coord_events(m.header_offset)
        bg_events, bg_counts = self.s.parse_bg_events(m.header_offset)
        map_scripts = self.s.parse_map_scripts(m.header_offset)
        script_payload = self.script_catalog.map_payload(m.id) if self.script_catalog else {"roots": [], "reachable_script_pointers": [], "scripts": []}
        # Keep one authoritative count object. All event passes read the same MapEvents header.
        for other_counts, label in ((warp_counts, "warp"), (coord_counts, "coord"), (bg_counts, "bg")):
            if other_counts != event_counts:
                self.warnings.append(f"Map {m.id}: event-count header differed during {label} parsing; using NPC pass counts")
        for npc in npcs:
            key = f"gfx_{int(npc.get('graphics_id', 0)):03d}"
            asset = self.sprite_manifest.get(key)
            npc["sprite_key"] = key
            if asset:
                npc["sprite_status"] = asset.get("status")
                npc["sprite_preview"] = asset.get("preview")
                npc["sprite_sheet"] = asset.get("sheet")
                npc["sprite_project_import_safe"] = bool(asset.get("project_import_safe"))
            else:
                npc["sprite_status"] = "not_extracted"
                npc["sprite_preview"] = None
                npc["sprite_sheet"] = None
                npc["sprite_project_import_safe"] = False
        (folder / "connections.json").write_text(json.dumps(connections, indent=2), encoding="utf-8")
        (folder / "warps.json").write_text(json.dumps(warps, indent=2), encoding="utf-8")
        (folder / "npcs.json").write_text(json.dumps(npcs, indent=2), encoding="utf-8")
        (folder / "coord_events.json").write_text(json.dumps(coord_events, indent=2), encoding="utf-8")
        (folder / "bg_events.json").write_text(json.dumps(bg_events, indent=2), encoding="utf-8")
        (folder / "map_scripts.json").write_text(json.dumps(map_scripts, indent=2), encoding="utf-8")
        (folder / "scripts.json").write_text(json.dumps(script_payload, indent=2, ensure_ascii=False), encoding="utf-8")

        meta = {
            "id": m.id,
            "group": m.group,
            "map": m.number,
            "name": m.name,
            "header_pointer": ptr_hex(m.header_offset),
            "layout_pointer": ptr_hex(layout.offset),
            "width": layout.width,
            "height": layout.height,
            "border": {"width": 2, "height": 2, "pointer": ptr_hex(layout.border_offset)},
            "blockdata_pointer": ptr_hex(layout.blockdata_offset),
            "primary_tileset": primary_key,
            "secondary_tileset": secondary_key,
            "region_map_section_id": m.region_map_section_id,
            "region_map_section_name": self.s.region_map_names.get(m.region_map_section_id, m.name),
            "map_type": m.map_type,
            "weather": m.weather,
            "music": m.music,
            "layout_id": m.layout_id,
            "show_map_name": bool(header.get("show_map_name", True)),
            "allow_cycling": bool(header.get("allow_cycling", False)),
            "allow_escaping": bool(header.get("allow_escaping", False)),
            "allow_running": bool(header.get("allow_running", True)),
            "battle_type": int(header.get("battle_type", 0)),
            "connections": connections,
            "warps": warps,
            "npcs": npcs,
            "coord_events": coord_events,
            "bg_events": bg_events,
            "map_scripts": map_scripts,
            "script_summary": {
                "root_count": len(script_payload.get("roots", [])),
                "reachable_script_count": len(script_payload.get("scripts", [])),
            },
            "event_counts": event_counts,
            "visual_map_sha256": hashlib.sha256(visual).hexdigest(),
            "blockdata_sha256": hashlib.sha256(blockdata).hexdigest(),
        }
        (folder / "map.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        return meta

    def extract(self, maps: Iterable[MapInfo]) -> dict:
        self.out.mkdir(parents=True, exist_ok=True)
        selected_maps = list(maps)

        # Catalog map scripts and all event-script roots before writing map packages.
        # The decoder is conservative: unsupported/custom opcodes stop only that
        # script and preserve a raw diagnostic tail rather than guessing lengths.
        try:
            self.script_catalog = ScriptCatalog(self.s, self.out)
            self.script_diagnostics = self.script_catalog.extract(selected_maps)
            self.warnings.extend(self.script_catalog.warnings)
        except Exception as exc:
            self.script_catalog = None
            self.script_diagnostics = {"error": str(exc)}
            self.warnings.append(f"Script extraction failed: {exc}")

        # Extract every static object-event sprite referenced by the selected maps.
        # Dynamic VAR_OBJ_GFX IDs are retained as unresolved because this tool does
        # not execute scripts by design.
        graphics_ids = set()
        for m in selected_maps:
            npcs, _ = self.s.parse_npcs(m.header_offset)
            graphics_ids.update(int(npc.get("graphics_id", 0)) for npc in npcs)
        try:
            sprite_catalog = ObjectSpriteCatalog(self.s.data, self.out)
            self.sprite_manifest = sprite_catalog.extract(graphics_ids)
            self.warnings.extend(sprite_catalog.warnings)
            sprite_diagnostics = {
                "graphics_pointer_table": ptr_hex(sprite_catalog.pointer_table_offset),
                "static_graphics_count": sprite_catalog.static_count,
                "palette_table": ptr_hex(sprite_catalog.palette_table_offset),
                "requested_graphics_ids": sorted(graphics_ids),
                "extracted_count": sum(1 for x in self.sprite_manifest.values() if x.get("status") == "extracted"),
                "unresolved_count": sum(1 for x in self.sprite_manifest.values() if x.get("status") != "extracted"),
            }
        except Exception as exc:
            sprite_diagnostics = {"error": str(exc)}
            self.warnings.append(f"Object sprite extraction failed: {exc}")

        map_metas = []
        for m in selected_maps:
            map_metas.append(self.extract_map(m))
        manifest = {
            "format": "A-Map Batch Bridge v1.0",
            "scope": "visual map data + NPC/warp/coord/background events + map connections + source map-section names + static object sprites + lossless-first Emerald event-script extraction/decompilation",
            "rom": self.s.diagnostics()["rom"],
            "scanner": self.s.diagnostics(),
            "maps": map_metas,
            "tilesets": self.tileset_manifest,
            "sprites": self.sprite_manifest,
            "sprite_diagnostics": sprite_diagnostics,
            "script_diagnostics": self.script_diagnostics,
            "warnings": self.warnings,
        }
        (self.out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        return manifest


def parse_map_selector(text: str) -> Tuple[int, int]:
    m = re.fullmatch(r"\s*(\d+)\.(\d+)\s*", text)
    if not m:
        raise argparse.ArgumentTypeError("Map IDs must look like 0.9")
    return int(m.group(1)), int(m.group(2))


def run_gui(initial_rom: Optional[Path] = None, names_path: Optional[Path] = None) -> int:
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox, ttk
    except Exception as exc:
        print(f"Tkinter is unavailable: {exc}", file=sys.stderr)
        return 2

    class App(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("A-Map Batch Bridge v1.0")
            self.geometry("1120x720")
            self.minsize(900, 600)
            self.scanner: Optional[RomScanner] = None
            self.rom_var = tk.StringVar(value=str(initial_rom or ""))
            self.status = tk.StringVar(value="Choose an Emerald-derived ROM, then Scan ROM.")
            self._build()
            if initial_rom:
                self.after(100, self.scan)

        def _build(self):
            top = ttk.Frame(self, padding=8)
            top.pack(fill="x")
            ttk.Label(top, text="ROM:").pack(side="left")
            ttk.Entry(top, textvariable=self.rom_var).pack(side="left", fill="x", expand=True, padx=6)
            ttk.Button(top, text="Browse", command=self.browse).pack(side="left", padx=3)
            ttk.Button(top, text="Scan ROM", command=self.scan).pack(side="left", padx=3)

            body = ttk.Panedwindow(self, orient="horizontal")
            body.pack(fill="both", expand=True, padx=8, pady=(0, 8))
            left = ttk.Frame(body)
            right = ttk.Frame(body, padding=10)
            body.add(left, weight=2)
            body.add(right, weight=3)

            self.tree = ttk.Treeview(left, columns=("size", "tiles"), selectmode="extended")
            self.tree.heading("#0", text="Advance Map bank / map")
            self.tree.heading("size", text="Size")
            self.tree.heading("tiles", text="Tilesets")
            self.tree.column("#0", width=310)
            self.tree.column("size", width=90, anchor="center")
            self.tree.column("tiles", width=160, anchor="center")
            sb = ttk.Scrollbar(left, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscrollcommand=sb.set)
            self.tree.pack(side="left", fill="both", expand=True)
            sb.pack(side="right", fill="y")
            self.tree.bind("<<TreeviewSelect>>", self.on_select)

            ttk.Label(right, text="Map details", font=("Segoe UI", 14, "bold")).pack(anchor="w")
            self.details = tk.Text(right, wrap="word", height=20, state="disabled")
            self.details.pack(fill="both", expand=True, pady=8)

            buttons = ttk.Frame(right)
            buttons.pack(fill="x")
            ttk.Button(buttons, text="Extract Selected", command=self.extract_selected).pack(side="left", padx=3)
            ttk.Button(buttons, text="Extract All", command=self.extract_all).pack(side="left", padx=3)
            ttk.Button(buttons, text="Expand All", command=self.expand_all).pack(side="left", padx=3)

            ttk.Label(self, textvariable=self.status, relief="sunken", anchor="w").pack(fill="x", side="bottom")

        def browse(self):
            p = filedialog.askopenfilename(title="Choose GBA ROM", filetypes=[("GBA ROM", "*.gba"), ("All files", "*.*")])
            if p:
                self.rom_var.set(p)

        def scan(self):
            path = Path(self.rom_var.get().strip())
            if not path.is_file():
                messagebox.showerror("A-Map Batch Bridge", "Choose a valid ROM file first.")
                return
            self.status.set("Scanning map headers and map groups...")
            self.update_idletasks()
            try:
                self.scanner = RomScanner(path, names_path=names_path)
                maps = self.scanner.discover()
            except Exception as exc:
                messagebox.showerror("Scan failed", str(exc))
                self.status.set("Scan failed.")
                return
            for x in self.tree.get_children():
                self.tree.delete(x)
            by_group: Dict[int, List[MapInfo]] = {}
            for m in maps:
                by_group.setdefault(m.group, []).append(m)
            for group in sorted(by_group):
                if group < len(GROUP_LABELS):
                    group_text = f"Bank {group}  {GROUP_LABELS[group]}"
                else:
                    group_text = f"Bank {group}"
                gid = self.tree.insert("", "end", iid=f"g:{group}", text=group_text, values=(f"{len(by_group[group])} maps", ""))
                for m in by_group[group]:
                    self.tree.insert(gid, "end", iid=f"m:{m.group}:{m.number}", text=f"{m.id}  {m.name}",
                                     values=(f"{m.width}x{m.height}", f"{m.primary_tileset_offset:06X}/{m.secondary_tileset_offset:06X}"))
            if "g:0" in self.tree.get_children(""):
                self.tree.item("g:0", open=True)
            d = self.scanner.diagnostics()
            self.status.set(f"Found {d['group_count']} banks, {d['map_count']} maps. Master table 0x{d['master_table_offset']:X}.")

        def expand_all(self):
            for g in self.tree.get_children(""):
                self.tree.item(g, open=True)

        def selected_maps(self) -> List[MapInfo]:
            if not self.scanner:
                return []
            ids = set()
            for item in self.tree.selection():
                if item.startswith("m:"):
                    _, g, m = item.split(":")
                    ids.add((int(g), int(m)))
                elif item.startswith("g:"):
                    g = int(item.split(":")[1])
                    for mitem in self.tree.get_children(item):
                        _, gg, mm = mitem.split(":")
                        ids.add((int(gg), int(mm)))
            return [self.scanner.get_map(g, m) for g, m in sorted(ids)]

        def on_select(self, _event=None):
            if not self.scanner:
                return
            maps = self.selected_maps()
            if len(maps) != 1:
                text = f"{len(maps)} maps selected." if maps else "Select a map to inspect it."
            else:
                m = maps[0]
                h = self.scanner.parse_header(m.header_offset)
                lay: LayoutInfo = h["layout"]
                p = self.scanner.parse_tileset(lay.primary_tileset_offset)
                s = self.scanner.parse_tileset(lay.secondary_tileset_offset)
                conns = self.scanner.parse_connections(m.header_offset)
                npcs, event_counts = self.scanner.parse_npcs(m.header_offset)
                map_scripts = self.scanner.parse_map_scripts(m.header_offset)
                text = (
                    f"{m.id}  {m.name}\n\n"
                    f"Map header: {ptr_hex(m.header_offset)}\n"
                    f"Layout: {ptr_hex(m.layout_offset)}\n"
                    f"Dimensions: {m.width} x {m.height}\n"
                    f"Blockdata: {ptr_hex(lay.blockdata_offset)}\n"
                    f"Border: {ptr_hex(lay.border_offset)}\n"
                    f"Region map section: {m.region_map_section_id}  "
                    f"{self.scanner.region_map_names.get(m.region_map_section_id, '(unresolved)')}\n"
                    f"NPC object events: {len(npcs)}\n"
                    f"Connections: {len(conns)}\n"
                    f"Warp events: {event_counts['warp']}  |  Coord events: {event_counts['coord']}  |  BG events: {event_counts['bg']}\n"
                    f"Map script entries: {len(map_scripts.get('entries', []))}  |  Table: {map_scripts.get('table_pointer') or '(none)'}\n\n"
                    f"Primary tileset: {ptr_hex(lay.primary_tileset_offset)}\n"
                    f"  tiles: {ptr_hex(p.tiles_offset)}\n  palettes: {ptr_hex(p.palettes_offset)}\n"
                    f"  metatiles: {ptr_hex(p.metatiles_offset)}\n  attrs: {ptr_hex(p.attributes_offset)}\n\n"
                    f"Secondary tileset: {ptr_hex(lay.secondary_tileset_offset)}\n"
                    f"  tiles: {ptr_hex(s.tiles_offset)}\n  palettes: {ptr_hex(s.palettes_offset)}\n"
                    f"  metatiles: {ptr_hex(s.metatiles_offset)}\n  attrs: {ptr_hex(s.attributes_offset)}\n"
                )
            self.details.configure(state="normal")
            self.details.delete("1.0", "end")
            self.details.insert("1.0", text)
            self.details.configure(state="disabled")

        def _extract(self, maps: List[MapInfo]):
            if not self.scanner or not maps:
                messagebox.showinfo("A-Map Batch Bridge", "Select at least one map.")
                return
            out = filedialog.askdirectory(title="Choose extraction folder")
            if not out:
                return
            target = Path(out) / f"{sanitize_name(self.scanner.path.stem)}_amap_export"
            self.status.set(f"Extracting {len(maps)} maps...")
            self.update_idletasks()
            try:
                manifest = Extractor(self.scanner, target).extract(maps)
            except Exception as exc:
                messagebox.showerror("Extraction failed", str(exc))
                self.status.set("Extraction failed.")
                return
            self.status.set(f"Extracted {len(manifest['maps'])} maps to {target}")
            messagebox.showinfo("Extraction complete", f"Extracted {len(manifest['maps'])} maps.\n\n{target}")

        def extract_selected(self):
            self._extract(self.selected_maps())

        def extract_all(self):
            if not self.scanner:
                return
            self._extract(self.scanner.maps)

    app = App()
    app.mainloop()
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Batch-discover and extract Emerald-derived GBA maps, events, sprites, map scripts, and conservatively decoded event-script bytecode.")
    ap.add_argument("rom", nargs="?", type=Path, help="Path to .gba ROM")
    ap.add_argument("--names", type=Path, help="Optional pokeemerald-style map_groups.json for friendly names")
    ap.add_argument("--gui", action="store_true", help="Open the graphical bank/map browser")
    ap.add_argument("--scan", action="store_true", help="Print scanner diagnostics and map list")
    ap.add_argument("--extract-all", action="store_true", help="Extract every discovered map")
    ap.add_argument("--extract", type=parse_map_selector, action="append", default=[], metavar="BANK.MAP", help="Extract one map; repeatable")
    ap.add_argument("--out", type=Path, default=Path("amap_export"), help="Extraction output folder")
    args = ap.parse_args(argv)

    if args.gui or (not args.scan and not args.extract_all and not args.extract):
        return run_gui(args.rom, args.names)
    if not args.rom:
        ap.error("ROM path is required for command-line scan/extraction")

    scanner = RomScanner(args.rom, names_path=args.names)
    scanner.discover()

    if args.scan:
        print(json.dumps(scanner.diagnostics(), indent=2))
        for m in scanner.maps:
            print(f"{m.id:>7}  {m.width:>3}x{m.height:<3}  {m.name}")

    targets: List[MapInfo] = []
    if args.extract_all:
        targets = scanner.maps
    elif args.extract:
        targets = [scanner.get_map(g, m) for g, m in args.extract]
    if targets:
        manifest = Extractor(scanner, args.out).extract(targets)
        print(f"Extracted {len(manifest['maps'])} map(s) to {args.out.resolve()}")
        if manifest["warnings"]:
            print("Warnings:")
            for w in manifest["warnings"]:
                print(f"  - {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
