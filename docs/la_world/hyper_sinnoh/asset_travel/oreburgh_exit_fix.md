# Oreburgh exit crash correction

The initial additive Sinnoh registry exceeded Emerald's native signed WarpData map-identity range. Oreburgh group123 loaded normally, but Route207 group139 and Oreburgh Gate group167 promoted negative signed bytes into out-of-range unsigned header indices. This explains why entering Oreburgh worked while leaving north or through the gate crashed. Earlier ROM checks compared source bytes but omitted this signed runtime conversion.

Only the new Sinnoh group registry is consolidated:178 groups become127 valid groups0–126, reserving127 for native dynamic-map semantics. Nearby routes, dungeons and interiors are appended to existing Sinnoh area groups. No native runtime/map-lookup code or save structure changes. All old Hoenn/BWA/SWSH group/map identities are exact; Oreburgh and every map originally in groups0–126 retain their IDs. Previously invalid new-map IDs are reassigned and all compiled warps/connections, popup IDs and script map references rebuild together.

Your recent Mystery Events house geometry/event edits, region-section formatting and removal of the temporary size probe were captured as pre-existing changes and preserved. They are recorded separately from this correction's changes. Porymap's registry now uses valid groups.

A host test using the actual native WarpData struct and map-header lookup function reproduces the old signed-index error for139/167 before lookup. All1,290 current registered map lookups pass with AddressSanitizer/UndefinedBehaviorSanitizer, with the saved warp struct still8 bytes and its coordinates at offset4. The reusable migration and ownership verifier now reject map group/number IDs outside0–126.

Runtime retest: load the corrected ROM from a normal in-game save in Oreburgh, leave north to Route207, return south, enter Oreburgh Gate and leave to Route203, then return. Test house entrances, the Oreburgh return scientist, map-name popups and save/reload. A save made in Oreburgh keeps its map identity. This new correction requires in-game confirmation.
