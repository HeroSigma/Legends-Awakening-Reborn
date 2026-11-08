#ifndef GUARD_DYNAMIC_ENCOUNTERS_H
#define GUARD_DYNAMIC_ENCOUNTERS_H

#include "global.h"
#include "wild_encounter.h"
#include "constants/dynamic_encounters.h"

// Zero flag/variable IDs mean no condition. All conditions must match.
// Species, weights and levels belong to authored tables, never this resolver.
struct DynamicEncounterRule
{
    u16 requiredFlag;
    u16 forbiddenFlag;
    u16 variable;
    u16 minValue;
    u16 maxValue;
    u16 profile;
};

u16 ResolveDynamicEncounterRules(const struct DynamicEncounterRule *rules, u32 count, u32 profileCount);
u16 GetDynamicEncounterProfileForMap(u16 mapGroup, u16 mapNum);
u16 GetCurrentDynamicEncounterProfile(void);
const struct WildEncounterTypes *GetEffectiveWildEncounterTypes(u32 headerId, u32 timeOfDay);

#endif
