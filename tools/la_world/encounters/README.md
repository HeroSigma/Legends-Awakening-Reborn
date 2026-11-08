# Regional encounter authoring

Run author_pools.py to refresh inventory and species metadata.
Run author_pools.py --write to regenerate game tables and wild-availability ancestry.
The preserved baseline is versioned here. Normal builds compile current editable
wild_encounters.json without regenerating its content.

area_rules.json contains explicit safety and donor-metadata corrections.
The tool reads configured species through the ARM preprocessor and uses current
layout metatile attributes. It never registers maps or opens construction gates.
All active regions temporarily follow Hoenn badges. Legendary/mythical/Paradox/
Ultra Beast pools are excluded except Poipole; Naganadel remains evolution-only.

See docs/la_world/wild_pools/review.md for rules, limits and native validation.

Regional homes are authored per evolution family. Gen 5 and later imports are split between Kanto, Johto, Hoenn and Sinnoh. Unova is preserved but cannot satisfy species coverage. See docs/la_world/wild_pools/regional-distribution.md and run test_regional_assignment.py after rebuilding.
