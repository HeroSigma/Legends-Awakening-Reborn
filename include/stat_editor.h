#ifndef GUARD_INCLUDE_STAT_EDITOR_H
#define GUARD_INCLUDE_STAT_EDITOR_H

#include "main.h"
#include "config/stat_editor.h"

void Task_OpenStatEditorFromStartMenu(u8 taskId);
void StatEditor_Init(MainCallback callback);
void StatEditor_ReturnToSummary(void);

#endif // GUARD_INCLUDE_STAT_EDITOR_H
