# First downstairs scene: the rift report

The scheduled Petalburg Gym broadcast is interrupted by Hoenn news: unstable rifts briefly show unfamiliar cities/mountains, none is safe for travel, and unusual non-native Pokemon outbreaks may be connected. Lead scientist Colress is named. Elara quietly recognizes him and deflects the player's question. No deeper backstory is revealed.

The player and Elara watch the existing TV from native movement paths verified against the current Hyper house geometry. ELARA, NEWS ANCHOR and the selected player name use the implemented namebox system; player lines retain light blue. New dialogue uses complete-thought pages with no scrolling-line fragments. All dialogue is editable in data/scripts/legends_downstairs.inc; dialogue.json is the reading copy.

## Story state
- Existing VAR_LITTLEROOT_INTRO_STATE is authoritative; new semantic LA_INTRO_RIFT_REPORT = 15 runs this scene.
- FLAG_LA_WATCHED_RIFT_REPORT = 0x26 (verified unused before allocation) records completion once.
- The scene requires a Legends story save and the completed upstairs package scene. It runs only in the player's own house, only before rescuing Birch, and never replays once watched.
- Completion restores LA_INTRO_COMPLETE = 7 and the existing home-TV flag. No rival, starter, rescue, badge, encounter or regional-travel progression is granted or reset.
- VAR_TEMP_2 guards a once-per-load check for old previews resumed at the stair landing. Saves elsewhere downstairs can trigger the scene on their next normal entry. No save is relocated.
- Elara directs the player next door, preserving the existing rival-family → rival → Route 101/Birch progression. Her reminder is available before Birch rescue; later native healing, match-call and reward logic remains authoritative.
- No rift travel is unlocked by hearing a news report.
- Existing legacy truck/Petalburg report states 1–6 retain their old meanings for non-Legends saves. No save structure is changed.

Release uses the permanent Legends-Awakening-Reborn.gba filename; its battery save must never be overwritten.

## Validation
42 native emulator checks pass across both character choices, including the entire bedroom sequence, TV staging, report completion, restored control, native save/soft reset/Continue before and after the report, and subsequent rival-family/rival readiness progression. Five Creator/Birch intro regression checks also pass. Colress news and Elara whisper screenshots were visually reviewed. Native ROM build and changed-file whitespace checks pass.
