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
