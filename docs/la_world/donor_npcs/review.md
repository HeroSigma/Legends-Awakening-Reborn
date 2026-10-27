# Donor NPC asset library

Hyper Giovanni: **gfx_081**. Hyper Cyrus: **gfx_096**. Both are preserved with original graphics metadata and palettes.

| Donor / source | Sheets |
|---|---:|
| hyper | 246 |
| bwa | 152 |
| swsh | 240 |
| aestheticred | 176 |
| mercury | 1024 |
| hyper_legacy_variants | 564 |
| hns | 923 |

Sheets include NPCs, creatures, effects and props; these are not counts of unique human characters. Legacy variants are intentionally counted separately.

## Use and validation

Open `gallery.html` to browse, or open individual PNGs in LibreSprite. `inventory.csv` lists assets and their review status; `manifest.json` records original source paths and exact file hashes. HnS palettes and visual declarations are retained beside its art.

These files are staged under `assets/donor_npcs`, outside the build. They do not assign runtime graphics IDs or create map events. Existing HnS Giovanni is already available as `OBJ_EVENT_GFX_HNS_GIOVANNI_HNS`; the Hyper versions remain separate.

Source copies are hash-checked and all indexed sheets are decoded. Fallback palettes and unusual frame strides remain in manual review. Runtime animation, palette-slot and subsprite validation is required when a character is selected for use.

## Remaining source gaps

GS Chronicles: original ROM is missing at its recorded path, and its map export contains no sprite catalog. Recovery remains pending; no source art is invented. Mercury is archived only and is not reactivated. BW3G / Rainbow Mistralton were single-map asset experiments without complete NPC exports, so this pass makes no full donor coverage claim for them.

## Status counts

- ASSET_CANDIDATE: 518
- MANUAL_REVIEW: 1320
- VARIANT_REVIEW: 564
- SOURCE_ASSET: 923

Selected native NPC appearances are now tracked separately in [the named roster](../../art/npc_roster/README.md). This preservation archive retains its original source copies.
