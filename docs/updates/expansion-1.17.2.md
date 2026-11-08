# Expansion 1.17.2 integration

Based on Fixed-Legend-Update at e5596ce6192c8f55162691c8dd86ef627e7840af.
Upstream stable tag expansion/1.17.2: 79dd436920845ebc145577649de624f65298c209.
Includes 31 upstream commits after common ancestor dfb0f84374230f4d462191601179b742f9f077df.
Later untagged master changes are deliberately outside this stable update.

The merge preserves Legends Awakening story, maps, graphics, encounter pools,
quests, storage and expanded bag, trainers, portraits, menus, mounts and other
custom features. Custom-only files are unchanged except the README engine version
and a portable project-root lookup in the integration test helper.

Two conflicts were resolved explicitly. README keeps project identity and credits
1.17.2. BattleLoadAllHealthBoxesGfx keeps our BW BattleUI dispatch, then uses
upstream's revised native health-box loader. BW's own loader already chooses
single/double graphics per battler coordinates, including asymmetric layouts.

Pokemon/BoxPokemon sizes, all three SaveBlock sizes, storage size and flags/vars
offsets are unchanged, as is sizeof(BattleStruct). See expansion-1.17.2-abi.json.
Source saves and original working-tree files are never used as writable test data.

## Verified results

Production ROM build passed. All eight native mGBA suites passed: PC/storage/
save/menu (2,196 assertions), Dynamax, quests (209), villain alliance (151),
existing player-save compatibility using an isolated copy, overworld resource
exhaustion (7), Ashes/Silph (285), and the full prologue for both protagonists.
Evidence is saved under expansion-1.17.2-validation, including the ROM hash.
These focused regressions do not claim to run the entire upstream battle suite.

Static EWRAM usage: 261,484 / 262,144 bytes; IWRAM: 28,152 / 32,768;
ROM linked payload: 33,228,764 / 33,554,432. These match prior static RAM use;
battle heap availability is exercised by tests, not inferred from linker totals.
Pokemon/save/storage ABI sizes and story offsets are unchanged.
No custom-only source files changed beyond the documented test-root portability fix.
Upstream changelog whitespace is retained.

Published locally as the reusable Legend Test.gba. The permanent main ROM and both
paired saves were SHA-256 checked unchanged. The original dirty checkout and
Fixed-Legend-Update backup branch remain intact; integration is isolated on
update/expansion-1.17.2. No default-branch merge is performed.
