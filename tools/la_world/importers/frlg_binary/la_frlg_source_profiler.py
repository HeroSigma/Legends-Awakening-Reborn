#!/usr/bin/env python3
"""
LA FireRed Source Profiler v0.1
Read-only profiler for FireRed-derived GBA donor ROMs.

Goals:
- Fingerprint the ROM.
- Parse optional IPS provenance.
- Scan for plausible FireRed MapHeader / MapLayout structures.
- Rank candidate map-group master tables.
- Decode a master table when supplied explicitly.
- Emit JSON + Markdown reports.

No ROM bytes are modified.
"""

from __future__ import annotations
import argparse
import hashlib
import json
import struct
import sys
from array import array
from pathlib import Path

GBA_BASE = 0x08000000

def u16(data: bytes, off: int) -> int:
    return struct.unpack_from("<H", data, off)[0]

def u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]

def s32(data: bytes, off: int) -> int:
    return struct.unpack_from("<i", data, off)[0]

def rom_ptr_to_off(ptr: int, size: int):
    off = ptr - GBA_BASE
    return off if 0 <= off < size else None

def is_rom_ptr(v: int, size: int) -> bool:
    return GBA_BASE <= v < GBA_BASE + size

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def parse_hex_int(text: str | None):
    if text is None:
        return None
    return int(text, 0)

def parse_ips(path: Path):
    data = path.read_bytes()
    if not data.startswith(b"PATCH"):
        raise ValueError("Not an IPS patch: missing PATCH header")
    pos = 5
    records = []
    total_bytes = 0
    rle_records = 0
    while pos + 3 <= len(data):
        if data[pos:pos+3] == b"EOF":
            pos += 3
            break
        off = int.from_bytes(data[pos:pos+3], "big")
        pos += 3
        if pos + 2 > len(data):
            raise ValueError("Truncated IPS record")
        size = int.from_bytes(data[pos:pos+2], "big")
        pos += 2
        if size == 0:
            if pos + 3 > len(data):
                raise ValueError("Truncated IPS RLE record")
            rle_size = int.from_bytes(data[pos:pos+2], "big")
            value = data[pos+2]
            pos += 3
            records.append((off, off + rle_size, True, value))
            total_bytes += rle_size
            rle_records += 1
        else:
            if pos + size > len(data):
                raise ValueError("Truncated IPS data record")
            pos += size
            records.append((off, off + size, False, None))
            total_bytes += size
    merged = []
    for start, end, _, _ in sorted(records):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return {
        "path": str(path),
        "sha256": sha256(data),
        "record_count": len(records),
        "rle_record_count": rle_records,
        "total_patched_bytes": total_bytes,
        "lowest_offset": min((r[0] for r in records), default=None),
        "highest_offset_exclusive": max((r[1] for r in records), default=None),
        "merged_ranges": merged,
    }

def touched(off: int | None, length: int, ranges):
    if off is None:
        return False
    end = off + length
    for a, b in ranges:
        if a < end and off < b:
            return True
    return False

def parse_layout(data: bytes, ptr: int):
    size = len(data)
    off = rom_ptr_to_off(ptr, size)
    if off is None or off + 0x1A > size:
        return None
    width = s32(data, off)
    height = s32(data, off + 4)
    border = u32(data, off + 8)
    map_ptr = u32(data, off + 0x0C)
    primary = u32(data, off + 0x10)
    secondary = u32(data, off + 0x14)
    border_width = data[off + 0x18]
    border_height = data[off + 0x19]
    return {
        "address": f"0x{ptr:08X}",
        "offset": off,
        "width": width,
        "height": height,
        "border": f"0x{border:08X}",
        "map": f"0x{map_ptr:08X}",
        "primary_tileset": f"0x{primary:08X}",
        "secondary_tileset": f"0x{secondary:08X}",
        "border_width": border_width,
        "border_height": border_height,
    }

def layout_plausible(data: bytes, ptr: int, loose=False) -> bool:
    size = len(data)
    off = rom_ptr_to_off(ptr, size)
    if off is None or off + 0x1A > size:
        return False
    w = s32(data, off)
    h = s32(data, off + 4)
    limit = 1024 if loose else 512
    if not (1 <= w <= limit and 1 <= h <= limit):
        return False
    border = u32(data, off + 8)
    map_ptr = u32(data, off + 0x0C)
    primary = u32(data, off + 0x10)
    secondary = u32(data, off + 0x14)
    if not all(is_rom_ptr(x, size) for x in (border, map_ptr, primary, secondary)):
        return False
    if not loose:
        bw = data[off + 0x18]
        bh = data[off + 0x19]
        if not (1 <= bw <= 8 and 1 <= bh <= 8):
            return False
    return True

def header_plausible(data: bytes, off: int, loose=False) -> bool:
    size = len(data)
    if off < 0 or off + 0x1C > size:
        return False
    layout_ptr = u32(data, off)
    if not layout_plausible(data, layout_ptr, loose=loose):
        return False
    if loose:
        return True
    events = u32(data, off + 4)
    scripts = u32(data, off + 8)
    conns = u32(data, off + 0x0C)
    if not all(x == 0 or is_rom_ptr(x, size) for x in (events, scripts, conns)):
        return False
    layout_id = u16(data, off + 0x12)
    cave = data[off + 0x15]
    weather = data[off + 0x16]
    map_type = data[off + 0x17]
    biking = data[off + 0x18]
    battle_type = data[off + 0x1B]
    if layout_id > 5000 or cave > 1 or weather > 30 or map_type > 20 or biking > 1 or battle_type > 20:
        return False
    return True

def scan_headers(data: bytes, loose=False):
    size = len(data)
    words = array("I")
    words.frombytes(data[:(size // 4) * 4])
    if sys.byteorder != "little":
        words.byteswap()
    out = set()
    for i, v in enumerate(words[:-7]):
        if is_rom_ptr(v, size):
            off = i * 4
            if header_plausible(data, off, loose=loose):
                out.add(off)
    return out, words

def parse_events(data: bytes, ptr: int):
    size = len(data)
    off = rom_ptr_to_off(ptr, size)
    if off is None or off + 0x14 > size:
        return None
    return {
        "address": f"0x{ptr:08X}",
        "offset": off,
        "object_count": data[off],
        "warp_count": data[off+1],
        "coord_count": data[off+2],
        "bg_count": data[off+3],
        "object_events": f"0x{u32(data, off+4):08X}",
        "warps": f"0x{u32(data, off+8):08X}",
        "coord_events": f"0x{u32(data, off+0x0C):08X}",
        "bg_events": f"0x{u32(data, off+0x10):08X}",
    }

def parse_connections(data: bytes, ptr: int):
    size = len(data)
    off = rom_ptr_to_off(ptr, size)
    if off is None or off + 8 > size:
        return None
    count = s32(data, off)
    entries = u32(data, off + 4)
    return {
        "address": f"0x{ptr:08X}",
        "offset": off,
        "count": count,
        "entries": f"0x{entries:08X}",
    }

def parse_header(data: bytes, off: int, ips_ranges=None):
    addr = GBA_BASE + off
    layout_ptr = u32(data, off)
    events_ptr = u32(data, off+4)
    scripts_ptr = u32(data, off+8)
    conns_ptr = u32(data, off+0x0C)
    layout = parse_layout(data, layout_ptr)
    events = parse_events(data, events_ptr)
    conns = parse_connections(data, conns_ptr)
    result = {
        "address": f"0x{addr:08X}",
        "offset": off,
        "map_layout": f"0x{layout_ptr:08X}",
        "events": f"0x{events_ptr:08X}",
        "map_scripts": f"0x{scripts_ptr:08X}",
        "connections": f"0x{conns_ptr:08X}",
        "music": u16(data, off+0x10),
        "map_layout_id": u16(data, off+0x12),
        "region_map_section_id": data[off+0x14],
        "cave": data[off+0x15],
        "weather": data[off+0x16],
        "map_type": data[off+0x17],
        "biking_allowed": data[off+0x18],
        "header_flags": data[off+0x19],
        "floor_number": struct.unpack_from("<b", data, off+0x1A)[0],
        "battle_type": data[off+0x1B],
        "layout": layout,
        "event_summary": events,
        "connection_summary": conns,
    }
    if ips_ranges is not None:
        result["ips_touched"] = {
            "header": touched(off, 0x1C, ips_ranges),
            "layout": touched(rom_ptr_to_off(layout_ptr, len(data)), 0x1A, ips_ranges),
            "events_header": touched(rom_ptr_to_off(events_ptr, len(data)), 0x14, ips_ranges),
            "connections_header": touched(rom_ptr_to_off(conns_ptr, len(data)), 8, ips_ranges),
        }
    return result

def pointer_runs_to_headers(data: bytes, words, headers, min_len=2):
    size = len(data)
    mask = bytearray(len(words))
    for i, v in enumerate(words):
        off = rom_ptr_to_off(v, size)
        if off in headers:
            mask[i] = 1
    runs = []
    i = 0
    while i < len(mask):
        if not mask[i]:
            i += 1
            continue
        start = i
        while i < len(mask) and mask[i]:
            i += 1
        length = i - start
        if length >= min_len:
            runs.append({"offset": start*4, "address": GBA_BASE + start*4, "length": length})
    return runs

def master_candidates(data: bytes, words, loose_headers):
    size = len(data)
    # Any word location that contains a pointer to a loose MapHeader can be a candidate
    # beginning of a per-group map pointer array.
    group_like_offsets = set()
    for i, v in enumerate(words):
        off = rom_ptr_to_off(v, size)
        if off in loose_headers:
            group_like_offsets.add(i*4)

    candidates = []
    i = 0
    while i < len(words):
        if not is_rom_ptr(words[i], size):
            i += 1
            continue
        start = i
        while i < len(words) and is_rom_ptr(words[i], size):
            i += 1
        length = i - start
        if 4 <= length <= 100:
            hits = 0
            for j in range(start, i):
                target = rom_ptr_to_off(words[j], size)
                if target in group_like_offsets:
                    hits += 1
            if hits >= 4:
                score = hits / length
                candidates.append({
                    "offset": start*4,
                    "address": GBA_BASE + start*4,
                    "pointer_run_length": length,
                    "group_like_targets": hits,
                    "score": round(score, 4),
                })
    candidates.sort(key=lambda x: (x["score"], x["group_like_targets"], x["pointer_run_length"]), reverse=True)
    return candidates[:50]

def infer_group_count(data: bytes, table_off: int, max_groups=128):
    size = len(data)
    count = 0
    for i in range(max_groups):
        pos = table_off + i*4
        if pos + 4 > size:
            break
        v = u32(data, pos)
        if not is_rom_ptr(v, size):
            break
        count += 1
    return count

def parse_master_table(data: bytes, table_addr: int, group_count: int, loose_headers, ips_ranges=None):
    size = len(data)
    table_off = rom_ptr_to_off(table_addr, size)
    if table_off is None:
        raise ValueError("Master table address is outside ROM")
    groups = []
    starts = []
    for g in range(group_count):
        ptr = u32(data, table_off + g*4)
        off = rom_ptr_to_off(ptr, size)
        starts.append((g, ptr, off))
    # Use next greater group start as a strong boundary when arrays are packed.
    all_offsets = sorted({off for _,_,off in starts if off is not None})
    for g, ptr, off in starts:
        rec = {"group": g, "array_address": f"0x{ptr:08X}", "array_offset": off, "maps": []}
        if off is None:
            groups.append(rec)
            continue
        next_bound = min((x for x in all_offsets if x > off), default=None)
        max_entries = 256
        for m in range(max_entries):
            pos = off + m*4
            if pos + 4 > size:
                break
            if next_bound is not None and pos >= next_bound:
                break
            hp = u32(data, pos)
            hoff = rom_ptr_to_off(hp, size)
            if hoff is None or hoff not in loose_headers:
                break
            rec["maps"].append(parse_header(data, hoff, ips_ranges))
        rec["map_count"] = len(rec["maps"])
        groups.append(rec)
    return {
        "master_address": f"0x{table_addr:08X}",
        "master_offset": table_off,
        "group_count": group_count,
        "groups": groups,
        "decoded_map_count": sum(g["map_count"] for g in groups),
    }

def make_report(profile: dict):
    rom = profile["rom"]
    lines = []
    lines.append("# LA FireRed Source Profiler v0.1")
    lines.append("")
    lines.append(f"**File:** `{rom['file']}`")
    lines.append(f"**Size:** {rom['size']} bytes")
    lines.append(f"**SHA-256:** `{rom['sha256']}`")
    lines.append(f"**Title:** `{rom['title']}`")
    lines.append(f"**Game code:** `{rom['game_code']}`")
    lines.append(f"**Revision:** {rom['revision']}")
    lines.append("")
    if profile.get("ips"):
        ips = profile["ips"]
        lines.append("## IPS provenance")
        lines.append("")
        lines.append(f"- Records: {ips['record_count']}")
        lines.append(f"- RLE records: {ips['rle_record_count']}")
        lines.append(f"- Total patched bytes: {ips['total_patched_bytes']}")
        lines.append(f"- Lowest offset: `{hex(ips['lowest_offset']) if ips['lowest_offset'] is not None else 'n/a'}`")
        lines.append(f"- Highest offset exclusive: `{hex(ips['highest_offset_exclusive']) if ips['highest_offset_exclusive'] is not None else 'n/a'}`")
        lines.append("")
    scan = profile["scan"]
    lines.append("## Structural scan")
    lines.append("")
    lines.append(f"- Strict plausible MapHeaders: **{scan['strict_header_count']}**")
    lines.append(f"- Loose plausible MapHeaders: **{scan['loose_header_count']}**")
    lines.append(f"- Header-pointer runs: **{scan['pointer_run_count']}**")
    lines.append("")
    lines.append("### Top master-table candidates")
    lines.append("")
    lines.append("| Address | Pointer run | Group-like targets | Score |")
    lines.append("|---|---:|---:|---:|")
    for c in scan["master_candidates"][:12]:
        lines.append(f"| `0x{c['address']:08X}` | {c['pointer_run_length']} | {c['group_like_targets']} | {c['score']:.2f} |")
    if not scan["master_candidates"]:
        lines.append("| _none_ | | | |")
    if profile.get("decoded_master"):
        dm = profile["decoded_master"]
        lines.append("")
        lines.append("## Explicit master-table decode")
        lines.append("")
        lines.append(f"- Master: `{dm['master_address']}`")
        lines.append(f"- Groups: **{dm['group_count']}**")
        lines.append(f"- Decoded maps: **{dm['decoded_map_count']}**")
        lines.append("")
        lines.append("| Group | Array | Maps decoded |")
        lines.append("|---:|---|---:|")
        for g in dm["groups"]:
            lines.append(f"| {g['group']} | `{g['array_address']}` | {g['map_count']} |")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- This is a read-only structural profiler.")
    lines.append("- Candidate master tables are heuristics, not proof. Use `--group-table` and `--group-count` after a candidate is validated.")
    lines.append("- v0.1 intentionally does not modify or export donor assets.")
    return "\n".join(lines) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rom", type=Path)
    ap.add_argument("--ips", type=Path)
    ap.add_argument("--group-table", help="GBA address, e.g. 0x09025288")
    ap.add_argument("--group-count", type=int)
    ap.add_argument("--out-dir", type=Path, default=Path("la_profile_out"))
    args = ap.parse_args()

    data = args.rom.read_bytes()
    size = len(data)
    title = data[0xA0:0xAC].rstrip(b"\0").decode("ascii", "replace")
    game_code = data[0xAC:0xB0].decode("ascii", "replace")
    revision = data[0xBC]

    ips = parse_ips(args.ips) if args.ips else None
    ips_ranges = ips["merged_ranges"] if ips else None

    strict_headers, words = scan_headers(data, loose=False)
    loose_headers, _ = scan_headers(data, loose=True)
    runs = pointer_runs_to_headers(data, words, strict_headers)
    masters = master_candidates(data, words, loose_headers)

    profile = {
        "tool": "LA FireRed Source Profiler v0.1",
        "rom": {
            "file": args.rom.name,
            "path": str(args.rom),
            "size": size,
            "sha256": sha256(data),
            "title": title,
            "game_code": game_code,
            "revision": revision,
        },
        "ips": ips,
        "scan": {
            "strict_header_count": len(strict_headers),
            "loose_header_count": len(loose_headers),
            "pointer_run_count": len(runs),
            "top_header_pointer_runs": [
                {
                    "address": f"0x{x['address']:08X}",
                    "offset": x["offset"],
                    "length": x["length"],
                }
                for x in sorted(runs, key=lambda x: x["length"], reverse=True)[:50]
            ],
            "master_candidates": masters,
        },
    }

    if args.group_table:
        addr = parse_hex_int(args.group_table)
        off = rom_ptr_to_off(addr, size)
        if off is None:
            raise SystemExit("group table address is outside ROM")
        count = args.group_count or infer_group_count(data, off)
        profile["decoded_master"] = parse_master_table(
            data, addr, count, loose_headers, ips_ranges
        )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.rom.stem.replace(" ", "_")
    json_path = args.out_dir / f"{stem}.profile.json"
    md_path = args.out_dir / f"{stem}.report.md"
    json_path.write_text(json.dumps(profile, indent=2), encoding="utf-8")
    md_path.write_text(make_report(profile), encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Strict headers: {len(strict_headers)}")
    print(f"Loose headers: {len(loose_headers)}")
    if masters:
        best = masters[0]
        print(f"Top master candidate: 0x{best['address']:08X} score={best['score']:.2f} "
              f"targets={best['group_like_targets']}/{best['pointer_run_length']}")
    else:
        print("No master candidate found")

if __name__ == "__main__":
    main()
