# Gold jacket / Lyra overalls

The fourth wardrobe slot is gender-specific: Gold for Aren and Lyra for Aria.
Gold has a yellow/gold long-sleeved jacket, dark inset, collar and zipper details;
the new sleeve pixels cover previously bare upper arms. Lyra has blue overall
straps, chest bib, white buttons and divided shorts over a red blouse. Her earlier
Leaf skirt remains available as a different garment. This is native pixel art on
the original protagonists, not a character sprite swap or palette-only preset.

New assets under graphics/player_outfits/johto cover the same complete animation
set as the existing outfits: walking/running, bikes, surfing/diving, field moves,
fishing, watering, decorating and mounts. Separate four-frame battle backs and
front portraits feed the existing player portrait hooks. Head/face pixel geometry
is preserved; the outfit's headgear accents can follow its clothing palette.

Style 3 saves as 0xC202 in VAR_LA_PLAYER_OUTFIT. Values 0/C101/C201 keep Emerald,
Ruby/Sapphire and Red-vest/Leaf garments. Colors stay independent. Invalid values
and retired colorway saves retain their existing safe fallback policy.

Authoring: tools/la_world/art/build_johto_wardrobe.py uses original project player
sprites and shared face-detection helpers from the first garment tool. Existing
trainer picture IDs remain unchanged; the new IDs are appended. NPC rivals are
untouched.

Native tests exercise both protagonists and storage modes, real appearance menu
cycling/accept/cancel, saved outfit/color values, mounts and all avatar states.
They also check preserved front-head pixels, newly covered jacket-arm pixels and
non-uniform bib/strap edits. Render tests compare all 36 native walking/running
frames byte-for-byte and capture actual battle entries. Intro commit is checked
for both protagonists. Test saves are isolated from the user's save.
