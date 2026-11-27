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

Style changes garment artwork. Aren's choices are Emerald, Ruby/Sapph, Red vest and Gold;
Aria's choices are Emerald, Ruby/Sapph, Leaf and Lyra. The classic style has dedicated
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
