# Project working instructions

## Release ROM policy

User instruction: use ONE permanent playable release file:
C:/Users/aadair/Downloads/Legends-Awakening-Reborn/Legends-Awakening-Reborn.gba
(WSL: /mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Legends-Awakening-Reborn.gba).

After a requested rebuild, replace this ROM in place. Do not create a new version-named ROM or release folder for routine updates. Preserve its paired Legends-Awakening-Reborn.sav; never overwrite, delete or reset it during packaging. The initial migration may copy the previous RTC-Friendly-Intro battery save only if the permanent save does not exist. Existing archival ROMs remain untouched.

## Protagonist dialogue

Aren and Aria are speaking protagonists. In story conversations, give the player spoken questions, responses and decisions using SP_NAME_PLAYER and their chosen name. Internal thoughts are occasional characterization, not a substitute for participation. NPCs should respond to what the player actually says instead of inferring an unspoken request. Preserve existing story flags, rewards and scene gates when improving dialogue unless a progression change is explicitly needed.

Use the established dialogue colors: player LIGHT_BLUE, Brendan GREEN, May/Red RED, Wally LIGHT_GREEN. The field message renderer supplies these defaults from the active speaker; explicit script color controls remain supported. Unnamed researcher/narrator dialogue uses the normal readable color; named professors use their character colors.

Evil-team field dialogue uses the central affiliation palette in src/field_name_box.c. Giovanni/Rocket crimson, Aqua deep blue, Magma burnt orange, Cyrus/Galactic violet, Triad/Plasma steel blue, Flare scarlet, Skull charcoal, Yell magenta, Star dark gold, Aether teal. Use the corresponding SP_NAME_TEAM_* speaker tags for future faction dialogue; restore SP_NAME_NONE after conversations. See docs/story/spoken_protagonist/faction-colors.md.

Named rivals and professors use the central custom speaker palette; see docs/story/spoken_protagonist/character-colors.md. Birch uses forest green. Preserve established player/Brendan/May/Red/Wally colors. Use SP_NAME_<NAME> tags for newly authored character dialogue.

## Story polish workflow

Polish the completed story rather than bulk-editing untouched or future scenes. When adding a new scene, review its dialogue, line fit, speaker colors, staging and progression as part of that scene's work. Keep Aren/Aria speaking naturally and retain established character voices.

## Villain alliance canon

Giovanni has united the villain factions. Their operations support a coordinated
plan; distinct ambitions and disagreements do not make them independent enemies.
The completed Hoenn scenes must reflect shared research, equipment and orders.
Do not write Aqua, Magma, Galactic or the Shadow Triad as unrelated competing
investigations unless an explicitly authored deception explains it.

The first Woods scene uses anonymous, faction-colored speaker aliases.
Giovanni's name is first explicitly heard during the Kanto Power Plant shutdown
interruption (FLAG_LA_HEARD_GIOVANNI). The subsequent Paradigm call connects that
name to Norman's description, without revealing every allied leader.
Only use the player's acquired knowledge in later dialogue. Existing saves that
already finished the rescue must not replay it or claim to remember the new radio.


## Saved raid research decision (2026-11-07)

User requested retaining the raid review for future implementation. Prefer a native
pokeemerald-expansion implementation: PR #10319 for newer battle hooks and compact
state, PR #2869 for intro/partner UI, 2v1 presentation and capture-flow references.
CFRU is a behavioral reference, not a FireRed engine transplant. Both Expansion
PRs were closed/unmerged WIP at review; do not treat their feature lists as tested
working code. First prove one isolated Max Raid before adding world dens.
Read docs/features/raids/expansion-pr-review.md and cfru-feasibility.md before work.
Measure runtime battle heap separately from static EWRAM headroom. Preserve story
capture restrictions, ordinary gimmick selection, storage and quest/rift gates.
This is saved research, not authorization to start implementing raids now.

## Test ROM policy

User instruction (2026-11-08): keep ONE reusable test ROM beside the permanent main ROM:
C:/Users/aadair/Downloads/Legends-Awakening-Reborn/Legend Test.gba
(WSL: /mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Legend Test.gba).
For future test builds, replace this test ROM in place; do not create version-named test ROMs or new release folders. Keep the main release ROM unchanged for test-only work. Preserve Legend Test.sav and the main release save; never overwrite, delete or reset either during packaging.


## Branch workflow (user instruction, 2026-11-08)

main is the complete integrated project and must be the GitHub default branch.
Create a new feature/*, fix/* or art/* branch from current main before making any
non-story change. Story work may use main or a story/* branch. Keep main inclusive
of completed work by merging finished branches after appropriate validation.
Do not develop non-story features directly on main. Preserve existing branches.
The current regional atlas work is tracked on feature/world-map-hub.
