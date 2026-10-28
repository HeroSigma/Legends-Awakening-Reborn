# Free Pokémon Training Scientist

Every currently functional registered Pokémon Center upstairs room has a scientist at X4/Y2. There are 17 rooms, including the existing Frontier center rooms. Legacy donor inspection copies are left alone. The manifest lists each map and actor; rerun tools/la_world/place_training_scientists.py when adding future upstairs centers.

All services are free and require a hatched party Pokémon. No money, items or new save fields are used. EVs can be set to 252, 4, 0 or any exact value from 0–252; the total cannot exceed 510. Resetting all EVs requires confirmation. IVs can be set to any value from 0–31. Nature adjustment uses the existing mint-style stat modifier, preserving personality and the original Nature. Ability choices include only distinct normal and Hidden Abilities actually supported by the selected species. Build inspection displays level, Nature effects, Ability, EVs and IVs.

Level catch-up raises the Pokémon to a chosen level within the current player cap; it never lowers levels or exceeds the cap. Before the Dex milestone, this service caps at 16 rather than bypassing the introduction with level 100. Existing over-cap Pokémon cannot gain another level through the service. Eligible evolutions use the native evolution scene, respect normal conditions and cancellation, and can continue through multiple eligible stages. Moves remain available through the existing summary-screen relearning feature; the scientist adds no move-relearner service.

Each change is previewed and confirmed before it is applied, then validated again at commit. Cancelled, invalid or unchanged choices do not modify the Pokémon. EV, IV and Nature changes recalculate current stats. Eggs and bad eggs are rejected. Personality, OT ID, friendship, held items and the save layout remain unchanged.

Tests use isolated emulator saves. Coverage includes EV/IV boundaries, total limits, legal Ability/Nature changes, cap enforcement, identity preservation, both storage modes, box save/load, upstairs placements, real menu cancellation, numeric value 127 (which must not collide with B/cancel), and native evolution flow. Slateport Market is outside this task.
