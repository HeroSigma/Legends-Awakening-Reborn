# Optional 60-box collection storage

Reborn implementation of switchable 14-box normal / 60-box collection storage (1,800 slots).

In-game Options > PC BOXES > A opens two confirmations. Switching erases boxed Pokémon; party and story progress remain. Collection records simplify nicknames, trainer/met history and cosmetic personality data. Battle traits, friendship, eggs and evolution-relevant fields are preserved. Collection mode retires Frontier, contests, Trainer Hill and associated side systems; their maps remain registered.

## Porting status

This branch isolates storage changes from the working Legends Awakening Reborn project. Its tested runtime was the complete Reborn checkout; this isolated branch has not yet been built independently. It is a porting reference, not a tested drop-in patch for arbitrary pokeemerald-expansion revisions.

Before using in another project, regenerate and review save ABI spans and activity gates, adapt map constants and test helpers, check species/move/item limits, and revalidate save capacity. Never apply Reborn numeric save offsets to a different ABI. A released save format needs an explicit migration when changed. Back up battery saves; old emulator save states are incompatible with the RAM layout.

## Source layout

- src/la_pc_*: runtime storage, cache and compact codec wrappers.
- src/la_collection_save.c: transactional collection flash banks and checksums.
- tools/la_world/storage/: reusable codec, adapter, tests and generators.
- src/data/la_collection_save_spans.h: generated Reborn ABI spans, must be regenerated for another project.
- src/la_pc_features.c: activity guards, must be regenerated/adapted for another project.

## Validation in the complete Reborn checkout

2,211 production integration assertions, all 1,800 slots, mode transitions, save/load and corruption fallback; opening story checks in both modes; existing normal battery save loaded read-only. Full PC scan: seven emulated frames. These results do not certify another project or this extracted branch in isolation.

No ROMs, battery saves, donor graphics or unrelated story/map changes are included in this feature commit. Use the repository's existing license; do not distribute copyrighted game ROMs.
