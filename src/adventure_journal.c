#include "global.h"
#include "adventure_journal.h"
#include "rift_tracker.h"
#include "event_data.h"
#include "event_object_lock.h"
#include "event_object_movement.h"
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

static const struct WindowTemplate sJournalWindow = {
    .bg = 0, .tilemapLeft = 2, .tilemapTop = 1,
    .width = 26, .height = 18, .paletteNum = 15, .baseBlock = 1,
};

static void DrawJournal(u8 taskId)
{
    RiftTracker_Draw(gTasks[taskId].data[0], gTasks[taskId].data[1], gTasks[taskId].data[2]);
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
    else if (RiftTracker_IsActive() && gTasks[taskId].data[1] == 1 && JOY_NEW(DPAD_UP | DPAD_DOWN))
    {
        u32 count = RiftTracker_Count();
        gTasks[taskId].data[2] = (gTasks[taskId].data[2] + (JOY_NEW(DPAD_UP) ? count - 1 : 1)) % count;
        DrawJournal(taskId);
    }
    else if (JOY_NEW(DPAD_LEFT | DPAD_RIGHT | L_BUTTON | R_BUTTON))
    {
        gTasks[taskId].data[1] = (gTasks[taskId].data[1] + (JOY_NEW(DPAD_LEFT | L_BUTTON) ? 2 : 1)) % 3;
        DrawJournal(taskId);
    }
}

void AdventureJournal_Open(void)
{
    u8 win;
    LockPlayerFieldControls();
    FreezeObjectEvents();
    win = AddWindow(&sJournalWindow);
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
