# Heart & Soul canary #1

Verdict: suitable for a larger source-based migration trial. Build, compiled-data checks and 30 targeted mGBA runtime checks pass.

## Included

New Bark Town, Route 29, Cherrygrove City, Route 30, Route 31, Route 31/Violet gate, Violet City, Cherrygrove Mart and Violet Gym. Registered in `gMapGroup_HnS_Canary` as `HnSTest_*`. New Game starts in New Bark with native exploration supplies. Scientists offer travel to the next test map.

## Verified in the emulator

- Mart and Gym exterior/interior artwork is present; entrances and exits work.
- All eight selected warp records work through normal player input, including both gate directions.
- Eight traversable directional connection boundaries work.
- Route 31 diagonal stairs ascend and descend, with both avatar genders.
- A native shop purchase reduces money from 3000 to 2800; cancellation restores walking control.
- Shoreline blocks walking onto water.
- Outdoor and Gym flower animation callbacks change their expected VRAM tile payloads.

## Ownership and conversion

Pinned public source commit: 167aa6d537b109bb229c231ddce4616974c4da71. Source palettes, tiles, metatiles, layouts, collision/elevation and graphical animation callbacks are adapted to Reborn's 512/512 tileset split and native three-layer metatiles. Metatile IDs remain unchanged. Donor story scripts, NPC/trainer logic, flags, variables, encounters and save code are excluded. Mart service and inspection NPCs are project-owned test scripts. Unsupported donor special interactions remain deferred.

## Retired donors

865 former Johto/Kanto registry maps are inactive in the compiled ROM, with group/layout slots reserved to avoid renumbering unrelated maps. A verified archive at `/home/allan/legends-region-archives/mercury-kanto-before-hns/source-and-porymap-edits.tar.gz` preserves source data and Porymap edits. Existing art files remain available as inactive references. Hub Johto travel enters the HnS test; Kanto travel is closed pending migration. Other preexisting map data and artwork were checked for preservation.

## Limits

This is a nine-map asset/travel test, not the full regional replacement or a playable HnS story. Other interiors and routes are outside the batch. Gym battles and donor puzzles are not activated. Runtime setup bypasses the naming/intro menus using the native new-game callback; tested entrances, movement and shop interactions use ordinary game inputs. Use New Game with a separate save. Older saves located in retired regions are not part of this test. The complete remaining Johto/Kanto migration needs a correspondence inventory and further batches.
