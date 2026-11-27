# First actual player garments

Aren: Red-inspired open vest over a white undershirt, garment panels, pocket/seam
pixels and matching vest back/undershirt sleeves. Aria: Leaf-inspired sleeveless
blue top and red flared skirt, including a new filled hem and silhouette. Aria does
not receive Red's vest. Both keep their original protagonist heads/faces and poses.
These are native indexed edits of project player art, not full Red/Leaf character
swaps and not the large AI design preview imported into the ROM.

The complete sets cover walking/running, Mach/Acro bikes, surfing, diving, field
moves, fishing, watering, decorating and both ride modes. Dedicated front and
four-frame back portraits also feed the wardrobe preview, naming screen, field
portrait, battles, Trainer Card and continue-screen portrait through existing hooks.

Style index 2 resolves by the player gender: Red vest (male), Leaf (female).
VAR_LA_PLAYER_OUTFIT stores 0xC201. The existing Emerald/RS values stay valid;
retired colorway values C102?C105 resolve to RS. Clothes/Accent remain independent.
NPC rival artwork, including sapphire May, is not changed.

The deterministic native asset authoring script is tools/la_world/art/build_classic_wardrobe.py.
Source art remains under graphics/object_events/pics/people and graphics/trainers;
new garments live under graphics/player_outfits/classic. All frame dimensions and
animation ordering match the established player sets. Added trainer picture IDs
are appended, preserving existing trainer picture IDs.

Validation: test_classic_wardrobe.py checks both protagonists, regular/60-box saves,
PC selection/cancellation, every animation state, colors, persistence and mounts;
it also checks exact original front-head geometry and changed garment topology.
test_classic_wardrobe_render.py checks all 36 packed walking/running frames and
native battle entry/back sprites. test_player_colorways.py verifies all sixteen
colors, independent garment/color choices and safe legacy migration. The existing
outfit intro tests remain applicable. No real player save is loaded by tests.
