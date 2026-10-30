# HnS regional map artwork

Recovered directly from the existing Heart & Soul source checkout. Includes Kanto, Johto, and combined Johto–Kanto PokeNav and Pokedex graphics, palettes, and tilemaps. Source files are staged under assets/regional_maps/hns, outside the build.

All 18 source files match their recorded hashes. The three PokeNav 64×64 affine tilemaps decode with valid tile indices; Pokedex assets are preserved without a rendering claim. Full previews retain the entire backing map; preview images show the top-left 240×160 viewport at 3× nearest-neighbor scale. Runtime cursor coordinates, town names, Fly destinations, story locks and scrolling have not been ported or validated. No ROM or save was changed.

Credit Pokemon Heart & Soul, Lil Dill and the HnS team, Modern Emerald/resetes12, RHH and pret; upstream credits are preserved with the assets. See the manifest for the exact donor commit and file hashes.

## Connected world map

The normal PokeNav Map selection and field/wall map now open one scrolling 512×512 atlas. Hoenn is southwest of the combined HnS Johto/Kanto landmass. The D-pad moves a tile cursor; the header identifies the hovered region and the footer names the town, route, or landmark. Ocean has an explicit Open Sea label. B returns to the field menu/caller. The player marker uses the current map display name, with case-insensitive matching; unrecognized locations do not get a fabricated player marker.

This is a geographical display, not an unlock for travel. Native Fly and scripted PokeNav tutorials keep their existing code. Selecting Map in normal PokeNav closes that device before opening the atlas; B returns to the field menu. Other regions are not drawn yet. Atlas placement is a UI arrangement, not a claim about new physical connections.

Art is regenerated with tools/la_world/build_world_map_art.py. It merges ocean colors and uses fewer than 512 unique 8bpp tiles, reserving the UI character bank and four palette banks. No save fields were added. Runtime validation and screenshots are in runtime/. The test uses disposable emulator SRAM, never the player save.
