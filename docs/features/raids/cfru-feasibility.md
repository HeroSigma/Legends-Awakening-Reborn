# CFRU Max Raid feasibility review

Reviewed 2026-11-07. Research only; no raid gameplay enabled and no playable ROM replaced.

## Reference implementation

https://github.com/Skeli789/Complete-Fire-Red-Upgrade/blob/master/src/dynamax.c
https://github.com/Skeli789/Complete-Fire-Red-Upgrade/blob/master/src/raid_intro.c
https://github.com/Skeli789/Complete-Fire-Red-Upgrade/blob/master/src/wild_encounter.c
https://github.com/Skeli789/Complete-Fire-Red-Upgrade/blob/master/src/Tables/raid_encounters.h
https://github.com/Skeli789/Complete-Fire-Red-Upgrade/blob/master/src/Tables/raid_partners.h

CFRU identifies raids through FLAG_RAID_BATTLE on a wild battle. Its raid intro offers up to three NPC partner candidates, each with a three-Pokemon team, and writes the selected partner into the multi-battle setup. This is selection among partners, not three additional simultaneously active trainers. Raid rank is determined from progression, with six star ranks and separate level ranges. Encounter creation applies rank-dependent IVs, ability and egg-move selection. Den completion flags support repeat availability. Reward tables and quantity rules are separate from the combat loop.

Boss rules are integrated across Dynamax, damage, attack cancellation, start/end turn, fainting and battle-end scripts. Shield cycles depend on boss HP/level; shield counts additionally use base stat total. Higher-level bosses can repeat attacks and nullify stat changes. Raid-specific termination, ball escape and capture/reward scripts handle the ending. It is not just a permanently enlarged wild Pokemon.

## Our engine

Already present: Dynamax/Gigantamax rendering and moves, normal trainer partner battles, item/reward APIs, scripted encounter gates and the quest/rift framework. Existing BATTLE_TYPE_RAID, ITEMMENULOCATION_RAIDEND and Dynamax raid TODO comments are placeholders; they do not implement an operational raid loop. CFRU uses its own FireRed hooks, gNewBS structures and some fixed RAM addresses; those must not be copied into this Emerald engine.

Last measured build: EWRAM 261484/262144 bytes (660 bytes left). ROM is approximately 99.1% full. A native implementation is feasible in principle, but its memory budget must be proven by the linker as features are added. Use compact battle-only state and avoid new large permanent save structures. Partner availability should initially use existing story flags and verified backsprites; unavailable backsprite characters cannot be selected as visual partners.

## Recommended implementation order

1. One isolated development encounter: player plus one NPC partner against one boss. Confirm the empty opponent slot, targeting, spread moves, AI and faint/replacement handling. Keep ordinary doubles unchanged.
2. Raid-specific permanent boss Dynamax and increased HP, with safe turn accounting and clean restoration of player Pokemon. Separate from ordinary three-turn Dynamax.
3. Shield phases, extra boss actions and stat/status cleansing, with explicit tests for multi-hit moves, residual damage, immunity/OHKO effects and forced switching.
4. Win/loss/retreat flow, post-win capture only, full-party/PC handling and exactly-once rewards. No normal prize-money loss for a failed optional raid unless deliberately designed.
5. Badge/cap-scaled star ranks, regional den species, cooldowns and partner selection. Never overwrite story force-loss battles or the natural-wormhole League/quest seals.
6. Rift presentation and tracker/quest integration after combat is validated. Hoopa is a story companion, not a raid reward courier.

Use CFRU as a mechanical reference and port selected logic to native engine structures with attribution if reused. Do not merge the full FireRed upgrade or enable raid placeholder flags as a shortcut. A first version should prove combat and capture before building a large den menu or distributing raids throughout the maps.
