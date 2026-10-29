# Crowded overworld maps and blank debug TMs

Ordinary generated overworld encounters are limited to two active Pokemon. The four reserved encounter local IDs remain unchanged, preserving existing object identity rules. Before attempting a spawn, the engine requires more than two free object-event slots, leaving two slots for followers and story actors. If a subsequent allocation still fails (including sprite exhaustion), it quietly retries later rather than opening an assertion screen. Missing local-ID lookups are checked before dereferencing an old object.

Manual story Pokemon and DexNav searches retain their existing behavior. This is a cap on generated wild Pokemon, not a total cap on NPCs, followers or story Pokemon. Maps with fewer available slots can show fewer than two wild Pokemon.

Fill Bag and Fill Pocket TMHM omit machine items whose move is MOVE_NONE. Current reserved TM51–TM100 entries are blank; the 50 working TMs and eight HMs remain. Re-running a Fill Bag/category command also removes blank machines previously added by older builds. No legitimate machine items or player save files are removed during ROM replacement.

Validation uses isolated native mGBA saves in both 14- and 60-box modes, seeds all blank machines, checks cleanup, valid machines, all-category counts and save/reload, exercises object-capacity boundaries, and observes Route 116 for 3,600 frames. The debug-fill regression suite checks migration, inventory quantities and PC-fill termination. DexNav approach/contact is tested separately.
