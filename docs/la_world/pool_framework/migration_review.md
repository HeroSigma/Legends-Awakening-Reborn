# Wild and trainer pool framework — Reborn

## Scope
User decision: bring over the framework, keep current encounters and trainer teams. The old scaling system is excluded.

Reference: HeroSigma/Legends-Awakening tag la-v0.5.0, commit 01d51631f3aaefa9f271948978768d444aea1960:
https://github.com/HeroSigma/Legends-Awakening/tree/la-v0.5.0

## Findings and adaptation
The tagged trainer-pool engine is byte-for-byte identical to Reborn's existing src/trainer_pools.c, and Reborn already calls DoTrainerPartyPool while constructing trainer parties. The existing lead/ace, composition-rule and selection framework is reused. No trainer teams or pool settings are changed.

The tagged custom wild registry contains development-only Route 101 profiles. Those species tables and their world-phase/region-state save dependencies are NOT activated or imported. Reborn instead adapts the shared profile-selection architecture to native flags and variables.

New files:
- include/constants/dynamic_encounters.h: profile IDs; only DEFAULT is registered.
- include/dynamic_encounters.h: rule and lookup API.
- src/dynamic_encounters.c: deterministic, read-only rule resolution and effective encounter view.
- src/data/dynamic_encounters.h: empty authored map/profile registry.
- tools/la_world/importers/amap/hns_runtime/test_dynamic_encounters.py: tests real linked ARM functions in isolated native mGBA.

Public authoring/debug APIs are retained by EXTERN roots in ld_script_modern.ld, even while an empty registry allows the optimizer to remove their callers.

## Runtime coverage
Normal encounters, Sweet Scent, fishing, Rock Smash, overworld encounters, DexNav, Pokedex area display and match-call encounter lookups use the same effective view. Battle Pike/Pyramid tables retain their native handling. No map identity or encounter JSON is replaced.

Profile zero returns the original header/time table by identity. Invalid header/time inputs return an empty safe view. Invalid rules fail closed to DEFAULT. First matching rule wins. Conditions support a required flag, forbidden flag and inclusive native-variable range; zero IDs disable the condition. No random numbers, levels or species are changed by rule selection.

A future profile must supply TIMES_OF_DAY_COUNT complete WildEncounterTypes entries. Each entry owns land, water, fishing, Rock Smash and hidden pointers; a NULL encounter-type pointer intentionally means no encounters of that type. Authors must preserve other pointers explicitly if only one type should change. Add map entries before the sentinel in sorted group/map order; use canonical Reborn MAP_* identities rather than donor numeric IDs.

## Excluded
No wild_scaling.c/h, scaled evolution/species substitution, trainer-rank calculations, party-average calculations, badge/level scaling or world-state/save framework was imported. No new save fields, flags, variables or progression writes are needed by this framework. Existing native level selection remains authoritative until a separate new scaling design is implemented.

## Validation
24 native ARM resolver checks cover conditions, precedence, inclusive boundaries, invalid inputs and fallback behavior. Every one of the 125 existing wild headers across four time views (500 comparisons) returns the original table pointer. Existing story/intro checks are rerun against the same ROM before release. Current content hashes are recorded in content_inventory.json.

The permanent release remains C:/Users/aadair/Downloads/Legends-Awakening-Reborn/Legends-Awakening-Reborn.gba. Never overwrite its paired save.

Release validation: all 71 combined resolver, bedroom/downstairs and Creator/Birch checks passed on SHA-256 0cb48db73cadb7b3c2df6d70323b93afd68dc5b4249fcc00c43239a14b4d62cc. The existing battery save was preserved during packaging.
