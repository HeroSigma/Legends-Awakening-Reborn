// Wild-only progression. No trainer scaling, player EXP caps or new save fields.
#include "global.h"
#include "wild_progression.h"
#include "pokemon.h"
#include "event_data.h"
#include "data.h"
#include "constants/flags.h"
#include "constants/opponents.h"

struct WildLevelParent { enum Species species; u8 level; };
#include "data/wild_level_parents.h"

u32 GetWildBadgeStage(void)
{
    u32 stage = 0;
    while (stage < NUM_BADGES && FlagGet(FLAG_BADGE01_GET + stage))
        stage++;
    return stage;
}

u32 GetWildProgressionCap(void)
{
    static const u16 leaders[] = { TRAINER_ROXANNE_1, TRAINER_BRAWLY_1,
        TRAINER_WATTSON_1, TRAINER_FLANNERY_1, TRAINER_NORMAN_1,
        TRAINER_WINONA_1, TRAINER_TATE_AND_LIZA_1, TRAINER_JUAN_1, TRAINER_SIDNEY };
    if (FlagGet(FLAG_SYS_GAME_CLEAR))
        return MAX_LEVEL;
    const struct Trainer *trainer = &gTrainers[DIFFICULTY_NORMAL][leaders[GetWildBadgeStage()]];
    u32 cap = MAX_LEVEL;
    for (u32 i = 0; i < trainer->partySize; i++)
        cap = min(cap, trainer->party[i].lvl);
    return max(2, cap);
}

static const struct Evolution *UnconditionalLevelEvolution(enum Species species)
{
    const struct Evolution *evo = GetSpeciesEvolutions(species);
    if (evo == NULL)
        return NULL;
    for (u32 i = 0; evo[i].method != EVOLUTIONS_END; i++)
        if (evo[i].method == EVO_LEVEL && evo[i].params == NULL)
            return &evo[i];
    return NULL;
}

enum Species ResolveWildLevelSpecies(enum Species species, u32 level)
{
    if (species >= NUM_SPECIES)
        return SPECIES_NONE;
    for (u32 i = 0; i < 10; i++)
    {
        const struct WildLevelParent *parent = &sWildLevelParents[species];
        if (parent->species == SPECIES_NONE || level >= parent->level)
            break;
        species = parent->species;
    }
    for (u32 i = 0; i < 10; i++)
    {
        const struct Evolution *evo = UnconditionalLevelEvolution(species);
        if (evo == NULL || level < evo->param)
            break;
        const struct SpeciesInfo *target = &gSpeciesInfo[evo->targetSpecies];
        if (target->isRestrictedLegendary || target->isSubLegendary || target->isMythical
         || target->isUltraBeast || target->isParadox)
            break;
        species = evo->targetSpecies;
    }
    return species;
}

u32 ClampWildBonusLevel(enum Species species, u32 level)
{
    level = min(level, GetWildProgressionCap());
    const struct Evolution *evo = UnconditionalLevelEvolution(species);
    // Keep the DexNav search identity valid: bonuses cannot silently change its species.
    if (evo != NULL && evo->param > 1)
        level = min(level, evo->param - 1);
    return max(1, level);
}

struct WildViewCache
{
    const struct WildEncounterTypes *source;
    u32 cap, stage, header, time;
    struct WildEncounterTypes types;
    struct WildPokemonInfo info[5];
    struct WildPokemon slots[5][NUM_LAND_MONS_ENCOUNTER_SLOTS];
};
// Consumers retain views only during a synchronous lookup. Four entries retain all
// current-map TOD views, including land/water pointers queried in the same function.
static EWRAM_DATA struct WildViewCache sViews[4] = {0};
static EWRAM_DATA u32 sNextView = 0;

const struct WildEncounterTypes *GetProgressionWildTypes(u32 headerId, u32 time, const struct WildEncounterTypes *source)
{
    u32 stage = GetWildBadgeStage(), cap = GetWildProgressionCap();
    for (u32 i = 0; i < ARRAY_COUNT(sViews); i++)
        if (sViews[i].source == source && sViews[i].cap == cap && sViews[i].stage == stage
         && sViews[i].header == headerId && sViews[i].time == time)
            return &sViews[i].types;
    struct WildViewCache *view = &sViews[sNextView++ % ARRAY_COUNT(sViews)];
    *view = (struct WildViewCache){ .source=source, .cap=cap, .stage=stage, .header=headerId, .time=time };
    const struct WildPokemonInfo *inputs[] = {source->landMonsInfo, source->waterMonsInfo,
        source->rockSmashMonsInfo, source->fishingMonsInfo, source->hiddenMonsInfo};
    const u8 sizes[] = {NUM_LAND_MONS_ENCOUNTER_SLOTS, NUM_WATER_MONS_ENCOUNTER_SLOTS,
        NUM_ROCK_SMASH_MONS_ENCOUNTER_SLOTS, NUM_FISHING_MONS_ENCOUNTER_SLOTS, NUM_HIDDEN_MONS_ENCOUNTER_SLOTS};
    const struct WildPokemonInfo **outputs[] = {&view->types.landMonsInfo, &view->types.waterMonsInfo,
        &view->types.rockSmashMonsInfo, &view->types.fishingMonsInfo, &view->types.hiddenMonsInfo};
    for (u32 area = 0; area < ARRAY_COUNT(inputs); area++)
    {
        if (inputs[area] == NULL)
            continue;
        view->info[area] = *inputs[area];
        view->info[area].wildPokemon = view->slots[area];
        *outputs[area] = &view->info[area];
        for (u32 slot = 0; slot < sizes[area]; slot++)
        {
            const struct WildPokemon *original = &inputs[area]->wildPokemon[slot];
            struct WildPokemon *mon = &view->slots[area][slot];
            u32 lo = min(original->minLevel, original->maxLevel) + stage * 3;
            u32 hi = max(original->minLevel, original->maxLevel) + stage * 3;
            // Retain a two-level range when a late-route baseline reaches the cap.
            mon->minLevel = min(lo, max(1, cap - 2));
            mon->species = ResolveWildLevelSpecies(original->species, mon->minLevel);
            mon->maxLevel = max(mon->minLevel, ClampWildBonusLevel(mon->species, hi));
        }
    }
    return &view->types;
}
