#include "global.h"
#include "legends_plates.h"
#include "legends_quests.h"
#include "rift_tracker.h"
#include "event_data.h"
#include "item.h"
#include "item_menu.h"
#include "pokemon.h"
#include "battle.h"
#include "string_util.h"
#include "text.h"
#include "constants/flags.h"
#include "constants/maps.h"
#include "constants/event_objects.h"

static const u16 sPlateItems[LEGENDS_PLATE_COUNT] = {
    ITEM_FLAME_PLATE,
    ITEM_SPLASH_PLATE,
    ITEM_ZAP_PLATE,
    ITEM_MEADOW_PLATE,
    ITEM_ICICLE_PLATE,
    ITEM_FIST_PLATE,
    ITEM_TOXIC_PLATE,
    ITEM_EARTH_PLATE,
    ITEM_SKY_PLATE,
    ITEM_MIND_PLATE,
    ITEM_INSECT_PLATE,
    ITEM_STONE_PLATE,
    ITEM_SPOOKY_PLATE,
    ITEM_DRACO_PLATE,
    ITEM_DREAD_PLATE,
    ITEM_IRON_PLATE,
    ITEM_PIXIE_PLATE,
};
static const struct LegendsQuest sPlateQuests[LEGENDS_PLATE_COUNT + 1] = {
    {COMPOUND_STRING("The Silent Plate"), COMPOUND_STRING("Professor Birch"),
     COMPOUND_STRING("Birch's Lab / resonance leads"), COMPOUND_STRING("Legend Plate awakening"),
     COMPOUND_STRING("Awaken all 17 resonances.\nReturn the Blank Plate to Birch."),
     OBJ_EVENT_GFX_LA_ROSTER_BIRCH, MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB, 0, 0},
    {COMPOUND_STRING("Flame Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Flame Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_FLAME_PLATE},
    {COMPOUND_STRING("Splash Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Splash Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_SPLASH_PLATE},
    {COMPOUND_STRING("Zap Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Zap Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_ZAP_PLATE},
    {COMPOUND_STRING("Meadow Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Meadow Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_MEADOW_PLATE},
    {COMPOUND_STRING("Icicle Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Icicle Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_ICICLE_PLATE},
    {COMPOUND_STRING("Fist Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Fist Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_FIST_PLATE},
    {COMPOUND_STRING("Toxic Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Toxic Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_TOXIC_PLATE},
    {COMPOUND_STRING("Earth Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Earth Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_EARTH_PLATE},
    {COMPOUND_STRING("Sky Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Sky Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_SKY_PLATE},
    {COMPOUND_STRING("Mind Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Mind Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_MIND_PLATE},
    {COMPOUND_STRING("Insect Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Insect Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_INSECT_PLATE},
    {COMPOUND_STRING("Stone Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Stone Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_STONE_PLATE},
    {COMPOUND_STRING("Spooky Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Spooky Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_SPOOKY_PLATE},
    {COMPOUND_STRING("Draco Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Draco Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_DRACO_PLATE},
    {COMPOUND_STRING("Dread Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Dread Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_DREAD_PLATE},
    {COMPOUND_STRING("Iron Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Iron Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_IRON_PLATE},
    {COMPOUND_STRING("Pixie Resonance"), COMPOUND_STRING("Blank Plate"),
     COMPOUND_STRING("Await a story resonance lead"), COMPOUND_STRING("Pixie Plate resonance"),
     COMPOUND_STRING("Follow the awakened resonance.\nOvercome its guardian."),
     OBJ_EVENT_GFX_ITEM_BALL, 0, 0, ITEM_PIXIE_PLATE},
};
#define ACTIVE(i) (FLAG_LA_PLATE_ACTIVE_BASE + (i))
#define WON(i) (FLAG_LA_PLATE_WON_BASE + (i))

u32 LegendsPlates_CountCompleted(void)
{
    u32 count = 0;
    for (u32 i = 0; i < LEGENDS_PLATE_COUNT; i++)
        if (FlagGet(WON(i)) && !FlagGet(ACTIVE(i))) count++;
    return count;
}
u32 LegendsPlates_QuestState(u32 quest)
{
    if (quest < LA_QUEST_PLATES || quest >= LA_QUEST_COUNT) return QUEST_LOCKED;
    if (quest == LA_QUEST_PLATES) {
        if (FlagGet(FLAG_LA_LEGEND_PLATE_AWAKENED)) return QUEST_CLAIMED;
        if (!FlagGet(FLAG_LA_BLANK_PLATE_RECEIVED)) return QUEST_LOCKED;
        return LegendsPlates_CountCompleted() == LEGENDS_PLATE_COUNT ? QUEST_REWARD_READY : QUEST_ACTIVE;
    }
    if (!FlagGet(FLAG_LA_BLANK_PLATE_RECEIVED)) return QUEST_LOCKED;
    u32 i = quest - LA_QUEST_PLATE_FIRST;
    if (FlagGet(WON(i))) return FlagGet(ACTIVE(i)) ? QUEST_REWARD_READY : QUEST_CLAIMED;
    return FlagGet(ACTIVE(i)) ? QUEST_ACTIVE : QUEST_LOCKED;
}
const struct LegendsQuest *LegendsPlates_QuestMetadata(u32 quest)
{
    return quest >= LA_QUEST_PLATES && quest < LA_QUEST_COUNT ? &sPlateQuests[quest - LA_QUEST_PLATES] : NULL;
}
bool32 LegendsPlates_Activate(u32 index)
{
    if (index >= LEGENDS_PLATE_COUNT || !FlagGet(FLAG_LA_BLANK_PLATE_RECEIVED)
        || FlagGet(WON(index))) return FALSE;
    FlagSet(ACTIVE(index));
    return TRUE;
}
// Called only by a future scripted guardian's battle-return handler. Ordinary
// wild/trainer battles do not invoke this, and capture/flee/loss cannot complete it.
bool32 LegendsPlates_GuardianWon(u32 index)
{
    if (index >= LEGENDS_PLATE_COUNT || gBattleOutcome != B_OUTCOME_WON
        || LegendsPlates_QuestState(LA_QUEST_PLATE_FIRST + index) != QUEST_ACTIVE) return FALSE;
    FlagSet(WON(index));
    return TRUE;
}
// The won bit is recorded before inventory delivery. A full Bag leaves reward
// ready, so the guardian need not be defeated again; only successful delivery
// clears ACTIVE and marks the resonance collected. Existing Plates confer no win.
u32 LegendsPlates_ClaimGuardian(u32 index)
{
    if (index >= LEGENDS_PLATE_COUNT
        || LegendsPlates_QuestState(LA_QUEST_PLATE_FIRST + index) != QUEST_REWARD_READY) return 0;
    if (!CheckBagHasItem(sPlateItems[index], 1) && !AddBagItem(sPlateItems[index], 1)) return 2;
    FlagClear(ACTIVE(index));
    return 1;
}
u32 LegendsPlates_StartResearch(void)
{
    if (!RiftTracker_IsActive() || FlagGet(FLAG_LA_BLANK_PLATE_RECEIVED)) return 0;
    if (!CheckBagHasItem(ITEM_BLANK_PLATE, 1) && !AddBagItem(ITEM_BLANK_PLATE, 1)) return 2;
    FlagSet(FLAG_LA_BLANK_PLATE_RECEIVED);
    return 1;
}
u32 LegendsPlates_TryAwaken(void)
{
    if (!FlagGet(FLAG_LA_BLANK_PLATE_RECEIVED) || FlagGet(FLAG_LA_LEGEND_PLATE_AWAKENED)
        || LegendsPlates_CountCompleted() != LEGENDS_PLATE_COUNT
        || gSaveBlock1Ptr->location.mapGroup != MAP_GROUP(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)
        || gSaveBlock1Ptr->location.mapNum != MAP_NUM(MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB)
        || !CheckBagHasItem(ITEM_BLANK_PLATE, 1)) return 0;
    bool32 added = !CheckBagHasItem(ITEM_LEGEND_PLATE, 1);
    if (added && !AddBagItem(ITEM_LEGEND_PLATE, 1)) return 2;
    if (!RemoveBagItem(ITEM_BLANK_PLATE, CountTotalItemQuantityInBag(ITEM_BLANK_PLATE))) {
        if (added) RemoveBagItem(ITEM_LEGEND_PLATE, 1);
        return 2;
    }
    FlagSet(FLAG_LA_LEGEND_PLATE_AWAKENED);
    return 1;
}
void LegendsPlates_PrepareBirch(void)
{
    gSpecialVar_Result = 0;
    if (!RiftTracker_IsActive()) return;
    if (!FlagGet(FLAG_LA_BLANK_PLATE_RECEIVED)) gSpecialVar_Result = 1;
    else if (!FlagGet(FLAG_LA_LEGEND_PLATE_AWAKENED)
        && LegendsPlates_CountCompleted() == LEGENDS_PLATE_COUNT) gSpecialVar_Result = 2;
}
void LegendsPlates_BeginResearch(void) {gSpecialVar_Result = LegendsPlates_StartResearch();}
void LegendsPlates_Awaken(void) {gSpecialVar_Result = LegendsPlates_TryAwaken();}
void ItemUseOutOfBattle_LegendsPlate(u8 taskId)
{
    ConvertIntToDecimalStringN(gStringVar1, LegendsPlates_CountCompleted(), STR_CONV_MODE_LEFT_ALIGN, 2);
    StringExpandPlaceholders(gStringVar4, FlagGet(FLAG_LA_LEGEND_PLATE_AWAKENED)
        ? COMPOUND_STRING("All 17 resonances are awakened.")
        : COMPOUND_STRING("Resonances awakened: {STR_VAR_1}/17."));
    DisplayItemMessage(taskId, FONT_NORMAL, gStringVar4, CloseItemMessage);
}

// Script entry points for the guardian/SOS chapter. They remain dormant until
// actual quest-trigger and battle-return scripts call them.
void LegendsPlates_ActivateQuest(void) {gSpecialVar_Result = LegendsPlates_Activate(gSpecialVar_0x8004);}
void LegendsPlates_RecordGuardianResult(void) {gSpecialVar_Result = LegendsPlates_GuardianWon(gSpecialVar_0x8004);}
void LegendsPlates_CollectResonance(void) {gSpecialVar_Result = LegendsPlates_ClaimGuardian(gSpecialVar_0x8004);}
