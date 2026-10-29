#include "global.h"
#include "data.h"
#include "event_data.h"
#include "legends_trainers.h"
#include "pokemon.h"
#include "caps.h"
#include "move.h"
#include "battle_setup.h"
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

enum { THEME_BALANCE, THEME_RAIN, THEME_SUN, THEME_SAND, THEME_SNOW, THEME_TRICK };
struct LegendsTeamProfile {
    u16 species[PARTY_SIZE];
    u8 level, theme, shinyAce, formatChoice;
};
#include "data/legends_trainer_profiles.h"
static EWRAM_DATA u16 sCachedIds[4] = {0};
static EWRAM_DATA u8 sCachedCaps[4] = {0};
static EWRAM_DATA u8 sCachedPlayerLevels[4] = {0};
static EWRAM_DATA u8 sCachedFormats[4] = {0};
static EWRAM_DATA const struct Trainer *sCachedBases[4] = {0};
static EWRAM_DATA u8 sNextCache = 0;
static EWRAM_DATA u16 sFormatTrainer = 0;
static EWRAM_DATA bool8 sDoubleFormat = FALSE;

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
        if (mon->moves[i] == MOVE_NONE) {
            if (i == 0) return FALSE;
            continue;
        }
        if (!LegendsTrainer_MoveLegal(mon->species,mon->lvl,mon->moves[i])) return FALSE;
        for (u32 j=0;j<i;j++) if (mon->moves[j]==mon->moves[i]) return FALSE;
    }
    return TRUE;
}

// Role palettes are ordered, deterministic move preferences. Every candidate is
// checked against this build's learnsets at the actual battle level.
static const u8 sEV_slowPhysical[] = {252,252,4,0,0,0};
static const u8 sEV_slowSpecial[] = {252,0,4,252,0,0};
static EWRAM_DATA bool8 sBuildingDoubles = FALSE;
static const u16 sPhysicalMoves[] = {
 MOVE_CLOSE_COMBAT, MOVE_DRAIN_PUNCH, MOVE_BODY_PRESS,
 MOVE_EARTHQUAKE, MOVE_HIGH_HORSEPOWER, MOVE_ROCK_SLIDE, MOVE_STONE_EDGE,
 MOVE_BRAVE_BIRD, MOVE_ACROBATICS, MOVE_DUAL_WINGBEAT, MOVE_IRON_HEAD,
 MOVE_BULLET_PUNCH, MOVE_BULLET_SEED, MOVE_POWER_WHIP, MOVE_LEAF_BLADE,
 MOVE_LIQUIDATION, MOVE_WATERFALL, MOVE_AQUA_JET, MOVE_ICICLE_CRASH,
 MOVE_ICE_PUNCH, MOVE_PLAY_ROUGH, MOVE_POISON_JAB, MOVE_GUNK_SHOT,
 MOVE_KNOCK_OFF, MOVE_CRUNCH, MOVE_SUCKER_PUNCH, MOVE_SHADOW_CLAW,
 MOVE_SHADOW_SNEAK, MOVE_FLARE_BLITZ, MOVE_FIRE_PUNCH, MOVE_WILD_CHARGE,
 MOVE_THUNDER_PUNCH, MOVE_DRAGON_CLAW, MOVE_OUTRAGE, MOVE_X_SCISSOR,
 MOVE_U_TURN, MOVE_FACADE, MOVE_RETURN, MOVE_BODY_SLAM, MOVE_DOUBLE_EDGE,
 MOVE_ROCK_TOMB, MOVE_BULLDOZE, MOVE_BITE, MOVE_AERIAL_ACE, MOVE_QUICK_ATTACK,
};
static const u16 sSpecialMoves[] = {
 MOVE_HYDRO_PUMP, MOVE_SCALD, MOVE_SURF, MOVE_MUDDY_WATER, MOVE_WATER_PULSE,
 MOVE_THUNDERBOLT, MOVE_VOLT_SWITCH, MOVE_THUNDER, MOVE_GIGA_DRAIN,
 MOVE_ENERGY_BALL, MOVE_LEAF_STORM, MOVE_FLAMETHROWER, MOVE_HEAT_WAVE,
 MOVE_FIRE_BLAST, MOVE_ICE_BEAM, MOVE_BLIZZARD, MOVE_MOONBLAST,
 MOVE_DAZZLING_GLEAM, MOVE_FLASH_CANNON, MOVE_SHADOW_BALL, MOVE_HEX,
 MOVE_SLUDGE_BOMB, MOVE_SLUDGE_WAVE, MOVE_PSYCHIC, MOVE_PSYSHOCK,
 MOVE_DARK_PULSE, MOVE_AURA_SPHERE, MOVE_FOCUS_BLAST, MOVE_DRAGON_PULSE,
 MOVE_DRACO_METEOR, MOVE_EARTH_POWER, MOVE_BUG_BUZZ, MOVE_AIR_SLASH,
 MOVE_BOOMBURST, MOVE_HYPER_VOICE, MOVE_ANCIENT_POWER, MOVE_CONFUSION,
 MOVE_GUST, MOVE_FAIRY_WIND, MOVE_MIRROR_COAT, MOVE_COUNTER,
};
static const u16 sRecoveryMoves[] = {MOVE_RECOVER, MOVE_ROOST, MOVE_SOFT_BOILED, MOVE_SLACK_OFF, MOVE_MOONLIGHT, MOVE_MORNING_SUN, MOVE_SYNTHESIS, MOVE_WISH, MOVE_PAIN_SPLIT, MOVE_REST};
static const u16 sUtilityMoves[] = {MOVE_TOXIC, MOVE_LEECH_SEED, MOVE_WILL_O_WISP, MOVE_THUNDER_WAVE, MOVE_SPORE, MOVE_SLEEP_POWDER, MOVE_ENCORE, MOVE_TAUNT, MOVE_STEALTH_ROCK, MOVE_SPIKES, MOVE_LIGHT_SCREEN, MOVE_REFLECT};
static const u16 sDoubleMoves[] = {MOVE_FAKE_OUT, MOVE_TAILWIND, MOVE_HELPING_HAND, MOVE_FOLLOW_ME, MOVE_RAGE_POWDER, MOVE_WIDE_GUARD, MOVE_ICY_WIND, MOVE_ELECTROWEB, MOVE_SNARL};
static const u16 sZCrystals[] = {
 [TYPE_NORMAL]=ITEM_NORMALIUM_Z, [TYPE_FIGHTING]=ITEM_FIGHTINIUM_Z,
 [TYPE_FLYING]=ITEM_FLYINIUM_Z, [TYPE_POISON]=ITEM_POISONIUM_Z,
 [TYPE_GROUND]=ITEM_GROUNDIUM_Z, [TYPE_ROCK]=ITEM_ROCKIUM_Z,
 [TYPE_BUG]=ITEM_BUGINIUM_Z, [TYPE_GHOST]=ITEM_GHOSTIUM_Z,
 [TYPE_STEEL]=ITEM_STEELIUM_Z, [TYPE_FIRE]=ITEM_FIRIUM_Z,
 [TYPE_WATER]=ITEM_WATERIUM_Z, [TYPE_GRASS]=ITEM_GRASSIUM_Z,
 [TYPE_ELECTRIC]=ITEM_ELECTRIUM_Z, [TYPE_PSYCHIC]=ITEM_PSYCHIUM_Z,
 [TYPE_ICE]=ITEM_ICIUM_Z, [TYPE_DRAGON]=ITEM_DRAGONIUM_Z,
 [TYPE_DARK]=ITEM_DARKINIUM_Z, [TYPE_FAIRY]=ITEM_FAIRIUM_Z,
};

static enum Species CappedSpecies(enum Species species, u32 level)
{
    // Evaluate all ancestors: a final stage may have a lower special-method gate
    // than the level its middle stage actually becomes available.
    for (u32 attempts=0;attempts<10;attempts++) {
        enum Species ancestor=species;
        bool32 legal=TRUE;
        for (u32 depth=0;depth<10 && sWildLevelParents[ancestor].species;depth++) {
            if (level<sWildLevelParents[ancestor].level) legal=FALSE;
            ancestor=sWildLevelParents[ancestor].species;
        }
        if (legal || !sWildLevelParents[species].species) return species;
        species=sWildLevelParents[species].species;
    }
    return species;
}

static bool32 AddMove(struct TrainerMon *mon, u32 move)
{
    if (!LegendsTrainer_MoveLegal(mon->species,mon->lvl,move)) return FALSE;
    for (u32 i=0;i<MAX_MON_MOVES;i++) if (mon->moves[i]==move) return FALSE;
    for (u32 i=0;i<MAX_MON_MOVES;i++) if (!mon->moves[i]) {mon->moves[i]=move;return TRUE;}
    return FALSE;
}

static bool32 PickMove(struct TrainerMon *mon,const u16 *moves,u32 count,s32 stab,s32 category)
{
    for (u32 i=0;i<count;i++) {
        u32 move=moves[i];
        if (sBuildingDoubles && (move==MOVE_EARTHQUAKE || move==MOVE_SURF || move==MOVE_SLUDGE_WAVE || move==MOVE_BOOMBURST)) continue;
        if (category>=0 && gMovesInfo[move].category!=category) continue;
        if (stab>=0) {
            bool32 matches=gSpeciesInfo[mon->species].types[0]==gMovesInfo[move].type || gSpeciesInfo[mon->species].types[1]==gMovesInfo[move].type;
            if (matches!=stab) continue;
        }
        if (AddMove(mon,move)) return TRUE;
    }
    return FALSE;
}
#define PICK(mon, moves, stab, category) PickMove(mon,moves,ARRAY_COUNT(moves),stab,category)

static void BuildMember(struct TrainerMon *mon,enum Species desired,u32 level,u32 theme,u32 slot,bool32 doubles,bool32 shiny)
{
    *mon=(struct TrainerMon){0};
    sBuildingDoubles=doubles;
    mon->species=CappedSpecies(desired,level);
    mon->lvl=level;
    mon->iv=0x3fffffff;
    mon->gender=TRAINER_MON_RANDOM_GENDER;
    mon->ball=BALL_POKE;
    mon->friendship=255;
    mon->isShiny=shiny;
    mon->teraType=TYPE_MYSTERY;
    const struct SpeciesInfo *info=&gSpeciesInfo[mon->species];
    bool32 special=info->baseSpAttack>info->baseAttack;
    bool32 wall=(slot==2 || slot==3) && info->baseHP+info->baseDefense+info->baseSpDefense>=165;
    mon->ability=info->abilities[0];
    static const u16 preferred[]={ABILITY_INTIMIDATE,ABILITY_REGENERATOR,ABILITY_MAGIC_GUARD,ABILITY_UNAWARE,ABILITY_COMPOUND_EYES,ABILITY_WATER_BUBBLE,ABILITY_TECHNICIAN,ABILITY_PRANKSTER,ABILITY_STURDY,ABILITY_PURE_POWER,ABILITY_HUGE_POWER,ABILITY_GUTS,ABILITY_ADAPTABILITY,ABILITY_IMPOSTER};
    for (u32 j=ARRAY_COUNT(preferred);j>0;j--)
        for (u32 a=0;a<NUM_ABILITY_SLOTS;a++)
            if (info->abilities[a]==preferred[j-1]) mon->ability=preferred[j-1];
    u32 weatherAbility=theme==THEME_RAIN?ABILITY_DRIZZLE:theme==THEME_SUN?ABILITY_DROUGHT:theme==THEME_SAND?ABILITY_SAND_STREAM:theme==THEME_SNOW?ABILITY_SNOW_WARNING:ABILITY_NONE;
    for (u32 a=0;a<NUM_ABILITY_SLOTS;a++) {
        u32 ability=info->abilities[a];
        if (ability && (ability==weatherAbility || (theme==THEME_RAIN && ability==ABILITY_SWIFT_SWIM) || (theme==THEME_SUN && ability==ABILITY_CHLOROPHYLL) || (theme==THEME_SAND && ability==ABILITY_SAND_RUSH))) mon->ability=ability;
    }
    mon->nature=wall?(special?NATURE_BOLD:NATURE_IMPISH):(special?NATURE_MODEST:NATURE_ADAMANT);
    mon->ev=wall?sEV_wall:special?sEV_special:sEV_physical;
    mon->heldItem=wall?ITEM_LEFTOVERS:ITEM_LIFE_ORB;
    if (theme==THEME_TRICK && info->baseSpeed<=70 && !wall) {
        mon->nature=special?NATURE_QUIET:NATURE_BRAVE;
        mon->ev=special?sEV_slowSpecial:sEV_slowPhysical;
    }
    if (desired!=mon->species || info->evolutions) mon->heldItem=ITEM_EVIOLITE;
    // Guts is useful only when its activation and a compatible attack are supplied.
    if (mon->ability==ABILITY_GUTS) {mon->heldItem=ITEM_FLAME_ORB;AddMove(mon,MOVE_FACADE);}
    if (mon->species==SPECIES_PIKACHU) mon->heldItem=ITEM_LIGHT_BALL;
    if (mon->species==SPECIES_DITTO) {mon->heldItem=ITEM_CHOICE_SCARF;AddMove(mon,MOVE_TRANSFORM);return;}
    if (slot==0) {
        if (theme==THEME_RAIN && mon->ability!=ABILITY_DRIZZLE) AddMove(mon,MOVE_RAIN_DANCE);
        if (theme==THEME_SUN && mon->ability!=ABILITY_DROUGHT) AddMove(mon,MOVE_SUNNY_DAY);
        if (theme==THEME_SAND && mon->ability!=ABILITY_SAND_STREAM) AddMove(mon,MOVE_SANDSTORM);
        if (theme==THEME_SNOW && mon->ability!=ABILITY_SNOW_WARNING) AddMove(mon,MOVE_SNOWSCAPE);
        if (theme==THEME_TRICK) AddMove(mon,MOVE_TRICK_ROOM);
    }
    // A STAB attack comes before utility so the ace can always use its gimmick.
    if (special) PICK(mon,sSpecialMoves,TRUE,DAMAGE_CATEGORY_SPECIAL);
    else PICK(mon,sPhysicalMoves,TRUE,DAMAGE_CATEGORY_PHYSICAL);
    if (doubles) {
        if (slot<2 || wall) PICK(mon,sDoubleMoves,-1,-1);
        AddMove(mon,MOVE_PROTECT);
    } else if (wall) {
        PICK(mon,sRecoveryMoves,-1,-1);
        if (mon->moves[1]==MOVE_REST || mon->moves[2]==MOVE_REST) AddMove(mon,MOVE_SLEEP_TALK);
        else PICK(mon,sUtilityMoves,-1,-1);
    } else if (slot==4 || slot==5) {
        // Do not put a physical setup move on a special attacker, or vice versa.
        if (special) { if (!AddMove(mon,MOVE_NASTY_PLOT)) AddMove(mon,MOVE_CALM_MIND); }
        else { if (!AddMove(mon,MOVE_SWORDS_DANCE)) AddMove(mon,MOVE_BULK_UP); }
    }
    if (special) PICK(mon,sSpecialMoves,FALSE,DAMAGE_CATEGORY_SPECIAL);
    else PICK(mon,sPhysicalMoves,FALSE,DAMAGE_CATEGORY_PHYSICAL);
    AddMove(mon,MOVE_PROTECT);
    if (special) PICK(mon,sSpecialMoves,-1,DAMAGE_CATEGORY_SPECIAL);
    else PICK(mon,sPhysicalMoves,-1,DAMAGE_CATEGORY_PHYSICAL);
    const struct LevelUpMove *learnset=GetSpeciesLevelUpLearnset(mon->species);
    for (u32 i=0;learnset[i].move!=LEVEL_UP_MOVE_END;i++)
        if (learnset[i].level<=level) AddMove(mon,learnset[i].move);
    PICK(mon,sUtilityMoves,-1,-1);
}

bool32 LegendsTrainer_HasProfile(u32 id)
{
    return id<TRAINERS_COUNT && sFullProfiles[id].species[0]!=SPECIES_NONE;
}

bool32 LegendsTrainer_IsFormatChoice(u32 id)
{
    return LegendsTrainer_HasProfile(id) && sFullProfiles[id].formatChoice && FlagGet(FLAG_LA_RED_DEX_GIFTS);
}

void LegendsTrainer_PrepareFormat(void)
{
    sFormatTrainer=TRAINER_BATTLE_PARAM.opponentA;
    sDoubleFormat=FALSE;
    gSpecialVar_Result=LegendsTrainer_IsFormatChoice(sFormatTrainer);
}

void LegendsTrainer_SelectFormat(void)
{
    bool32 requested=gSpecialVar_Result==TRUE;
    sDoubleFormat=requested && GetMonsStateToDoubles()==PLAYER_HAS_TWO_USABLE_MONS;
    gSpecialVar_Result=requested && !sDoubleFormat?2:0;
}

static void ApplyGimmick(u32 id,struct TrainerMon *team)
{
    for (s32 slot=PARTY_SIZE-1;slot>=0;slot--) {
        for (u32 i=0;i<MAX_MON_MOVES;i++) {
            u32 move=team[slot].moves[i];
            if (!move || gMovesInfo[move].category==DAMAGE_CATEGORY_STATUS) continue;
            u32 type=gMovesInfo[move].type;
            if (type>=ARRAY_COUNT(sZCrystals) || !sZCrystals[type]) continue;
            if (LegendsTrainer_Gimmick(id)==1) team[slot].teraType=type;
            else team[slot].heldItem=sZCrystals[type];
            return;
        }
    }
}

// Party-relative scaling adapted from Graion Dilach's dynamic-level approach.
// The badge cap is always authoritative; eggs and empty slots cannot inflate it.
u32 __attribute__((noinline)) LegendsTrainer_PlayerLevel(void)
{
    u32 highest = 1;
    for (u32 i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
    {
        struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][i];
        if (GetMonData(mon, MON_DATA_SPECIES) != SPECIES_NONE && !GetMonData(mon, MON_DATA_IS_EGG))
            highest = max(highest, GetMonData(mon, MON_DATA_LEVEL));
    }
    return min(highest, GetCurrentLevelCap());
}

u32 __attribute__((noinline)) LegendsTrainer_ScaledLevel(u32 authoredLevel)
{
    return min(GetCurrentLevelCap(), max(authoredLevel, LegendsTrainer_PlayerLevel()));
}

const struct Trainer *LegendsTrainer_Get(u16 trainerId,const struct Trainer *base)
{
    if (!FlagGet(FLAG_LA_RED_DEX_GIFTS) || !LegendsTrainer_HasProfile(trainerId)) return base;
    u32 cap=GetCurrentLevelCap();
    u32 playerLevel=LegendsTrainer_PlayerLevel();
    bool32 doubles=LegendsTrainer_IsFormatChoice(trainerId)?(sFormatTrainer==trainerId && sDoubleFormat):base->battleType==TRAINER_BATTLE_TYPE_DOUBLES;
    for (u32 i=0;i<4;i++)
        if (sCachedIds[i]==trainerId && sCachedCaps[i]==cap && sCachedPlayerLevels[i]==playerLevel && sCachedFormats[i]==doubles && sCachedBases[i]==base) return &sTrainers[i];
    u32 index=sNextCache++%4;
    struct Trainer *trainer=&sTrainers[index];
    *trainer=*base;
    struct TrainerMon *team=sMembers[index];
    s32 canary=Profile(trainerId);
    if (canary>=0) {
        for (u32 i=0;i<PARTY_SIZE;i++) team[i]=sProfiles[canary].team[i];
        if (LegendsTrainer_Gimmick(trainerId)==1) team[5].teraType=sProfiles[canary].tera;
        else team[5].heldItem=sProfiles[canary].crystal;
    } else {
        const struct LegendsTeamProfile *profile=&sFullProfiles[trainerId];
        u32 level=LegendsTrainer_ScaledLevel(profile->level);
        for (u32 i=0;i<PARTY_SIZE;i++) BuildMember(&team[i],profile->species[i],level>(i%3)?level-(i==5?0:i%3):1,profile->theme,i,doubles,profile->shinyAce && i==5);
        ApplyGimmick(trainerId,team);
    }
    for (u32 i=0;i<PARTY_SIZE;i++)
        if (!LegendsTrainer_MemberLegal(&team[i])) return base;
    trainer->party=team;
    trainer->partySize=PARTY_SIZE;
    trainer->poolSize=0;
    trainer->poolRuleIndex=0;
    trainer->poolPickIndex=0;
    trainer->poolPruneIndex=0;
    trainer->overrideTrainer=0;
    trainer->aiFlags=AI_FLAG_SMART_TRAINER;
    trainer->battleType=doubles?TRAINER_BATTLE_TYPE_DOUBLES:TRAINER_BATTLE_TYPE_SINGLES;
    for (u32 i=0;i<MAX_TRAINER_ITEMS;i++) trainer->items[i]=ITEM_NONE;
    u32 item=cap<=26?ITEM_SUPER_POTION:cap<=49?ITEM_HYPER_POTION:ITEM_FULL_RESTORE;
    trainer->items[0]=item;trainer->items[1]=item;
    sCachedIds[index]=trainerId;sCachedCaps[index]=cap; sCachedPlayerLevels[index]=playerLevel;sCachedFormats[index]=doubles;sCachedBases[index]=base;
    return trainer;
}
