# Regional wild distribution

Ordinary evolution families now have explicit regional homes. Distribution follows the earliest National Dex member in a connected evolution family, including babies, later evolutions and ancestry through ordinary alternate forms. Kanto families can also occur in Johto; Johto, Hoenn and Sinnoh families keep their respective native region. Habitat, time of day, available encounter methods and level/evolution gates still apply.

Gen 5 is distributed across the four available regions, with no dependency on unfinished Unova. Later-generation families are also assigned homes in these regions. Existing Unova tables are retained unchanged and do not count toward coverage. No map is opened or registered by this encounter update.

Examples:
- Kanto: Patrat, Lillipup, Pidove, Drilbur, Timburr, Trubbish, Klink, Tynamo, Elgyem and Pawniard families.
- Johto: Snivy, Purrloin, Munna, Sewaddle, Venipede, Cottonee, Petilil, Solosis, Deerling, Foongus, Joltik and Mienfoo families.
- Hoenn: Tepig, Oshawott, Roggenrola, Tympole, Sandile, Darumaka, Dwebble, Scraggy, Sigilyph, Tirtouga, Archen, Frillish and Larvesta families.
- Sinnoh: Vanillite, Karrablast, Cryogonal, Shelmet, Golett, Rufflet, Vullaby and Deino families.

All starter families are restricted to the last two rare slots of their encounter method. They remain subject to habitat and region; they are not forced into every route. Evolution relatives remain in the same regional policy even when a later-generation evolution or earlier-stage baby changes the apparent generation.

The full family roster is regional_families.json. encounter_slots.csv lists exact route, time, method, species and baseline level. regional_assignment_validation.json records source coverage and linked native checks across badge stages and championship. Reproduce with tools/la_world/encounters/author_pools.py --write, then rebuild and run test_regional_assignment.py from the project root.

This pass includes standard National Dex representatives and all 54 ordinary Alolan, Galarian, Hisuian and Paldean forms configured in this build. Exact form locations are in regional_form_locations.csv. Costume, Totem, Zen Mode and legendary forms remain outside ordinary regional-variant distribution. Cosmetic patterns and unrelated alternate forms are not exhaustively distributed. Scripted legendary, mythical, Paradox and Ultra Beast battles are unchanged; the pre-existing rare nighttime Poipole exception is retained. Region-specific progression after Hoenn remains separate future work.


## Regional forms

Alolan forms mainly inhabit Hoenn; Alolan Vulpix and Sandshrew families use snowy Sinnoh habitats. Galarian forms are split between Johto forests/haunted areas, Sinnoh snow, Kanto industrial habitats and Hoenn coasts. Hisuian forms inhabit Sinnoh. Paldean Combat Tauros uses Kanto grasslands, Blaze Tauros Hoenn volcanic/desert areas, and Aqua Tauros/Paldean Wooper Hoenn marsh/coastal habitats.

Shared ancestors can occur in the additional region needed by their regional descendants. Perrserker, Sirfetch’d, Cursola, Obstagoon, Runerigus, Mr. Rime, Overqwil, Sneasler and Clodsire follow their specific regional evolution branch. Existing wild level gates remain in force; advanced forms do not appear below their availability threshold. Starter regional evolutions retain rare-slot placement.

Validation: all 54 regional forms appear in the linked, level-resolved encounter pools at an eligible progression stage. The native audit inspected 307,050 slots across all badge stages and the championship state; regional membership, exclusions and level ceilings passed. Total authored coverage is 955 species/forms.
