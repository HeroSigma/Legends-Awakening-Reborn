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
West Woods warps 2/3 return to Route 102 at (6,3)/(7,3); the exit thought allows the emergence row through y=4. Only x=6..7 qualifies. Ralts enters from Petalburg (37,15) to (36,15), beside Wally (35,15); player (35,14). All four are grass behavior 2, collision 0 in the linked native map. Existing tutorial escort movements and gym return warp remain intact.

Gym family-specific trainer, guide, battle/rematch and badge dialogue was updated to Norman's mentor role. Appended NORMAN/WALLY namebox entries preserve prior speaker IDs. No save structure or MAP identities change. Local user Devon map edits are excluded from this story commit.
