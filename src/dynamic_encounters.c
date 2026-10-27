// Profile-selection architecture adapted from HeroSigma/Legends-Awakening
// tag la-v0.5.0 (01d51631f3aaefa9f271948978768d444aea1960).
// No legacy scaling, trainer rank, world-state storage or development pools.
#include "global.h"
#include "dynamic_encounters.h"
#include "event_data.h"
#include "wild_progression.h"
#include "constants/flags.h"
#include "constants/vars.h"

struct DynamicEncounterMap
{
    u16 mapGroup;
    u16 mapNum;
    const struct DynamicEncounterRule *rules;
    u32 count;
};

#include "data/dynamic_encounters.h"

extern const u32 gWildMonHeaderCount;
static const struct WildEncounterTypes sEmptyTypes;

u16 ResolveDynamicEncounterRules(const struct DynamicEncounterRule *rules, u32 count, u32 profileCount)
{
    if (rules == NULL || profileCount == 0)
        return DYNAMIC_ENCOUNTER_PROFILE_DEFAULT;

    for (u32 i = 0; i < count; i++)
    {
        const struct DynamicEncounterRule *rule = &rules[i];
        // Invalid configuration fails closed; never read beyond native save data.
        if (rule->profile >= profileCount
         || rule->requiredFlag >= FLAGS_COUNT || rule->forbiddenFlag >= FLAGS_COUNT
         || (rule->variable != 0
             && (rule->variable < VARS_START || rule->variable > VARS_END
                 || rule->minValue > rule->maxValue)))
            return DYNAMIC_ENCOUNTER_PROFILE_DEFAULT;
        if (rule->requiredFlag != 0 && !FlagGet(rule->requiredFlag))
            continue;
        if (rule->forbiddenFlag != 0 && FlagGet(rule->forbiddenFlag))
            continue;
        if (rule->variable != 0)
        {
            u16 value = VarGet(rule->variable);
            if (value < rule->minValue || value > rule->maxValue)
                continue;
        }
        return rule->profile;
    }
    return DYNAMIC_ENCOUNTER_PROFILE_DEFAULT;
}

u16 GetDynamicEncounterProfileForMap(u16 mapGroup, u16 mapNum)
{
    // Exclude the sentinel. No map IDs are copied from the donor project.
    u32 lo = 0, hi = ARRAY_COUNT(sDynamicMaps) - 1;
    if (mapGroup >= 0xFF || mapNum >= 0xFF)
        return DYNAMIC_ENCOUNTER_PROFILE_DEFAULT;
    u32 key = (mapGroup << 8) | mapNum;
    while (lo < hi)
    {
        u32 mid = lo + (hi - lo) / 2;
        const struct DynamicEncounterMap *map = &sDynamicMaps[mid];
        u32 candidate = (map->mapGroup << 8) | map->mapNum;
        if (candidate == key)
            return ResolveDynamicEncounterRules(map->rules, map->count, ARRAY_COUNT(sProfiles));
        if (candidate < key)
            lo = mid + 1;
        else
            hi = mid;
    }
    return DYNAMIC_ENCOUNTER_PROFILE_DEFAULT;
}

u16 GetCurrentDynamicEncounterProfile(void)
{
    return GetDynamicEncounterProfileForMap(gSaveBlock1Ptr->location.mapGroup, gSaveBlock1Ptr->location.mapNum);
}

const struct WildEncounterTypes *GetEffectiveWildEncounterTypes(u32 headerId, u32 timeOfDay)
{
    if (headerId >= gWildMonHeaderCount || timeOfDay >= TIMES_OF_DAY_COUNT)
        return &sEmptyTypes;
    const struct WildPokemonHeader *header = &gWildMonHeaders[headerId];
    u16 profile = GetDynamicEncounterProfileForMap(header->mapGroup, header->mapNum);
    if (profile != DYNAMIC_ENCOUNTER_PROFILE_DEFAULT && sProfiles[profile] != NULL)
        return GetProgressionWildTypes(headerId, timeOfDay, &sProfiles[profile][timeOfDay]);
    return GetProgressionWildTypes(headerId, timeOfDay, &header->encounterTypes[timeOfDay]);
}
