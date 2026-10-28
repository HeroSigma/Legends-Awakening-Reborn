# Free Pokémon Training Scientist

Every currently functional registered Pokémon Center upstairs room has a scientist at X4/Y2. There are 17 rooms, including the existing Frontier center rooms. Legacy donor inspection copies are left alone. The manifest lists each map and actor; rerun tools/la_world/place_training_scientists.py when adding future upstairs centers.

All services are free and require a hatched party Pokémon. No money, items or new save fields are used. EVs can be set to 252, 4, 0 or any exact value from 0–252; the total cannot exceed 510. Resetting all EVs requires confirmation. IVs can be set to any value from 0–31. Nature adjustment uses the existing mint-style stat modifier, preserving personality and the original Nature. Ability choices include only distinct normal and Hidden Abilities actually supported by the selected species. Build inspection displays level, Nature effects, Ability, EVs and IVs.

Level catch-up raises the Pokémon to a chosen level within the current player cap; it never lowers levels or exceeds the cap. Before the Dex milestone, this service caps at 16 rather than bypassing the introduction with level 100. Existing over-cap Pokémon cannot gain another level through the service. Eligible evolutions use the native evolution scene, respect normal conditions and cancellation, and can continue through multiple eligible stages. Moves remain available through the existing summary-screen relearning feature; the scientist adds no move-relearner service.

Each change is previewed and confirmed before it is applied, then validated again at commit. Cancelled, invalid or unchanged choices do not modify the Pokémon. EV, IV and Nature changes recalculate current stats. Eggs and bad eggs are rejected. Personality, OT ID, friendship, held items and the save layout remain unchanged.

Tests use isolated emulator saves. Coverage includes EV/IV boundaries, total limits, legal Ability/Nature changes, cap enforcement, identity preservation, both storage modes, box save/load, upstairs placements, real menu cancellation, numeric value 127 (which must not collide with B/cancel), and native evolution flow. Slateport Market is outside this task.

## Sprite compatibility

Training scientists use the native Emerald Scientist 1 sprite. The generic FireRed scientist ID previously pointed at an empty Emerald graphics slot, so the actor existed but contributed no visible pixels. A graphics-table alias also maps that old ID to the Emerald sprite for existing saved actors. Pixel-difference tests verify visible bodies in all 17 rooms, alongside training/evolution and Nurse Joy regressions.

The IV adjustment stat list includes **31 All** after Speed. It uses the normal confirmation, sets all six IVs to 31, recalculates stats, and reports an unchanged build when all six are already maximum. Cancellation preserves the original IVs.

## Build visibility

EV and IV stat lists show each current value beside its stat. The EV selection screen keeps used points (out of 510) and remaining points visible in the dialogue box, without an extra confirmation press. The budget is recomputed on each visit, including after edits or cancellations. Inspect Build includes the same budget. Individual editing and 31 All keep their existing confirmation and legality checks.

## EV presets

EV presets offers four complete 510-point spreads in stat order HP / Attack / Defense / Sp. Attack / Sp. Defense / Speed:

- Physical attacker: 6 / 252 / 0 / 0 / 0 / 252.
- Special attacker: 6 / 0 / 0 / 252 / 0 / 252.
- Physical wall: 252 / 0 / 252 / 0 / 6 / 0.
- Special wall: 252 / 0 / 6 / 0 / 252 / 0.

The preview states that all current EVs are replaced, lists all six values and the 510/510 total, and requires confirmation. Canceling preserves the entire original spread; selecting an identical spread reports that no change is needed. Presets do not alter IVs, nature, ability, or level, and remain free. Individual EV adjustments remain available for custom builds.

## Editing flow

Confirmed edits, cancelled confirmations, and unchanged/invalid choices return to the EV/IV stat picker or the relevant nature, ability, or preset list. EV/IV pickers retain the selected stat, including 31 All. Nature and ability lists highlight the current setting, and preset lists retain the selected build. B backs out to the service menu. Numeric EV/IV cancellation returns to the stat picker, and the EV quick-value list can also back out one level. Level evolution and one-shot EV reset retain their existing flow.
