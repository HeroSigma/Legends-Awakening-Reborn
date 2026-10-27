# Selected NPC overworld roster

All 40 donor/source IDs are taken from the user selection. See manifest.json and roster.png. Alain is the conventional spelling of the user label “Alaine”. These are NPC overworld appearances, not trainer battle portraits or replacement player avatars.

Selected characters are registered as OBJ_EVENT_GFX_LA_ROSTER_<NAME>. Existing Red, Blue, Brendan, May, Birch, Silver, Kris, Wally, Archie and Maxie walking NPC role IDs resolve to the selected art. Other selections are available in Porymap but are not placed on maps. Specialized cycling/surfing/field-action variants retain their existing contracts pending dedicated donor action-sheet selection.

The renderer resolves NPC role choices after dynamic/species graphics, ahead of legacy map-specific Hyper substitutions. This ensures Red, Birch and the rivals use the same selected sheets in already-converted Hoenn maps. Existing actor IDs, coordinates, movements, story flags, scripts, battles and rewards are preserved. Player-avatar IDs are not overridden.

Images are indexed losslessly from the donor PNG frames and exact ROM palettes. All original frames are kept, with standard nine-frame NPC walking animations. Native pointer-table declarations and indexed PNG sheets make each selection editable in Porymap. Palette banks are deduplicated among the 40 selections.

Missing selections are listed in missing_selections.json. That list compares the selected cast with main-series protagonist/rival groups through Generation 9; it is not a claim that their art is absent. Additional optional pairs cover Let's Go and Legends: Arceus.

## Additional selections

Ethan uses the exact requested legacy RGBA backup, sliced using its 16x32 nine-frame metadata and indexed against the recovered palette. Oak uses Aesthetic Red 071; Juniper BWA 071; Cynthia Hyper 183; Random Portals SWSH 091. Ethan and normal Oak NPC roles resolve to these choices; Alolan Oak keeps its own identity. No new map placements are added.

HoopaRing is a **single** graphics entry from Hyper 004, with all seven images. The original 20 visual AnimCmd sequences are ported and checked byte-for-byte. Animation 20 is a project-owned emergence presentation: ring frames, large open ring, then Hoopa. It finishes holding Hoopa rather than looping the reveal. The larger-form frame is retained in the same source sheet, with no separate character registration. No teleport, encounter or donor gameplay behavior is activated.
