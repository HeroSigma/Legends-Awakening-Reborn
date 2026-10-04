from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import legacy_emerald_bridge as legacy

ROM_BASE = legacy.ROM_BASE

PROFILES = {
    "bwa_demo_v2": {
        "label": "Pokemon Black & White Advanced (Demo v2)",
        "sha256": "12a2e11285b5a4c57ede151d78ad3308b9a96b406b0d41fdade6f6da57b3fef4",
        "group_table": 0x09025288,
        "group_counts": [6,123,60,66,6,8,9,10,6,8,20,10,8,2,10,4,2,2,2,1,1,4,2,3,2,3,2,1,1,1,1,7,5,5,8,8,5,5,1,1,1,2,4,1,4,2,1],
        "map_name_table": 0x083F1CAC,
        "mapsec_base": 88,
        "region": "unova",
    },
    "swsh_ultimate_plus": {
        "label": "Sword & Shield Ultimate+ v1.2.1.2",
        "sha256": "f6d2e7092831b983318b685132a19567ff5e6428665255738c4e5a63371bcce3",
        "group_table": 0x087B1010,
        "group_counts": [21,123,60,67,13,17,36,24,27,21,30,14,19,21,12,4,2,2,2,1,1,3,2,3,2,3,2,1,1,1,1,7,5,5,8,29,25,23,45,43,16,2,16,1],
        "map_name_table": 0x083F1CAC,
        "mapsec_base": 88,
        "region": "galar",
    },
    "catalyst": {
        "label": "Pokemon Catalyst (patched FireRed Rev 1)",
        "sha256": "eebac86bbf0994a51d80bebe29e5d7f0f8f5cf4ec9c3fa68d7a8fc3f8928d5ef",
        "group_table": 0x08352718,
        "group_counts": [5,123,32,0,4,6,8,10,6,8,20,10,8,2,11],
        "map_name_table": 0x083F1D1C,
        "mapsec_base": 88,
        "region": "unknown",
    },
}


def profile_for_sha(sha: str) -> Optional[Tuple[str, dict]]:
    for key, profile in PROFILES.items():
        if profile["sha256"] == sha:
            return key, profile
    return None


class FireRedScanner(legacy.RomScanner):
    """Exact-build FireRed donor scanner feeding the legacy Batch Bridge package schema."""

    def __init__(self, path: Path, profile_key: str, names_path: Optional[Path] = None):
        super().__init__(path, names_path)
        if profile_key not in PROFILES:
            raise ValueError(f"Unknown FireRed donor profile '{profile_key}'")
        self.profile_key = profile_key
        self.profile = PROFILES[profile_key]
        if self.sha256 != self.profile["sha256"]:
            raise ValueError(
                f"ROM SHA-256 does not match profile {profile_key}\n"
                f"expected {self.profile['sha256']}\nactual   {self.sha256}"
            )
        self.layout_border_sizes: Dict[int, Tuple[int, int]] = {}
        self.region_map_table_offset = self.profile["map_name_table"] - ROM_BASE

    def parse_tileset(self, off: int) -> Optional[legacy.TilesetInfo]:
        if off in self._tileset_cache:
            return self._tileset_cache[off]
        if off < 0 or off + 0x18 > self.size:
            self._tileset_cache[off] = None
            return None
        comp = self.data[off]
        secondary = self.data[off + 1]
        if comp not in (0, 1) or secondary not in (0, 1):
            self._tileset_cache[off] = None
            return None
        tiles_raw = legacy.u32(self.data, off + 0x04)
        pals_raw = legacy.u32(self.data, off + 0x08)
        metas_raw = legacy.u32(self.data, off + 0x0C)
        callback_raw = legacy.u32(self.data, off + 0x10)
        attrs_raw = legacy.u32(self.data, off + 0x14)
        vals = [tiles_raw, pals_raw, metas_raw, attrs_raw]
        ptrs = [legacy.gba_to_offset(v, self.size) for v in vals]
        if any(v is None for v in ptrs):
            self._tileset_cache[off] = None
            return None
        if callback_raw:
            cb = callback_raw & ~1
            if not (ROM_BASE <= cb < ROM_BASE + self.size):
                self._tileset_cache[off] = None
                return None
        out = legacy.TilesetInfo(
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

    def parse_layout(self, off: int) -> Optional[legacy.LayoutInfo]:
        if off in self._layout_cache:
            return self._layout_cache[off]
        if off < 0 or off + 0x1A > self.size:
            self._layout_cache[off] = None
            return None
        width, height = struct.unpack_from("<ii", self.data, off)
        border_ptr, map_ptr, primary_ptr, secondary_ptr = struct.unpack_from("<4I", self.data, off + 8)
        if not (1 <= width <= 1024 and 1 <= height <= 1024):
            self._layout_cache[off] = None
            return None
        border_width = self.data[off + 0x18]
        border_height = self.data[off + 0x19]
        if not (1 <= border_width <= 16 and 1 <= border_height <= 16):
            self._layout_cache[off] = None
            return None
        converted = [legacy.gba_to_offset(x, self.size) for x in (border_ptr, map_ptr, primary_ptr, secondary_ptr)]
        if any(x is None for x in converted):
            self._layout_cache[off] = None
            return None
        border_off, map_off, primary_off, secondary_off = map(int, converted)
        if map_off + width * height * 2 > self.size:
            self._layout_cache[off] = None
            return None
        if border_off + border_width * border_height * 2 > self.size:
            self._layout_cache[off] = None
            return None
        if not self.parse_tileset(primary_off) or not self.parse_tileset(secondary_off):
            self._layout_cache[off] = None
            return None
        out = legacy.LayoutInfo(
            offset=off,
            width=width,
            height=height,
            border_offset=border_off,
            blockdata_offset=map_off,
            primary_tileset_offset=primary_off,
            secondary_tileset_offset=secondary_off,
        )
        self.layout_border_sizes[off] = (border_width, border_height)
        self._layout_cache[off] = out
        return out

    def parse_header(self, off: int) -> Optional[dict]:
        if off in self._header_cache:
            return self._header_cache[off]
        if off < 0 or off + 0x1C > self.size:
            self._header_cache[off] = None
            return None
        layout_ptr, events_ptr, scripts_ptr, connections_ptr = struct.unpack_from("<4I", self.data, off)
        layout_off = legacy.gba_to_offset(layout_ptr, self.size)
        if layout_off is None:
            self._header_cache[off] = None
            return None
        layout = self.parse_layout(int(layout_off))
        if layout is None:
            self._header_cache[off] = None
            return None
        # Heavily modified binary hacks sometimes leave a stale/non-ROM value in
        # an optional events/scripts/connections field while the map layout itself
        # remains valid and AdvanceMap still opens it.  Do not discard the map for
        # that.  Preserve raw values and expose only safely addressable offsets.
        events_off = legacy.gba_to_offset(events_ptr, self.size) if events_ptr else None
        scripts_off = legacy.gba_to_offset(scripts_ptr, self.size) if scripts_ptr else None
        connections_off = legacy.gba_to_offset(connections_ptr, self.size) if connections_ptr else None
        flags = self.data[off + 0x19]
        out = {
            "offset": off,
            "layout": layout,
            "events_offset": events_off,
            "scripts_offset": scripts_off,
            "connections_offset": connections_off,
            "events_pointer_raw": events_ptr,
            "scripts_pointer_raw": scripts_ptr,
            "connections_pointer_raw": connections_ptr,
            "music": legacy.u16(self.data, off + 0x10),
            "layout_id": legacy.u16(self.data, off + 0x12),
            "region_map_section_id": self.data[off + 0x14],
            "cave": self.data[off + 0x15],
            "weather": self.data[off + 0x16],
            "map_type": self.data[off + 0x17],
            "allow_cycling": bool(self.data[off + 0x18]),
            "allow_escaping": bool(flags & 0x01),
            "allow_running": bool(flags & 0x02),
            "show_map_name": bool((flags >> 2) & 0x3F),
            "floor_number": struct.unpack_from("<b", self.data, off + 0x1A)[0],
            "battle_type": self.data[off + 0x1B],
        }
        self._header_cache[off] = out
        return out

    def discover_region_map_names(self, max_section_id: int) -> Dict[int, str]:
        names: Dict[int, str] = {}
        table_off = self.profile["map_name_table"] - ROM_BASE
        base = self.profile["mapsec_base"]
        for i in range(256):
            pos = table_off + i * 4
            if pos < 0 or pos + 4 > self.size:
                break
            text_ptr = legacy.u32(self.data, pos)
            text_off = legacy.gba_to_offset(text_ptr, self.size)
            if text_off is None:
                break
            text = self.decode_gen3_text(int(text_off), max_len=64)
            if not text:
                break
            names[base + i] = text
        self.region_map_names = names
        return names

    def discover(self) -> List[legacy.MapInfo]:
        master = self.profile["group_table"] - ROM_BASE
        counts = list(self.profile["group_counts"])
        self.master_table_offset = master
        self.group_counts = counts
        self.group_starts = []
        for i in range(len(counts)):
            ptr = legacy.u32(self.data, master + i * 4)
            off = legacy.gba_to_offset(ptr, self.size)
            if off is None:
                raise RuntimeError(f"Profile group {i} points outside ROM")
            self.group_starts.append(int(off))

        self.discover_region_map_names(255)
        maps: List[legacy.MapInfo] = []
        invalid_slots = 0
        for group, (start, count) in enumerate(zip(self.group_starts, counts)):
            for number in range(count):
                pos = start + number * 4
                if pos + 4 > self.size:
                    invalid_slots += 1
                    continue
                header_off = legacy.gba_to_offset(legacy.u32(self.data, pos), self.size)
                if header_off is None:
                    invalid_slots += 1
                    continue
                header = self.parse_header(int(header_off))
                if not header:
                    invalid_slots += 1
                    continue
                layout: legacy.LayoutInfo = header["layout"]
                explicit = self.external_names.get((group, number))
                name = explicit or self.region_map_names.get(header["region_map_section_id"]) or f"Map_{group:02d}_{number:02d}"
                maps.append(legacy.MapInfo(
                    group=group,
                    number=number,
                    name=name,
                    header_offset=int(header_off),
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
        self._invalid_profile_slots = invalid_slots
        return maps

    def diagnostics(self) -> dict:
        base = super().diagnostics()
        base.update({
            "engine": "firered",
            "profile": self.profile_key,
            "profile_label": self.profile["label"],
            "group_table": f"0x{self.profile['group_table']:08X}",
            "profile_slot_count": sum(self.profile["group_counts"]),
            "invalid_or_blank_profile_slots": getattr(self, "_invalid_profile_slots", 0),
            "normalization_target": "emerald_512_512",
        })
        return base


class FireRedNormalizedExtractor(legacy.Extractor):
    """Convert FireRed 640/384 assets into an Emerald 512/512 package losslessly for visuals.

    The global tile/metatile IDs stay unchanged:
      source primary 0..511       -> destination primary 0..511
      source primary 512..639     -> destination secondary 0..127
      source secondary 0..383     -> destination secondary 128..511

    Thus source global IDs 0..1023 remain identical after repartitioning.
    """

    SRC_PRIMARY_TILES = 640
    SRC_SECONDARY_TILES = 384
    SRC_PRIMARY_METATILES = 640
    SRC_SECONDARY_METATILES = 384
    DST_PRIMARY = 512
    DST_SECONDARY = 512

    def __init__(self, scanner: FireRedScanner, out_dir: Path):
        super().__init__(scanner, out_dir)
        self.s: FireRedScanner = scanner
        self._pair_cache: Dict[Tuple[int, int], Tuple[str, str]] = {}

    @staticmethod
    def _ensure_size(data: bytes, size: int) -> bytes:
        if len(data) < size:
            return data + bytes(size - len(data))
        return data[:size]

    def _source_tiles(self, t: legacy.TilesetInfo, count: int) -> bytes:
        size = count * 32
        if t.is_compressed:
            try:
                raw = self.lz77_decompress(t.tiles_offset)
                mode = "gba_lz77" if self.s.data[t.tiles_offset] == 0x10 else f"gba_lz77_bios_compatible_header_0x{self.s.data[t.tiles_offset]:02X}"
            except Exception as exc:
                self.warnings.append(f"Tileset {legacy.ptr_hex(t.offset)} LZ decode failed ({exc}); raw fallback used")
                raw = self.s.data[t.tiles_offset:t.tiles_offset + size]
                mode = "raw_fallback_after_lz_failure"
        else:
            raw = self.s.data[t.tiles_offset:t.tiles_offset + size]
            mode = "raw_uncompressed"
        self.tileset_decode_modes[t.offset] = mode
        return self._ensure_size(raw, size)

    @staticmethod
    def _frlg_attr_to_rse(attr: int) -> Tuple[int, bool]:
        behavior = attr & 0x1FF
        layer = (attr >> 29) & 0x3
        overflow = behavior > 0xFF
        return (behavior & 0xFF) | ((layer & 0xF) << 12), overflow

    def _convert_attrs(self, raw: bytes) -> Tuple[bytes, int]:
        out = bytearray()
        overflow = 0
        for i in range(0, len(raw), 4):
            attr = struct.unpack_from("<I", raw, i)[0]
            converted, ov = self._frlg_attr_to_rse(attr)
            overflow += int(ov)
            out += struct.pack("<H", converted)
        return bytes(out), overflow

    def _palette_file(self, folder: Path, slot: int, palette_source: legacy.TilesetInfo) -> dict:
        colors = self.read_palette_bank(palette_source.palettes_offset + slot * 32)
        path = folder / "palettes" / f"{slot:02d}.pal"
        self.write_jasc(path, colors)
        return {"slot": slot, "path": str(path.relative_to(self.out))}

    def _write_normalized_tileset(self, key: str, role: str, tiles: bytes, defs: bytes, attrs_rse: bytes,
                                  raw_attrs_frlg: bytes, palette_specs: List[Tuple[int, legacy.TilesetInfo]],
                                  source: dict, behavior_overflow: int) -> str:
        if key in self.tileset_manifest:
            return key
        folder = self.out / "tilesets" / key
        (folder / "palettes").mkdir(parents=True, exist_ok=True)
        (folder / "tiles.4bpp").write_bytes(tiles)
        palette_banks = [self._palette_file(folder, slot, ts) for slot, ts in palette_specs]
        first_slot, first_ts = palette_specs[0]
        first_colors = self.read_palette_bank(first_ts.palettes_offset + first_slot * 32)
        self.write_tiles_png(folder / "tiles.png", tiles, first_colors)
        (folder / "metatiles.bin").write_bytes(defs)
        (folder / "metatile_attributes.bin").write_bytes(attrs_rse)
        (folder / "source_frlg_metatile_attributes.bin").write_bytes(raw_attrs_frlg)
        count = len(defs) // 16
        bvd = struct.pack("<I", count) + defs + attrs_rse + b"RSE "
        (folder / "metatiles.bvd").write_bytes(bvd)
        meta = {
            "id": key,
            "role": role,
            "source_engine": "firered",
            "normalized_engine": "emerald",
            "normalization": "frlg_640_384_to_rse_512_512_global_ids_preserved",
            "tile_count": len(tiles) // 32,
            "metatile_count": count,
            "palette_banks": palette_banks,
            "source": source,
            "behavior_ids_over_255_truncated_in_rse_compat_attrs": behavior_overflow,
            "raw_frlg_attributes": str((folder / "source_frlg_metatile_attributes.bin").relative_to(self.out)),
            "sha256": {
                "tiles_4bpp": hashlib.sha256(tiles).hexdigest(),
                "metatiles_bvd": hashlib.sha256(bvd).hexdigest(),
                "raw_frlg_attributes": hashlib.sha256(raw_attrs_frlg).hexdigest(),
            },
        }
        (folder / "tileset.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        self.tileset_manifest[key] = meta
        return key

    def extract_tileset_pair(self, primary_off: int, secondary_off: int) -> Tuple[str, str]:
        pair = (primary_off, secondary_off)
        if pair in self._pair_cache:
            return self._pair_cache[pair]
        p = self.s.parse_tileset(primary_off)
        q = self.s.parse_tileset(secondary_off)
        if not p or not q:
            raise RuntimeError("Invalid FireRed tileset pair")

        p_tiles = self._source_tiles(p, self.SRC_PRIMARY_TILES)
        q_tiles = self._source_tiles(q, self.SRC_SECONDARY_TILES)
        p_defs = self.s.data[p.metatiles_offset:p.metatiles_offset + self.SRC_PRIMARY_METATILES * 16]
        q_defs = self.s.data[q.metatiles_offset:q.metatiles_offset + self.SRC_SECONDARY_METATILES * 16]
        p_attrs_raw = self.s.data[p.attributes_offset:p.attributes_offset + self.SRC_PRIMARY_METATILES * 4]
        q_attrs_raw = self.s.data[q.attributes_offset:q.attributes_offset + self.SRC_SECONDARY_METATILES * 4]
        p_defs = self._ensure_size(p_defs, self.SRC_PRIMARY_METATILES * 16)
        q_defs = self._ensure_size(q_defs, self.SRC_SECONDARY_METATILES * 16)
        p_attrs_raw = self._ensure_size(p_attrs_raw, self.SRC_PRIMARY_METATILES * 4)
        q_attrs_raw = self._ensure_size(q_attrs_raw, self.SRC_SECONDARY_METATILES * 4)

        prim_tiles = p_tiles[:self.DST_PRIMARY * 32]
        prim_defs = p_defs[:self.DST_PRIMARY * 16]
        prim_raw_attrs = p_attrs_raw[:self.DST_PRIMARY * 4]
        prim_attrs, prim_ov = self._convert_attrs(prim_raw_attrs)
        donor_tag = {
            "bwa_demo_v2": "BWA",
            "swsh_ultimate_plus": "SWSH",
            "catalyst": "CATALYST",
        }.get(self.s.profile_key, self.s.profile_key.upper())

        p_key = f"primary_f2e_{donor_tag}_{legacy.offset_to_gba(primary_off):08X}"
        p_key = self._write_normalized_tileset(
            p_key, "primary", prim_tiles, prim_defs, prim_attrs, prim_raw_attrs,
            [(i, p) for i in range(6)],
            {
                "primary_tileset_struct": legacy.ptr_hex(primary_off),
                "tiles_pointer": legacy.ptr_hex(p.tiles_offset),
                "palette_pointer": legacy.ptr_hex(p.palettes_offset),
                "metatiles_pointer": legacy.ptr_hex(p.metatiles_offset),
                "attributes_pointer": legacy.ptr_hex(p.attributes_offset),
                "compression_mode": self.tileset_decode_modes.get(p.offset),
            },
            prim_ov,
        )

        # Move FireRed primary slots 512..639 in front of its 384 secondary slots.
        # The resulting Emerald secondary bank has 512 entries and source global IDs are unchanged.
        sec_tiles = p_tiles[512*32:640*32] + q_tiles[:384*32]
        sec_defs = p_defs[512*16:640*16] + q_defs[:384*16]
        sec_raw_attrs = p_attrs_raw[512*4:640*4] + q_attrs_raw[:384*4]
        sec_attrs, sec_ov = self._convert_attrs(sec_raw_attrs)
        pair_tag = f"P{legacy.offset_to_gba(primary_off):08X}S{legacy.offset_to_gba(secondary_off):08X}"
        s_key = f"secondary_f2e_{donor_tag}_{pair_tag}"
        palette_specs = [(6, p)] + [(i, q) for i in range(7, 13)]
        s_key = self._write_normalized_tileset(
            s_key, "secondary", sec_tiles, sec_defs, sec_attrs, sec_raw_attrs,
            palette_specs,
            {
                "primary_tileset_struct_for_moved_128": legacy.ptr_hex(primary_off),
                "secondary_tileset_struct": legacy.ptr_hex(secondary_off),
                "primary_palette_pointer": legacy.ptr_hex(p.palettes_offset),
                "secondary_palette_pointer": legacy.ptr_hex(q.palettes_offset),
                "secondary_tiles_pointer": legacy.ptr_hex(q.tiles_offset),
                "secondary_metatiles_pointer": legacy.ptr_hex(q.metatiles_offset),
                "secondary_attributes_pointer": legacy.ptr_hex(q.attributes_offset),
                "compression_mode": self.tileset_decode_modes.get(q.offset),
            },
            sec_ov,
        )
        self._pair_cache[pair] = (p_key, s_key)
        return p_key, s_key

    def make_am195_visual_map(self, layout: legacy.LayoutInfo) -> bytes:
        border_width, border_height = self.s.layout_border_sizes.get(layout.offset, (2, 2))
        border_bytes = self.s.data[layout.border_offset:layout.border_offset + border_width * border_height * 2]
        block_bytes = self.s.data[layout.blockdata_offset:layout.blockdata_offset + layout.width * layout.height * 2]
        header = bytearray(52)
        struct.pack_into("<I", header, 0x00, layout.width)
        struct.pack_into("<I", header, 0x04, layout.height)
        struct.pack_into("<I", header, 0x08, 0)
        struct.pack_into("<I", header, 0x0C, 1)
        header[0x10] = border_width
        header[0x11] = border_height
        header[0x14:0x18] = self.s.game_code.encode("ascii", "replace")[:4].ljust(4, b" ")
        struct.pack_into("<I", header, 0x18, 52)
        return bytes(header) + border_bytes + block_bytes

    def render_preview(self, folder: Path, width: int, height: int, blockdata: bytes, p_key: str, s_key: str) -> None:
        try:
            from PIL import Image
        except Exception:
            return
        pdir = self.out / "tilesets" / p_key
        sdir = self.out / "tilesets" / s_key
        tiles = (pdir / "tiles.4bpp").read_bytes() + (sdir / "tiles.4bpp").read_bytes()
        metas = (pdir / "metatiles.bin").read_bytes() + (sdir / "metatiles.bin").read_bytes()
        palettes = []
        for slot in range(13):
            src = pdir if slot <= 5 else sdir
            pal = src / "palettes" / f"{slot:02d}.pal"
            lines = pal.read_text().splitlines()[3:19]
            palettes.append([tuple(map(int, line.split())) + (255,) for line in lines])
        def tile_pixels(tile_id: int):
            base = tile_id * 32
            if base + 32 > len(tiles):
                return [[0]*8 for _ in range(8)]
            out=[]
            for y in range(8):
                row=[]
                for x in range(4):
                    b=tiles[base+y*4+x]
                    row += [b & 0xF, (b>>4)&0xF]
                out.append(row)
            return out
        cache={}
        def meta(mid: int):
            if mid in cache: return cache[mid]
            img=Image.new("RGBA",(16,16),(0,0,0,0)); px=img.load(); base=mid*16
            if base+16 > len(metas): return img
            words=struct.unpack_from("<8H",metas,base)
            for layer in (0,1):
                for q in range(4):
                    w=words[layer*4+q]; tid=w&0x3FF; hf=bool(w&0x400); vf=bool(w&0x800); pal=(w>>12)&0xF
                    tp=tile_pixels(tid); ox=(q%2)*8; oy=(q//2)*8
                    if pal>=len(palettes): continue
                    for y in range(8):
                        sy=7-y if vf else y
                        for x in range(8):
                            sx=7-x if hf else x; ci=tp[sy][sx]
                            if layer==1 and ci==0: continue
                            px[ox+x,oy+y]=palettes[pal][ci]
            cache[mid]=img; return img
        out=Image.new("RGBA",(width*16,height*16),(0,0,0,255))
        for y in range(height):
            for x in range(width):
                raw=struct.unpack_from("<H",blockdata,(y*width+x)*2)[0]
                out.alpha_composite(meta(raw&0x3FF),(x*16,y*16))
        out.convert("RGB").save(folder/"preview.png")

    def extract_map(self, m: legacy.MapInfo) -> dict:
        header = self.s.parse_header(m.header_offset)
        if not header:
            raise RuntimeError(f"Cannot parse map header {m.id}")
        layout: legacy.LayoutInfo = header["layout"]
        primary_key, secondary_key = self.extract_tileset_pair(layout.primary_tileset_offset, layout.secondary_tileset_offset)
        name = legacy.sanitize_name(m.name)
        folder = self.out / "maps" / f"{m.group:02d}.{m.number:02d}_{name}"
        folder.mkdir(parents=True, exist_ok=True)
        visual = self.make_am195_visual_map(layout)
        (folder / f"{m.group}.{m.number}_{name}.map").write_bytes(visual)
        bw, bh = self.s.layout_border_sizes.get(layout.offset, (2, 2))
        border = self.s.data[layout.border_offset:layout.border_offset + bw*bh*2]
        blockdata = self.s.data[layout.blockdata_offset:layout.blockdata_offset + layout.width*layout.height*2]
        (folder / "border.bin").write_bytes(border)
        (folder / "blockdata.bin").write_bytes(blockdata)
        connections = self.s.parse_connections(m.header_offset)
        warps, warp_counts = self.s.parse_warps(m.header_offset)
        npcs, event_counts = self.s.parse_npcs(m.header_offset)
        coord_events, _ = self.s.parse_coord_events(m.header_offset)
        bg_events, _ = self.s.parse_bg_events(m.header_offset)
        map_scripts = self.s.parse_map_scripts(m.header_offset)
        for npc in npcs:
            npc["sprite_key"] = f"gfx_{int(npc.get('graphics_id',0)):03d}"
            npc["sprite_status"] = "not_extracted_frlg_profile"
            npc["sprite_preview"] = None
            npc["sprite_sheet"] = None
            npc["sprite_project_import_safe"] = False
        for filename, obj in (
            ("connections.json",connections),("warps.json",warps),("npcs.json",npcs),
            ("coord_events.json",coord_events),("bg_events.json",bg_events),("map_scripts.json",map_scripts),
        ):
            (folder/filename).write_text(json.dumps(obj,indent=2),encoding="utf-8")
        scripts_payload={"status":"not_decompiled_for_firered_profile_v1.1","roots":[],"reachable_script_pointers":[],"scripts":[]}
        (folder/"scripts.json").write_text(json.dumps(scripts_payload,indent=2),encoding="utf-8")
        meta={
            "id":m.id,"group":m.group,"map":m.number,"name":m.name,
            "header_pointer":legacy.ptr_hex(m.header_offset),"layout_pointer":legacy.ptr_hex(layout.offset),
            "width":layout.width,"height":layout.height,
            "border":{"width":bw,"height":bh,"pointer":legacy.ptr_hex(layout.border_offset)},
            "blockdata_pointer":legacy.ptr_hex(layout.blockdata_offset),
            "primary_tileset":primary_key,"secondary_tileset":secondary_key,
            "source_engine":"firered","normalized_engine":"emerald",
            "normalization":"frlg_640_384_to_rse_512_512_global_ids_preserved",
            "region_map_section_id":m.region_map_section_id,
            "region_map_section_name":self.s.region_map_names.get(m.region_map_section_id,m.name),
            "map_type":m.map_type,"weather":m.weather,"music":m.music,"layout_id":m.layout_id,
            "show_map_name":bool(header.get("show_map_name",True)),
            "allow_cycling":bool(header.get("allow_cycling",False)),
            "allow_escaping":bool(header.get("allow_escaping",False)),
            "allow_running":bool(header.get("allow_running",True)),
            "battle_type":int(header.get("battle_type",0)),
            "connections":connections,"warps":warps,"npcs":npcs,"coord_events":coord_events,"bg_events":bg_events,
            "map_scripts":map_scripts,"script_summary":{"root_count":0,"reachable_script_count":0},
            "event_counts":event_counts,
            "visual_map_sha256":hashlib.sha256(visual).hexdigest(),
            "blockdata_sha256":hashlib.sha256(blockdata).hexdigest(),
        }
        (folder/"map.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")
        self.render_preview(folder,layout.width,layout.height,blockdata,primary_key,secondary_key)
        return meta

    def extract(self, maps: Iterable[legacy.MapInfo]) -> dict:
        self.out.mkdir(parents=True, exist_ok=True)
        selected=list(maps)
        map_metas=[self.extract_map(m) for m in selected]
        manifest={
            "format":"A-Map Batch Bridge v1.1",
            "scope":"FireRed donor visual/world extraction normalized to the proven Emerald A-Map Batch Bridge package contract; NPC/warp/coord/bg events and map connections preserved; source scripts kept pointer-structural only in v1.1",
            "rom":self.s.diagnostics()["rom"],
            "profile":self.s.profile_key,
            "profile_label":self.s.profile["label"],
            "source_engine":"firered","package_engine":"emerald",
            "normalization":"frlg_640_384_to_rse_512_512_global_ids_preserved",
            "scanner":self.s.diagnostics(),"maps":map_metas,"tilesets":self.tileset_manifest,
            "sprites":{},"sprite_diagnostics":{"status":"deferred_for_firered_profile_v1.1"},
            "script_diagnostics":{"status":"deferred_for_firered_profile_v1.1"},
            "warnings":self.warnings,
        }
        (self.out/"manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
        return manifest
