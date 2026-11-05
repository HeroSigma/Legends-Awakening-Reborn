#ifndef GUARD_DYNAMIC_PALETTES_H
#define GUARD_DYNAMIC_PALETTES_H
#include "task.h"
#define DYNAMIC_PAL_SKIN_COUNT 4
#define DYNAMIC_PAL_COLOR_COUNT 8
u32 PlayerOutfit_Get(void);
void PlayerOutfit_Set(u32 outfit);
u32 PlayerOutfit_TrainerPic(u32 pic);
void DynamicPal_BeginIntro(void);
void DynamicPal_EndIntro(void);
void DynamicPal_CommitIntro(void);
bool32 DynamicPal_IsIntro(void);
u16 DynamicPal_GetSelection(void);
void DynamicPal_SetSelection(u16 selection);
const u16 *DynamicPal_ObjectPalette(u16 tag, const u16 *base);
const u16 *DynamicPal_TrainerPalette(u32 trainerPic, bool32 front);
const u16 *DynamicPal_MugshotPalette(const u16 *base, u32 gender);
void DynamicPal_ShowMenu(u8 taskId, TaskFunc done, TaskFunc cancel, u8 previewSprite, bool32 field);
#endif
