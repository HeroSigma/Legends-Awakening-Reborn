#!/usr/bin/env python3
"""
LA FireRed Source Profiler v0.2

Read-only structural census tool for FireRed-derived donor ROMs used by
Legends Awakening Reborn.

v0.2 adds:
- SHA-256 donor profiles for Catalyst, Black & White Advanced, and SWSH Ultimate+
- validated/known gMapGroups addresses for those donor builds
- map-section name table decoding
- group/map census including stale/blank header slots
- MapHeader, MapLayout, events, and connection summaries
- CSV + JSON + Markdown output
- optional IPS provenance
- conservative handling of the final group when no next group boundary exists

No ROM bytes are modified.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import struct
from pathlib import Path

GBA_BASE = 0x08000000
MAPSEC_BASE_FRLG = 88
MAX_GROUP_SLOTS = 512

KNOWN_PROFILES = {
    "eebac86bbf0994a51d80bebe29e5d7f0f8f5cf4ec9c3fa68d7a8fc3f8928d5ef": {
        "id": "catalyst",
        "label": "Pokemon Catalyst (patched FireRed Rev 1)",
        "group_table": 0x08352718,
        "group_count": 15,
        "map_name_table": 0x083F1D1C,
        "mapsec_base": 88,
        "notes": [
            "gMapGroups address is corroborated by a direct ROM code/data reference.",
            "Catalyst retains a truncated/partial FireRed group set in this build.",
            "The final group's boundary is not followed by another active group pointer, so v0.2 uses conservative layout-valid termination there."
        ],
    },
    "12a2e11285b5a4c57ede151d78ad3308b9a96b406b0d41fdade6f6da57b3fef4": {
        "id": "black_white_advanced_demo_v2",
        "label": "Pokemon Black & White Advanced (Demo v2)",
        "group_table": 0x09025288,
        "group_count": 47,
        "map_name_table": 0x083F1CAC,
        "mapsec_base": 88,
        "notes": [
            "47/47 master-table entries resolve to group-like structures.",
            "Groups 43-46 are donor-added/relocated groups beyond the vanilla FireRed 0-42 range."
        ],
    },
    "f6d2e7092831b983318b685132a19567ff5e6428665255738c4e5a63371bcce3": {
        "id": "swsh_ultimate_plus_1_2_1_2",
        "label": "Sword & Shield Ultimate+ v1.2.1.2",
        "group_table": 0x087B1010,
        "group_count": 44,
        "map_name_table": 0x083F1CAC,
        "mapsec_base": 88,
        "notes": [
            "The master table begins at 0x087B1010; four unrelated pointers immediately precede it.",
            "Some legacy FireRed map slots remain structurally present while their layouts are blank/stale. v0.2 reports those separately from usable layouts."
        ],
    },
}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def u16(data: bytes, off: int) -> int:
    return struct.unpack_from("<H", data, off)[0]

def u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]

def s32(data: bytes, off: int) -> int:
    return struct.unpack_from("<i", data, off)[0]

def s8(data: bytes, off: int) -> int:
    return struct.unpack_from("<b", data, off)[0]

def is_rom_ptr(v: int, size: int) -> bool:
    return GBA_BASE <= v < GBA_BASE + size

def ptr_to_off(v: int, size: int):
    off = v - GBA_BASE
    return off if 0 <= off < size else None

def hx(v):
    return None if v is None else f"0x{v:08X}"

def parse_int(text):
    return int(text, 0) if text is not None else None

def parse_ips(path: Path):
    raw = path.read_bytes()
    if not raw.startswith(b"PATCH"):
        raise ValueError("Not an IPS patch")
    pos = 5
    records = []
    rle_count = 0
    total = 0
    while pos + 3 <= len(raw):
        if raw[pos:pos+3] == b"EOF":
            pos += 3
            break
        off = int.from_bytes(raw[pos:pos+3], "big")
        pos += 3
        if pos + 2 > len(raw):
            raise ValueError("Truncated IPS record")
        n = int.from_bytes(raw[pos:pos+2], "big")
        pos += 2
        if n == 0:
            if pos + 3 > len(raw):
                raise ValueError("Truncated IPS RLE record")
            rn = int.from_bytes(raw[pos:pos+2], "big")
            value = raw[pos+2]
            pos += 3
            records.append((off, off + rn, True, value))
            rle_count += 1
            total += rn
        else:
            if pos + n > len(raw):
                raise ValueError("Truncated IPS data")
            pos += n
            records.append((off, off + n, False, None))
            total += n

    merged = []
    for a, b, _, _ in sorted(records):
        if not merged or a > merged[-1][1]:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)

    return {
        "file": path.name,
        "sha256": sha256(raw),
        "record_count": len(records),
        "rle_record_count": rle_count,
        "total_patched_bytes": total,
        "lowest_offset": min((x[0] for x in records), default=None),
        "highest_offset_exclusive": max((x[1] for x in records), default=None),
        "merged_ranges": merged,
    }

def range_touched(off, length, ranges):
    if off is None:
        return False
    end = off + length
    return any(a < end and off < b for a, b in ranges)

# A practical subset of the Gen III English charmap sufficient for location names.
def decode_gba_text(data: bytes, ptr: int, max_len: int = 80):
    off = ptr_to_off(ptr, len(data))
    if off is None:
        return None
    out = []
    terminated = False
    for b in data[off:off+max_len]:
        if b == 0xFF:
            terminated = True
            break
        if b == 0x00:
            out.append(" ")
        elif 0xA1 <= b <= 0xAA:
            out.append(str(b - 0xA1))
        elif 0xBB <= b <= 0xD4:
            out.append(chr(ord("A") + b - 0xBB))
        elif 0xD5 <= b <= 0xEE:
            out.append(chr(ord("a") + b - 0xD5))
        elif b == 0xAB:
            out.append("!")
        elif b == 0xAC:
            out.append("?")
        elif b == 0xAD:
            out.append(".")
        elif b == 0xAE:
            out.append("-")
        elif b == 0xB0:
            out.append("…")
        elif b == 0xB1:
            out.append("“")
        elif b == 0xB2:
            out.append("”")
        elif b == 0xB3:
            out.append("‘")
        elif b == 0xB4:
            out.append("'")
        elif b == 0xB8:
            out.append(",")
        elif b == 0xB9:
            out.append("×")
        elif b == 0x1B:
            out.append("é")
        elif b == 0xB3:
            out.append("'")
        else:
            out.append(f"<{b:02X}>")
    if not terminated:
        return None
    return "".join(out)

def parse_map_name_table(data: bytes, addr: int, mapsec_base: int, max_entries=256):
    off = ptr_to_off(addr, len(data))
    if off is None:
        raise ValueError("Map-name table outside ROM")
    entries = []
    for i in range(max_entries):
        pos = off + i * 4
        if pos + 4 > len(data):
            break
        ptr = u32(data, pos)
        text = decode_gba_text(data, ptr)
        if text is None or not text or len(text) > 64:
            break
        entries.append({
            "table_index": i,
            "mapsec_id": mapsec_base + i,
            "pointer": ptr,
            "address": hx(ptr),
            "name": text,
        })
    return entries

def parse_layout(data: bytes, ptr: int):
    off = ptr_to_off(ptr, len(data))
    if off is None or off + 0x1A > len(data):
        return None
    return {
        "address": hx(ptr),
        "offset": off,
        "width": s32(data, off),
        "height": s32(data, off + 4),
        "border": hx(u32(data, off + 8)),
        "map": hx(u32(data, off + 0x0C)),
        "primary_tileset": hx(u32(data, off + 0x10)),
        "secondary_tileset": hx(u32(data, off + 0x14)),
        "border_width": data[off + 0x18],
        "border_height": data[off + 0x19],
    }

def layout_valid(data: bytes, ptr: int):
    lay = parse_layout(data, ptr)
    if not lay:
        return False
    if not (1 <= lay["width"] <= 1024 and 1 <= lay["height"] <= 1024):
        return False
    for key in ("border", "map", "primary_tileset", "secondary_tileset"):
        v = int(lay[key], 16)
        if not is_rom_ptr(v, len(data)):
            return False
    return True

def header_shell_valid(data: bytes, off: int):
    if off is None or off % 4 or off < 0 or off + 0x1C > len(data):
        return False
    size = len(data)
    layout_ptr = u32(data, off)
    events = u32(data, off + 4)
    scripts = u32(data, off + 8)
    conns = u32(data, off + 0x0C)

    if not is_rom_ptr(layout_ptr, size):
        return False
    if not all(v == 0 or is_rom_ptr(v, size) for v in (events, scripts, conns)):
        return False

    if u16(data, off + 0x12) >= 4096:
        return False
    if data[off + 0x15] > 1:
        return False
    if data[off + 0x16] >= 64:
        return False
    if data[off + 0x17] >= 32:
        return False
    if data[off + 0x18] > 1:
        return False
    if data[off + 0x1B] >= 32:
        return False
    return True

def header_candidate(data: bytes, off: int):
    if off is None:
        return False
    lp = u32(data, off) if off + 4 <= len(data) else 0
    return header_shell_valid(data, off) or layout_valid(data, lp)

def parse_events(data: bytes, ptr: int):
    off = ptr_to_off(ptr, len(data))
    if off is None or off + 0x14 > len(data):
        return None
    return {
        "address": hx(ptr),
        "offset": off,
        "object_count": data[off],
        "warp_count": data[off + 1],
        "coord_count": data[off + 2],
        "bg_count": data[off + 3],
        "object_events": hx(u32(data, off + 4)),
        "warps": hx(u32(data, off + 8)),
        "coord_events": hx(u32(data, off + 0x0C)),
        "bg_events": hx(u32(data, off + 0x10)),
    }

def parse_connections(data: bytes, ptr: int):
    off = ptr_to_off(ptr, len(data))
    if off is None or off + 8 > len(data):
        return None
    count = s32(data, off)
    entries = u32(data, off + 4)
    # Avoid presenting obviously bogus stale values as authoritative.
    plausible = 0 <= count <= 32 and (count == 0 or is_rom_ptr(entries, len(data)))
    return {
        "address": hx(ptr),
        "offset": off,
        "count": count if plausible else None,
        "entries": hx(entries),
        "plausible": plausible,
    }

def parse_header(data: bytes, ptr: int, names_by_id, ips_ranges=None):
    off = ptr_to_off(ptr, len(data))
    if off is None or off + 0x1C > len(data):
        return None

    layout_ptr = u32(data, off)
    events_ptr = u32(data, off + 4)
    scripts_ptr = u32(data, off + 8)
    conns_ptr = u32(data, off + 0x0C)
    region_id = data[off + 0x14]
    lay_valid = layout_valid(data, layout_ptr)
    lay = parse_layout(data, layout_ptr)

    rec = {
        "address": hx(ptr),
        "offset": off,
        "layout_ptr": hx(layout_ptr),
        "events_ptr": hx(events_ptr),
        "scripts_ptr": hx(scripts_ptr),
        "connections_ptr": hx(conns_ptr),
        "music": u16(data, off + 0x10),
        "map_layout_id": u16(data, off + 0x12),
        "region_map_section_id": region_id,
        "map_section_name": names_by_id.get(region_id),
        "cave": data[off + 0x15],
        "weather": data[off + 0x16],
        "map_type": data[off + 0x17],
        "biking_allowed": data[off + 0x18],
        "header_flags": data[off + 0x19],
        "floor_number": s8(data, off + 0x1A),
        "battle_type": data[off + 0x1B],
        "layout_valid": lay_valid,
        "layout": lay if lay_valid else None,
        "events": parse_events(data, events_ptr),
        "connections": parse_connections(data, conns_ptr),
    }

    if ips_ranges is not None:
        rec["ips_touched"] = {
            "header": range_touched(off, 0x1C, ips_ranges),
            "layout_header": range_touched(ptr_to_off(layout_ptr, len(data)), 0x1A, ips_ranges),
            "events_header": range_touched(ptr_to_off(events_ptr, len(data)), 0x14, ips_ranges),
            "connections_header": range_touched(ptr_to_off(conns_ptr, len(data)), 8, ips_ranges),
        }

    return rec

def enumerate_groups(data: bytes, group_table_addr: int, group_count: int, names_by_id, ips_ranges=None):
    master_off = ptr_to_off(group_table_addr, len(data))
    if master_off is None:
        raise ValueError("gMapGroups table outside ROM")

    group_ptrs = [u32(data, master_off + i * 4) for i in range(group_count)]
    group_starts = {ptr_to_off(p, len(data)) for p in group_ptrs if is_rom_ptr(p, len(data))}
    groups = []

    for gi, gp in enumerate(group_ptrs):
        goff = ptr_to_off(gp, len(data))
        group = {
            "group": gi,
            "array_address": hx(gp),
            "array_offset": goff,
            "slots": [],
            "boundary_reason": None,
        }
        if goff is None:
            group["boundary_reason"] = "group pointer outside ROM"
            groups.append(group)
            continue

        # The final group has no next active-group boundary. For that one, stop
        # at the first layout-invalid entry to avoid flowing into abandoned
        # adjacent pointer arrays (important for the Catalyst partial table).
        conservative_final = (gi == group_count - 1)

        for mi in range(MAX_GROUP_SLOTS):
            pos = goff + mi * 4
            if pos + 4 > len(data):
                group["boundary_reason"] = "end of ROM"
                break
            if mi > 0 and pos in group_starts:
                group["boundary_reason"] = "next active group array"
                break

            hp = u32(data, pos)
            hoff = ptr_to_off(hp, len(data))
            if hoff is None:
                group["boundary_reason"] = "non-ROM map-header pointer"
                break

            if conservative_final:
                if not layout_valid(data, u32(data, hoff) if hoff + 4 <= len(data) else 0):
                    group["boundary_reason"] = "final-group conservative layout boundary"
                    break
            else:
                if not header_candidate(data, hoff):
                    group["boundary_reason"] = "non-header candidate"
                    break

            header = parse_header(data, hp, names_by_id, ips_ranges)
            if header is None:
                group["boundary_reason"] = "unparseable header"
                break

            group["slots"].append({
                "map": mi,
                "pointer_slot_address": hx(GBA_BASE + pos),
                "header": header,
            })
        else:
            group["boundary_reason"] = f"hard cap {MAX_GROUP_SLOTS}"

        group["slot_count"] = len(group["slots"])
        group["usable_map_count"] = sum(1 for x in group["slots"] if x["header"]["layout_valid"])
        group["stale_or_blank_count"] = group["slot_count"] - group["usable_map_count"]
        groups.append(group)

    return groups

def flatten_rows(groups):
    rows = []
    for g in groups:
        for s in g["slots"]:
            h = s["header"]
            lay = h["layout"]
            ev = h["events"] or {}
            cn = h["connections"] or {}
            rows.append({
                "group": g["group"],
                "map": s["map"],
                "header": h["address"],
                "layout_valid": h["layout_valid"],
                "map_section_id": h["region_map_section_id"],
                "map_section_name": h["map_section_name"] or "",
                "width": lay["width"] if lay else "",
                "height": lay["height"] if lay else "",
                "layout": h["layout_ptr"],
                "primary_tileset": lay["primary_tileset"] if lay else "",
                "secondary_tileset": lay["secondary_tileset"] if lay else "",
                "objects": ev.get("object_count", ""),
                "warps": ev.get("warp_count", ""),
                "coord_events": ev.get("coord_count", ""),
                "bg_events": ev.get("bg_count", ""),
                "connections": cn.get("count", ""),
                "music": h["music"],
                "weather": h["weather"],
                "map_type": h["map_type"],
            })
    return rows

def write_csv(path: Path, rows):
    fields = [
        "group", "map", "header", "layout_valid", "map_section_id",
        "map_section_name", "width", "height", "layout", "primary_tileset",
        "secondary_tileset", "objects", "warps", "coord_events", "bg_events",
        "connections", "music", "weather", "map_type",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def coverage(groups):
    by_name = {}
    unknown = {}
    for g in groups:
        for s in g["slots"]:
            h = s["header"]
            if not h["layout_valid"]:
                continue
            sid = h["region_map_section_id"]
            name = h["map_section_name"]
            if name:
                item = by_name.setdefault(name, {"mapsec_id": sid, "maps": []})
                item["maps"].append([g["group"], s["map"], h["address"]])
            else:
                item = unknown.setdefault(str(sid), [])
                item.append([g["group"], s["map"], h["address"]])
    return {
        "named_sections": dict(sorted(by_name.items(), key=lambda kv: (kv[1]["mapsec_id"], kv[0]))),
        "unknown_mapsec_ids": unknown,
    }

def report_md(profile):
    rom = profile["rom"]
    census = profile["census"]
    lines = [
        "# LA FireRed Source Profiler v0.2",
        "",
        f"**Donor:** {profile['profile']['label']}",
        f"**File:** `{rom['file']}`",
        f"**SHA-256:** `{rom['sha256']}`",
        f"**Title / code / revision:** `{rom['title']}` / `{rom['game_code']}` / `{rom['revision']}`",
        f"**ROM size:** {rom['size']} bytes",
        "",
        "## Validated profile",
        "",
        f"- gMapGroups: `{profile['profile']['group_table']}`",
        f"- Group count: **{profile['profile']['group_count']}**",
        f"- Map-name pointer table: `{profile['profile']['map_name_table']}`",
        f"- Map-section base: **{profile['profile']['mapsec_base']}**",
        f"- Decoded map-section names: **{profile['map_name_count']}**",
        "",
        "## Census",
        "",
        f"- Candidate map-header slots: **{census['slot_count']}**",
        f"- Usable maps with valid layouts: **{census['usable_map_count']}**",
        f"- Stale/blank map slots: **{census['stale_or_blank_count']}**",
        f"- Named map sections referenced by usable maps: **{census['named_section_count']}**",
        f"- Unresolved map-section IDs referenced by usable maps: **{census['unknown_mapsec_id_count']}**",
        "",
        "### Groups",
        "",
        "| Group | Array | Slots | Usable | Stale/blank | Stop reason |",
        "|---:|---|---:|---:|---:|---|",
    ]
    for g in profile["groups"]:
        lines.append(
            f"| {g['group']} | `{g['array_address']}` | {g['slot_count']} | "
            f"{g['usable_map_count']} | {g['stale_or_blank_count']} | {g['boundary_reason']} |"
        )

    lines += ["", "## Referenced map-section names", "", "| ID | Name | Usable maps |", "|---:|---|---:|"]
    cov = profile["coverage"]["named_sections"]
    for name, item in cov.items():
        lines.append(f"| {item['mapsec_id']} | {name} | {len(item['maps'])} |")

    if profile.get("ips"):
        ips = profile["ips"]
        lines += [
            "",
            "## IPS provenance",
            "",
            f"- Patch: `{ips['file']}`",
            f"- SHA-256: `{ips['sha256']}`",
            f"- Records: **{ips['record_count']}**",
            f"- RLE records: **{ips['rle_record_count']}**",
            f"- Total patched bytes represented by records: **{ips['total_patched_bytes']}**",
        ]

    lines += ["", "## Profile notes", ""]
    for n in profile["profile"].get("notes", []):
        lines.append(f"- {n}")

    lines += [
        "",
        "## Interpretation",
        "",
        "- A **usable map** means the MapHeader resolves to a plausible FireRed MapLayout with valid ROM pointers and dimensions.",
        "- A **stale/blank slot** is still part of the donor's map-group pointer population but its layout is not currently usable as a map asset.",
        "- Map-section names identify the location label assigned by the donor. Multiple physical maps can share one label.",
        "- v0.2 is still read-only. It does not extract tileset graphics or write pokeemerald-expansion map files.",
        "",
    ]
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rom", type=Path)
    ap.add_argument("--ips", type=Path)
    ap.add_argument("--group-table")
    ap.add_argument("--group-count", type=int)
    ap.add_argument("--map-name-table")
    ap.add_argument("--mapsec-base", type=int)
    ap.add_argument("--label")
    ap.add_argument("--out-dir", type=Path, default=Path("la_profile_out"))
    args = ap.parse_args()

    data = args.rom.read_bytes()
    digest = sha256(data)
    known = KNOWN_PROFILES.get(digest, {}).copy()

    group_table = parse_int(args.group_table) if args.group_table else known.get("group_table")
    group_count = args.group_count if args.group_count is not None else known.get("group_count")
    name_table = parse_int(args.map_name_table) if args.map_name_table else known.get("map_name_table")
    mapsec_base = args.mapsec_base if args.mapsec_base is not None else known.get("mapsec_base", MAPSEC_BASE_FRLG)
    label = args.label or known.get("label") or args.rom.stem

    if group_table is None or group_count is None or name_table is None:
        raise SystemExit(
            "Unknown donor build. Supply --group-table, --group-count, and --map-name-table "
            "(or use one of the SHA-profiled donor ROMs)."
        )

    map_names = parse_map_name_table(data, name_table, mapsec_base)
    names_by_id = {x["mapsec_id"]: x["name"] for x in map_names}

    ips = parse_ips(args.ips) if args.ips else None
    ips_ranges = ips["merged_ranges"] if ips else None

    groups = enumerate_groups(data, group_table, group_count, names_by_id, ips_ranges)
    rows = flatten_rows(groups)
    cov = coverage(groups)

    profile = {
        "tool": "LA FireRed Source Profiler v0.2",
        "rom": {
            "file": args.rom.name,
            "path": str(args.rom),
            "size": len(data),
            "sha256": digest,
            "title": data[0xA0:0xAC].rstrip(b"\0").decode("ascii", "replace"),
            "game_code": data[0xAC:0xB0].decode("ascii", "replace"),
            "revision": data[0xBC],
        },
        "profile": {
            "id": known.get("id", "manual"),
            "label": label,
            "group_table": hx(group_table),
            "group_count": group_count,
            "map_name_table": hx(name_table),
            "mapsec_base": mapsec_base,
            "notes": known.get("notes", []),
        },
        "ips": ips,
        "map_name_count": len(map_names),
        "map_names": map_names,
        "groups": groups,
        "coverage": cov,
        "census": {
            "slot_count": len(rows),
            "usable_map_count": sum(1 for r in rows if r["layout_valid"]),
            "stale_or_blank_count": sum(1 for r in rows if not r["layout_valid"]),
            "named_section_count": len(cov["named_sections"]),
            "unknown_mapsec_id_count": len(cov["unknown_mapsec_ids"]),
        },
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    base = known.get("id", args.rom.stem.replace(" ", "_"))
    json_path = args.out_dir / f"{base}.profile.json"
    csv_path = args.out_dir / f"{base}.maps.csv"
    md_path = args.out_dir / f"{base}.report.md"

    json_path.write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding="utf-8")
    write_csv(csv_path, rows)
    md_path.write_text(report_md(profile), encoding="utf-8")

    print(f"Donor: {label}")
    print(f"SHA-256: {digest}")
    print(f"gMapGroups: {hx(group_table)} ({group_count} groups)")
    print(f"Map-name table: {hx(name_table)} ({len(map_names)} decoded names)")
    print(f"Candidate slots: {profile['census']['slot_count']}")
    print(f"Usable maps: {profile['census']['usable_map_count']}")
    print(f"Stale/blank slots: {profile['census']['stale_or_blank_count']}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {csv_path}")
    print(f"Wrote: {md_path}")

if __name__ == "__main__":
    main()
