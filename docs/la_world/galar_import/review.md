# Galar removed from active project

The current Galar map style was rejected by the project owner on 2026-10-06. All 484 donor maps and their tileset declarations were removed from the active build; the nine pre-existing map slots are reserved return-home stubs to preserve other regions' numeric map IDs. Galar and Motostoke teleport options were removed.

Backup: `/home/allan/projects/Galar-archive-20261006`. See `removal.json`. The import ledgers and previous reports below describe the archived import, not the current build.

## Historical import review

# Galar asset and travel test build

484 candidate maps registered: 475 new maps plus nine existing imports. 63 shared tileset banks. New maps have no donor gameplay scripts, trainers or encounters. Existing project events on the original nine imports are retained, with an additional inspection scientist. Existing music is reused; no donor audio or animations were added.

## Enter and test

Talk to Littleroot's teleport scientist and choose GALAR. This starts at Postwick. Talk to the Galar inspection scientist: YES visits the next map; NO returns to Littleroot. His prompt shows the donor map number. Main towns and routes appear first, then the remaining candidates. 426 maps have checked floor arrivals; the other 58 are listed in editor_only_maps.json for Porymap review. Open Locations > Galar in Porymap; new maps also use the Galar_ prefix. The existing nine retain their AMap_ names and map IDs.

Walk through enabled doors and connections. Report the map number shown by the scientist, the doorway/stair location, and the direction you approached it. Test entering and exiting buildings in both directions, stairs, water boundaries and map seams. Save normally before changing ROM versions; this build does not require a new save, but runtime save compatibility has not been tested here.

## Travel and review limits

940 tile-triggered warp records and 170 connections enabled. 580 warp records remain disabled, including normal-ground donor story transitions that cannot safely run without donor scripts. Twenty clear reciprocal destination indices were repaired. Disabled slots retain their original indices outside the map. Inspection arrivals now prefer connected areas with actual exits. Postwick starts on the road at (18,24), outside the house instead of the fenced field.

All 63 editor PNGs and their palettes were restored and checked against the compiled graphics. Reopen Porymap to reload them.

This is the complete non-excluded candidate set, not a claim that all 484 are authentic, finished Galar locations. The earlier review contains 428 manual-review candidates; legacy FireRed maps and superseded versions are excluded. Unknown behaviors, static animations and donor graph gaps still need play testing and visual review. This build is not a fully validated continuous Galar adventure.

## Validation and space

Build and linked Galar checks pass: maps, layouts, compressed tile bytes, native palette colors, map IDs, events, warps, connections and inspection arrival floors. All map group/index values stay below the signed warp sentinel 127. Kanto (425), Johto (266), BWA (19), and audio checks pass. 7,380 existing regional asset files were checksum-protected. Champion Island is retained for future PWT.

Used ROM: 33,257,384 bytes. Free: 297,048 bytes (290.1 KiB). ROM remains 32 MiB. Seven unused original Galar bank declarations are guarded out in free-space mode, reusing the new shared copies. Their restoration branch compiles. Graphics are preserved apart from tracked scoped warp metatile clones; old palette conversion issues are explicitly checked.

Runtime exploration has not been verified in an emulator by this audit. Your play test is the next check.
