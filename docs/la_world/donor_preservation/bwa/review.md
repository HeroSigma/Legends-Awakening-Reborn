# BWA donor preservation

444 usable maps, 62 normalized tilesets; all blockdata, borders, palettes, metatiles and raw FRLG attributes preserved and checksummed. Object counts are populated from actual NPC arrays. All duplicate/legacy maps remain reference-only.

Open `editor` as a separate Porymap project. It is an asset-only workspace with no build target, objects, events, warps, connections or donor scripts. Donor relationships and events remain in `reference/export` for research. Do not copy its map registry over Reborn. Native gameplay constants copied for editor parsing only.

Full hash-verified ROM anchor retains otherwise unextracted graphical data. 152/160 catalogued graphics IDs yielded heuristic art candidates (all discovered static IDs plus map-referenced dynamic IDs); table identity, frame closure and dynamic IDs require review. These are not verified runtime art. 6 nonzero tileset callbacks retain exact header/pointer references but animation frame extraction and Reborn scheduling are pending. 2120 normalized metatiles have behavior IDs beyond the 8-bit editor field; raw 32-bit attributes are losslessly retained. All behavior semantics still require a FRLG-to-Reborn translation contract before future activation.

This completes source preservation and editor staging, not runtime asset integration. Existing live maps and ROM are unchanged.
