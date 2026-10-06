# Johto manual editing in the main Reborn project

Open `\\wsl.localhost\Ubuntu\home\allan\projects\Legends-Awakening-Reborn` as the Porymap project folder.

All 266 GSJohto maps are registered in the main project, using direct tileset declarations in src/data/tilesets/headers.h, graphics.h and metatiles.h. Find them under Locations -> Johto, or filter GSJohto.

Route 30: GSJohto_3_20_Route_30. Reported staircase: x16,y4-5; landing: x17,y5-6. These are zero-based Porymap coordinates.

Layout data: data/gs_johto_assets/layouts/GSJohto_3_20_Route_30/map.bin.

Primary tileset: gTileset_GSJohto_primary_f2e_GS_CHRONICLES_276_082D4A94.
Secondary tileset: gTileset_GSJohto_secondary_f2e_GS_CHRONICLES_276_P082D4A94S082D4AAC.

Save map edits in this project. A ROM rebuild is required before runtime testing. Imported gameplay remains project-owned. Shared metatile behavior/art edits affect all maps using that tileset; map collision/elevation edits apply to individual cells.
