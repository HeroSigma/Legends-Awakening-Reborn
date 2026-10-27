#include "global.h"
#include "legends_tera.h"
#include "battle.h"
#include "event_data.h"
#include "item.h"
#include "random.h"
#include "script.h"
#include "string_util.h"
#include "constants/flags.h"
#include "constants/items.h"
#include "constants/form_change_types.h"

// Native Devon milestones also support existing saves, without new save fields.
bool32 LegendsTeraUnlocked(void)
{
    return FlagGet(FLAG_RETURNED_DEVON_GOODS) && FlagGet(FLAG_RECEIVED_POKENAV);
}

static const u16 sShards[NUMBER_OF_MON_TYPES] = {
    [TYPE_NORMAL] = ITEM_NORMAL_TERA_SHARD,
    [TYPE_FIRE] = ITEM_FIRE_TERA_SHARD,
    [TYPE_WATER] = ITEM_WATER_TERA_SHARD,
    [TYPE_GRASS] = ITEM_GRASS_TERA_SHARD,
    [TYPE_ELECTRIC] = ITEM_ELECTRIC_TERA_SHARD,
    [TYPE_ICE] = ITEM_ICE_TERA_SHARD,
    [TYPE_FIGHTING] = ITEM_FIGHTING_TERA_SHARD,
    [TYPE_POISON] = ITEM_POISON_TERA_SHARD,
    [TYPE_GROUND] = ITEM_GROUND_TERA_SHARD,
    [TYPE_FLYING] = ITEM_FLYING_TERA_SHARD,
    [TYPE_PSYCHIC] = ITEM_PSYCHIC_TERA_SHARD,
    [TYPE_BUG] = ITEM_BUG_TERA_SHARD,
    [TYPE_ROCK] = ITEM_ROCK_TERA_SHARD,
    [TYPE_GHOST] = ITEM_GHOST_TERA_SHARD,
    [TYPE_DRAGON] = ITEM_DRAGON_TERA_SHARD,
    [TYPE_DARK] = ITEM_DARK_TERA_SHARD,
    [TYPE_STEEL] = ITEM_STEEL_TERA_SHARD,
    [TYPE_FAIRY] = ITEM_FAIRY_TERA_SHARD,
    [TYPE_STELLAR] = ITEM_STELLAR_TERA_SHARD,
};
static const u16 sCrystals[NUMBER_OF_MON_TYPES] = {
    [TYPE_NORMAL] = ITEM_NORMALIUM_Z,
    [TYPE_FIRE] = ITEM_FIRIUM_Z,
    [TYPE_WATER] = ITEM_WATERIUM_Z,
    [TYPE_GRASS] = ITEM_GRASSIUM_Z,
    [TYPE_ELECTRIC] = ITEM_ELECTRIUM_Z,
    [TYPE_ICE] = ITEM_ICIUM_Z,
    [TYPE_FIGHTING] = ITEM_FIGHTINIUM_Z,
    [TYPE_POISON] = ITEM_POISONIUM_Z,
    [TYPE_GROUND] = ITEM_GROUNDIUM_Z,
    [TYPE_FLYING] = ITEM_FLYINIUM_Z,
    [TYPE_PSYCHIC] = ITEM_PSYCHIUM_Z,
    [TYPE_BUG] = ITEM_BUGINIUM_Z,
    [TYPE_ROCK] = ITEM_ROCKIUM_Z,
    [TYPE_GHOST] = ITEM_GHOSTIUM_Z,
    [TYPE_DRAGON] = ITEM_DRAGONIUM_Z,
    [TYPE_DARK] = ITEM_DARKINIUM_Z,
    [TYPE_STEEL] = ITEM_STEELIUM_Z,
    [TYPE_FAIRY] = ITEM_FAIRIUM_Z,
};
static const u8 sTeraChoices[] = {TYPE_NORMAL, TYPE_FIRE, TYPE_WATER, TYPE_GRASS, TYPE_ELECTRIC, TYPE_ICE, TYPE_FIGHTING, TYPE_POISON, TYPE_GROUND, TYPE_FLYING, TYPE_PSYCHIC, TYPE_BUG, TYPE_ROCK, TYPE_GHOST, TYPE_DRAGON, TYPE_DARK, TYPE_STEEL, TYPE_FAIRY, TYPE_STELLAR};

u16 LegendsShardForType(u32 type)
{
    return type < NUMBER_OF_MON_TYPES ? sShards[type] : ITEM_NONE;
}

// Walk forward along the evolution family: a Charmander can carry either stone.
static u32 CollectMegaStones(u16 species, u16 *items, u32 count, u32 depth)
{
    const struct FormChange *forms = GetSpeciesFormChanges(species);
    const struct Evolution *evos = GetSpeciesEvolutions(species);
    u32 i, j;
    if (forms != NULL)
        for (i = 0; forms[i].method != FORM_CHANGE_TERMINATOR; i++)
            if (forms[i].method == FORM_CHANGE_BATTLE_MEGA_EVOLUTION_ITEM)
            {
                for (j = 0; j < count && items[j] != forms[i].param1; j++);
                if (j == count && count < 8)
                    items[count++] = forms[i].param1;
            }
    if (depth < 3 && evos != NULL)
        for (i = 0; evos[i].method != EVOLUTIONS_END; i++)
            if (evos[i].targetSpecies != species)
                count = CollectMegaStones(evos[i].targetSpecies, items, count, depth + 1);
    return count;
}

u16 LegendsChooseWildHeldItem(u16 species)
{
    u16 mega[8];
    u32 count, choice;
    const struct SpeciesInfo *info;
    if (species == SPECIES_NONE || species >= NUM_SPECIES)
        return ITEM_NONE;
    info = &gSpeciesInfo[species];
    count = CollectMegaStones(species, mega, 0, 0);
    choice = Random() % 4;
    if (count && choice < 2)
        return mega[Random() % count];
    if (choice == 2 && sCrystals[info->types[0]] != ITEM_NONE)
        return sCrystals[info->types[0]];
    // Preserve native species items as candidates, rather than guaranteed extras.
    if (choice == 3 && info->itemRare != ITEM_NONE)
        return info->itemRare;
    if (choice == 3 && info->itemCommon != ITEM_NONE)
        return info->itemCommon;
    switch (Random() % 6)
    {
    case 0: return ITEM_LEFTOVERS;
    case 1: return ITEM_FOCUS_SASH;
    case 2: return ITEM_LIFE_ORB;
    case 3: return ITEM_CHOICE_SCARF;
    case 4: return info->baseAttack >= info->baseSpAttack ? ITEM_CHOICE_BAND : ITEM_CHOICE_SPECS;
    default: return GetSpeciesEvolutions(species) != NULL ? ITEM_EVIOLITE : ITEM_ASSAULT_VEST;
    }
}

static EWRAM_DATA u8 sCaughtShardSlot = 0;

static bool32 IsShardRewardBattle(void)
{
    return LegendsTeraUnlocked()
        && !(gBattleTypeFlags & (BATTLE_TYPE_TRAINER | BATTLE_TYPE_LINK | BATTLE_TYPE_RECORDED
             | BATTLE_TYPE_FRONTIER | BATTLE_TYPE_FIRST_BATTLE | BATTLE_TYPE_CATCH_TUTORIAL
             | BATTLE_TYPE_GHOST | BATTLE_TYPE_POKEDUDE));
}

static void AwardSpeciesShard(u16 species)
{
    u16 item;
    if (!IsShardRewardBattle() || species == SPECIES_NONE || species >= NUM_SPECIES)
        return;
    item = LegendsShardForType(gSpeciesInfo[species].types[0]);
    if (item != ITEM_NONE)
    {
        AddBagItem(item, 1);
        if (Random() % 100 == 0)
            AddBagItem(ITEM_STELLAR_TERA_SHARD, 1);
    }
}

void LegendsAwardCaughtShard(u16 species, u16 partyIndex)
{
    sCaughtShardSlot = partyIndex;
    AwardSpeciesShard(species);
}

// Called once at battle end, before enemy parties are cleared.
void LegendsAwardWildShards(void)
{
    u32 i;
    if (!IsShardRewardBattle())
        return;
    for (i = 0; i < PARTY_SIZE; i++)
    {
        struct Pokemon *mon = &gParties[B_TRAINER_OPPONENT_A][i];
        if (gBattleOutcome == B_OUTCOME_CAUGHT && i == sCaughtShardSlot)
            continue; // Capture already paid during successful ownership transfer.
        if (GetMonData(mon, MON_DATA_HP) == 0)
            AwardSpeciesShard(GetMonData(mon, MON_DATA_SPECIES));
    }
}

// Results: 0 ready/success, 1 short of shards, 2 invalid/egg, 3 same type, 4 locked.
void LegendsPrepareTeraChange(void)
{
    u32 slot = gSpecialVar_0x8004, choice = gSpecialVar_0x8005;
    u32 type;
    gSpecialVar_Result = 2;
    if (!LegendsTeraUnlocked()) { gSpecialVar_Result = 4; return; }
    if (slot >= gPartiesCount[B_TRAINER_PLAYER] || choice >= ARRAY_COUNT(sTeraChoices))
        return;
    if (GetMonData(&gParties[B_TRAINER_PLAYER][slot], MON_DATA_IS_EGG))
        return;
    type = sTeraChoices[choice];
    gSpecialVar_0x8006 = LegendsShardForType(type);
    gSpecialVar_0x8007 = type == TYPE_STELLAR ? 150 : 50;
    GetMonData(&gParties[B_TRAINER_PLAYER][slot], MON_DATA_NICKNAME, gStringVar1);
    if (GetMonData(&gParties[B_TRAINER_PLAYER][slot], MON_DATA_TERA_TYPE) == type)
        gSpecialVar_Result = 3;
    else
        gSpecialVar_Result = CheckBagHasItem(gSpecialVar_0x8006, gSpecialVar_0x8007) ? 0 : 1;
}

void LegendsCommitTeraChange(void)
{
    u32 type;
    LegendsPrepareTeraChange();
    if (gSpecialVar_Result != 0)
        return;
    type = sTeraChoices[gSpecialVar_0x8005];
    if (!RemoveBagItem(gSpecialVar_0x8006, gSpecialVar_0x8007))
    { gSpecialVar_Result = 1; return; }
    SetMonData(&gParties[B_TRAINER_PLAYER][gSpecialVar_0x8004], MON_DATA_TERA_TYPE, &type);
}
