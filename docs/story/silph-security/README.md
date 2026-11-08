# Past Silph security and Lavaridge return

Use the Kanto_SilphCo maps, not the alternate Silph donor maps.

The native card-door geometry is restored across the tower. Eighteen doors start locked; the two ninth-floor bed-area doors stay open so Wally and shiny Kirlia remain reachable. Wally explains that the Card Key is in the stopped ninth-floor elevator. Inspect the elevator door at X24–25 Y3 to enter; the ball inside gives the key. Its exit returns to the ninth floor.

Petrel and Ariana remain at X0 Y17 and X2 Y17 on 11F. The final security door requires the key, Wally's discovery and both admin victories. Entering the office automatically stages the player and starts the two-Giovanni scene. The room's wall is restored to prevent a side bypass; Giovanni, Mewtwo and the rift have coordinated exit paths.

## Optional pickups

| Floor | Position | Reward |
|---|---|---|
| 3F | 8,10 | Alakazite |
| 4F | 3,11 | Manectite |
| 6F | 2,14 | Scizorite |
| 5F | 4,9 | Normalium Z |
| 7F | 30,11 | Electrium Z |
| 10F | 5,15 | Psychium Z |
| 5F | 22,21 | Level 25 Porygon |

Mega Stone and Z-Crystal pickups use the established special overworld icon. Porygon is a one-time gift and goes to storage if the party is full; a full storage system retains the pickup. Failed bag additions retain their world rewards.

The return to Lavaridge includes Birch's report, a named and colored Flannery conversation, then Flannery walking around the player into the Gym. Players who already earned her badge receive a compatible greeting and still see her return indoors.

## Reserved state

- 0x26D–0x280: twenty independent Silph door flags. Never reuse the native FireRed door flags, which collide with Hoenn story state.
- 0x2AD–0x2AF: Blue briefing, station meeting and boarding.
- 0x2B0: Flannery returned indoors.
- 0x2B1: Card Key collected.
- 0x2B2: Porygon collected.
- 0x2B3–0x2B8: six item pickups.

Validation uses disposable saves: `test_silph_security.py` checks door state, actual key search, rewards, persistence and unchanged Hoenn flags; `test_ashes_silph.py` checks the chapter, admin teams, office entry, escape, Hoopa and Flannery's return. No player save is loaded by these tests.
