#ifndef GUARD_WILD_PROGRESSION_H
#define GUARD_WILD_PROGRESSION_H
#include "wild_encounter.h"
u32 GetWildBadgeStage(void);
u32 GetWildProgressionCap(void);
enum Species ResolveWildLevelSpecies(enum Species species, u32 level);
u32 ClampWildBonusLevel(enum Species species, u32 level);
const struct WildEncounterTypes *GetProgressionWildTypes(u32 headerId, u32 time, const struct WildEncounterTypes *source);
#endif
