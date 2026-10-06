# Unova and Galar preservation

Source preservation and isolated editor staging are implemented for BWA (444 maps / 62 normalized tilesets) and SWSH (701 maps / 69 normalized tilesets). Assets live in `.la_work/amap/donor_preservation/{bwa,swsh}`. These are separate asset-only editor projects, not additions to the live game.

Regenerate from the repository root:

```sh
python3 tools/la_world/importers/amap/preserve_donor_assets.py --donor both
python3 tools/la_world/importers/amap/verify_donor_preservation.py
```

Regeneration overwrites generated editor copies. Back up manual editor edits first. The original full exports are read-only inputs. Source ROMs must match the export SHA-256; a lossless archival anchor retains all donor assets, including currently unextracted animation and dynamic graphics data. No donor bytecode is copied into Reborn build sources.

## Validation

All 1,145 maps have matching dimensions, borders and declared tilesets. Every staged file is checksummed. All editor maps have empty events and no travel connections; callbacks are NULL. Existing `data`, `src` and `include` files were hashed before/after generation and remain identical. No ROM rebuild is needed for this inactive staging change. Porymap GUI rendering has not yet been tested.

## Remaining completion work

- Recover animation frame/timing closure for nonzero callback headers (6 BWA, 5 SWSH), without transplanting executable donor callbacks.
- Verify discovered graphics table identities, exact sprite frame closure, palettes and map-used dynamic graphics references. Static table candidates cover 152 BWA and 240 SWSH IDs; dynamic IDs remain references.
- Build semantic FRLG-to-Reborn behavior mappings before runtime use. Lossless 32-bit attributes are preserved; editor compatibility attributes truncate 2,120 BWA and 4,201 SWSH normalized metatile entries with behavior IDs above 255. Counts include duplicated normalized tileset assets.
- Open both isolated workspaces in Porymap and check representative layouts and palette rendering.

Neither preservation phase is marked fully runtime-ready while these closure items are open. Existing validated imports are unchanged, and no new maps are activated.

FRLG graphics-info ABI reference: https://github.com/pret/pokefirered/blob/master/include/global.fieldmap.h . Layout compatibility permits reuse of the existing sprite extractor, but heuristic discovery alone does not establish donor identity or frame completeness.
