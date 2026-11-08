# Regional wild pools

This pass authors 424 intended encounter maps, 1696 explicit
morning/day/evening/night tables, and 31,524 source slots. Coverage includes
901 ordinary National Dex species through Gen 9, including starters and Poipole.

## Area safety
Littleroot and Oldale have no encounters. Native Hoenn encounter-area ownership is
preserved. Gyms, shops, ordinary houses, transport interiors and other safe areas
are excluded. Decorative grass/water alone never establishes a town encounter pool.
Established town fishing/Surf locations receive only water methods, not grass.
Explicit area rules correct unreliable donor map-type labels on Unova's routes,
Pinwheel Forest and Dreamyard.

No maps were registered, no construction gates opened and no map assets changed.
Retired Mercury/GS/FRLG maps and Galar are outside the active rollout. Battle
facility challenge pools remain native. Existing scripted legendary encounters
are not part of these ordinary pools and remain unchanged.

## Habitat and time
Species are assigned to meadow, forest, marsh, coast, cave, mountain, desert,
volcanic, haunted or snowy habitats. Current translated terrain determines which
encounter methods can exist, after area safety has been checked.
Water pools use aquatic families rather than generic land pools. Native common species remain where
appropriate. Other slots provide compatible cross-generation diversity.
Night pools prioritize compatible Dark/Ghost species; daylight favors the
corresponding route's ordinary wildlife. Ocean night pools still use aquatic
species. Poipole is confined to rare nighttime forest/haunted slots.

This is a generated ecology/balance pass, not a claim that every individual slot
has received human review. Complete editable route/time placement is supplied
for tuning. One ordinary representative form per National Dex entry is used;
cosmetic and regional alternatives are not exhaustively distributed.

## Badge levels and evolution
All active regions temporarily follow consecutive Hoenn badges. Each badge adds
three levels to the route's per-slot baseline, capped at the next normal Gym
Leader's lowest team level. Fishing rod tiers retain separate baselines.

| Badges | Next opponent | Ceiling |
|---:|---|---:|
| 0 | Roxanne | 12 |
| 1 | Brawly | 16 |
| 2 | Wattson | 20 |
| 3 | Flannery | 24 |
| 4 | Norman | 27 |
| 5 | Winona | 29 |
| 6 | Tate & Liza | 41 |
| 7 | Juan | 41 |
| 8 | Sidney / League | 46 |

After the Hoenn championship the ceiling is 100; route baselines still apply.
Ceilings are read from compiled teams, not a duplicated hardcoded level list.
Player EXP and trainer teams are unchanged.

Evolution stages use the resulting Pokémon level. Unconditional level evolutions
advance before DexNav reads the table. Under-level evolved forms fall back through
their ancestry. Special evolutions without a level requirement have authored wild
availability gates of 20/36/50 by stage, never below an ancestor's real level gate.
This prevents early low-level Raichu or other special evolved forms. It does not
grant item/trade/friendship or other special evolutions to player-owned Pokémon.
Poipole does not auto-evolve; Naganadel is evolution-only.

Slot maxima and DexNav/lure bonuses stop before the searched species' next
unconditional evolution threshold. The search identity therefore matches the
actual encounter. Random battles are blocked before the player has a starter.
No persistent fields or new progression flags were added.

## Outputs
- encounter_slots.csv: map, time, method, species and baseline levels.
- badge_level_ranges.csv: ranges measured from the linked ROM at every badge stage.
- map_inventory.csv: active maps, terrain and area eligibility decisions.
- species_catalog.json: configured eligibility and evolution ancestry.
- runtime_validation.json: isolated native mGBA checks against the built ROM.
- area_rules.json under tools/la_world/encounters: explicit area safety policy.
- src/data/wild_encounters.json: editable game data, compatible with normal tools.

The author_pools.py --write command deliberately regenerates encounter data from
its preserved baseline. A normal ROM build does not regenerate the authored pools
or overwrite manual encounter edits.

## Validation and review
Native checks cover every linked slot at all nine badge stages, excluded species,
safe areas, evolution boundaries, DexNav level generation and actual wild-mon
creation. Story intro and bedroom/save-reload regressions are checked separately.
No user battery save is loaded by these tests.

Runtime balance review remains useful: test grass/caves, Surf, all fishing rods,
Rock Smash, morning versus night, and rare species in each region.

Regional encounter maps: Hoenn: 176, Sinnoh: 83, Unova: 9, Johto: 110, Kanto: 46.

Final native validation: 59 checks passed; 283,149 linked slots inspected. Framework: 24 checks. Bedroom/save-reload: 42 checks. Intro: 5 checks. All reports match the final ROM.
