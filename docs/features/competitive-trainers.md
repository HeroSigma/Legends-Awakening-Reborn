# Competitive trainer rollout

The first playable batch replaces Route 102 Calvin, Rick, Tiana and Allen after the National Dex gift. Before that story milestone, native teams and uncapped progression remain intact.

Each trainer has an authored six-member themed team at levels 14–16, perfect IVs, legal EV spreads, native Smart AI and two Super Potions. Their last Pokémon uses either a supported Tera type or matching Z Crystal. The choice is deterministic from the player Trainer ID and opponent identity, so reopening the battle does not reroll it. Ordinary trainers have no guaranteed shiny.

Learnset validation uses this project's level-up, teachable and egg-move data. Level-evolved Pokémon must meet their minimum evolution level. All four teams are checked before activation; invalid definitions retain the original roster. Editable team descriptions are in competitive-trainers-rosters.json; compiled rosters are in src/data/legends_trainer_teams.h.

After the Dex gift, party experience and Rare Candy growth follow these next-challenge caps: Roxanne 16, Brawly 20, Wattson 26, Flannery 32, Norman 37, Winona 43, Tate and Liza 49, Juan 56, League 65. Post-Champion regional caps remain future work. Wild encounter scaling retains its existing next-leader lowest-level policy.

## Test in game

Use the usual permanent ROM and paired battery save. After receiving the National Dex, challenge an undefeated Calvin, Rick, Tiana or Allen on Route 102. An already defeated trainer is not reset. Check six party indicators and the trainer's healing and ace gimmick during battle. Both normal storage and 60-box collection mode are covered by isolated emulator tests; player battery files are not used for tests.

Native emulator validation covers party generation, IVs, EVs, move/evolution legality, cap transitions, stable gimmicks and actual trainerbattle setup. These checks do not prove optimal AI decisions in every matchup. AI uses the existing project implementation.

## Remaining rollout

Other trainers, major-character shiny aces, Gym/League Singles–Doubles prompts, later regional caps and additional supported gimmicks are not enabled by this batch. Story battles retain their existing format. The next batch should author Roxanne's distinct singles and doubles strategies and verify both before expanding further.
