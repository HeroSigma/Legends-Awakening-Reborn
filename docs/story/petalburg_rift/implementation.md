# Petalburg rift report and Wally outing

Norman knows the player through Elara, not as a parent. After the Timeless Woods meeting, its west exits onto Route 102 can queue a once-only thought. The first Norman conversation accepts the account and descriptions, then the existing Wally entrance interrupts his recognition. Norman sends the player with Wally while he contacts Birch.

The native Wally tutorial still saves/restores the player party, supplies the loan Pokemon and runs the Ralts catch. An added visible Ralts reacts to the player's unease and Wally's reassurance before that battle. Wally remains unaware of the rift report. On returning, he thanks everyone and leaves before Norman confirms Birch has been informed. No automatic Birch call is invented yet.

## Persistent state (existing unused slots)
- FLAG_LA_WOODS_EXIT_THOUGHT: 0x03D.
- FLAG_LA_REPORTED_WOODS_TO_NORMAN: 0x03E.
- FLAG_LA_WALLY_RALTS_BOND: 0x03F.
- FLAG_LA_NORMAN_CONTACTED_BIRCH: 0x040.
- VAR_LA_PETALBURG_ARC: 0x4091; 0 pending, 1 report heard, 2 Ralts caught, 3 Birch contacted.

The native Petalburg city/gym vars remain authoritative for the outing and badges. Ralts uses FLAG_TEMP_9, explicitly hidden on map transition; no permanent extra actor flag. Old saves with a completed outing can deliver a late report without replaying the tutorial or falsely marking the new Ralts scene as seen. Nothing rewinds gym progress.

## Geometry
West Woods warps 2/3 return to Route 102 at (6,3)/(7,3); the exit thought allows the emergence row through y=4. Only x=6..7 qualifies.

The native Wally escort crosses Petalburg's east connection into Route 102. The player ends at (5,5), Wally at (5,6). Ralts is registered on Route 102 at (7,5), and approaches to (6,5). All four cells have grass behavior 2 and collision 0. Ralts stands one row above Wally so its small sprite remains visible above the dialogue window. The cutscene explicitly resets its position before spawning; FLAG_TEMP_9 hides it outside the scene. The incorrect out-of-bounds Petalburg actor was removed. Native escort movements, catch battle and gym return warp remain intact.

Gym family-specific trainer, guide, battle/rematch and badge dialogue was updated to Norman's mentor role. Appended NORMAN/WALLY namebox entries preserve prior speaker IDs. No save structure or MAP identities change. Local user Devon map edits are excluded from this story commit.

