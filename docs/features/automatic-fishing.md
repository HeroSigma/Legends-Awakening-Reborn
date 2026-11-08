# Automatic fishing

Implemented independently on this feature branch; not merged into reborn.

Use an owned rod normally beside valid water. The cast and bite animation remain, but a map with a fishing table always produces a bite and reeling needs no button timing or repeated dot rounds. The native rod slot selection, region/time-of-day species, levels, Feebas rules, shinies and fishing counters remain authoritative. This hooks a battle; it does not automatically catch Pokemon or repeatedly cast.

B cancels before the hook is committed, using the native no-catch cleanup. Maps without fishing data still fail normally. Set I_FISHING_AUTOMATIC to FALSE in include/config/fishing.h for the original minigame. No new save fields.

Validation: native-ROM test covers all rods, both storage modes, unsupported maps and cancellation. Manual checks: fish from land and Surf, cancel, catch/flee/lose, confirm control and avatar restore after battle.
