#include "global.h"
#include "legends_sos.h"
#include "legends_plates.h"
#include "legends_quests.h"
#include "battle.h"
#include "battle_setup.h"
#include "battle_util.h"
#include "battle_controllers.h"
#include "battle_scripts.h"
#include "pokemon.h"
#include "event_data.h"
#include "constants/species.h"
#include "constants/flags.h"

struct GuardianSpecies {u16 guardian, ally;};
// Plate order is the same as legends_plates.c. No normal encounter invokes SOS.
static const struct GuardianSpecies sGuardians[LEGENDS_PLATE_COUNT] = {
    {SPECIES_NINETALES, SPECIES_VULPIX},
    {SPECIES_MILOTIC, SPECIES_MARILL},
    {SPECIES_AMPHAROS, SPECIES_FLAAFFY},
    {SPECIES_BRELOOM, SPECIES_SHROOMISH},
    {SPECIES_FROSLASS, SPECIES_SNORUNT},
    {SPECIES_HARIYAMA, SPECIES_MAKUHITA},
    {SPECIES_CROBAT, SPECIES_GOLBAT},
    {SPECIES_CLAYDOL, SPECIES_BALTOY},
    {SPECIES_ALTARIA, SPECIES_SWABLU},
    {SPECIES_XATU, SPECIES_NATU},
    {SPECIES_LEAVANNY, SPECIES_SWADLOON},
    {SPECIES_AGGRON, SPECIES_LAIRON},
    {SPECIES_DUSKNOIR, SPECIES_DUSCLOPS},
    {SPECIES_FLYGON, SPECIES_VIBRAVA},
    {SPECIES_ABSOL, SPECIES_MIGHTYENA},
    {SPECIES_MAGNEZONE, SPECIES_MAGNETON},
    {SPECIES_CLEFABLE, SPECIES_CLEFAIRY},
};
static EWRAM_DATA struct {
    bool8 active;
    u8 index;
    u8 level;
    u8 calls;
    u16 lastCallTurn;
} sSOS = {0};
extern const u8 BattleScript_LegendsSOSArrival[];

bool32 LegendsSOS_IsActive(void) {return sSOS.active;}

// Script inputs: activated Plate index in 8004, guardian level in 8005.
// Refuse invalid/pending/completed quests before touching either party.
void LegendsSOS_StartGuardian(void)
{
    u32 index = gSpecialVar_0x8004, level = gSpecialVar_0x8005, ready = 0;
    gSpecialVar_Result = 0;
    if (sSOS.active || index >= LEGENDS_PLATE_COUNT || level < 1 || level > MAX_LEVEL
        || LegendsPlates_QuestState(LA_QUEST_PLATE_FIRST + index) != QUEST_ACTIVE)
        return;
    for (u32 i = 0; i < PARTY_SIZE; i++)
        if (IsValidForBattle(&gParties[B_TRAINER_PLAYER][i])) ready++;
    // Initial implementation uses native player-controlled doubles.
    if (ready < 2) {gSpecialVar_Result = 2; return;}
    memset(&sSOS, 0, sizeof(sSOS));
    sSOS.active = TRUE;
    sSOS.index = index;
    sSOS.level = level;
    ZeroEnemyPartyMons();
    CreateRandomMonWithIVs(&gParties[B_TRAINER_OPPONENT_A][0], sGuardians[index].guardian,
        level, 31);
    memset(gQueuedStatBoosts, 0, sizeof(gQueuedStatBoosts));
    gQueuedStatBoosts[B_BATTLER_1].stats = (1 << STAT_DEF) | (1 << STAT_SPDEF);
    gQueuedStatBoosts[B_BATTLER_1].statChanges[STAT_DEF] = 1;
    gQueuedStatBoosts[B_BATTLER_1].statChanges[STAT_SPDEF] = 1;
    gSpecialVar_Result = 1;
    BattleSetup_StartScriptedDoubleWildBattle();
}

// Run only after normal end-turn damage/fainting has resolved. One ally at a
// time, at most two arrivals, separated by two turns. A defeated guardian never
// calls again. Fresh party slots preserve EXP receipts and switch-in state.
bool32 LegendsSOS_TryCall(void)
{
    enum BattlerId guardian = GetBattlerAtPosition(B_POSITION_OPPONENT_LEFT);
    enum BattlerId ally = GetBattlerAtPosition(B_POSITION_OPPONENT_RIGHT);
    if (!sSOS.active || gBattleOutcome || sSOS.calls >= 2 || !gBattleTurnCounter
        || !IsBattlerAlive(guardian) || IsBattlerAlive(ally)
        || (sSOS.calls && gBattleTurnCounter - sSOS.lastCallTurn < 2))
        return FALSE;
    u32 slot = ++sSOS.calls;
    sSOS.lastCallTurn = gBattleTurnCounter;
    CreateRandomMonWithIVs(&gParties[B_TRAINER_OPPONENT_A][slot], sGuardians[sSOS.index].ally,
        sSOS.level > 5 ? sSOS.level - 5 : sSOS.level, 20);
    gBattleStruct->monToSwitchIntoId[ally] = slot;
    gAbsentBattlerFlags &= ~(1u << ally);
    gBattlerAttacker = guardian;
    gBattlerTarget = gBattlerFainted = ally;
    gHitMarker &= ~HITMARKER_FAINTED(ally);
    BattleScriptCall(BattleScript_LegendsSOSArrival);
    return TRUE;
}

void LegendsSOS_Finish(void)
{
    if (!sSOS.active) return;
    if (gBattleOutcome == B_OUTCOME_WON)
        LegendsPlates_GuardianWon(sSOS.index);
    memset(&sSOS, 0, sizeof(sSOS));
}

// Temporary map visibility is recalculated on every Woods load. Persistent
// quest receipts, not possession of a Meadow Plate, determine availability.
void LegendsSOS_PrepareMeadow(void)
{
    u32 state = LegendsPlates_QuestState(LA_QUEST_PLATE_FIRST + 3);
    if (state == QUEST_ACTIVE || state == QUEST_REWARD_READY)
        FlagClear(FLAG_TEMP_13);
    else
        FlagSet(FLAG_TEMP_13);
}
void LegendsSOS_CheckMeadow(void)
{
    gSpecialVar_Result = LegendsPlates_QuestState(LA_QUEST_PLATE_FIRST + 3);
}
