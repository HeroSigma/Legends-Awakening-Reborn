Nuvema uses native user artwork with original RGB555 colours.

Town pair: gTileset_UnovaGeneral_Primary + gTileset_UnovaNuvema_Secondary.

The complete untrimmed 256x256 user sheets are also available as three exact source pairs, gTileset_UnovaNuvemaOriginal1_Primary/Secondary through Original3. Every source pixel and alpha is verified by reconstructing both full sheets from serialized GBA tiles/metatiles/palettes: 131072 pixel comparisons. No scaling, redraw, colour quantization or dropped source pieces.

Import data/tilesets/unova_wesley_prefabs.json for full source-piece prefabs; select the corresponding Original pair when using those source variants. Original sheets remain untouched.

For regeneration use build_nuvema_exact.py, finish_exact_nuvema.py, document_exact_nuvema.py, pack_complete_nuvema_sources.py in that order. Older rebuild/polish commands use reduced palettes and must not be used for this version.

Town retains the existing map edits; full native path corner crops replace the former generated 8px transitions. Hedge bases exposed by moving two hedges one metatile up. Source shoreline and repeating boardwalk supplement pieces absent from the user sheet. Door interiors remain pending.
