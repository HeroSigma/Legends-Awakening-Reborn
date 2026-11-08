# Regional town-map candidates (2026-11-08)

User supplied:
- https://github.com/LiderMorti00/Sinnoh-pokeemerald-expansion/tree/master/graphics/pokenav/region_map
- https://github.com/PokemonHnS-Development/pokemonHnS/tree/main/graphics/pokenav/region_map

Inspected source graphics and reconstructed their affine tilemaps. The Sinnoh source has Sinnoh geography in a classic Hoenn-like style, with map.png, map.bin and map.pal; it also includes separate Kanto and Sevii assets. Its map.png is a 128x128 tile atlas, not the displayed map image. The 4096-byte map.bin is a 64x64 affine byte tilemap, not a 16-bit text tilemap. Its source loads 8bpp graphics and palette data.

HnS provides map.png/map.bin for combined Johto/Kanto geography and johtomap.png/johtomap.bin for Johto. Their source tile atlas and palette style differ from the Sinnoh asset, so palette/style normalization may be needed for a cohesive world map.

Review downloads and assembled previews: .la_work/region-map-sources. No playable map artwork has been changed by this inspection. Sinnoh had previously been removed at the user request; do not claim it has been restored. Integration still requires matching the region-map grid/town metadata, player marker and Fly/progression gates to the maps actually active in our game. Preserve source credits when importing.
