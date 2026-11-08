#include "global.h"
#include "rift_tracker.h"
#include "legends_quests.h"
#include "event_data.h"
#include "battle.h"
#include "string_util.h"
#include "text.h"
#include "window.h"
#include "constants/flags.h"
#include "constants/vars.h"
#include "constants/battle.h"
#include "constants/maps.h"
#include "script.h"
#include "overworld.h"

struct RiftSite
{
    const u8 *name;
    u8 badges, x, y;
    u8 mapGroup, mapNum, warpId;
    bool8 travel;
};
static const struct RiftSite sSites[] = {
    {COMPOUND_STRING("Granite Cave"), 6, 29, 0, MAP_GROUP(MAP_GRANITE_CAVE_B2F), MAP_NUM(MAP_GRANITE_CAVE_B2F), 5, FALSE},
    {COMPOUND_STRING("Allearth Forest"), 6, 21, 37, MAP_GROUP(MAP_HYPERHOENN_34_39_ALLEARTH_FOREST), MAP_NUM(MAP_HYPERHOENN_34_39_ALLEARTH_FOREST), 6, FALSE},
    {COMPOUND_STRING("Basement"), 6, 6, 9, MAP_GROUP(MAP_HYPERHOENN_34_10_BASEMENT), MAP_NUM(MAP_HYPERHOENN_34_10_BASEMENT), 1, FALSE},
    {COMPOUND_STRING("Crescent Isle"), 6, 7, 19, MAP_GROUP(MAP_HYPERHOENN_34_28_CRESCENT_ISLE), MAP_NUM(MAP_HYPERHOENN_34_28_CRESCENT_ISLE), 0, FALSE},
    {COMPOUND_STRING("Deep Sea"), 6, 9, 18, MAP_GROUP(MAP_HYPERHOENN_34_7_DEEP_SEA), MAP_NUM(MAP_HYPERHOENN_34_7_DEEP_SEA), 0, FALSE},
    {COMPOUND_STRING("Desert Ruins"), 5, 29, 2, MAP_GROUP(MAP_HYPERHOENN_34_45_DESERT_RUINS), MAP_NUM(MAP_HYPERHOENN_34_45_DESERT_RUINS), 1, FALSE},
    {COMPOUND_STRING("EV Training Cave"), 6, 19, 7, MAP_GROUP(MAP_HYPERHOENN_35_49_EV_TRAINING_CAVE), MAP_NUM(MAP_HYPERHOENN_35_49_EV_TRAINING_CAVE), 1, FALSE},
    {COMPOUND_STRING("EV Training Cave"), 6, 12, 4, MAP_GROUP(MAP_HYPERHOENN_35_36_EV_TRAINING_CAVE), MAP_NUM(MAP_HYPERHOENN_35_36_EV_TRAINING_CAVE), 0, FALSE},
    {COMPOUND_STRING("Mt Silver"), 6, 32, 32, MAP_GROUP(MAP_HYPERHOENN_34_53_MT_SILVER), MAP_NUM(MAP_HYPERHOENN_34_53_MT_SILVER), 0, FALSE},
    {COMPOUND_STRING("Remote Island"), 6, 24, 21, MAP_GROUP(MAP_HYPERHOENN_35_56_REMOTE_ISLAND), MAP_NUM(MAP_HYPERHOENN_35_56_REMOTE_ISLAND), 1, FALSE},
    {COMPOUND_STRING("Remote Island depths"), 6, 16, 2, MAP_GROUP(MAP_HYPERHOENN_35_63_REMOTE_ISLAND), MAP_NUM(MAP_HYPERHOENN_35_63_REMOTE_ISLAND), 0, FALSE},
    {COMPOUND_STRING("Timeless Woods"), 4, 24, 8, MAP_GROUP(MAP_HYPERHOENN_34_67_TIMELESS_WOODS), MAP_NUM(MAP_HYPERHOENN_34_67_TIMELESS_WOODS), 5, FALSE},
    {COMPOUND_STRING("Timeless chamber"), 6, 4, 28, MAP_GROUP(MAP_HYPERHOENN_35_27_TIMELESS_WOODS), MAP_NUM(MAP_HYPERHOENN_35_27_TIMELESS_WOODS), 0, FALSE},
    {COMPOUND_STRING("Meteor Falls"), 6, 5, 2, MAP_GROUP(MAP_METEOR_FALLS_B1F_2R), MAP_NUM(MAP_METEOR_FALLS_B1F_2R), 1, FALSE},
    {COMPOUND_STRING("Mirage Tower"), 5, 6, 3, MAP_GROUP(MAP_MIRAGE_TOWER_4F), MAP_NUM(MAP_MIRAGE_TOWER_4F), 1, FALSE},
    {COMPOUND_STRING("Mt. Pyre"), 6, 6, 7, MAP_GROUP(MAP_MT_PYRE_6F), MAP_NUM(MAP_MT_PYRE_6F), 2, FALSE},
    {COMPOUND_STRING("New Mauville south"), 6, 35, 39, MAP_GROUP(MAP_NEW_MAUVILLE_INSIDE), MAP_NUM(MAP_NEW_MAUVILLE_INSIDE), 1, FALSE},
    {COMPOUND_STRING("New Mauville north"), 6, 33, 13, MAP_GROUP(MAP_NEW_MAUVILLE_INSIDE), MAP_NUM(MAP_NEW_MAUVILLE_INSIDE), 2, FALSE},
    {COMPOUND_STRING("Route 116"), 6, 88, 10, MAP_GROUP(MAP_ROUTE116), MAP_NUM(MAP_ROUTE116), 6, FALSE},
    {COMPOUND_STRING("Route 133"), 6, 37, 14, MAP_GROUP(MAP_ROUTE133), MAP_NUM(MAP_ROUTE133), 0, FALSE},
    {COMPOUND_STRING("Scorched Slab"), 6, 7, 2, MAP_GROUP(MAP_SCORCHED_SLAB), MAP_NUM(MAP_SCORCHED_SLAB), 1, FALSE},
    {COMPOUND_STRING("Shoal Cave"), 6, 12, 1, MAP_GROUP(MAP_SHOAL_CAVE_LOW_TIDE_ICE_ROOM), MAP_NUM(MAP_SHOAL_CAVE_LOW_TIDE_ICE_ROOM), 1, FALSE},
    {COMPOUND_STRING("Sinnoh Route 210"), 8, 8, 22, MAP_GROUP(MAP_HYPERSINNOH_36_27_ROUTE_210), MAP_NUM(MAP_HYPERSINNOH_36_27_ROUTE_210), 0, FALSE},
    {COMPOUND_STRING("Sinnoh Spear Pillar"), 8, 15, 24, MAP_GROUP(MAP_HYPERSINNOH_35_11_SPEAR_PILLAR), MAP_NUM(MAP_HYPERSINNOH_35_11_SPEAR_PILLAR), 0, FALSE},
};
static const u16 sBadgeFlags[] = {
    FLAG_BADGE01_GET, FLAG_BADGE02_GET, FLAG_BADGE03_GET, FLAG_BADGE04_GET,
    FLAG_BADGE05_GET, FLAG_BADGE06_GET, FLAG_BADGE07_GET, FLAG_BADGE08_GET,
};
bool32 RiftTracker_IsActive(void) { return VarGet(VAR_LA_RIFT_TRACKER) == 2; }
u32 RiftTracker_Count(void) { return ARRAY_COUNT(sSites); }
const u8 *RiftTracker_SiteName(u32 id) { return id < ARRAY_COUNT(sSites) ? sSites[id].name : COMPOUND_STRING("Unknown signal"); }

// Shared by the UI and field interaction. Discovery never bypasses either gate.
static u32 SiteState(u32 id)
{
    u32 i;
    if (id >= ARRAY_COUNT(sSites) || !RiftTracker_IsActive()) return 0;
    if (!sSites[id].travel)
        return !FlagGet(FLAG_SYS_GAME_CLEAR) ? 5 : LegendsQuest_RiftAllowed(id) ? 3 : 2; // League victory, then the individual story seal.
    for (i = 0; i < sSites[id].badges; i++)
        if (!FlagGet(sBadgeFlags[i])) return 1;
    if (sSites[id].travel && VarGet(VAR_LA_PARADIGM_ARC) < 5) return 2;
    return 3;
}
void RiftTracker_Check(void)
{
    u32 id = gSpecialVar_0x8004;
    gSpecialVar_Result = SiteState(id);
    if (id < ARRAY_COUNT(sSites) && RiftTracker_IsActive())
    {
        if (id < 16) VarSet(VAR_LA_RIFT_SURVEYED, VarGet(VAR_LA_RIFT_SURVEYED) | (1 << id));
        LegendsQuest_SurveyRift(id);
        StringCopy(gStringVar1, sSites[id].name);
    }
}
extern const u8 RiftResearch_BlockNoDetector[], RiftResearch_BlockRepelled[], RiftResearch_BlockSealed[], RiftResearch_BlockLeague[];
bool32 RiftTracker_BlockWarp(const struct MapHeader *map, u32 warpId)
{
    u32 i, state;
    if (warpId >= map->events->warpCount) return FALSE;
    for (i = 0; i < ARRAY_COUNT(sSites); i++)
    {
        if (sSites[i].travel || sSites[i].mapGroup != gSaveBlock1Ptr->location.mapGroup
            || sSites[i].mapNum != gSaveBlock1Ptr->location.mapNum || sSites[i].warpId != warpId)
            continue;
        LegendsQuest_SurveyRift(i);
        state = SiteState(i);
        if (state == 3) return FALSE;
        ScriptContext_SetupScript(state == 0 ? RiftResearch_BlockNoDetector
            : state == 1 ? RiftResearch_BlockRepelled
            : state == 5 ? RiftResearch_BlockLeague : RiftResearch_BlockSealed);
        return TRUE;
    }
    return FALSE;
}

static void Print(u8 win, const u8 *text, u8 x, u8 y)
{
    AddTextPrinterParameterized(win, FONT_SMALL, text, x, y, TEXT_SKIP_DRAW, NULL);
}
static const u8 *Lead(void)
{
    if (FlagGet(FLAG_LA_WALLY_RESCUED)) return COMPOUND_STRING("Wally and Kirlia are home.\nSilph's past connects to the alliance.\nAwait Paradigm; keep training.");
    if (FlagGet(FLAG_LA_CHIMNEY_RESONANCE)) return COMPOUND_STRING("Hoopa opened a controlled crossing.\nFollow its ring on Mt. Chimney.\nWally's signal points to Saffron.");
    if (FlagGet(FLAG_LA_ASHES_WOODS_DEPARTURE)) return COMPOUND_STRING("The matching pulse points north.\nMeet May at Cozmo's house\nin Fallarbor Town.");
    switch (VarGet(VAR_LA_PARADIGM_ARC))
    {
    case 2: return COMPOUND_STRING("Wally and Kirlia are missing.\nKeep your PokeNav ready for a call.\nParadigm is checking the readings.");
    case 3: return COMPOUND_STRING("Wally called from Kanto.\nVisit his family in Verdanturf.\nTell them he and Kirlia are safe.");
    case 4: return COMPOUND_STRING("May is following the Woods lead.\nMeet her at the clearing in\nTimeless Woods.");
    default: return COMPOUND_STRING("The scout was guarding their route.\nInvestigate the northern opening\nin Timeless Woods with May.");
    }
}
static const u8 *const sStatus[] = {
    COMPOUND_STRING("No detector"), COMPOUND_STRING("Training needed"), COMPOUND_STRING("Sealed"), COMPOUND_STRING("Stable"), COMPOUND_STRING("Quiet"), COMPOUND_STRING("League first")
};
void RiftTracker_Draw(u8 win, u8 page, u8 selected)
{
    u8 buffer[32], *end;
    u32 i, state, first;
    FillWindowPixelBuffer(win, PIXEL_FILL(1));
    Print(win, page == 0 ? COMPOUND_STRING("RIFT TRACKER  1/3") : page == 1 ? COMPOUND_STRING("DETECTED SIGNALS  2/3") : COMPOUND_STRING("RESEARCH NOTES  3/3"), 4, 0);
    if (page == 0)
    {
        Print(win, COMPOUND_STRING("CURRENT INVESTIGATION"), 4, 20);
        Print(win, Lead(), 4, 36);
        Print(win, COMPOUND_STRING("LAST CONFIRMED INCIDENT"), 4, 84);
        Print(win, FlagGet(FLAG_LA_WALLY_RESCUED) ? COMPOUND_STRING("Past Saffron / Silph Co.\nTwo Giovannis met over shared data.\nHoopa brought everyone home.") : COMPOUND_STRING("Mauville Gym / Kanto Power Plant\nWally and Kirlia crossed together.\nTheir return did not reach the Gym."), 4, 96);
    }
    else if (page == 1)
    {
        if (selected >= ARRAY_COUNT(sSites)) selected = 0;
        first = selected / 6 * 6;
        for (i = first; i < ARRAY_COUNT(sSites) && i < first + 6; i++)
        {
            Print(win, i == selected ? COMPOUND_STRING(">") : COMPOUND_STRING(" "), 2, 20 + (i - first) * 13);
            Print(win, sSites[i].name, 12, 20 + (i - first) * 13);
            state = SiteState(i);
            Print(win, sStatus[state], 124, 20 + (i - first) * 13);
        }
        Print(win, sSites[selected].travel ? COMPOUND_STRING("Travel / Gym rift signature") : COMPOUND_STRING("Pokemon / natural wormhole"), 4, 100);
        if (!sSites[selected].travel)
        {
            Print(win, COMPOUND_STRING("Requires: Hoenn League victory"), 4, 114);
        }
        else
        {
        StringCopy(buffer, COMPOUND_STRING("Badges: "));
        end = ConvertIntToDecimalStringN(buffer + StringLength(buffer), sSites[selected].badges, STR_CONV_MODE_LEFT_ALIGN, 1);
        StringCopy(end, COMPOUND_STRING("   X:"));
        end = ConvertIntToDecimalStringN(buffer + StringLength(buffer), sSites[selected].x, STR_CONV_MODE_LEFT_ALIGN, 2);
        StringCopy(end, COMPOUND_STRING(" Y:"));
        ConvertIntToDecimalStringN(buffer + StringLength(buffer), sSites[selected].y, STR_CONV_MODE_LEFT_ALIGN, 2);
        Print(win, buffer, 4, 114);
        }
    }
    else
    {
        Print(win, COMPOUND_STRING("NATURAL WORMHOLES\nMost dangerous. League victory first.\nTRAVEL RIFTS\nGym signature. Connect places.\nGOLDEN RINGS\nHoopa's signature is different.\nBADGES + STORY\nDetection alone cannot open a rift."), 4, 20);
    }
    Print(win, page == 1 ? COMPOUND_STRING("L/R: pages UP/DOWN: select B: exit") : COMPOUND_STRING("L/R: pages  B: exit"), 4, 132);
    CopyWindowToVram(win, COPYWIN_FULL);
}
