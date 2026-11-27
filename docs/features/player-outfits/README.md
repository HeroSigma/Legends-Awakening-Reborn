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

## Character-inspired colorways

The Style row additionally offers Red style, Gold style, Blue style and Silver.
These use the complete Ruby/Sapphire outfit cut with themed clothing/trim defaults;
they are colorway presets, not newly drawn jackets or imported character sprites.
Aren/Aria keep their own head, hair, face, and animation set. Colors default to
red/white, gold/charcoal, navy/cream and charcoal/crimson respectively. Set Clothes
and Accent to Original to see the theme defaults; explicit color choices override
each independently. Cancel restores style and colors together.

Added palette choices: Navy, Cream, Crimson, Forest, Orange, Teal, Brown and Lilac.
The existing 4-bit color fields accommodate all 16 values without expanding saves.
Signed outfit values 0xC101?0xC105 select the five non-Emerald styles; invalid values
still fall back to Emerald. Existing Ruby/Sapphire saves retain their selection.

Native validation: 222 colorway checks across both protagonists (all avatar state
lookups, preserved identity palette entries, every color value, independent overrides,
UI cycling in both directions, cancel, save/load and intro commitment), plus the
existing 60 outfit checks and 16 introduction checks. Screenshots are under colorways/.
Distinct Red/Gold jacket shapes and additional rival wardrobes still require new
complete compatible sprite artwork and are not claimed as implemented by these presets.
