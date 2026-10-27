# Conversation staging revision

- Rescue: Red and Pikachu visibly walk south toward Littleroot, routing around the player, Birch and starter bag before disappearing offscreen.
- Lab: Red starts beside Pikachu at (5,4) and walks down to (5,5) after the Birch conversation and starter naming, just before the player introduction; player (6,5) faces west, Red faces east, Pikachu turns east toward the conversation. Red turns toward Birch for the Riolu explanation.
- Greeting: “Red. Glad to meet you properly.”
- Route 103: user-edited automatic approach triggers on row 5 at x1–7 while chapter state is 2. Player walks east to (10,4), directly before Brendan (10,3). Red (11,4) faces May (11,3); Pikachu (12,4) faces west into the group.
- Successful battle advances chapter state to 3, disabling approach triggers. An unsuccessful battle leaves the group available for another attempt.
- Existing story flags, trainer teams, rewards and save layout remain authoritative.

Each row-5 trigger now follows its own collision-checked approach. At x1 the player first steps right around the tree, then steps north to row 4; all paths walk east to Brendan at (10,4). Trigger positions and map geometry were preserved.
