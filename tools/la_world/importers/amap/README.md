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

## Donor classification (metadata only)

From the repository root:

```bash
python3 tools/la_world/importers/amap/classify_donor_maps.py
```

Inputs default to `.la_work/amap/bwa_full_v11` and
`.la_work/amap/swsh_full_v11`. Reports are written separately under
`.la_work/amap/classification_v11/{bwa,swsh}/`:

- `inventory.csv`: every usable map, category, confidence, scores and evidence.
- `world_candidates.csv`: HIGH confidence WORLD maps without review flags.
- `interior_dungeon_candidates.csv`: all INTERIOR/CAVE_DUNGEON suggestions,
  including flagged entries; inspect confidence and review fields.
- `review_unknown.csv`: ambiguous, unspecified, count-mismatched or shared-layout
  entries. This overlaps candidate files intentionally.
- `report.md`: compact summary, world shortlist and review preview.

Use `--bwa-root`, `--swsh-root` and `--out` to select alternate paths. Counts
must match the validated 444/701 inventory unless `--allow-count-change` is
explicitly supplied. The script never imports maps or writes into exports.

### Confirmed v1.1 schema

Only `maps/*/map.json` is inventoried; sidecars are not additional maps.
Identity is `id`, `group`, `map`; dimensions are `width`, `height`.
Object counts are `event_counts.object`, not `objects`; exported records are
`npcs`. Other declared counts are `event_counts.warp/coord/bg`, with parsed
records in `warps`, `coord_events`, and `bg_events`. Connections are a list.
Declared counts can exceed exported lengths, so both are retained and review
flags are generated. Inspection found 6 BWA and 31 SWSH maps with at least one
mismatch, including BWA Nuvema's BG events (6 declared, 5 exported).

Map types follow `include/constants/map_types.h`: 0 unspecified, 1 town,
2 city, 3 route, 4 underground, 5 underwater, 6 ocean route, 8 indoor,
9 secret base. Names are region labels and may recur across interiors.
Group 3 and connections strengthen outdoor classifications. Secondary tileset
families provide only weak donor-local evidence for unspecified maps. Small
sparse multi-warp interiors suggest transitions but remain ambiguous when
indoor evidence competes. Explicit names can suggest utilities/debug maps;
absence of events alone never proves a debug map or stale content.

CSV provenance includes ROM hash/profile, source JSON hash/path, header,
layout and blockdata pointers, all nested event/script pointers, source tileset
addresses, layout-sharing peers, and connection/warp target IDs. Shared layouts
are review evidence, not grounds to discard donor maps.

Nuvema and Postwick remain validated canaries at donor-local `3.0`. Classification
confidence is not gameplay validation or authorization for bulk import.

## BWA / Unova canonical review

```bash
python3 tools/la_world/importers/amap/build_bwa_unova_manifest.py
python3 -m unittest discover -s tools/la_world/importers/amap/tests -v
```

Uses BWA full v1.1 JSON plus the existing donor metadata CSV/Markdown. Outputs
are separate under `.la_work/amap/bwa_unova_review/`; original exports and
metadata reports are not overwritten. Corrected BWA-only metadata fills
`objects` from `event_counts.object` and retains parsed array lengths.

`bwa_unova_rules.json` contains manually reviewed per-map choices guarded by
both JSON and preview SHA-256. Changed inputs fall back to manual review.
`firered_map_reference.json` provides offline FireRed slot ancestry, dimensions,
and blockdata hashes from pret/pokefirered at commit
`037335f4c725d7c9aecdac87066f2002b4bd7e14`. Exact geometry does not imply stock
scripts/events or prove that a donor intended no repurposing. Legacy exclusions
are conservative quarantine, not deletion or a claim that all content is stale.

The JSON manifest inventories all 444 BWA maps, chosen regional sectors,
duplicate-name families, incoming/outgoing relationships, pointers, provenance,
and dependencies. The selected list has 25 visually reviewed asset candidates;
313 maps are excluded legacy geometry/host families, 105 require review, and
Nuvema 3.0 is protected. Accumula and Nimbasa are provisional spine nodes with
import disabled. SWSH/Postwick are not advanced by this classifier.

**`import_flag` means future visual asset selection only.** `execution_allowed`,
`runtime_import_flag`, event/script import and relationship import are always
false. Relationships carry explicit deferred actions and blockers; selecting
an asset never recursively imports a legacy dependency. This manifest is not
an executable gameplay migration plan. Destination IDs, scripts, NPC graphics,
warps and connections must be implemented separately before playable import.

Source reference:
https://github.com/pret/pokefirered/tree/037335f4c725d7c9aecdac87066f2002b4bd7e14

The BWA builder also reads matching destination `AMap_*` maps to record existing
imports. `already_imported`, `import_action=SKIP_EXISTING_IMPORT`, and
`reimport_flag=false` prevent mistaking selected assets for pending reimports.
`bwa_unova_import_status.csv` records registration, geometry comparison, active
and pending links, unspecified destination types, and duplicate object local IDs.
This is a read-only audit and does not confer gameplay validation. The selected
asset list remains classification history; `remaining_asset_candidates` excludes
existing imports.

User-confirmed game testing is tracked separately from the file audit in
`destination_verifications` within `bwa_unova_rules.json`. Matching destination
JSON, blockdata and layout-definition hashes produce
`GAME_TESTED_VERIFIED_BY_USER`; subsequent changes produce
`USER_VERIFICATION_STALE_RECHECK_REQUIRED`. This never enables reimport or claims
that the classifier itself ran the game. The six-map Striaton/Route 3/Nacrene/
Pinwheel stretch has user-reported game verification; its pending external links
remain deferred.
