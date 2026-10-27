#include "global.h"
#include "pokemon.h"
#include "main.h"
#include "string_util.h"
#include "constants/species.h"
#include "constants/characters.h"
#include "reborn_pc_adapter.h"

STATIC_ASSERT(MOVES_COUNT <= 1024, CollectionMoveIdBudget);
static const u8 sCollectionOt[] = {CHAR_T, CHAR_R, CHAR_A, CHAR_I, CHAR_N, CHAR_E, CHAR_R, EOS};

static u32 Read(struct BoxPokemon *mon, enum MonData field)
{
    return GetBoxMonData(mon, field);
}

static void Write(struct BoxPokemon *mon, enum MonData field, u32 value)
{
    SetBoxMonData(mon, field, &value);
}

static bool32 Supported(const struct LaPcTraits *v)
{
    return v->species < NUM_SPECIES && v->item < ITEMS_COUNT
        && v->tera_type < NUMBER_OF_MON_TYPES && v->ability <= 2
        && v->moves[0] < MOVES_COUNT && v->moves[1] < MOVES_COUNT
        && v->moves[2] < MOVES_COUNT && v->moves[3] < MOVES_COUNT;
}

int LaPcEncodeBoxMon(struct BoxPokemon *mon, unsigned char out[LA_PC_RECORD_BYTES])
{
    struct LaPcTraits v = {0};
    u32 i, pid;
    if (mon == NULL || out == NULL || Read(mon, MON_DATA_SANITY_IS_BAD_EGG))
        return FALSE;
    v.species = Read(mon, MON_DATA_SPECIES);
    if (v.species == SPECIES_NONE)
        return LaPcEncode(&v, out);
    if (v.species >= NUM_SPECIES)
        return FALSE;
    pid = Read(mon, MON_DATA_PERSONALITY);
    v.original_nature = pid % 25;
    v.personality_mod100_quotient = (pid % 100) / 25;
    v.wurmple_branch = (pid >> 16) % 10 >= 5;
    v.female = GetGenderFromSpeciesAndPersonality(v.species, pid) == MON_FEMALE;
    v.shiny = Read(mon, MON_DATA_IS_SHINY);
    v.item = Read(mon, MON_DATA_HELD_ITEM);
    v.experience = Read(mon, MON_DATA_EXP);
    v.tera_type = Read(mon, MON_DATA_TERA_TYPE);
    v.pp_bonuses = Read(mon, MON_DATA_PP_BONUSES);
    v.evolution_tracker = Read(mon, MON_DATA_EVOLUTION_TRACKER);
    for (i = 0; i < 4; i++)
        v.moves[i] = Read(mon, MON_DATA_MOVE1 + i);
    for (i = 0; i < 6; i++)
    {
        v.evs[i] = Read(mon, MON_DATA_HP_EV + i);
        v.ivs[i] = Read(mon, MON_DATA_HP_IV + i);
        v.hyper_trained |= Read(mon, MON_DATA_HYPER_TRAINED_HP + i) << i;
    }
    v.ability = Read(mon, MON_DATA_ABILITY_NUM);
    v.mint_nature = Read(mon, MON_DATA_HIDDEN_NATURE);
    v.friendship = Read(mon, MON_DATA_FRIENDSHIP);
    v.egg = Read(mon, MON_DATA_IS_EGG);
    v.ball = Read(mon, MON_DATA_POKEBALL);
    v.foreign_ot = Read(mon, MON_DATA_OT_ID) != (u32)READ_OTID_FROM_SAVE;
    v.foreign_language = Read(mon, MON_DATA_LANGUAGE) != gGameLanguage;
    v.shadow = Read(mon, MON_DATA_IS_SHADOW);
    v.fateful = Read(mon, MON_DATA_MODERN_FATEFUL_ENCOUNTER);
    v.champion_ribbon = Read(mon, MON_DATA_CHAMPION_RIBBON);
    v.markings = Read(mon, MON_DATA_MARKINGS);
    v.pokerus = Read(mon, MON_DATA_POKERUS);
    v.beauty = Read(mon, MON_DATA_BEAUTY);
    v.dynamax_level = Read(mon, MON_DATA_DYNAMAX_LEVEL);
    v.gigantamax_factor = Read(mon, MON_DATA_GIGANTAMAX_FACTOR);
    return Supported(&v) && LaPcEncode(&v, out);
}

static bool32 MakePersonality(const struct LaPcTraits *v, u32 *result)
{
    u32 remainder = v->original_nature + 25 * v->personality_mod100_quotient;
    u32 i;
    u32 start = v->wurmple_branch ? ((5u << 16) + 99 - remainder) / 100 : 0;
    /* Every low-byte residue compatible with PID modulo 100 is visited;
     * both upper-half Wurmple branches are searched. Shiny is stored separately
     * by expansion, so generation does not consume the gameplay RNG. */
    for (i = 0; i < 64; i++)
    {
        u32 pid = 100 * (start + i) + remainder;
        bool32 female = GetGenderFromSpeciesAndPersonality(v->species, pid) == MON_FEMALE;
        if (female == v->female && ((pid >> 16) % 10 >= 5) == v->wurmple_branch)
        {
            *result = pid;
            return TRUE;
        }
    }
    return FALSE;
}

int LaPcDecodeBoxMon(const unsigned char in[LA_PC_RECORD_BYTES], struct BoxPokemon *out)
{
    struct LaPcTraits v;
    struct BoxPokemon mon;
    u32 pid, i;
    if (out == NULL || !LaPcDecode(in, &v))
        return FALSE;
    if (v.species == SPECIES_NONE)
    {
        ZeroBoxMonData(out);
        return TRUE;
    }
    if (!Supported(&v) || !MakePersonality(&v, &pid))
        return FALSE;
    CreateBoxMon(&mon, v.species, 1, pid, (struct OriginalTrainerId) {
        .method = OT_ID_PRESET,
        .value = READ_OTID_FROM_SAVE ^ (v.foreign_ot ? 0x80000000u : 0),
    });
    Write(&mon, MON_DATA_IS_SHINY, v.shiny);
    /* Keep the foreign-language distinction without Japanese five-character
     * nickname rendering on regenerated Latin species names. */
    Write(&mon, MON_DATA_LANGUAGE, v.foreign_language ? (gGameLanguage == LANGUAGE_FRENCH ? LANGUAGE_ENGLISH : LANGUAGE_FRENCH) : gGameLanguage);
    if (v.foreign_ot)
        SetBoxMonData(&mon, MON_DATA_OT_NAME, sCollectionOt);
    Write(&mon, MON_DATA_HELD_ITEM, v.item);
    Write(&mon, MON_DATA_EXP, v.experience);
    Write(&mon, MON_DATA_TERA_TYPE, v.tera_type);
    Write(&mon, MON_DATA_PP_BONUSES, v.pp_bonuses);
    Write(&mon, MON_DATA_EVOLUTION_TRACKER, v.evolution_tracker);
    for (i = 0; i < 4; i++)
    {
        Write(&mon, MON_DATA_MOVE1 + i, v.moves[i]);
        Write(&mon, MON_DATA_PP1 + i, CalculatePPWithBonus(v.moves[i], v.pp_bonuses, i));
    }
    for (i = 0; i < 6; i++)
    {
        Write(&mon, MON_DATA_HP_EV + i, v.evs[i]);
        Write(&mon, MON_DATA_HP_IV + i, v.ivs[i]);
        Write(&mon, MON_DATA_HYPER_TRAINED_HP + i, (v.hyper_trained >> i) & 1);
    }
    Write(&mon, MON_DATA_ABILITY_NUM, v.ability);
    Write(&mon, MON_DATA_HIDDEN_NATURE, v.mint_nature);
    Write(&mon, MON_DATA_FRIENDSHIP, v.friendship);
    Write(&mon, MON_DATA_IS_EGG, v.egg);
    Write(&mon, MON_DATA_POKEBALL, v.ball);
    Write(&mon, MON_DATA_IS_SHADOW, v.shadow);
    Write(&mon, MON_DATA_MODERN_FATEFUL_ENCOUNTER, v.fateful);
    Write(&mon, MON_DATA_CHAMPION_RIBBON, v.champion_ribbon);
    Write(&mon, MON_DATA_MARKINGS, v.markings);
    Write(&mon, MON_DATA_POKERUS, v.pokerus);
    Write(&mon, MON_DATA_BEAUTY, v.beauty);
    Write(&mon, MON_DATA_DYNAMAX_LEVEL, v.dynamax_level);
    Write(&mon, MON_DATA_GIGANTAMAX_FACTOR, v.gigantamax_factor);
    *out = mon;
    return TRUE;
}
