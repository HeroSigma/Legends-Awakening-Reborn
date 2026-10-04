# A-Map Batch Bridge v1.1

v1.1 keeps the proven Hyper Emerald v1.0 extraction path and adds exact-build FireRed donor profiles for Legends Awakening Reborn.

## New donor profiles

- `bwa_demo_v2` — Pokémon Black & White Advanced Demo v2
- `swsh_ultimate_plus` — Sword & Shield Ultimate+ v1.2.1.2
- `catalyst` — current patched FireRed Rev 1 Catalyst test build

Profiles are selected automatically by SHA-256 when possible.

## Key FireRed normalization

The old Porymap Batch Bridge importer and the Emerald-based Reborn project expect a 512-primary / 512-secondary tileset split. FireRed uses 640 / 384.

v1.1 normalizes this *without changing global tile or metatile IDs*:

```text
FireRed primary 0..511    -> Emerald primary 0..511
FireRed primary 512..639  -> Emerald secondary 0..127
FireRed secondary 0..383  -> Emerald secondary 128..511
```

The same partition is applied to 8x8 tiles and 16x16 metatiles. Because the 128-entry excess primary slice is inserted before the 384-entry FireRed secondary slice, global IDs 0..1023 remain unchanged in map blockdata and metatile definitions.

Palette normalization is similarly role-aware:

- destination primary slots 0..5 come from the FireRed primary tileset
- destination secondary slot 6 comes from the FireRed primary tileset
- destination secondary slots 7..12 come from the FireRed secondary tileset

FireRed 32-bit metatile attributes are preserved verbatim in `source_frlg_metatile_attributes.bin`; the importer-facing RSE `.bvd` receives a compatibility conversion containing behavior low 8 bits and layer type. Full behavior translation remains a later semantic pass.

## First validation target: Nuvema Town

```bash
python3 amap_batch_bridge.py \
  "/path/to/Pokemon Black & White Advanced (Demo v2).gba" \
  --extract 3.0 \
  --out BWA_Nuvema_v11
```

Expected identity:

```text
3.0 Nuvema Town
40 x 40
MapHeader 0x08350618
```

The map folder includes `preview.png` for visual validation before Porymap import.

## Scan

```bash
python3 amap_batch_bridge.py ROM.gba --scan
```

## Extract all usable maps

```bash
python3 amap_batch_bridge.py ROM.gba --extract-all --out FullExport
```

## Current v1.1 FireRed boundary

Map geometry, borders, normalized tilesets, palettes, metatiles, raw FireRed attributes, NPC metadata, warps, coord events, bg events, connections, location names, and structural map-script tables are exported.

FireRed script bytecode decompilation and exact FireRed object-sprite extraction are intentionally deferred instead of reusing Emerald-specific tables unsafely.

## Validation result

The included validation pass confirmed:

- Hyper Emerald legacy path: **38 groups / 922 maps**
- Black & White Advanced Demo v2: **444 / 444 usable maps**
- Sword & Shield Ultimate+ v1.2.1.2: **701 usable maps from 761 profiled slots**
- BWA `3.0 Nuvema Town` renders correctly after normalization
- SWSH `3.0 Postwick` renders correctly after normalization
- importer-facing normalized tilesets are 512/512 with 6/7 palette banks and `RSE ` BVD signatures

The FireRed normalization is specifically designed to feed the existing Porymap A-Map Batch Import v0.8 contract rather than requiring the destination project to interpret a 640/384 FireRed tileset split.
