# Hyper Emerald rival portraits

Brendan and May now use Hyper Emerald's ORAS-style front portraits for named field dialogue and all 36 of their trainer battle entries. Their existing Hyper overworld sprites remain unchanged. The player retains separate Emerald/Ruby-Sapphire front/back pictures, outfit selection and dynamic colors.

The donor's active trainer picture table is at 0x101BE90 and its matching palette table at 0x101C660. Brendan is entry 71 and May entry 72. The old vanilla table at 0x301418 is stale: many of its pointers reference graphics overwritten by donor changes. The active entries were decoded and visually reviewed before importing.

Only two 64x64 indexed pictures and their original palettes were extracted. No donor scripts, gameplay, trainer teams or save data were imported. New portrait IDs are appended so existing IDs remain stable. Field portraits use the rival's own palette directly; player palette/outfit settings do not affect these IDs. Battle trainer definitions use the new IDs and the competitive adapter preserves them.

## Credits

Source: Hyper Emerald / HypEm v5.7 EN+QoL, Hyper Emerald's graphics contributors and the original Pokémon/Game Freak artwork. See source.json for the exact donor SHA-256, table entries, offsets and decoded graphic/palette hashes. The extraction is reproducible with tools/la_world/importers/amap/extract_hyper_rival_portraits.py.

## Validation

The targeted native test checks both protagonists, both storage modes, both supported player outfits, original/custom player colors, exact rival pixels in VRAM, independent rival palettes, player palette preservation and all 36 adapted trainer entries. Its isolated emulator never loads the user's save. The existing field-mugshot suite checks speaker switching, cleanup, cave masks and resource exhaustion with the new rival palettes.

The rejected modular wardrobe prototype remains parked and is not part of this build.
