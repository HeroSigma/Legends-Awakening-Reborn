#ifndef GUARD_CUSTOM_START_MENU_H
#define GUARD_CUSTOM_START_MENU_H
#include "global.h"
#include "constants/vars.h"
#define VAR_LEGENDS_MENU_THEME VAR_UNUSED_0x40F7
#define LEGENDS_MENU_THEME_COUNT 4
bool32 CustomStartMenu_Open(const u8 *icons, u8 count, u8 cursor, const u8 *label, u8 page);
void CustomStartMenu_Select(u8 cursor, const u8 *label);
void CustomStartMenu_Close(void);
bool32 CustomStartMenu_IsActive(void);
u8 CustomStartMenu_GetTheme(void);
void CustomStartMenu_SetTheme(u8 theme);
#endif
