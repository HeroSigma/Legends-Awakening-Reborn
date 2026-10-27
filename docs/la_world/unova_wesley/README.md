# WesleyFG Unova / Nuvema implementation

Nuvema Town is rebuilt as a 40 x 40 editable map using `gTileset_UnovaGeneral_Primary` and `gTileset_UnovaNuvema_Secondary`. Open `Unova_NuvemaTown` after reopening the project in Porymap. The Prefabs tab has 46 Unova assemblies and sections, including separate building roof, wall, eave and entrance rows and stair top/middle/base pieces.

## Source artwork and native scale

Artwork: WesleyFG. The three provided original building, nature and vehicle PNG files are retained unchanged under `graphics/unova_wesley/source/`. The additional user-provided `nuvema_town_bw_by_wesleyfg_d3r861t.png` supplies the exact forest and coastline / boardwalk / ocean crops and composition reference. The map is rebuilt from metatiles, not flattened into a full-map image.

No source art was resized or smoothed. Native blue-house art is 70 x 87 pixels, padded to 5 x 6 metatiles; the lab is 142 x 110 pixels, padded to 10 x 7. The ruler measures 16 x 16 map rows, including partial edges. Stair tread top/middle/base bands are each 48 x 8 pixels. Side panels retain their native 16 x 48 pixels. Paired tread bands produce TopMiddle, MiddleMiddle and MiddleBase 16-pixel-high editor pieces; the middle can repeat.

## Capacity and palettes

| Resource | Primary used / free | Secondary used / free |
| --- | --- | --- |
| 8 x 8 graphics patterns | 107 / 405 | 300 / 212 |
| 16 x 16 metatiles | 158 / 354 | 118 / 394 |

Both banks have 512 slots and padded files. Graphics usage includes the primary blank tile and 16 reserved animated water tiles; deduplication includes flipped patterns. Thirteen material palettes use transparent index zero and at most 15 opaque RGB5 colors each. Grass, trees, paths, earth, ocean, stone, blue roofs, orange roofs, wood/windows, metal, boardwalk, hedges/flowers and white fence/sign materials are separated. There is no whole-sheet global quantization. See `report.json` for exact crops, dimensions, palettes and counts.

Shared assets include 47 organic path states, reusable forest interior/edge/partial/cluster assemblies, earth/coast pieces, rocks, flowers, fences, signs and stairs. Four ocean frames animate 16 private primary tile slots at indices 384..399, switching every 16 ticks.

## Map and event changes

Changed Nuvema files: `data/maps/Unova_NuvemaTown/map.json`, its existing layout entry in `data/layouts/layouts.json`, and map / border blocks under `data/layouts/AMap_3_0_Nuvema_Town_Layout/`. Both new tilesets are registered in the normal graphics, metatile, header and label includes. The editor prefab file is `data/tilesets/unova_wesley_prefabs.json`, configured in `porymap.project.cfg`.

All 5 existing NPC identities, flags, scripts and movement types are preserved. Positions were adjusted to reachable path cells; exact original/new coordinates are recorded in `report.json`. Nuvema travel arrival is (19,23). The original exterior has zero active door warps; pending donor records remain inactive. Doors are passable entrance tiles, but interior transitions still need wiring.

Route 1's road at x22..24 aligns with Nuvema x25..27 using reciprocal offsets +3 / -3. Route 1's original terrain and tilesets are retained. A local runtime translation adapts each map's seven-row connection strip to its own graphics; this strip is a palette-compatible approximation. Other map connections are unchanged. A Nuvema-only border hook extends forest on land edges and ocean below the waterfront.

## Verification

Normal game build: PASS. ROM uses 31,045,084 of 33,554,432 bytes (2,509,348 bytes remain before padding). New tileset headers, ocean frames, callback and boundary translation tables are present in the linked ROM.

Dedicated validation: PASS (4233 assertions). Checks include file sizes and indices, palettes, collision / behaviors, editor prefabs, water frame sizes, event preservation and reciprocal road alignment. 437 ground tiles are reachable from the travel arrival, including all four door cells, northern exit and waterfront. Before/after and atlas previews are rendered from the actual GBA files.

Porymap native UI and a walking playthrough have not been performed in this session. The normal headless test runner passed its targeted LoadSheetGraphicsInfo object-graphics regression (1/1); the full battle suite was not run. Linked graphics, metatiles, attributes, palettes and animation frames were also verified byte-for-byte against the ROM.

## Limits and future assets

GBA conversion reduces colors locally to RGB5 / 15 opaque colors per palette; native pixel geometry stays intact. The supplied ocean is a still texture, so its animation consists of subtle native-pixel scrolling phases. Boundary graphics between the new Nuvema and old BWA Route 1 are approximate. These are explicit engine adaptations, not a resolution reduction.

Eight native transparent vehicle crops are prepared in `graphics/unova_wesley/vehicles/`: three boats and two cargo ship orientations for Castelia, truck and loader for Driftveil, aircraft for Mistralton. They are source preparations for later object-sprite conversion, not active sprites or wasted Nuvema metatiles. No other city's tileset was created.

## Rebuilding the assets

Run in order: `rebuild_unova_wesley.py`, `integrate_unova_wesley.py`, `prepare_unova_editor_and_connections.py`, `validate_unova_wesley.py`, then the normal game build. Scripts are under `tools/la_world/`. Original files used for the before preview are retained in `.la_work/unova_wesley/original/`.
