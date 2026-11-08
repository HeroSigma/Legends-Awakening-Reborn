// Reborn adaptation of HeroSigma/Legends-Awakening la-v0.5.0's profile registry.
// Intentionally no active overrides: existing wild encounter tables stay in use.
// Each future non-default profile points to TIMES_OF_DAY_COUNT complete entries.
static const struct WildEncounterTypes *const sProfiles[DYNAMIC_ENCOUNTER_PROFILE_COUNT] =
{
    [DYNAMIC_ENCOUNTER_PROFILE_DEFAULT] = NULL,
};

// Add maps before the sentinel, sorted by (mapGroup, mapNum). Rules are ordered:
// first match wins; profile DEFAULT explicitly falls back to the native table.
static const struct DynamicEncounterMap sDynamicMaps[] =
{
    {.mapGroup = 0xFF, .mapNum = 0xFF},
};
