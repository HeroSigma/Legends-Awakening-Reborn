# Dynamic character palettes

Adapts kyphii's character-palette-parts design: https://github.com/kyphii/pokeemerald/tree/feature/dynpal at 575bef6c0cc668b694fdd05b5ae047ac1ed133a2. The donor is reference material; its SaveBlock2 fields, sample palettes and vanilla intro are not merged.

New Game offers live color selection after Boy/Girl. Up/down selects Skin tone, Outfit or Accent; left/right changes it. A/Start accepts; B restores the previous choices and returns to gender selection. Original preserves our current palettes exactly. Skin choices: Original, Light, Tan, Deep. Outfit/accent choices: Original, Blue, Red, Violet, Gold, White, Charcoal, Pink. This provides 256 combinations per protagonist. Hair, pants, outlines and sprite artwork retain their original indices.

Existing saves use the player's own PC, then Appearance. Bedroom PCs include it too. The controls and preview are the same; B restores the original choices. Accepted colors persist when the player saves. No restart is required. This is the player's PC menu, separate from Pokemon storage.

A signature-checked packed selection uses the previously unused 0x409B, now VAR_LA_PLAYER_COLORS. No save structures, storage formats, inventory layout or 14/60-box settings change. Zero or unrecognized values use Original, and invalid parts clamp to Original. Intro choices remain temporary until new-game event initialization commits them. Merely previewing New Game does not change the old save.

Player-tagged walking, running, bike, surfing, fishing, field-action, underwater and ride palettes use the selected parts. Ordinary reflections inherit the recolored source and retain pond/ice filtering. Naming, intro, trainer card and player battle-back paths use the matching trainer palette. The Continue portrait has its own explicit index mapping. Rival/NPC overworld tags and opponent battle palette loaders keep their original colors. In the current standard player/trainer palettes, skin uses indices 1-4, outfit 10-11 and accents 12-13. Transparency, black/white and hair/pants indices are unchanged.

This adds 40 bytes of persistent EWRAM (261420/262144 total), plus temporary heap resources while the picker is open. Each 16-color palette is generated on demand. Intro and field windows use separate graphics ranges to avoid text maps and existing frames. Preview resources are released before returning to the PC.

Native disposable-save tests verify all combinations for both protagonists, invalid/default choices, unchanged rival tags, real PC selection and repeated accept/cancel, save/load/relocation, preserved Pokévial/potions/final box, soft reset and Continue portrait, complete New Game/naming/handoff, actual battle palette loading and bag return. Intro, field-menu and all 1800 compact slots also pass. The reports share the final ROM hash: 3242 checks. Tests never open the user's battery save.
