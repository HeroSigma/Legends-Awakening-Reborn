# Mercury Johto runtime checklist

Use the supplied Reborn ROM. Start from a normal battery save in Hoenn and use the existing Johto travel scientist/menu to enter New Bark; do not begin this test by loading an old emulator save state. Existing numeric map IDs remain stable, but replaced geometry uses new coordinates.

- New Bark: correct graphics, movement, doors and return to Littleroot through the scientist.
- Both player genders and follower graphics; save/reload on a safe land cell.
- Route 29 → Cherrygrove → Routes 30/31 → Violet. Test ledges, stairs and gate entrances/returns.
- Route 32, Union Cave, Route 33, Azalea, Slowpoke Well, Ilex Forest and Route 34.
- All Goldenrod segments, doors, department-store floors, stairs/escalators and map boundaries.
- Routes 35/36, National Park, Route 37 and Ecruteak; Bell/Burned Tower construction exploration.
- Routes 38/39, Olivine and Lighthouse; Routes 40/41, Surf-only sectors and Cianwood.
- Routes 42/43, Mt. Mortar, Lake of Rage and Mahogany.
- Route 44, Ice Path, Blackthorn, Dragon's Den, Routes 45/46.
- Routes 47/48 and cave/exterior transitions.
- Routes 27/26 and Victory Road: distinguish held/out-of-region exits from working internal traversal.
- Route 28, Mt. Silver and Sinjoh Ruins remain registered but have no active entrances.
- Construction scientists: YES advances inspection; NO returns to Littleroot. Use these exits in one-way rooms while gameplay/puzzles are unimplemented.
- Test all source-water shorelines: walking must require Surf where appropriate; test currents, stairs, elevation and bridge transitions.
- Animations/custom donor callbacks remain pending; static scenery is expected in this asset/travel build.
- Open representative new maps in Porymap, including Goldenrod, cave rooms, water sectors and the third interior group.
- Regression visits to validated Hoenn, Sinnoh, Unova, Galar and Kanto destinations; test blackout and saving.

Build/static validation does not replace these in-game tests. Report the map and coordinates for any blocker, passable water, broken door or misaligned boundary.
