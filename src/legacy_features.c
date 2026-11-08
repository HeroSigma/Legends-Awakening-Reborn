#include "global.h"
#include "legacy_features.h"
#include "script.h"
#include "task.h"

#if LA_FREE_SPACE
static void Task_ResumeDisabledFeature(u8 taskId)
{
    ScriptContext_Enable();
    DestroyTask(taskId);
}

// Disabled asynchronous specials must still complete their caller's waitstate.
void LegacyFeature_ResumeScript(void)
{
    CreateTask(Task_ResumeDisabledFeature, 0);
}
#else
void LegacyFeature_ResumeScript(void) {}
#endif
