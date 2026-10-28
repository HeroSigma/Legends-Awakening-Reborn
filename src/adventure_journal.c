#include "global.h"
#include "adventure_journal.h"
#include "event_data.h"
#include "event_object_lock.h"
#include "field_player_avatar.h"
#include "script.h"
#include "main.h"
#include "menu.h"
#include "overworld.h"
#include "string_util.h"
#include "task.h"
#include "text.h"
#include "window.h"
#include "constants/game_stat.h"
#include "constants/flags.h"

struct JournalRow { const u8 label[32]; u16 id; };
static const struct JournalRow sJourney[] = {
    {_("Steps taken"), GAME_STAT_STEPS},
    {_("Battles"), GAME_STAT_TOTAL_BATTLES},
    {_("Wild battles"), GAME_STAT_WILD_BATTLES},
    {_("Trainer battles"), GAME_STAT_TRAINER_BATTLES},
    {_("Pokemon caught"), GAME_STAT_POKEMON_CAPTURES},
    {_("Eggs hatched"), GAME_STAT_HATCHED_EGGS},
    {_("Evolutions"), GAME_STAT_EVOLVED_POKEMON},
    {_("Fishing encounters"), GAME_STAT_FISHING_ENCOUNTERS},
};
static const struct JournalRow sField[] = {
    {_("DexNav searches"), GAME_STAT_DEXNAV_SCANNED},
    {_("Pokemon Center visits"), GAME_STAT_USED_POKECENTER},
    {_("Berries planted"), GAME_STAT_PLANTED_BERRIES},
    {_("Cut used"), GAME_STAT_USED_CUT},
    {_("Rock Smash used"), GAME_STAT_USED_ROCK_SMASH},
    {_("Ledges jumped"), GAME_STAT_JUMPED_DOWN_LEDGES},
    {_("Times saved"), GAME_STAT_SAVED_GAME},
    {_("League victories"), GAME_STAT_ENTERED_HOF},
};
static const struct JournalRow sStory[] = {
    {_("Delivery message read"), FLAG_LA_PC_DELIVERY_MESSAGE_READ},
    {_("Tera Orb received"), FLAG_LA_RECEIVED_TERA_ORB},
    {_("Met Brendan and May"), FLAG_LA_MET_BRENDAN_AND_MAY},
    {_("Met Red"), FLAG_LA_MET_RED},
    {_("DexNav received"), FLAG_LA_DEXNAV_RECEIVED},
    {_("Devon goods returned"), FLAG_RETURNED_DEVON_GOODS},
    {_("Timeless call heard"), FLAG_LA_TIMELESS_WOODS_CALL_HEARD},
    {_("Woods meeting seen"), FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN},
};
static const u8 sTitleJourney[] = _("ADVENTURE JOURNAL  1/3");
static const u8 sTitleField[] = _("FIELD RECORDS  2/3");
static const u8 sTitleStory[] = _("STORY NOTES  3/3");
static const u8 *const sTitles[] = {sTitleJourney, sTitleField, sTitleStory};
static const u8 sFooter[] = _("Left/Right: pages   B: close");
static const u8 sDone[] = _("Done");
static const u8 sPending[] = _("Pending");
static const struct WindowTemplate sJournalWindow = {
    .bg = 0, .tilemapLeft = 2, .tilemapTop = 1,
    .width = 26, .height = 18, .paletteNum = 15, .baseBlock = 1,
};

static void DrawJournal(u8 taskId)
{
    u8 number[12];
    u32 i;
    u8 win = gTasks[taskId].data[0], page = gTasks[taskId].data[1];
    const struct JournalRow *rows = page == 0 ? sJourney : page == 1 ? sField : sStory;
    FillWindowPixelBuffer(win, PIXEL_FILL(1));
    AddTextPrinterParameterized(win, FONT_NORMAL, sTitles[page], 4, 0, TEXT_SKIP_DRAW, NULL);
    for (i = 0; i < 8; i++)
    {
        const u8 *value;
        AddTextPrinterParameterized(win, FONT_SMALL, rows[i].label, 4, 20 + 14*i, TEXT_SKIP_DRAW, NULL);
        if (page == 2)
            value = FlagGet(rows[i].id) ? sDone : sPending;
        else
        {
            ConvertIntToDecimalStringN(number, GetGameStat(rows[i].id), STR_CONV_MODE_LEFT_ALIGN, 10);
            value = number;
        }
        AddTextPrinterParameterized(win, FONT_SMALL, value, 150, 20 + 14*i, TEXT_SKIP_DRAW, NULL);
    }
    AddTextPrinterParameterized(win, FONT_SMALL, sFooter, 4, 132, TEXT_SKIP_DRAW, NULL);
    CopyWindowToVram(win, COPYWIN_FULL);
}

static void Task_AdventureJournal(u8 taskId)
{
    if (JOY_NEW(B_BUTTON | START_BUTTON))
    {
        u8 win = gTasks[taskId].data[0];
        ClearStdWindowAndFrame(win, TRUE);
        RemoveWindow(win);
        DestroyTask(taskId);
        ScriptUnfreezeObjectEvents();
        UnlockPlayerFieldControls();
    }
    else if (JOY_NEW(DPAD_LEFT | DPAD_RIGHT | L_BUTTON | R_BUTTON))
    {
        gTasks[taskId].data[1] = (gTasks[taskId].data[1] + (JOY_NEW(DPAD_LEFT | L_BUTTON) ? 2 : 1)) % 3;
        DrawJournal(taskId);
    }
}

void AdventureJournal_Open(void)
{
    u8 win = AddWindow(&sJournalWindow);
    u8 taskId;
    if (win == WINDOW_NONE)
    {
        ScriptUnfreezeObjectEvents();
        UnlockPlayerFieldControls();
        return;
    }
    taskId = CreateTask(Task_AdventureJournal, 0);
    gTasks[taskId].data[0] = win;
    DrawStdWindowFrame(win, FALSE);
    PutWindowTilemap(win);
    DrawJournal(taskId);
}
