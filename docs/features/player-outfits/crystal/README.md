# Silver jacket / Kris sports clothing

Wardrobe slot 4 is gender-specific: Silver for Aren and Kris for Aria. Clothing
references are the existing donor_silver.png and donor_kris.png front portraits.
The NPC donor sprites are not modified or substituted as the player's identity.

Silver: raised collar, fitted dark closed jacket, long sleeves, red piping and a
ribbed waistband. Kris: cropped open white jacket, puffed sleeves, visible pink
top and fitted blue cycling shorts. The white jacket panels and longer shorts
cover new body pixels. Clothing construction differs from Gold/Lyra and from the
original Emerald player clothing; these are not palette presets. Original head
and face geometry is preserved. Clothing/headgear accents share the outfit colors.

Native assets: graphics/player_outfits/crystal. Authoring tool:
tools/la_world/art/build_crystal_wardrobe.py. Every player animation state and both
front/back portraits have native indexed assets. Standard Clothes/Accent controls
remain independent. Kris's original accent pair carries pink top/blue shorts;
manual accent colors can coordinate both sections with the selected color pair.

Save value: 0xC203 in VAR_LA_PLAYER_OUTFIT, no save layout change. Other garment
values remain unchanged. Trainer picture IDs are appended, not reordered. Player
object palettes now use a table indexed by the validated saved outfit and gender,
so all existing garments and underwater palettes keep their correct art.

Native tests cover both protagonists/storage modes, real PC choices, cancellation,
persistence, mounts, all player state graphics, exact original front heads and new
sleeve/shorts pixels. Render tests compare all 36 packed normal/running frames and
capture real battle entry/back sprites. New intro garment commit is checked for
both protagonists. Expanded palette tests include every existing garment. Earlier
garment and introduction suites are rerun. No real user save is loaded by tests.
