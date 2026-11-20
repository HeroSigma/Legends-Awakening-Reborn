# Past Saffron and Silph polish

## Reference and adaptation

Reference: [pret/pokefirered Saffron scripts](https://github.com/pret/pokefirered/tree/master/data/maps/SaffronCity), and its SilphCo_1F through SilphCo_11F event scripts, text and object coordinates. The supplied USA FireRed ROM was identified by its BPRE header and SHA-1; the source manifest records that hash and the exact reference commit. No ROM is committed or redistributed.

Restore the historical occupation, not the original game's progression wholesale. Saffron has eight Rocket sentries and its original signs. The city and tower now use their FireRed-era music instead of Route 104 music. The sleeping entrance guard leaves the infiltration entrance clear. Silph has its original floor-specific Rocket and scientist locations, employee hiding places, floor signs and ninth-floor healing attendant. Actors stay still to preserve the authored routes and prevent incidental wandering into doors or cutscenes. Battles are started by speaking to the opponents, consistent with this chapter's existing interaction scripts.

Thirty ordinary opponents use independent persistent defeat flags. Twenty-two additional six-member teams supplement the original eight: all use the existing smart AI, legal level-capped team builder, and two healing items. Defeated opponents switch to their own post-battle dialogue. Native FireRed trainer flags and scene variables are not imported.

The chapter retains Petrel and Ariana, Wally and shiny Kirlia, the ninth-floor elevator Card Key, all six special item pickups, Porygon, the two Giovannis, Mewtwo and Hoopa's escape. FireRed's Blue rival fight, vanilla Giovanni battle, Lapras/Master Ball awards and Mr. Fuji prerequisites are intentionally not connected to this different story. Kirlia now cries before Wally responds instead of silently acting as a talking Wally object.

Reserve flags 0x281–0x28F and 0x298–0x29E for the restored opponents; preserve 0x290–0x297 for the original eight. Defeated state from existing saves remains valid. Profile slot 11 belongs to the Cozmo scene; slots 12–33 serve the additional Silph opponents.

## Ongoing scene polish priorities

1. Establish the objective through a spoken exchange, then let play advance it. After a long scene, the final line should make the next location or person clear.
2. Stage each actor before opening dialogue: look at the current speaker, approach by a walkable route, react visibly to interruptions, and leave through an actual exit. Keep followers and portal effects out of the speaking lane.
3. Respect acquired knowledge. Do not name unseen professors, reveal the historical period before the player has evidence, or have past Rockets discuss the present alliance unless the scene explicitly exposes that information.
4. Give each location its own ambient evidence. Here that means a seized company, frightened employees, familiar old equipment and ordinary Rockets with their own concerns.
5. Verify first visit, defeat/retry, return visit, save/reload and already-completed saves. Optional pickups and healing must not advance the main story or bypass security.
6. Review text in the linked game font, together with speaker colors and portraits. Script line counts alone cannot prove that a dialogue box fits.

Next focused story reviews: the reactor interruption and Paradigm call; the Wally family report in Verdanturf; then the summit-to-Silph-to-Lavaridge handoff as one continuous playthrough. Keep new feature development separate from these scene reviews.
