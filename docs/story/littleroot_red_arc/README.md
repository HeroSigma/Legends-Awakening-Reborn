# Littleroot closing chapter

## Flow

1. Preserve the selected Route 101 starter; Birch recognizes Red, who explains the portal and his earlier Hoenn travels. Player and Red exchange names. Optional starter naming remains available.
2. Birch explains that an aide found Riolu near a rift, away from its native Sinnoh habitat. Red takes it as a fresh travelling partner, while Pikachu remains beside him.
3. Red spars using level 10 Riolu against the new level 5 starter. Aerial Ace, trained stats and a Focus Sash make this a loss for all three normal starter choices. This is a normal trainer fight, not the Birch first-battle tutorial; native tutorial enemy replacement is explicitly excluded for this fight. The loss heals the player and never deducts money or triggers blackout.
4. Red congratulates the player and gives the Mega Ring once. He and Pikachu walk down the lab aisle to leave together. Birch sends the player to call both children on Route 103.
5. Brendan and May recognize Red as Kanto's Champion. The player learns his identity and reason for investigating rifts. Player + Red battle both rivals using the native four-trainer multi-battle system. Red uses Riolu; Pikachu watches. Each rival uses one of the other Hoenn starters. Defeat is healed and permits retry. Victory advances native Birch lab / Route 103 progression.
6. On return, Birch gives a National Pokédex and enables the actual DexNav start-menu flag. May gives five Poké Balls. Temporary Red and Pikachu actors leave together. Native adventure progression unlocks the standard running-shoes event.
7. Elara hears the player's account, silently thinks of Caelum, then gives the running shoes and says goodbye. The player does not hear or answer the thought.

## Saved state and compatibility

`VAR_LA_LITTLEROOT_ARC` aliases unused var 0x4083: 0 pending lab, 1 spar/ring pending, 2 Route 103, 3 research gifts pending, 4 farewell pending, 5 complete.

Project flags use unused slots 0x02F–0x038: lab complete, Mega Ring received, lab Red visibility, lab rival visibility, Route 103 actor visibility, Route 103 complete, research gifts received, Elara farewell, active lab fight and active partner fight. DexNav uses its configured 0x901 flag.

Trainer IDs 855–861 are appended; the saved capacity remains 864 and earlier trainer IDs do not change. Partner Red is appended at partner ID 2. No save structures, map IDs, native flags or earlier imported regions are renumbered. National Dex acquisition does not advance the separate post-League Johto starter state.

The new lab arc starts for a save that met Red and is still at the starter-receiving lab event. Already completed adventures are not reset. Temporary actors have separate map-specific flags. Reward flags prevent repeated key items and Poké Balls. Bag-full gifts can be resumed by talking to Red/Birch without replaying a battle or trapping the player.

See `coordinate_ledger.json`, `dialogue.md` and `runtime_validation.json` for review. Native mGBA tests use disposable saves, both genders and all three starters; the permanent player save is never loaded by tests.
