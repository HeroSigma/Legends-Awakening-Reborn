#include "global.h"
#include "data.h"
#include "event_data.h"
#include "legends_trainers.h"
#include "pokemon.h"
#include "caps.h"
#include "constants/battle_ai.h"
#include "constants/items.h"
#include "constants/abilities.h"
#include "constants/flags.h"
#include "constants/opponents.h"
#include "constants/pokeball.h"

struct WildLevelParent { enum Species species; u8 level; };
#include "data/wild_level_parents.h"

static const u8 sEV_physical[] = {4,252,0,0,0,252};
static const u8 sEV_special[] = {4,0,0,252,0,252};
static const u8 sEV_wall[] = {252,0,252,0,4,0};
static const u8 sEV_specialwall[] = {252,0,4,0,252,0};
#include "data/legends_trainer_teams.h"

static const struct {u16 id; const struct TrainerMon *team; u8 tera; u16 crystal;} sProfiles[] = {
    {TRAINER_CALVIN_1,sTeam_CALVIN_1,TYPE_DARK,ITEM_DARKINIUM_Z},
    {TRAINER_RICK,sTeam_RICK,TYPE_WATER,ITEM_WATERIUM_Z},
    {TRAINER_TIANA,sTeam_TIANA,TYPE_FAIRY,ITEM_FAIRIUM_Z},
    {TRAINER_ALLEN,sTeam_ALLEN,TYPE_NORMAL,ITEM_NORMALIUM_Z},
};
// Independent stable views keep AI, party construction and inventory consistent.
// No save fields; random choice derives from the existing player trainer ID.
static EWRAM_DATA struct Trainer sTrainers[ARRAY_COUNT(sProfiles)] = {0};
static EWRAM_DATA struct TrainerMon sMembers[ARRAY_COUNT(sProfiles)][PARTY_SIZE] = {0};

static EWRAM_DATA u8 sValidated[ARRAY_COUNT(sProfiles)] = {0};

static s32 Profile(u32 id)
{
    for (u32 i=0;i<ARRAY_COUNT(sProfiles);i++)
        if (id==sProfiles[i].id) return i;
    return -1;
}

u32 LegendsTrainer_Gimmick(u32 trainerId)
{
    // 1=Tera, 2=Z. Each authored team supports either, exclusively on its last mon.
    u32 x=READ_OTID_FROM_SAVE ^ (trainerId*0x9e3779b9u);
    x ^= x>>16; x *= 0x7feb352du; x ^= x>>15;
    return 1+(x&1);
}

bool32 LegendsTrainer_MoveLegal(u32 species,u32 level,u32 move)
{
    if (!species || species>=NUM_SPECIES || !move || move>=MOVES_COUNT)
        return FALSE;
    if (CanLearnTeachableMove(species,move) || SpeciesHasEggMove(species,move))
        return TRUE;
    const struct LevelUpMove *learnset=GetSpeciesLevelUpLearnset(species);
    for (u32 i=0; learnset[i].move!=LEVEL_UP_MOVE_END; i++)
        if (learnset[i].move==move && learnset[i].level<=level)
            return TRUE;
    return FALSE;
}

bool32 LegendsTrainer_MemberLegal(const struct TrainerMon *mon)
{
    bool32 ability=FALSE;
    if (!mon->species || mon->species>=NUM_SPECIES || !mon->lvl || mon->lvl>GetCurrentLevelCap())
        return FALSE;
    for (u32 i=0;i<NUM_ABILITY_SLOTS;i++)
        if (gSpeciesInfo[mon->species].abilities[i]==mon->ability) ability=TRUE;
    if (!ability || mon->gender<TRAINER_MON_MALE || mon->gender>TRAINER_MON_RANDOM_GENDER) return FALSE;
    enum Species ancestor=mon->species;
    for (u32 i=0;i<10 && sWildLevelParents[ancestor].species;i++) {
        if (mon->lvl<sWildLevelParents[ancestor].level) return FALSE;
        ancestor=sWildLevelParents[ancestor].species;
    }
    u32 sum=0;
    for (u32 i=0;i<6;i++) {
        if (!mon->ev || mon->ev[i]>252) return FALSE;
        sum+=mon->ev[i];
    }
    if (sum>510) return FALSE;
    for (u32 i=0;i<MAX_MON_MOVES;i++) {
        if (!LegendsTrainer_MoveLegal(mon->species,mon->lvl,mon->moves[i])) return FALSE;
        for (u32 j=0;j<i;j++) if (mon->moves[j]==mon->moves[i]) return FALSE;
    }
    return TRUE;
}

const struct Trainer *LegendsTrainer_Get(u16 trainerId,const struct Trainer *base)
{
    s32 index=Profile(trainerId);
    if (index<0 || !FlagGet(FLAG_LA_RED_DEX_GIFTS)) return base;
    if (!sValidated[index]) {
        sValidated[index]=1;
        for (u32 i=0;i<PARTY_SIZE;i++)
            if (!LegendsTrainer_MemberLegal(&sProfiles[index].team[i])) sValidated[index]=2;
    }
    if (sValidated[index]==2) return base;
    struct Trainer *trainer=&sTrainers[index];
    *trainer=*base;
    for (u32 i=0;i<PARTY_SIZE;i++) sMembers[index][i]=sProfiles[index].team[i];
    struct TrainerMon *ace=&sMembers[index][PARTY_SIZE-1];
    if (LegendsTrainer_Gimmick(trainerId)==1) ace->teraType=sProfiles[index].tera;
    else ace->heldItem=sProfiles[index].crystal;
    trainer->party=sMembers[index];
    trainer->partySize=PARTY_SIZE;
    trainer->poolSize=0;
    trainer->poolRuleIndex=0;
    trainer->poolPickIndex=0;
    trainer->poolPruneIndex=0;
    trainer->overrideTrainer=0;
    trainer->aiFlags=AI_FLAG_SMART_TRAINER;
    trainer->battleType=TRAINER_BATTLE_TYPE_SINGLES;
    for (u32 i=0;i<MAX_TRAINER_ITEMS;i++) trainer->items[i]=ITEM_NONE;
    trainer->items[0]=ITEM_SUPER_POTION;
    trainer->items[1]=ITEM_SUPER_POTION;
    return trainer;
}
