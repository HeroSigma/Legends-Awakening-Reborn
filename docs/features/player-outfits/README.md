# Player outfit selection

Choose Emerald or Ruby/Sapphire on the existing appearance screen, during the new-game introduction or from the player's PC → Appearance. Use Up/Down to select Style, Left/Right to change it, A to keep all appearance choices, and B to restore the previous outfit and colors. No new item is required.

Skin tone, clothes color and accent color remain independent. Existing saves default to Emerald. The signed value 0xC101 in previously unused VAR_LA_PLAYER_OUTFIT (0x40A1) selects Ruby/Sapphire; all other values select Emerald. Intro selections are committed only when starting the new save. No save structure or bag layout changed.

The outfit applies to walking, running, Mach/Acro bikes, surfing, diving, fishing, watering, field moves, decorating, naming-screen sprites, the player's battle front/back portraits, field dialogue portrait and local Trainer Card. The continue screen uses the matching full trainer portrait for Ruby/Sapphire. NPC rivals retain their own Hyper Emerald graphics and portraits. PokéRide uses seated poses adapted from the outfit's surf frames.

## Assets and design references

Complete Ruby/Sapphire overworld sets: resetes12 / Modern Emerald, repository https://github.com/resetes12/pokeemerald, revision e983cc52f7d9cde0a54ff2fc430f653c26086c8c. Existing Ruby/Sapphire trainer front/back graphics and palettes in our project are reused. Credit the original Pokémon sprite artists/Game Freak and Modern Emerald's contributors. Mudskip's outfit system inspired the wardrobe feature, but its player-state/save overhaul and Outfit Box were not imported: our existing appearance interface supplies selection and preview.

Files in graphics/player_outfits/rs retain their indexed palettes. normal_running.png joins walking and running in animation order; compile it with 2×4 tile metaframes. The first prototype compiled these two sources with ordinary tile order, which split the small sprite into pieces; the current build corrects this. All 36 walking/running frames are checked against native ROM data. riding.png centers surf frames 0,2,4 into the existing rider canvas; both mount modes share the pose.

## Validation

Three isolated native mGBA suites record the final ROM hash:

- test_player_outfits.py: 60 checks, including both protagonists, normal/60-box save modes, live selection, cancel, colors, every avatar state, save relocation/reload, preserved boxed Pokémon, invalid save values and riding/dismounting.
- test_player_outfits_intro.py: 16 checks covering the intro, returning to gender selection without text/window residue, naming and commitment into the new save.
- test_player_outfits_render.py: 42 checks, including exact 4bpp walking/running frame packing and native battle-entry screenshots for each back sprite.

The real user's save is never opened by these tests. Native renders were reviewed after correcting the sprite packing.

## Actual gender-specific garments

Style changes garment artwork. Aren's choices are Emerald, Ruby/Sapph, Red vest, Gold and Silver;
Aria's choices are Emerald, Ruby/Sapph, Leaf, Lyra and Kris. The classic style has dedicated
front/back portraits and complete overworld sheets, built on original protagonist
heads and poses. Red's open vest has separate panels and a white shirt center;
Leaf's sleeveless top and skirt include a new flared hem silhouette. See classic/.
The earlier Red/Gold/Blue/Silver color-only style entries are retired. Their signed
save values 0xC102?0xC105 safely retain the RS base; the real gender-specific classic
garment uses 0xC201. Existing Emerald and 0xC101 RS selections remain unchanged.

## Independent color choices

Clothes and Accent remain separate palette controls for any garment. Navy, Cream,
Crimson, Forest, Orange, Teal, Brown and Lilac remain available alongside the
original colors. All 16 values fit the original 4-bit fields without expanding saves.
Original now means the chosen garment's own palette. Changing style preserves
manual colors; cancellation restores both the previous garment and colors.

## Johto-inspired garments

Gold adds a long-sleeved jacket with a dark inset and zipper for Aren. Lyra adds
shoulder straps, buttons, a bib and divided overall shorts over a red blouse for
Aria. Both have separate native art in every player state and front/back battle
portraits, preserving original heads and faces. Style index 3 uses saved value
0xC202; the existing classic pair remains 0xC201. No color preset is relabeled as
a garment. See johto/ for native renders and validation.

## Silver / Kris garments

Silver gives Aren a fitted dark jacket with a raised collar, closed front, red
piping and ribbed waist trim. Kris gives Aria a cropped white jacket with puffed
sleeves over a pink top and blue cycling shorts. This is a distinct garment slot,
index 4 / saved value 0xC203, with full animation and front/back portrait sets.
It does not replace Gold/Lyra or the earlier outfits. See crystal/ for validation.

## New-outfit brown-outline correction

The original field art shares palette index 4 between skin outlines and brown garment/boot outlines. New costume masks now separate exposed skin from those clothing outlines. Back-facing arms no longer act as face anchors, and narrow avatar torsos keep their native center. All three added outfit pairs are regenerated across field poses and trainer pictures; original Emerald and Ruby/Sapphire source art is untouched.

`test_wardrobe_color_masks.py` checks rear-facing anchors, isolated brown outlines and the Red vest back panel. Native wardrobe and rendering tests cover the compiled assets and palette selection.

### Mudskip framework assessment

Reference: https://github.com/mudskipper13/pokeemerald/tree/feature/outfits-system-rhh

Its outfit registry, unlock rules, animated field previews and front/back trainer previews are useful candidates for a later wardrobe-menu upgrade. The sample defines Emerald and Ruby/Sapphire outfits and aliases several missing RS actions to Emerald. It expects authored graphics; it does not repair garment masks or supply the new character-inspired costumes. A port must adapt its SaveBlock2 outfit state and older trainer-picture APIs to our existing saved variables, dynamic colors and unified trainer pictures. This correction does not transplant that framework.

## Portable Outfit Box

Mom gives the reusable Outfit Box with the Running Shoes in both the current Elara farewell and the original fallback gift path. It is a Key Item, supports registered-item access, and can be used on foot. The PC appearance option remains a convenience; it is no longer required. Continuing a save that already received the shoes adds the box if missing, without replaying scenes. No saved item IDs or player-outfit values were renumbered. The existing expanded-bag loader accepts the previous packed item count and zero-fills the new item.

The full-screen menu adapts Mudskip's outfit layout and preview design, re-themed in teal, using our existing gender-specific wardrobe and dynamic palettes. Front/back trainer pictures and four visible overworld previews show the selected colors. The selected overworld avatar walks; moving beyond the fourth entry scrolls the strip.

- Up/Down: browse outfits.
- L/R: switch between outfits and color controls.
- In colors, Up/Down selects Skin, Clothes or Accent; Left/Right changes it.
- A/Start: wear and save the previewed combination.
- B: leave colors, then cancel and return without applying.

Changing clothes is unavailable while cycling, surfing, diving, riding or linked. Both Bag and registered access return through the normal field rebuild, restoring player sprites, palettes and controls.

### Credits and validation

Mudskip, outfit system/layout: https://github.com/mudskipper13/pokeemerald/tree/feature/outfits-system-rhh
Background art/tilemap: `graphics/outfit_menu/main.png` and `main.bin` from that branch; indexed palette adapted to Legends Awakening. The menu code uses the native Expansion APIs and our existing save variables instead of importing the donor SaveBlock2 fields or older trainer-picture tables.

Native tests: `tools/la_world/storage/test_outfit_box.py` plays both Mom gift paths, Bag and registered access, previews, apply/cancel, riding restrictions, repeated exits, Start-menu reopening, save/load and old-count packed-bag import. Existing colorway, intro and brown-outline regression suites are also retained. No user battery save is loaded for tests. Screenshots and validation are under `outfit-box/`.

## Jacket linework polish

Removed the inherited internal shirt/backpack outline from the added male vest and jacket fronts. Brown fabric shadows now use nearby garment/neutral shadow colors instead of solid black; outer contours, exposed skin and original source art are preserved. The shared correction regenerates all added outfit pairs, including field and battle poses. Native captures in `linework/` cover Red, Gold and blue Silver in the new-game palette selector. Asset regressions check all three jacket interiors; the Outfit Box and compiled walking/battle rendering suites also pass.
