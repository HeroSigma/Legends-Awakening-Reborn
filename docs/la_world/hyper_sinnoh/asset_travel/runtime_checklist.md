# Hoenn closure and Sinnoh asset/travel runtime checklist

Use the combined Sinnoh Assets/Travel ROM. Build/static verification passed; boxes below require actual runtime testing. Close/reopen Porymap after the registry update, and retain any unsaved manual edits before reopening.

## Oreburgh exit retest

- [ ] Load the corrected ROM from a normal in-game Oreburgh save. Leave north to Route207, then return south.
- [ ] Enter Oreburgh Gate, exit to Route203 and return through the Gate to Oreburgh.
- [ ] Check the return scientist, both directions of travel, map names and a fresh save/reload.

## First Sinnoh canary

- [ ] Load an existing Hoenn save; native party/items/flags remain intact.
- [ ] Both player genders: enter Sootopolis Mystery Events house normally; visiting trainer/old-man interaction and native west stairs work in both house layouts.
- [ ] Annex scientist Cancel stays in the house; Yes arrives on Oreburgh street49,8 with the correct map name.
- [ ] Oreburgh scientist at50,8: Cancel stays; Yes returns to native house10,6. Repeat both ways.
- [ ] Oreburgh houses, Gate and Route207: door arrivals, exits, collision/elevation, and connections behave correctly; no roof/dummy door teleport.
- [ ] Explore Oreburgh Gate → Route203 → Jubilife → Route202 → Sandgem → Route201 → Twinleaf, checking map names and every boundary in both directions. Construction gates intentionally remain; use project debug map travel for gated inspection rather than deleting native story actors.
- [ ] Sinnoh primary flowers/water/terrain animate without corruption before and after map changes.
- [ ] Walk shoreline cells and Surf where appropriate; verify no walking on water, unintended bridge drops, invisible blockers or missing elevation transitions.
- [ ] Save/reload in Oreburgh and on a route, then return to Hoenn. Verify recorded met-location remains valid; confirm blackout returns through existing native heal semantics. Sinnoh heal/Fly/service registration is not implemented yet.

## Regional asset audit

- [ ] Porymap opens new HyperSinnoh groups/layouts and recovered tilesets; edits/reopen retain registration.
- [ ] Visit all split Floaroma/Route205/210/212/213 sectors and both sides of their seams; keep separately identified sectors.
- [ ] Inspect lakes, forests, Coronet floors, Spear Pillar, Galactic rooms, League, Safari and special links; test normal return doors and scientist inspection travel.
- [ ] Veilstone37.29/37.30/37.31: inspect recorded27 solid construction props against donor art before manual cleanup; no invalid graphic reads.
- [ ] Check manual-review held entrances; no foreign Kanto/Johto or donor scripted destination should activate unexpectedly.
- [ ] Town construction notices display correctly. New Sinnoh maps have no donor trainers/items/quests/shops/healing logic; absence is expected in this asset/travel phase.

## Hoenn finalization regression

- [ ] Pacifidlog EV Cave, Route129 Remote Island, Rainbow/Allearth links and Sootopolis annex have valid entrances/returns. Construction scientists may gate entrance access but should not trap an arrival inside.
- [ ] Route106 special scientists stand on valid cliff cells.
- [ ] Frontier west/east plazas: ferry arrival/return, facility entrances, Sudowoodo, native facility menus/rewards and save/reload.
- [ ] Native Trick House puzzles/rewards, SS Tidal cabin/deck travel, Artisan/Altering Cave and compatible event-island floors retain native gameplay.
- [ ] New Champion Island harbor inspection offer and both Outer Space aliases open/return; native Birth/Navel Island identities remain separate.
- [ ] Route110/114 water and Route119 Weather Institute/approach regressions stay fixed.
- [ ] Visit validated BWA and SWSH canaries, travel back, and save/reload without asset/animation/dynamic-rival regressions.

Record failures with map donor ID, coordinates, player gender, Surf/bike state and a screenshot. Runtime sign-off is still required for this new batch.

## Coronet gate retest

- [ ] Talk to the blocking Coronet scientist: Cancel stays put; Yes passes through the existing door.
- [ ] Continue through Coronet toward Route216/217 and Snowpoint; test both directions.
- [ ] Follow the upper Coronet floors to Spear Pillar; test inspection offers, return doors and save/reload.

## Rock Climb

- [ ] On foot, face the confirmed rocks and press A: Yes climbs, Cancel remains in place.
- [ ] Coronet36.91: test both diagonal routes in both directions, correct landing elevation, follower behavior and save/reload.
- [ ] Route208 and Iron Island36.64: climb in both directions. Test party-supported climb and the project Bibarel helper.

## Vertical cliffs

- [ ] Acuity: from19,39 face north and press A; test Yes/Cancel, landing19,34, then face south to descend.
- [ ] Test all12 approved strips in the vertical ledger in both directions, followers, elevation and save/reload.
- [ ] Recheck the eight prior diagonal routes and native bumpy-slope/Acro Bike behavior outside these scoped Sinnoh approaches.
