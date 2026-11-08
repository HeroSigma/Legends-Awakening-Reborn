#include "global.h"
#include "decompress.h"
#include "malloc.h"
#include "palette.h"
#include "gpu_regs.h"
#include "legends_quests.h"
#include "legends_pokevial.h"
#include "rift_tracker.h"
#include "event_data.h"
#include "event_object_lock.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "item.h"
#include "item_icon.h"
#include "field_effect.h"
#include "main.h"
#include "menu.h"
#include "overworld.h"
#include "pokemon.h"
#include "script.h"
#include "sprite.h"
#include "string_util.h"
#include "task.h"
#include "text.h"
#include "window.h"
#include "constants/flags.h"
#include "constants/items.h"
#include "constants/maps.h"
#include "constants/vars.h"
#include "constants/event_objects.h"

struct LegendsQuest {
    const u8 *title, *giver, *location, *reward, *objectives;
    u16 graphics, map, completionFlag, item;
};
#include "data/legends_quests.h"
#define ACCEPTED(id) (FLAG_LA_QUEST_BASE + (id) * 2)
#define CLAIMED(id) (FLAG_LA_QUEST_BASE + (id) * 2 + 1)
static bool32 MainComplete(u32 id)
{
    if (id >= 10) return FALSE;
    if (sQuests[id].completionFlag) return FlagGet(sQuests[id].completionFlag);
    switch (id) {
    case 8: return FlagGet(FLAG_LA_WALLY_RESCUED);
    case 6: return CheckBagHasItem(ITEM_Z_POWER_RING, 1);
    case 7: return RiftTracker_IsActive();
    case 9: return VarGet(VAR_LA_OAK_STARTER) >= 10;
    }
    return FALSE;
}
u32 LegendsQuest_State(u32 id)
{
    if (id >= LA_QUEST_COUNT) return QUEST_LOCKED;
    if (id == 44) return FlagGet(FLAG_LA_CHIMNEY_RESONANCE) ? QUEST_CLAIMED : FlagGet(FLAG_LA_ASHES_WOODS_DEPARTURE) ? QUEST_ACTIVE : QUEST_LOCKED;
    if (id == 45) return FlagGet(FLAG_LA_WALLY_RESCUED) ? QUEST_CLAIMED : FlagGet(FLAG_LA_CHIMNEY_RESONANCE) ? QUEST_ACTIVE : QUEST_LOCKED;
    if (FlagGet(CLAIMED(id))) return QUEST_CLAIMED;
    // Native story receipts are authoritative, including on pre-quest saves.
    if (id < 10) {
        if (MainComplete(id)) return QUEST_CLAIMED;
        if (FlagGet(ACCEPTED(id))) return QUEST_REWARD_READY;
        if (id == 0 || (id < 8 && MainComplete(id - 1))
            || (id == 8 && VarGet(VAR_LA_PARADIGM_ARC) >= 2)
            || (id == 9 && VarGet(VAR_LA_RIFT_TRACKER) >= 1)) return QUEST_ACTIVE;
        return QUEST_LOCKED;
    }
    if (id < 18) {
        if (FlagGet(sQuests[id].completionFlag)) return QUEST_REWARD_READY;
        if (id == 10 || FlagGet(sQuests[id - 1].completionFlag)) return QUEST_ACTIVE;
        return QUEST_LOCKED;
    }
    if (id < 20) {
        if (!FlagGet(ACCEPTED(id))) return QUEST_LOCKED;
        if (id == 18 && CheckBagHasItem(ITEM_SUPER_POTION, 3)) return QUEST_REWARD_READY;
        if (id == 19) {
            u32 i;
            for (i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
                if (GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_SPECIES) == SPECIES_RALTS
                    && !GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_EGG)
                    && !GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_SHINY)) return QUEST_REWARD_READY;
        }
        return QUEST_ACTIVE;
    }
    if (!RiftTracker_IsActive() || !FlagGet(FLAG_SYS_GAME_CLEAR)) return QUEST_LOCKED;
    return FlagGet(ACCEPTED(id)) ? QUEST_REWARD_READY : QUEST_ACTIVE;
}
bool32 LegendsQuest_RiftAllowed(u32 site)
{
    return site < RiftTracker_Count() && FlagGet(FLAG_SYS_GAME_CLEAR)
        && RiftTracker_IsActive() && FlagGet(CLAIMED(LA_QUEST_RIFT_FIRST + site));
}
void LegendsQuest_SurveyRift(u32 site)
{
    if (site < RiftTracker_Count() && RiftTracker_IsActive() && FlagGet(FLAG_SYS_GAME_CLEAR))
        FlagSet(ACCEPTED(LA_QUEST_RIFT_FIRST + site));
}
// Contextual claims only. Result: 0 not ready, 1 success, 2 bag full,
// 3 claim previous Gym reward first, 4 speak to the giver, 5 cancelled/invalid trade.
void LegendsQuest_Claim(void)
{
    u32 id = gSpecialVar_0x8004;
    u16 map = (gSaveBlock1Ptr->location.mapGroup << 8) | gSaveBlock1Ptr->location.mapNum;
    gSpecialVar_Result = 0;
    if (id >= LA_QUEST_COUNT || LegendsQuest_State(id) != QUEST_REWARD_READY) return;
    if (id >= LA_QUEST_RIFT_FIRST) {
        gSpecialVar_Result = 4;
        if (map != MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB) return;
        FlagSet(CLAIMED(id));
        gSpecialVar_Result = 1;
        return;
    }
    if (id < 10) {
        static const u16 items[] = {ITEM_TERA_ORB, ITEM_MEGA_RING, 0, ITEM_POKEVIAL, 0, ITEM_DYNAMAX_BAND, ITEM_Z_POWER_RING, ITEM_RIFT_TRACKER};
        gSpecialVar_Result = 4;
        if ((map != sQuests[id].map && !(id == 0 && map == MAP_LITTLEROOT_TOWN_MAYS_HOUSE_2F)) || id >= ARRAY_COUNT(items) || !items[id]) return;
        gSpecialVar_Result = 2;
        if (!CheckBagHasItem(items[id], 1) && !AddBagItem(items[id], 1)) return;
        if (id == 0) FlagSet(FLAG_LA_RECEIVED_TERA_ORB);
        if (id == 1) FlagSet(FLAG_LA_RECEIVED_RED_MEGA_RING);
        if (id == 3) LegendsPokevialGrant();
        FlagSet(CLAIMED(id));
        CopyItemName(items[id], gStringVar1);
        gSpecialVar_Result = 1;
        return;
    }
    if (id == 19) return;
    gSpecialVar_Result = 4;
    if (map != sQuests[id].map) return;
    if (id > 10 && id < 18 && !FlagGet(CLAIMED(id - 1))) {
        gSpecialVar_Result = 3;
        return;
    }
    gSpecialVar_Result = 2;
    if (id == 18 && !CheckBagHasItem(ITEM_SUPER_POTION, 3)) return;
    if (!AddBagItem(sQuests[id].item, 1)) return;
    if (id == 18) RemoveBagItem(ITEM_SUPER_POTION, 3);
    FlagSet(CLAIMED(id));
    CopyItemName(sQuests[id].item, gStringVar1);
    gSpecialVar_0x8005 = sQuests[id].item;
    gSpecialVar_Result = 1;
}
void LegendsQuest_Accept(void)
{
    u32 id = gSpecialVar_0x8004;
    if (id == 18 || id == 19) FlagSet(ACCEPTED(id));
    gSpecialVar_Result = LegendsQuest_State(id);
}
void LegendsQuest_TradeRalts(void)
{
    u32 slot = gSpecialVar_0x8004;
    struct Pokemon *mon;
    bool32 shiny = TRUE;
    gSpecialVar_Result = 5;
    if (slot >= gPartiesCount[B_TRAINER_PLAYER] || LegendsQuest_State(19) != QUEST_REWARD_READY) return;
    mon = &gParties[B_TRAINER_PLAYER][slot];
    if (GetMonData(mon, MON_DATA_SPECIES) != SPECIES_RALTS
        || GetMonData(mon, MON_DATA_IS_EGG) || GetMonData(mon, MON_DATA_IS_SHINY)) return;
    // A same-species exchange preserves the offered level, moves, held item,
    // battle traits and ownership. No party slot/storage is consumed or lost.
    SetMonData(mon, MON_DATA_IS_SHINY, &shiny);
    FlagSet(CLAIMED(19));
    gSpecialVar_Result = 1;
}

static const struct WindowTemplate sWindow = {
    .bg = 0, .tilemapLeft = 0, .tilemapTop = 0,
    .width = 30, .height = 20, .paletteNum = 15, .baseBlock = 1,
};
static void DestroyQuestSprite(u8 id)
{
    if (id != MAX_SPRITES) FieldEffectFreeGraphicsResources(&gSprites[id]);
}
static bool32 ObjectiveDone(u32 id, u32 part)
{
    static const u16 flags[6][2] = {
        {FLAG_LA_PC_DELIVERY_MESSAGE_READ, FLAG_LA_TERA_ORB_ACTIVATED},
        {FLAG_SYS_POKEMON_GET, FLAG_LA_RECEIVED_RED_MEGA_RING},
        {FLAG_LA_RED_ROUTE103_COMPLETE, FLAG_LA_RED_DEX_GIFTS},
        {FLAG_LA_WOODS_TRIAD_COMPLETE, FLAG_LA_POKEVIAL_RECEIVED},
        {FLAG_RETURNED_DEVON_GOODS, FLAG_LA_TERA_RESEARCH_INTRO},
        {FLAG_LA_DEWFORD_HOOPA_SEEN, FLAG_LA_HIDE_DEWFORD_DYNAMAX_BAND},
    };
    if (id == 44) return FlagGet(part ? FLAG_LA_CHIMNEY_RESONANCE : FLAG_LA_COZMO_BRIEFED);
    if (id == 45) return FlagGet(part ? FLAG_LA_WALLY_RESCUED : FLAG_LA_SILPH_WALLY_FOUND);
    if (id < 6) return FlagGet(flags[id][part]);
    if (id == 6) return part ? MainComplete(id) : VarGet(VAR_REGISTER_BIRCH_STATE) >= 1;
    if (id == 7) return part ? RiftTracker_IsActive() : VarGet(VAR_LA_MAUVILLE_RIFT) == 3;
    if (id == 8) return part ? FlagGet(FLAG_LA_WALLY_RESCUED) : VarGet(VAR_LA_PARADIGM_ARC) >= 4;
    if (id == 9) return VarGet(VAR_LA_OAK_STARTER) >= (part ? 10 : 2);
    if (id < 18) return part ? id == 10 || FlagGet(CLAIMED(id - 1)) : FlagGet(sQuests[id].completionFlag);
    if (id < 20) return LegendsQuest_State(id) >= QUEST_REWARD_READY;
    return part ? FlagGet(ACCEPTED(id)) : FlagGet(FLAG_SYS_GAME_CLEAR);
}

// Layout/art adapted from PokemonSanFran's Unbound Quest Menu.
// Preserve the project's persistent quest ledger and transactions.
static const u32 sQuestBackground[] = INCGFX_U32("graphics/quests/unbound_menu.png", ".4bpp.smol");
static const u16 sQuestPalette[] = INCGFX_U16("graphics/quests/unbound_menu.pal", ".gbapal");
static EWRAM_DATA u16 *sQuestPaletteBackup = NULL;
static void QuestPrint(u8 win, const u8 *text, u8 x, u8 y, u8 color)
{
    const u8 colors[] = {0, color, 0};
    AddTextPrinterParameterized3(win, FONT_SMALL, x, y, colors, TEXT_SKIP_DRAW, text);
}
static const struct LegendsQuest sChapterQuests[] = {
    {COMPOUND_STRING("Ashes and Echoes"), COMPOUND_STRING("May / Professor Cozmo"), COMPOUND_STRING("Fallarbor / Mt. Chimney"),
     COMPOUND_STRING("Resonance recording"), COMPOUND_STRING("Investigate Cozmo's findings.\nStop the summit experiment."), OBJ_EVENT_GFX_LA_ROSTER_MAY, MAP_MT_CHIMNEY, 0, 0},
    {COMPOUND_STRING("A Door Through Time"), COMPOUND_STRING("Wally"), COMPOUND_STRING("Saffron / Silph Co."),
     COMPOUND_STRING("Wally's return / Hoopa"), COMPOUND_STRING("Find Wally inside Silph Co.\nEscape the past together."), OBJ_EVENT_GFX_LA_ROSTER_WALLY, MAP_KANTOAR_1_53_SILPHCO_7F, 0, 0},
};
static const struct LegendsQuest *QuestMetadata(u32 id)
{
    return id < 20 ? &sQuests[id] : id >= 44 && id < 46 ? &sChapterQuests[id - 44] : NULL;
}
static const u8 *QuestTitle(u32 id)
{
    if (id >= LA_QUEST_COUNT) return COMPOUND_STRING("No matching quests");
    if (LegendsQuest_State(id) == QUEST_LOCKED) return COMPOUND_STRING("??????");
    return QuestMetadata(id) ? QuestMetadata(id)->title : RiftTracker_SiteName(id - 20);
}
static bool32 Matches(u32 id, u32 side, u32 filter)
{
    u32 state;
    if (id >= LA_QUEST_COUNT || (id >= 18 && id < 44) != side) return FALSE;
    state = LegendsQuest_State(id);
    return !filter || state == filter;
}
static s32 FindQuest(s32 current, u32 side, u32 filter, s32 direction)
{
    s32 id = current;
    u32 i;
    for (i = 0; i < LA_QUEST_COUNT; i++) {
        id = (id + direction + LA_QUEST_COUNT) % LA_QUEST_COUNT;
        if (Matches(id, side, filter)) return id;
    }
    return -1;
}
static void FitText(u8 win, const u8 *text, u8 x, u8 y, u32 width, u8 color)
{
    u8 line[96];
    u32 n = 0;
    while (text[n] != EOS && text[n] != CHAR_NEWLINE && n < sizeof(line) - 4) {
        line[n] = text[n]; line[n + 1] = EOS;
        if (GetStringWidth(FONT_SMALL, line, 0) > width) break;
        n++;
    }
    line[n] = EOS;
    if (text[n] != EOS && text[n] != CHAR_NEWLINE && n > 3) {
        line[n - 3] = CHAR_PERIOD;
        line[n - 2] = CHAR_PERIOD;
        line[n - 1] = CHAR_PERIOD;
    }
    QuestPrint(win, line, x, y, color);
}
static void CloseQuest(u8 taskId, bool32 script)
{
    s16 *d = gTasks[taskId].data;
    DestroyQuestSprite(d[2]);
    ClearWindowTilemap(d[0]);
    CopyWindowToVram(d[0], COPYWIN_MAP);
    RemoveWindow(d[0]);
    if (sQuestPaletteBackup != NULL) {
        LoadPalette(sQuestPaletteBackup, 15 * 16, 32);
        SetGpuRegBits(REG_OFFSET_DISPCNT, sQuestPaletteBackup[16]);
        Free(sQuestPaletteBackup);
        sQuestPaletteBackup = NULL;
    }
    DestroyTask(taskId);
    if (!script) {
        ScriptUnfreezeObjectEvents();
        UnlockPlayerFieldControls();
    }
}
static void DrawQuest(u8 taskId)
{
    s16 *d = gTasks[taskId].data;
    s32 id = d[1];
    u8 win = d[0], buf[24];
    u32 count = 0, selected = 0, i, row, first, state;
    const struct LegendsQuest *q = id >= 0 ? QuestMetadata(id) : NULL;
    static const u8 *const filters[] = {
        COMPOUND_STRING("ALL"), COMPOUND_STRING("ACTIVE"),
        COMPOUND_STRING("READY"), COMPOUND_STRING("DONE")
    };
    static const u8 *const states[] = {
        COMPOUND_STRING("-"), COMPOUND_STRING("Active"),
        COMPOUND_STRING("Ready"), COMPOUND_STRING("Done")
    };
    static const u8 colors[] = {8, 10, 5, 7};
    CopyToWindowPixelBuffer(win, sQuestBackground, 0, 0);
    for (i = 0; i < LA_QUEST_COUNT; i++) if (Matches(i, d[5], d[4])) {
        if ((s32)i == id) selected = count;
        count++;
    }
    QuestPrint(win, d[5] ? COMPOUND_STRING("SIDE  L/R") : COMPOUND_STRING("MAIN  L/R"), 10, 2, 13);
    QuestPrint(win, COMPOUND_STRING("SEL:"), 82, 2, 13);
    QuestPrint(win, filters[d[4]], 105, 2, 13);
    u8 *end = ConvertIntToDecimalStringN(buf, count ? selected + 1 : 0, STR_CONV_MODE_LEFT_ALIGN, 2);
    *end++ = CHAR_SLASH;
    ConvertIntToDecimalStringN(end, count, STR_CONV_MODE_LEFT_ALIGN, 2);
    QuestPrint(win, buf, 197, 2, 13);
    if (!d[3]) {
        first = selected / 4 * 4;
        row = 0;
        u32 index = 0;
        for (i = 0; i < LA_QUEST_COUNT; i++) if (Matches(i, d[5], d[4])) {
            if (index >= first && row < 4) {
                state = LegendsQuest_State(i);
                if ((s32)i == id) {
                    FillWindowPixelRect(win, PIXEL_FILL(6), 12, 18 + row * 16, 178, 14);
                    QuestPrint(win, COMPOUND_STRING(">"), 12, 18 + row * 16, 13);
                }
                FitText(win, QuestTitle(i), 23, 18 + row * 16, 164, 13);
                QuestPrint(win, states[state], 200, 18 + row * 16, colors[state]);
                row++;
            }
            index++;
        }
        if (!count) QuestPrint(win, COMPOUND_STRING("No matching quests."), 22, 34, 13);
    } else if (id >= 0) {
        const u8 *objectives = q ? q->objectives : COMPOUND_STRING("Win the Hoenn League.\nSurvey this rift; return to Birch.");
        FitText(win, QuestTitle(id), 15, 18, 172, 13);
        for (i = 0; i < 2; i++) {
            FitText(win, objectives, 23, 34 + i * 16, 164, 13);
            QuestPrint(win, ObjectiveDone(id, i) ? COMPOUND_STRING("Done") : COMPOUND_STRING("-"), 200, 34 + i * 16, ObjectiveDone(id, i) ? 7 : 8);
            while (*objectives != EOS && *objectives != CHAR_NEWLINE) objectives++;
            if (*objectives == CHAR_NEWLINE) objectives++;
        }
        FitText(win, q ? q->giver : COMPOUND_STRING("Professor Birch"), 23, 70, 96, 13);
        QuestPrint(win, COMPOUND_STRING("A:claim B:list"), 124, 70, 13);
    }
    DestroyQuestSprite(d[2]); d[2] = MAX_SPRITES;
    if (id < 0 || LegendsQuest_State(id) == QUEST_LOCKED) {
        QuestPrint(win, COMPOUND_STRING("Keep exploring and speaking to people."), 10, 105, 1);
        QuestPrint(win, COMPOUND_STRING("New leads will appear as you progress."), 10, 120, 1);
        QuestPrint(win, COMPOUND_STRING("Up/Down: scroll   A: details   B: exit"), 10, 143, 1);
    } else {
        FitText(win, q ? q->location : RiftTracker_SiteName(id - 20), 42, 101, 192, 1);
        const u8 *objectives = q ? q->objectives : COMPOUND_STRING("Win the Hoenn League.\nSurvey this rift; return to Birch.");
        QuestPrint(win, objectives, 42, 116, 1);
        QuestPrint(win, COMPOUND_STRING("Reward:"), 42, 144, 1);
        FitText(win, q ? q->reward : COMPOUND_STRING("Individual passage permit"), 82, 144, 152, 1);
        d[2] = CreateObjectGraphicsSpriteWithTag(q ? q->graphics : OBJ_EVENT_GFX_LA_ROSTER_BIRCH,
            SpriteCallbackDummy, 20, 128, 0, 0xFFFF);
        if (d[2] != MAX_SPRITES) gSprites[d[2]].oam.priority = 0;
    }
    CopyWindowToVram(win, COPYWIN_FULL);
}
static void Task_Quests(u8 taskId)
{
    s16 *d = gTasks[taskId].data;
    s32 id = d[1];
    if (JOY_NEW(B_BUTTON | START_BUTTON)) {
        if (d[3] && JOY_NEW(B_BUTTON)) {d[3] = 0; DrawQuest(taskId);}
        else CloseQuest(taskId, FALSE);
        return;
    }
    if (JOY_NEW(L_BUTTON | R_BUTTON)) {
        d[5] ^= 1; d[3] = 0;
        d[1] = FindQuest(-1, d[5], d[4], 1);
    } else if (JOY_NEW(SELECT_BUTTON)) {
        d[4] = (d[4] + 1) % 4; d[3] = 0;
        d[1] = FindQuest(-1, d[5], d[4], 1);
    } else if (JOY_REPEAT(DPAD_UP | DPAD_DOWN) && !d[3])
        d[1] = FindQuest(id, d[5], d[4], JOY_REPEAT(DPAD_UP) ? -1 : 1);
    else if (JOY_NEW(A_BUTTON) && id >= 0 && LegendsQuest_State(id) != QUEST_LOCKED) {
        if (!d[3]) d[3] = 1;
        else if (LegendsQuest_State(id) == QUEST_REWARD_READY) {
            extern const u8 LegendsQuest_ClaimFromMenu[];
            gSpecialVar_0x8004 = id;
            CloseQuest(taskId, TRUE);
            ScriptContext_SetupScript(LegendsQuest_ClaimFromMenu);
            return;
        }
    } else return;
    DrawQuest(taskId);
}
void LegendsQuests_Open(void)
{
    u8 win, task;
    if (sQuestPaletteBackup != NULL) return;
    LockPlayerFieldControls();
    FreezeObjectEvents();
    sQuestPaletteBackup = Alloc(36);
    if (sQuestPaletteBackup == NULL) {
        ScriptUnfreezeObjectEvents(); UnlockPlayerFieldControls(); return;
    }
    CpuCopy16(gPlttBufferUnfaded + 15 * 16, sQuestPaletteBackup, 32);
    win = AddWindow(&sWindow);
    if (win == WINDOW_NONE) {
        Free(sQuestPaletteBackup); sQuestPaletteBackup = NULL;
        ScriptUnfreezeObjectEvents(); UnlockPlayerFieldControls(); return;
    }
    sQuestPaletteBackup[16] = GetGpuReg(REG_OFFSET_DISPCNT) & (DISPCNT_WIN0_ON | DISPCNT_WIN1_ON | DISPCNT_OBJWIN_ON);
    ClearGpuRegBits(REG_OFFSET_DISPCNT, DISPCNT_WIN0_ON | DISPCNT_WIN1_ON | DISPCNT_OBJWIN_ON);
    LoadPalette(sQuestPalette, 15 * 16, 32);
    task = CreateTask(Task_Quests, 0);
    gTasks[task].data[0] = win;
    gTasks[task].data[2] = MAX_SPRITES;
    PutWindowTilemap(win);
    DrawQuest(task);
}
void LegendsQuest_StoryPrepare(void)
{
    u32 id = gSpecialVar_0x8004;
    if (id < 10) FlagSet(ACCEPTED(id));
}
void LegendsQuest_StoryFinish(void)
{
    u32 id = gSpecialVar_0x8004;
    if (id < 10 && gSpecialVar_Result) FlagSet(CLAIMED(id));
}
