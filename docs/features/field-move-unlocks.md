# Field skills without teaching moves

Implemented on feature/field-move-unlocks, based on reborn. No save-layout changes.

Cut, Flash, Rock Smash, Strength, Surf, Fly, Dive and Waterfall require their original Hoenn badge plus the native received-HM flag (or the owned HM for older saves). A compatible, non-egg party Pokemon can assist without learning the move. Ordinary interaction prompts and animations stay native. Fainted-mon policy remains the native field-move policy. Pokemon that cannot learn a skill cannot assist unless they already know it.

Rock Climb recognizes native level-up and egg-move learnability as well as taught moves; it has no TM in this checkout. Both the party menu and verified Sinnoh traversal share the same selector. Rock Climb keeps the project's existing enabled/learnability policy and verified Sinnoh traversal; no new badge or unimplemented HM-giver is invented. Other field moves, including Teleport, Dig, Secret Power and healing moves, still require move knowledge.

Party > Pokemon > FIELD SKILLS exposes the acquired skills in two pages: Cut/Flash/Rock Smash/Strength/Surf/Fly, then Dive/Waterfall/Rock Climb. NEXT PAGE cycles, BACK/B returns. Only eligible skills are listed. Learned non-HM field moves keep their native menu entries. The native menu action buffer is extended to nine rows; the skill pages never exceed eight.

No battle moves or PP are changed. Surf interaction and bytecode selection use the same eligibility helper. Existing follower restrictions, terrain checks, story scripts and map destinations still apply. The feature does not grant badges or HM items.

Validation report: field-move-unlocks-validation.json. Runtime checklist: Cut and Rock Smash objects, Strength pushing, Surf entry/exit, Fly destination selection, Flash in a dark cave, Dive round trip, Waterfall ascent/descent and existing Sinnoh Rock Climb routes; verify before/after acquisition and badge, cancel each prompt, both genders, save/reload and both storage modes.
