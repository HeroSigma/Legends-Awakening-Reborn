#!/usr/bin/env python3
"""
LA FireRed World IR Exporter v0.3

Exports ONE selected FireRed-derived donor map into a self-contained,
read-only Legends Awakening World IR package.

Current output:
- source/provenance metadata
- FireRed MapHeader metadata
- raw layout block map and border
- decoded metatile grid CSV
- primary + secondary tileset resources
- decompressed 4bpp tile graphics
- palettes, metatiles, metatile attributes
- object/warp/coord/bg events
- map connections
- flattened PNG preview

It does not modify the donor ROM or Legends-Awakening-Reborn.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import struct
from pathlib import Path

GBA_BASE = 0x08000000

KNOWN_PROFILES = {
    "eebac86bbf0994a51d80bebe29e5d7f0f8f5cf4ec9c3fa68d7a8fc3f8928d5ef": {
        "id": "catalyst",
        "label": "Pokemon Catalyst (patched FireRed Rev 1)",
        "group_table": 0x08352718,
        "group_count": 15,
        "map_name_table": 0x083F1D1C,
        "mapsec_base": 88,
    },
    "12a2e11285b5a4c57ede151d78ad3308b9a96b406b0d41fdade6f6da57b3fef4": {
        "id": "black_white_advanced_demo_v2",
        "label": "Pokemon Black & White Advanced (Demo v2)",
        "group_table": 0x09025288,
        "group_count": 47,
        "map_name_table": 0x083F1CAC,
        "mapsec_base": 88,
    },
    "f6d2e7092831b983318b685132a19567ff5e6428665255738c4e5a63371bcce3": {
        "id": "swsh_ultimate_plus_1_2_1_2",
        "label": "Sword & Shield Ultimate+ v1.2.1.2",
        "group_table": 0x087B1010,
        "group_count": 44,
        "map_name_table": 0x083F1CAC,
        "mapsec_base": 88,
    },
}

PRIMARY_TILES = 640
SECONDARY_TILES = 384
PRIMARY_METATILES = 640
SECONDARY_METATILES = 384
PRIMARY_PALETTES = 7
SECONDARY_PALETTES = 6

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def u16(data, off):
    return struct.unpack_from("<H", data, off)[0]

def s16(data, off):
    return struct.unpack_from("<h", data, off)[0]

def u32(data, off):
    return struct.unpack_from("<I", data, off)[0]

def s32(data, off):
    return struct.unpack_from("<i", data, off)[0]

def s8(data, off):
    return struct.unpack_from("<b", data, off)[0]

def is_rom_ptr(v, size):
    return GBA_BASE <= v < GBA_BASE + size

def ptr_off(v, size):
    off = v - GBA_BASE
    return off if 0 <= off < size else None

def hx(v):
    return f"0x{v:08X}"

def read_ptr(data, ptr, n):
    off = ptr_off(ptr, len(data))
    if off is None or off + n > len(data):
        raise ValueError(f"ROM range out of bounds: {hx(ptr)} + {n}")
    return data[off:off+n]

def decode_gba_text(data, ptr, max_len=80):
    off = ptr_off(ptr, len(data))
    if off is None:
        return None
    out = []
    for b in data[off:off+max_len]:
        if b == 0xFF:
            return "".join(out)
        if b == 0x00:
            out.append(" ")
        elif 0xA1 <= b <= 0xAA:
            out.append(str(b - 0xA1))
        elif 0xBB <= b <= 0xD4:
            out.append(chr(ord("A") + b - 0xBB))
        elif 0xD5 <= b <= 0xEE:
            out.append(chr(ord("a") + b - 0xD5))
        elif b == 0x1B:
            out.append("é")
        elif b == 0xAB:
            out.append("!")
        elif b == 0xAC:
            out.append("?")
        elif b == 0xAD:
            out.append(".")
        elif b == 0xAE:
            out.append("-")
        elif b == 0xB4:
            out.append("'")
        elif b == 0xB8:
            out.append(",")
        else:
            out.append(f"<{b:02X}>")
    return None

def map_name_table(data, addr, base):
    off = ptr_off(addr, len(data))
    names = {}
    if off is None:
        return names
    for i in range(256):
        pos = off + i * 4
        if pos + 4 > len(data):
            break
        ptr = u32(data, pos)
        name = decode_gba_text(data, ptr)
        if not name:
            break
        names[base+i] = name
    return names

def parse_tileset(data, ptr):
    off = ptr_off(ptr, len(data))
    if off is None or off + 0x18 > len(data):
        raise ValueError(f"Bad tileset pointer: {hx(ptr)}")
    return {
        "address": hx(ptr),
        "is_compressed": data[off],
        "is_secondary": data[off+1],
        "tiles": u32(data, off+4),
        "palettes": u32(data, off+8),
        "metatiles": u32(data, off+0x0C),
        "callback": u32(data, off+0x10),
        "attributes": u32(data, off+0x14),
    }

def gba_lz77_decompress(data, ptr):
    off = ptr_off(ptr, len(data))
    if off is None or data[off] != 0x10:
        raise ValueError(f"Expected GBA LZ77 stream at {hx(ptr)}")
    out_len = data[off+1] | (data[off+2] << 8) | (data[off+3] << 16)
    pos = off + 4
    out = bytearray()
    while len(out) < out_len:
        flags = data[pos]
        pos += 1
        for bit in range(7, -1, -1):
            if len(out) >= out_len:
                break
            if flags & (1 << bit):
                b1 = data[pos]
                b2 = data[pos+1]
                pos += 2
                length = (b1 >> 4) + 3
                disp = (((b1 & 0xF) << 8) | b2) + 1
                for _ in range(length):
                    out.append(out[-disp])
                    if len(out) >= out_len:
                        break
            else:
                out.append(data[pos])
                pos += 1
    return bytes(out), data[off:pos]

def export_tileset(data, ptr, out_dir: Path, secondary: bool):
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = parse_tileset(data, ptr)

    tile_count = SECONDARY_TILES if secondary else PRIMARY_TILES
    metatile_count = SECONDARY_METATILES if secondary else PRIMARY_METATILES
    palette_count = SECONDARY_PALETTES if secondary else PRIMARY_PALETTES

    if ts["is_compressed"]:
        tiles_dec, tiles_comp = gba_lz77_decompress(data, ts["tiles"])
        (out_dir / "tiles.4bpp.lz").write_bytes(tiles_comp)
    else:
        tiles_dec = read_ptr(data, ts["tiles"], tile_count * 32)
        tiles_comp = None

    expected_tiles_len = tile_count * 32
    if len(tiles_dec) != expected_tiles_len:
        raise ValueError(
            f"Unexpected tileset decompressed length at {ts['address']}: "
            f"{len(tiles_dec)} != {expected_tiles_len}"
        )

    palettes = read_ptr(data, ts["palettes"], palette_count * 16 * 2)
    metatiles = read_ptr(data, ts["metatiles"], metatile_count * 8 * 2)
    attrs = read_ptr(data, ts["attributes"], metatile_count * 4)

    (out_dir / "tiles.4bpp").write_bytes(tiles_dec)
    (out_dir / "palettes.gbapal").write_bytes(palettes)
    (out_dir / "metatiles.bin").write_bytes(metatiles)
    (out_dir / "metatile_attributes.bin").write_bytes(attrs)

    desc = dict(ts)
    for k in ("tiles", "palettes", "metatiles", "callback", "attributes"):
        desc[k] = hx(desc[k])
    desc.update({
        "tile_count": tile_count,
        "metatile_count": metatile_count,
        "palette_count": palette_count,
        "decompressed_tiles_bytes": len(tiles_dec),
        "compressed_tiles_bytes": len(tiles_comp) if tiles_comp is not None else None,
    })
    (out_dir / "descriptor.json").write_text(json.dumps(desc, indent=2), encoding="utf-8")

    return {
        "descriptor": desc,
        "tiles": tiles_dec,
        "palettes": palettes,
        "metatiles": metatiles,
        "attributes": attrs,
    }

def parse_events(data, events_ptr):
    off = ptr_off(events_ptr, len(data))
    if off is None:
        return {"header": None, "objects": [], "warps": [], "coord_events": [], "bg_events": []}

    oc, wc, cc, bc = data[off:off+4]
    obj_ptr = u32(data, off+4)
    warp_ptr = u32(data, off+8)
    coord_ptr = u32(data, off+0x0C)
    bg_ptr = u32(data, off+0x10)

    objects = []
    oo = ptr_off(obj_ptr, len(data))
    if oo is not None:
        for i in range(oc):
            p = oo + i * 0x18
            ranges = u16(data, p+0x0A)
            objects.append({
                "index": i,
                "local_id": data[p],
                "graphics_id": data[p+1],
                "kind": data[p+2],
                "x": s16(data, p+4),
                "y": s16(data, p+6),
                "elevation": data[p+8],
                "movement_type": data[p+9],
                "movement_range_x": ranges & 0xF,
                "movement_range_y": (ranges >> 4) & 0xF,
                "trainer_type": u16(data, p+0x0C),
                "trainer_range_or_berry_id": u16(data, p+0x0E),
                "script": hx(u32(data, p+0x10)),
                "flag_id": u16(data, p+0x14),
            })

    warps = []
    wo = ptr_off(warp_ptr, len(data))
    if wo is not None:
        for i in range(wc):
            p = wo + i * 8
            warps.append({
                "index": i,
                "x": s16(data, p),
                "y": s16(data, p+2),
                "elevation": data[p+4],
                "warp_id": data[p+5],
                "dest_map_num": data[p+6],
                "dest_map_group": data[p+7],
            })

    coords = []
    co = ptr_off(coord_ptr, len(data))
    if co is not None:
        for i in range(cc):
            p = co + i * 16
            coords.append({
                "index": i,
                "x": u16(data, p),
                "y": u16(data, p+2),
                "elevation": data[p+4],
                "trigger": u16(data, p+6),
                "index_value": u16(data, p+8),
                "script": hx(u32(data, p+0x0C)),
            })

    bgs = []
    bo = ptr_off(bg_ptr, len(data))
    if bo is not None:
        for i in range(bc):
            p = bo + i * 12
            bgs.append({
                "index": i,
                "x": u16(data, p),
                "y": u16(data, p+2),
                "elevation": data[p+4],
                "kind": data[p+5],
                "raw_union": hx(u32(data, p+8)),
            })

    return {
        "header": {
            "address": hx(events_ptr),
            "object_count": oc,
            "warp_count": wc,
            "coord_count": cc,
            "bg_count": bc,
            "object_events": hx(obj_ptr),
            "warps": hx(warp_ptr),
            "coord_events": hx(coord_ptr),
            "bg_events": hx(bg_ptr),
        },
        "objects": objects,
        "warps": warps,
        "coord_events": coords,
        "bg_events": bgs,
    }

def parse_connections(data, ptr):
    off = ptr_off(ptr, len(data))
    if off is None:
        return []
    count = s32(data, off)
    entries = u32(data, off+4)
    eo = ptr_off(entries, len(data))
    if not (0 <= count <= 32) or (count and eo is None):
        return []
    out = []
    for i in range(count):
        p = eo + i * 12
        out.append({
            "index": i,
            "direction": data[p],
            "offset": s32(data, p+4),
            "map_group": data[p+8],
            "map_num": data[p+9],
        })
    return out

def gba_color(v):
    r = (v & 0x1F) * 255 // 31
    g = ((v >> 5) & 0x1F) * 255 // 31
    b = ((v >> 10) & 0x1F) * 255 // 31
    return (r, g, b, 255)

def render_preview(layout, primary, secondary, out_path: Path):
    try:
        from PIL import Image
    except ImportError:
        return False

    all_tiles = primary["tiles"] + secondary["tiles"]
    all_metatiles = primary["metatiles"] + secondary["metatiles"]

    palettes = []
    for blob, count in ((primary["palettes"], PRIMARY_PALETTES), (secondary["palettes"], SECONDARY_PALETTES)):
        for p in range(count):
            palettes.append([
                gba_color(struct.unpack_from("<H", blob, (p*16+i)*2)[0])
                for i in range(16)
            ])

    def tile_pixels(blob):
        px = []
        for y in range(8):
            row = []
            for x in range(4):
                b = blob[y*4+x]
                row.extend([b & 0xF, (b >> 4) & 0xF])
            px.append(row)
        return px

    tile_cache = [
        tile_pixels(all_tiles[i*32:(i+1)*32])
        for i in range(len(all_tiles)//32)
    ]

    def metatile_img(mid):
        base = mid * 16
        entries = [
            struct.unpack_from("<H", all_metatiles, base + i*2)[0]
            for i in range(8)
        ]
        img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
        pix = img.load()
        for layer in (0, 1):
            for q in range(4):
                e = entries[layer*4+q]
                tid = e & 0x3FF
                hflip = bool(e & 0x400)
                vflip = bool(e & 0x800)
                pal = (e >> 12) & 0xF
                if tid >= len(tile_cache) or pal >= len(palettes):
                    continue
                tp = tile_cache[tid]
                ox, oy = (q % 2) * 8, (q // 2) * 8
                for y in range(8):
                    sy = 7-y if vflip else y
                    for x in range(8):
                        sx = 7-x if hflip else x
                        ci = tp[sy][sx]
                        if layer == 1 and ci == 0:
                            continue
                        pix[ox+x, oy+y] = palettes[pal][ci]
        return img

    width, height = layout["width"], layout["height"]
    map_raw = layout["map_raw"]
    image = Image.new("RGBA", (width*16, height*16), (0, 0, 0, 255))
    for y in range(height):
        for x in range(width):
            raw = u16(map_raw, (y*width+x)*2)
            mid = raw & 0x03FF
            image.alpha_composite(metatile_img(mid), (x*16, y*16))
    image.convert("RGB").save(out_path)
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rom", type=Path)
    ap.add_argument("--group", required=True, type=int)
    ap.add_argument("--map", required=True, dest="map_num", type=int)
    ap.add_argument("--out-dir", type=Path, required=True)
    args = ap.parse_args()

    data = args.rom.read_bytes()
    digest = sha256(data)
    profile = KNOWN_PROFILES.get(digest)
    if not profile:
        raise SystemExit("Unknown donor SHA. Add/validate a donor profile before exporting.")

    if not (0 <= args.group < profile["group_count"]):
        raise SystemExit("Group is outside donor profile.")

    master_off = ptr_off(profile["group_table"], len(data))
    group_array = u32(data, master_off + args.group*4)
    group_off = ptr_off(group_array, len(data))
    if group_off is None:
        raise SystemExit("Bad group pointer.")

    header_ptr = u32(data, group_off + args.map_num*4)
    header_off = ptr_off(header_ptr, len(data))
    if header_off is None or header_off + 0x1C > len(data):
        raise SystemExit("Bad map header pointer.")

    layout_ptr = u32(data, header_off)
    layout_off = ptr_off(layout_ptr, len(data))
    if layout_off is None:
        raise SystemExit("Bad map layout pointer.")

    width = s32(data, layout_off)
    height = s32(data, layout_off+4)
    border_ptr = u32(data, layout_off+8)
    map_ptr = u32(data, layout_off+0x0C)
    primary_ptr = u32(data, layout_off+0x10)
    secondary_ptr = u32(data, layout_off+0x14)
    border_w = data[layout_off+0x18]
    border_h = data[layout_off+0x19]

    if not (1 <= width <= 1024 and 1 <= height <= 1024):
        raise SystemExit(f"Selected map has invalid/blank layout dimensions: {width}x{height}")

    names = map_name_table(data, profile["map_name_table"], profile["mapsec_base"])
    mapsec = data[header_off+0x14]
    map_name = names.get(mapsec, f"MAPSEC_{mapsec}")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    layout_dir = args.out_dir / "layout"
    event_dir = args.out_dir / "events"
    ts_dir = args.out_dir / "tilesets"
    layout_dir.mkdir(exist_ok=True)
    event_dir.mkdir(exist_ok=True)

    map_raw = read_ptr(data, map_ptr, width*height*2)
    border_raw = read_ptr(data, border_ptr, border_w*border_h*2)
    (layout_dir / "map.bin").write_bytes(map_raw)
    (layout_dir / "border.bin").write_bytes(border_raw)

    with (layout_dir / "metatile_grid.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["x", "y", "raw", "metatile_id", "collision", "elevation"])
        for y in range(height):
            for x in range(width):
                raw = u16(map_raw, (y*width+x)*2)
                w.writerow([
                    x, y, f"0x{raw:04X}",
                    raw & 0x03FF,
                    (raw >> 10) & 0x3,
                    (raw >> 12) & 0xF,
                ])

    primary = export_tileset(data, primary_ptr, ts_dir / "primary", secondary=False)
    secondary = export_tileset(data, secondary_ptr, ts_dir / "secondary", secondary=True)

    events_ptr = u32(data, header_off+4)
    scripts_ptr = u32(data, header_off+8)
    conns_ptr = u32(data, header_off+0x0C)
    events = parse_events(data, events_ptr)
    connections = parse_connections(data, conns_ptr)

    for key in ("objects", "warps", "coord_events", "bg_events"):
        (event_dir / f"{key}.json").write_text(
            json.dumps(events[key], indent=2), encoding="utf-8"
        )
    (event_dir / "connections.json").write_text(
        json.dumps(connections, indent=2), encoding="utf-8"
    )

    layout_info = {
        "address": hx(layout_ptr),
        "width": width,
        "height": height,
        "border_address": hx(border_ptr),
        "map_address": hx(map_ptr),
        "primary_tileset": hx(primary_ptr),
        "secondary_tileset": hx(secondary_ptr),
        "border_width": border_w,
        "border_height": border_h,
        "map_file": "layout/map.bin",
        "border_file": "layout/border.bin",
        "grid_file": "layout/metatile_grid.csv",
    }

    ir = {
        "format": "LA World IR v0.1",
        "source": {
            "donor_profile": profile["id"],
            "donor_label": profile["label"],
            "rom_file": args.rom.name,
            "rom_sha256": digest,
            "engine_family": "FireRed",
            "group": args.group,
            "map": args.map_num,
            "group_array": hx(group_array),
            "header": hx(header_ptr),
        },
        "identity": {
            "map_section_id": mapsec,
            "map_section_name": map_name,
        },
        "header": {
            "music": u16(data, header_off+0x10),
            "map_layout_id": u16(data, header_off+0x12),
            "region_map_section_id": mapsec,
            "cave": data[header_off+0x15],
            "weather": data[header_off+0x16],
            "map_type": data[header_off+0x17],
            "biking_allowed": data[header_off+0x18],
            "header_flags": data[header_off+0x19],
            "floor_number": s8(data, header_off+0x1A),
            "battle_type": data[header_off+0x1B],
            "scripts_pointer": hx(scripts_ptr),
        },
        "layout": layout_info,
        "tilesets": {
            "primary": primary["descriptor"],
            "secondary": secondary["descriptor"],
        },
        "events": {
            "header": events["header"],
            "objects_file": "events/objects.json",
            "warps_file": "events/warps.json",
            "coord_events_file": "events/coord_events.json",
            "bg_events_file": "events/bg_events.json",
        },
        "connections": {
            "header_pointer": hx(conns_ptr),
            "file": "events/connections.json",
            "count": len(connections),
        },
        "preview": "preview.png",
        "policy": {
            "source_scripts_preserved_as_pointer_only": True,
            "source_story_logic_imported": False,
            "rom_modified": False,
            "legends_awakening_modified": False,
        },
    }

    (args.out_dir / "world_ir.json").write_text(
        json.dumps(ir, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    preview_layout = dict(layout_info)
    preview_layout["map_raw"] = map_raw
    preview_ok = render_preview(preview_layout, primary, secondary, args.out_dir / "preview.png")

    readme = f"""# LA World IR export

**Map:** {map_name}
**Donor:** {profile['label']}
**Source map:** group {args.group}, map {args.map_num}
**Source header:** `{hx(header_ptr)}`
**Layout:** {width} × {height} metatiles
**Objects / warps / coord / bg:** {len(events['objects'])} / {len(events['warps'])} / {len(events['coord_events'])} / {len(events['bg_events'])}
**Connections:** {len(connections)}
**Preview generated:** {'yes' if preview_ok else 'no'}

This package is read-only source material for Legends Awakening Reborn.
No donor scripts or story logic have been converted into LA runtime code.
"""
    (args.out_dir / "README.md").write_text(readme, encoding="utf-8")

    print(f"Exported {profile['label']} group {args.group} map {args.map_num}")
    print(f"Map section: {mapsec} / {map_name}")
    print(f"Layout: {width}x{height}")
    print(f"Header: {hx(header_ptr)}")
    print(f"Primary tileset: {hx(primary_ptr)}")
    print(f"Secondary tileset: {hx(secondary_ptr)}")
    print(f"Events: objects={len(events['objects'])} warps={len(events['warps'])} "
          f"coord={len(events['coord_events'])} bg={len(events['bg_events'])}")
    print(f"Connections: {len(connections)}")
    print(f"Preview: {'generated' if preview_ok else 'not generated'}")
    print(f"Output: {args.out_dir}")

if __name__ == "__main__":
    main()
