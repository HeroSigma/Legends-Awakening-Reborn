# Team Aqua asset integration

Source: [Team Aqua’s Asset Repo](https://github.com/TeamAquasHideout/Team-Aquas-Asset-Repo). The exact upstream revision and original folders are recorded in source.json. Original creator notes are retained in upstream-1.md through upstream-9.md. The source repository permits use and editing with appropriate credit.

## Credits

- **Kaixer**: colored Hoenn trainer-card badges.
- **Lhea**, based on **Squid Eevee**: modern type/contest icons and palettes.
- **Mudskip**: dark mart UI, tiles, tilemaps and scrolling background.
- **Project Palladium team**: released master bag sheet. **Gridiron** created the bags, **BalladOfWindfishes** created the menu art, and **GameGuy** organized the sheet. This integration uses the bag sprites.
- **Zatsu**: Tera icons.
- **Buffel Saft / Pokemon Inclement Emerald**: gold item ball and animated Mega Stone overworld sprites.
- **KyuZee**: Tyrantrum fossil exhibit; the supplied fossil palette is used.
- **Eva / PurrfectDoodle**: improved berry trees and all seven Apricorn colors.

## Active replacements

The eight Hoenn trainer-card badges use Kaixer’s colored artwork. Existing other-region badges are retained because this supplied sheet contains Hoenn badges only. Full-size type and contest icons use Lhea’s graphics and three custom palettes. Zatsu’s compact Tera icons use a separate summary sprite sheet, color-remapped to those modern palettes, so normal types and Tera types remain visually distinct. Move/contest-page icons still switch back to the normal sheet.

Both playable bag sprites use Palladium artwork, extracted at original resolution, centered in the engine’s 64x64 frames. The resting pose is reused for the additional native frame; the existing expanded pockets and bag UI remain.

Ordinary mart Buy screens use Mudskip’s dark interface and scrolling pattern, with readable light item names and the original purchase flow. The separate Legends Store retains its category, pricing and sale interface.

The first ten berry trees (Cheri through Sitrus) use Eva’s improved artwork and dedicated palettes for the grown stages; dirt/sprout stages and other berries retain their existing assets and gameplay.

## World objects

- Timeless Woods’ story artifact now uses OBJ_EVENT_GFX_LA_GOLD_BALL. Its flags, pickup sequence and other item balls are unchanged.
- OBJ_EVENT_GFX_LA_MEGA_STONE is an animated, placeable Mega Stone object. No new reward locations are added.
- Devon Corporation 1F has a Tyrantrum exhibit at (11,6) with a short description. Existing map edits and story actors are retained.
- OBJ_EVENT_GFX_LA_APRICORN_RED / BLUE / YELLOW / GREEN / PINK / WHITE / BLACK register all seven Apricorn tree appearances for Porymap. They display ripe trees; no new trees, harvest scripts or farming mechanics are placed by this artwork pass. The source growth frames are retained in the sheets for future mechanics.

Existing static graphics IDs are preserved by appending the new objects. Player save fields, item IDs and progression flags are unchanged. The map commits contain only the requested artifact graphic swap and exhibit object, excluding unrelated user map edits.

Native visual evidence includes trainer card, summary, ordinary mart, bag for both genders, world sprites, custom berry palettes, and Devon lobby placement. Tests also cover menu returns, purchases, scientist Tera changes and existing story progression.
