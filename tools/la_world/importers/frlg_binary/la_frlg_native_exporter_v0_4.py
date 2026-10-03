#!/usr/bin/env python3

from pathlib import Path
import argparse
import hashlib
import json
import shutil
import struct
import zlib

GBA_BASE = 0x08000000

PRIMARY_TILE_BYTES = 640 * 32
SECONDARY_TILE_BYTES = 384 * 32

PRIMARY_METATILE_BYTES = 640 * 16
SECONDARY_METATILE_BYTES = 384 * 16

PRIMARY_ATTR_BYTES = 640 * 4
SECONDARY_ATTR_BYTES = 384 * 4

PALETTE_COUNT = 16
PALETTE_COLORS = 16
PALETTE_BYTES = PALETTE_COUNT * PALETTE_COLORS * 2


def die(msg):
    raise SystemExit(msg)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rom_offset(address, rom_size):
    if isinstance(address, str):
        address = int(address, 0)

    off = address - GBA_BASE

    if off < 0 or off >= rom_size:
        die(f"ROM address outside image: 0x{address:08X}")

    return off


def read_rom(rom, address, size):
    off = rom_offset(address, len(rom))

    if off + size > len(rom):
        die(f"ROM read exceeds image: 0x{address:08X} + {size}")

    return rom[off:off + size]


def gba_rgb(value):
    r5 = value & 31
    g5 = (value >> 5) & 31
    b5 = (value >> 10) & 31

    return (
        round(r5 * 255 / 31),
        round(g5 * 255 / 31),
        round(b5 * 255 / 31),
    )


def write_indexed_png_from_4bpp(path, raw_tiles, palette_data):
    """Write a Porymap-friendly 16-color indexed PNG.

    Tiles are arranged 16 tiles across, matching normal decomp tilesets.
    Pixel indices are preserved exactly from the source 4bpp graphics.
    """

    if len(raw_tiles) % 32 != 0:
        die("4bpp tile data is not a whole number of tiles")

    if len(palette_data) != 32:
        die("PNG source palette must contain exactly 16 GBA colors")

    tile_count = len(raw_tiles) // 32
    tiles_per_row = 16
    rows_of_tiles = (tile_count + tiles_per_row - 1) // tiles_per_row

    width = tiles_per_row * 8
    height = rows_of_tiles * 8

    pixels = bytearray(width * height)

    for tile_id in range(tile_count):
        tx = (tile_id % tiles_per_row) * 8
        ty = (tile_id // tiles_per_row) * 8
        base = tile_id * 32

        for y in range(8):
            for pair in range(4):
                b = raw_tiles[base + y * 4 + pair]

                x = pair * 2

                pixels[(ty + y) * width + tx + x] = b & 0x0F
                pixels[(ty + y) * width + tx + x + 1] = (b >> 4) & 0x0F

    plte = bytearray()

    for i in range(16):
        value = struct.unpack_from("<H", palette_data, i * 2)[0]
        r, g, b = gba_rgb(value)
        plte.extend((r, g, b))

    def chunk(kind, data):
        return (
            struct.pack(">I", len(data))
            + kind
            + data
            + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        )

    scanlines = bytearray()

    for y in range(height):
        scanlines.append(0)
        start = y * width
        scanlines.extend(pixels[start:start + width])

    png = bytearray(b"\x89PNG\r\n\x1a\n")
    png += chunk(
        b"IHDR",
        struct.pack(">IIBBBBB", width, height, 8, 3, 0, 0, 0)
    )
    png += chunk(b"PLTE", bytes(plte))
    png += chunk(b"IDAT", zlib.compress(bytes(scanlines), 9))
    png += chunk(b"IEND", b"")

    path.write_bytes(png)


def write_jasc_palette(path, palette_data):
    if len(palette_data) != 32:
        die(f"Palette must contain 32 bytes: {path}")

    lines = [
        "JASC-PAL",
        "0100",
        "16",
    ]

    for i in range(16):
        value = struct.unpack_from("<H", palette_data, i * 2)[0]
        r, g, b = gba_rgb(value)
        lines.append(f"{r} {g} {b}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def require_size(path, expected):
    actual = path.stat().st_size

    if actual != expected:
        die(
            f"Unexpected size for {path}\n"
            f"expected: {expected}\n"
            f"actual:   {actual}"
        )


def copy_file(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def create_tileset(
    source_dir,
    destination,
    rom,
    palette_address,
    expected_tile_bytes,
    expected_metatile_bytes,
    expected_attr_bytes,
):
    require_size(source_dir / "tiles.4bpp", expected_tile_bytes)
    require_size(source_dir / "metatiles.bin", expected_metatile_bytes)
    require_size(
        source_dir / "metatile_attributes.bin",
        expected_attr_bytes,
    )

    destination.mkdir(parents=True, exist_ok=True)

    copy_file(
        source_dir / "tiles.4bpp",
        destination / "tiles.4bpp",
    )

    copy_file(
        source_dir / "metatiles.bin",
        destination / "metatiles.bin",
    )

    copy_file(
        source_dir / "metatile_attributes.bin",
        destination / "metatile_attributes.bin",
    )

    # IMPORTANT:
    # FireRed secondary tilesets still contain a full palette table.
    # Runtime loads palettes [7] through [12].
    #
    # v0.3 incorrectly extracted only six palettes beginning at index 0.
    # v0.4 deliberately recovers the complete 16-palette table.
    raw_palettes = read_rom(
        rom,
        palette_address,
        PALETTE_BYTES,
    )

    palette_dir = destination / "palettes"
    palette_dir.mkdir(exist_ok=True)

    for i in range(PALETTE_COUNT):
        pal = raw_palettes[i * 32:(i + 1) * 32]
        write_jasc_palette(
            palette_dir / f"{i:02d}.pal",
            pal,
        )

    write_indexed_png_from_4bpp(
        destination / "tiles.png",
        (destination / "tiles.4bpp").read_bytes(),
        raw_palettes[:32],
    )


def make_tileset_header():
    palette_primary = "\n".join(
        f'    INCGFX_U16("data/tilesets/primary/la_unova_general/'
        f'palettes/{i:02d}.pal", ".gbapal"),'
        for i in range(16)
    )

    palette_secondary = "\n".join(
        f'    INCGFX_U16("data/tilesets/secondary/la_nuvema_town/'
        f'palettes/{i:02d}.pal", ".gbapal"),'
        for i in range(16)
    )

    return f'''// Auto-generated by LA FireRed Native Exporter v0.4
// Initial Legends Awakening donor tilesets.

const u32 gTilesetTiles_LA_UnovaGeneral[] =
    INCGFX_U32("data/tilesets/primary/la_unova_general/tiles.png", ".4bpp");

const u16 ALIGNED(4) gTilesetPalettes_LA_UnovaGeneral[][16] =
{{
{palette_primary}
}};

const u16 gMetatiles_LA_UnovaGeneral[] =
    INCBIN_U16("data/tilesets/primary/la_unova_general/metatiles.bin");

const u16 gMetatileAttributes_LA_UnovaGeneral[] =
    INCBIN_U16("data/tilesets/primary/la_unova_general/metatile_attributes.bin");


const u32 gTilesetTiles_LA_NuvemaTown[] =
    INCGFX_U32("data/tilesets/secondary/la_nuvema_town/tiles.png", ".4bpp");

const u16 ALIGNED(4) gTilesetPalettes_LA_NuvemaTown[][16] =
{{
{palette_secondary}
}};

const u16 gMetatiles_LA_NuvemaTown[] =
    INCBIN_U16("data/tilesets/secondary/la_nuvema_town/metatiles.bin");

const u16 gMetatileAttributes_LA_NuvemaTown[] =
    INCBIN_U16("data/tilesets/secondary/la_nuvema_town/metatile_attributes.bin");


const struct Tileset gTileset_LA_UnovaGeneral =
{{
    .isCompressed = FALSE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_LA_UnovaGeneral,
    .palettes = gTilesetPalettes_LA_UnovaGeneral,
    .metatiles = gMetatiles_LA_UnovaGeneral,
    .metatileAttributes = gMetatileAttributes_LA_UnovaGeneral,
    .callback = NULL,
}};


const struct Tileset gTileset_LA_NuvemaTown =
{{
    .isCompressed = FALSE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_LA_NuvemaTown,
    .palettes = gTilesetPalettes_LA_NuvemaTown,
    .metatiles = gMetatiles_LA_NuvemaTown,
    .metatileAttributes = gMetatileAttributes_LA_NuvemaTown,
    .callback = NULL,
}};
'''


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--world-ir", required=True, type=Path)
    ap.add_argument("--rom", required=True, type=Path)

    args = ap.parse_args()

    repo = args.repo.resolve()
    world = args.world_ir.resolve()
    rom_path = args.rom.resolve()

    ir_path = world / "world_ir.json"

    if not ir_path.exists():
        die(f"Missing World IR: {ir_path}")

    if not rom_path.exists():
        die(f"Missing donor ROM: {rom_path}")

    ir = json.loads(ir_path.read_text(encoding="utf-8"))
    rom = rom_path.read_bytes()

    expected_sha = ir["source"]["rom_sha256"]
    actual_sha = hashlib.sha256(rom).hexdigest()

    if actual_sha != expected_sha:
        die(
            "Donor ROM SHA mismatch\n"
            f"IR:  {expected_sha}\n"
            f"ROM: {actual_sha}"
        )

    width = ir["layout"]["width"]
    height = ir["layout"]["height"]

    if width != 40 or height != 40:
        die(f"Unexpected Nuvema layout: {width}x{height}")

    border_width = ir["layout"]["border_width"]
    border_height = ir["layout"]["border_height"]

    primary_desc = ir["tilesets"]["primary"]
    secondary_desc = ir["tilesets"]["secondary"]

    primary_palette_addr = int(
        primary_desc["palettes"],
        0,
    )

    secondary_palette_addr = int(
        secondary_desc["palettes"],
        0,
    )

    stage = repo / ".la_work/native_preview/nuvema_town"

    if stage.exists():
        shutil.rmtree(stage)

    stage.mkdir(parents=True)

    # ------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------

    layout_dst = stage / "data/layouts/LANuvemaTown"

    copy_file(
        world / "layout/map.bin",
        layout_dst / "map.bin",
    )

    copy_file(
        world / "layout/border.bin",
        layout_dst / "border.bin",
    )

    require_size(
        layout_dst / "map.bin",
        width * height * 2,
    )

    require_size(
        layout_dst / "border.bin",
        border_width * border_height * 2,
    )

    # ------------------------------------------------------------
    # Tilesets
    # ------------------------------------------------------------

    create_tileset(
        world / "tilesets/primary",
        stage / "data/tilesets/primary/la_unova_general",
        rom,
        primary_palette_addr,
        PRIMARY_TILE_BYTES,
        PRIMARY_METATILE_BYTES,
        PRIMARY_ATTR_BYTES,
    )

    create_tileset(
        world / "tilesets/secondary",
        stage / "data/tilesets/secondary/la_nuvema_town",
        rom,
        secondary_palette_addr,
        SECONDARY_TILE_BYTES,
        SECONDARY_METATILE_BYTES,
        SECONDARY_ATTR_BYTES,
    )

    # ------------------------------------------------------------
    # Blank/safe native map
    # ------------------------------------------------------------

    map_dir = stage / "data/maps/LANuvemaTown"
    map_dir.mkdir(parents=True)

    map_json = {
        "id": "MAP_LA_NUVEMA_TOWN",
        "name": "LANuvemaTown",
        "layout": "LAYOUT_LA_NUVEMA_TOWN",

        # Temporary safe music until Unova audio work begins.
        "music": "MUS_LITTLEROOT",

        "region": "REGION_UNOVA",
        "la_imported": True,

        # We deliberately postpone the Unova region-map section system.
        "region_map_section": "MAPSEC_NONE",

        "requires_flash": False,
        "weather": "WEATHER_SUNNY",
        "map_type": "MAP_TYPE_TOWN",

        "allow_cycling": True,
        "allow_escaping": False,
        "allow_running": True,

        # MAPSEC_NONE has no Nuvema display text yet.
        "show_map_name": False,

        "floor_number": 0,
        "battle_scene": "MAP_BATTLE_SCENE_NORMAL",

        # Story/runtime logic intentionally blank for first native boot.
        "connections": [],
        "object_events": [],
        "warp_events": [],
        "coord_events": [],
        "bg_events": [],
    }

    (map_dir / "map.json").write_text(
        json.dumps(map_json, indent=2) + "\n",
        encoding="utf-8",
    )

    (map_dir / "scripts.inc").write_text(
        """LANuvemaTown_MapScripts::\n"
        "    .byte 0\n""".replace('"', ''),
        encoding="utf-8",
    )

    # ------------------------------------------------------------
    # Tileset source fragment
    # ------------------------------------------------------------

    fragment = stage / "src/data/tilesets/la_imported.h"
    fragment.parent.mkdir(parents=True, exist_ok=True)

    fragment.write_text(
        make_tileset_header(),
        encoding="utf-8",
    )

    # ------------------------------------------------------------
    # Layout registry entry
    # ------------------------------------------------------------

    layout_entry = {
        "id": "LAYOUT_LA_NUVEMA_TOWN",
        "name": "LANuvemaTown_Layout",
        "width": width,
        "height": height,
        "border_width": border_width,
        "border_height": border_height,
        "primary_tileset": "gTileset_LA_UnovaGeneral",
        "secondary_tileset": "gTileset_LA_NuvemaTown",
        "border_filepath":
            "data/layouts/LANuvemaTown/border.bin",
        "blockdata_filepath":
            "data/layouts/LANuvemaTown/map.bin",
        "layout_version": "la_frlg",
    }

    (stage / "layout_registry_entry.json").write_text(
        json.dumps(layout_entry, indent=2) + "\n",
        encoding="utf-8",
    )

    # ------------------------------------------------------------
    # Map-group entry
    # ------------------------------------------------------------

    group_entry = {
        "group": "gMapGroup_LA_Unova",
        "maps": [
            "LANuvemaTown"
        ]
    }

    (stage / "map_group_entry.json").write_text(
        json.dumps(group_entry, indent=2) + "\n",
        encoding="utf-8",
    )

    # ------------------------------------------------------------
    # Install plan
    # ------------------------------------------------------------

    plan = f"""# LA Native Import Plan v0.4

Donor:
  {ir['source']['donor_label']}

Source:
  group {ir['source']['group']} map {ir['source']['map']}

Map:
  Nuvema Town

Layout:
  {width} x {height}

FRLG border:
  {border_width} x {border_height}

Target layout version:
  la_frlg

Region:
  REGION_UNOVA

Runtime donor logic:
  NOT imported

Events:
  intentionally blank

Connections:
  intentionally blank

Tilesets:
  gTileset_LA_UnovaGeneral
  gTileset_LA_NuvemaTown

Primary palette table:
  donor 16 slots recovered

Secondary palette table:
  donor 16 slots recovered
  runtime will consume slots 7 through 12

Required repository edits after approval:

1. Copy staged data/layouts/LANuvemaTown
2. Copy staged data/maps/LANuvemaTown
3. Copy staged LA tilesets
4. Copy src/data/tilesets/la_imported.h
5. Include la_imported.h from src/tilesets.c
6. Add tileset extern declarations to include/tilesets.h
7. Append layout_registry_entry.json to data/layouts/layouts.json
8. Add gMapGroup_LA_Unova to data/maps/map_groups.json
9. Build
10. Open in Porymap

NO REPOSITORY FILES WERE MODIFIED BY THIS RUN.
"""

    (stage / "INSTALL_PLAN.md").write_text(
        plan,
        encoding="utf-8",
    )

    manifest = {
        "tool": "LA FireRed Native Exporter v0.4",
        "mode": "dry-run",
        "repo": str(repo),
        "donor_rom": str(rom_path),
        "donor_sha256": actual_sha,
        "map": "Nuvema Town",
        "layout": {
            "width": width,
            "height": height,
            "border_width": border_width,
            "border_height": border_height,
            "version": "la_frlg",
        },
        "region": "REGION_UNOVA",
        "palette_fix": {
            "primary_slots_exported": 16,
            "secondary_slots_exported": 16,
            "secondary_runtime_slots": "7-12",
        },
        "story_logic_imported": False,
        "repository_modified": False,
    }

    (stage / "dry_run_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    print("LA FireRed Native Exporter v0.4")
    print("--------------------------------")
    print("DRY RUN COMPLETE")
    print()
    print(f"Map:           Nuvema Town")
    print(f"Layout:        {width}x{height}")
    print(f"Layout type:   la_frlg")
    print(f"Region:        REGION_UNOVA")
    print(f"Primary pals:  16 recovered")
    print(f"Secondary pals:16 recovered")
    print(f"Runtime sec:   palette slots 7-12")
    print()
    print("Donor story/events: NOT imported")
    print("Repository modified: NO")
    print()
    print(f"Stage: {stage}")


if __name__ == "__main__":
    main()
