// Character palette parts adapted from kyphii's feature/dynpal design.
// Original sprite indices and the save layout remain authoritative.
#include "global.h"
#include "dynamic_palettes.h"
#include "data.h"
#include "event_data.h"
#include "field_player_avatar.h"
#include "field_weather.h"
#include "graphics.h"
#include "malloc.h"
#include "main.h"
#include "menu.h"
#include "palette.h"
#include "sound.h"
#include "sprite.h"
#include "string_util.h"
#include "text.h"
#include "trainer_pokemon_sprites.h"
#include "trainer.h"
#include "window.h"
#include "bg.h"
#include "constants/event_objects.h"
#include "constants/rgb.h"
#include "constants/songs.h"
#include "constants/trainers.h"

#define COLOR_SIGNATURE 0xA000
#define COLOR_WINDOW_WIDTH 11
#define COLOR_WINDOW_HEIGHT 12
#define COLOR_INTRO_BASE 0x6D
STATIC_ASSERT(COLOR_INTRO_BASE + COLOR_WINDOW_WIDTH * COLOR_WINDOW_HEIGHT <= 0xF3, ColorPickerBeforeIntroFrames);
static EWRAM_DATA u16 sIntroSelection;
static EWRAM_DATA bool8 sInIntro;
static EWRAM_DATA u16 ALIGNED(4) sPalette[16];
struct PaletteMenu
{
    TaskFunc done, cancel;
    u16 original;
    u8 window, cursor, preview;
    bool8 field;
};
static EWRAM_DATA struct PaletteMenu *sMenu;
static const u16 sSkin[][4] = {
    {0,0,0,0},
    {RGB(31,27,24),RGB(29,22,18),RGB(24,16,12),RGB(15,9,7)},
    {RGB(27,20,14),RGB(24,16,10),RGB(19,11,7),RGB(12,6,4)},
    {RGB(20,13,10),RGB(16,9,7),RGB(12,6,5),RGB(8,3,3)},
};
static const u16 sColors[][2] = {
    {0,0},
    {RGB(9,24,29), RGB(4,15,22)}, // blue
    {RGB(30,11,10),RGB(21,5,7)},  // red
    {RGB(24,14,30),RGB(14,7,22)}, // violet
    {RGB(31,24,8),RGB(23,15,4)},  // gold
    {RGB(29,30,31),RGB(20,23,26)},// white
    {RGB(11,13,17),RGB(5,7,10)},  // charcoal
    {RGB(31,15,24),RGB(23,7,15)}, // pink
};
static const u8 *const sSkinNames[] = {COMPOUND_STRING("Original"),COMPOUND_STRING("Light"),COMPOUND_STRING("Tan"),COMPOUND_STRING("Deep")};
static const u8 *const sColorNames[] = {COMPOUND_STRING("Original"),COMPOUND_STRING("Blue"),COMPOUND_STRING("Red"),COMPOUND_STRING("Violet"),COMPOUND_STRING("Gold"),COMPOUND_STRING("White"),COMPOUND_STRING("Charcoal"),COMPOUND_STRING("Pink")};
static const u8 *const sLabels[] = {COMPOUND_STRING("Skin tone"),COMPOUND_STRING("Outfit"),COMPOUND_STRING("Accent")};

static u16 Validate(u16 choice)
{
    if ((choice & 0xF000) != COLOR_SIGNATURE)
        return 0;
    if ((choice & 15) >= DYNAMIC_PAL_SKIN_COUNT) choice &= ~15;
    if (((choice >> 4) & 15) >= DYNAMIC_PAL_COLOR_COUNT) choice &= ~0xF0;
    if (((choice >> 8) & 15) >= DYNAMIC_PAL_COLOR_COUNT) choice &= ~0xF00;
    return choice & 0xFFF;
}
u16 __attribute__((noinline, noclone)) DynamicPal_GetSelection(void)
{
    return sInIntro ? sIntroSelection : Validate(VarGet(VAR_LA_PLAYER_COLORS));
}
void DynamicPal_SetSelection(u16 selection)
{
    selection = Validate(COLOR_SIGNATURE | (selection & 0xFFF));
    if (sInIntro) sIntroSelection = selection;
    else VarSet(VAR_LA_PLAYER_COLORS, selection ? COLOR_SIGNATURE | selection : 0);
}
void DynamicPal_BeginIntro(void) {sInIntro = TRUE;sIntroSelection = 0;}
void DynamicPal_EndIntro(void) {sInIntro = FALSE;sIntroSelection = 0;}
bool32 DynamicPal_IsIntro(void) {return sInIntro;}
void DynamicPal_CommitIntro(void)
{
    u16 selection = sInIntro ? sIntroSelection : 0;
    sInIntro = FALSE;
    DynamicPal_SetSelection(selection);
    sIntroSelection = 0;
}
static const u16 *Build(const u16 *base, const u8 *skin, const u8 *outfit, const u8 *accent, u32 skinCount)
{
    u16 choice = DynamicPal_GetSelection();
    if (!choice) return base;
    CpuCopy16(base, sPalette, PLTT_SIZE_4BPP);
    u32 tone = choice & 15, clothes = (choice >> 4) & 15, trim = (choice >> 8) & 15;
    if (tone) for (u32 i=0;i<skinCount;i++) sPalette[skin[i]] = sSkin[tone][i];
    if (clothes) for (u32 i=0;i<2;i++) sPalette[outfit[i]] = sColors[clothes][i];
    if (trim) for (u32 i=0;i<2;i++) sPalette[accent[i]] = sColors[trim][i];
    return sPalette;
}
static const u16 *Standard(const u16 *base)
{
    static const u8 skin[]={1,2,3,4},outfit[]={10,11},accent[]={12,13};
    return Build(base,skin,outfit,accent,4);
}
const u16 *DynamicPal_ObjectPalette(u16 tag, const u16 *base)
{
    if (tag == OBJ_EVENT_PAL_TAG_AREN || tag == OBJ_EVENT_PAL_TAG_ARIA || tag == OBJ_EVENT_PAL_TAG_PLAYER_UNDERWATER)
        return Standard(base);
    return base;
}
const u16 *DynamicPal_TrainerPalette(u32 pic, bool32 front)
{
    const u16 *base = front ? GetTrainerFrontPicPalette(pic) : GetTrainerBackPicPalette(pic);
    if ((pic == TRAINER_PIC_BRENDAN || pic == TRAINER_PIC_MAY)
     && (sInIntro || pic == (gSaveBlock2Ptr->playerGender == MALE ? TRAINER_PIC_BRENDAN : TRAINER_PIC_MAY)))
        return Standard(base);
    return base;
}
const u16 *DynamicPal_MugshotPalette(const u16 *base, u32 gender)
{
    static const u8 skin[2][3]={{4,6,7},{4,5,7}};
    static const u8 outfit[2][2]={{9,5},{11,10}},accent[2][2]={{11,10},{12,9}};
    gender = gender == FEMALE;
    return Build(base,skin[gender],outfit[gender],accent[gender],3);
}
static void RefreshPlayer(void)
{
    u32 gender = gSaveBlock2Ptr->playerGender == FEMALE;
    u8 slot = gSprites[gPlayerAvatar.spriteId].oam.paletteNum;
    const u16 *base = gender ? gObjectEventPal_May : gObjectEventPal_Brendan;
    LoadPalette(Standard(base),OBJ_PLTT_ID(slot),PLTT_SIZE_4BPP);
    UpdateSpritePaletteWithWeather(slot,FALSE);
}
static void DrawMenu(void)
{
    static const u8 colors[]={1,2,3};
    u8 win = sMenu->window;
    u16 choice = DynamicPal_GetSelection();
    FillWindowPixelBuffer(win,PIXEL_FILL(1));
    for (u32 i=0;i<3;i++)
    {
        u32 value = (choice >> (i*4)) & 15;
        AddTextPrinterParameterized4(win,FONT_SMALL,10,i*32,0,0,colors,TEXT_SKIP_DRAW,sLabels[i]);
        AddTextPrinterParameterized4(win,FONT_NORMAL,16,i*32+14,0,0,colors,TEXT_SKIP_DRAW,i?sColorNames[value]:sSkinNames[value]);
        if (sMenu->cursor==i) AddTextPrinterParameterized4(win,FONT_NORMAL,0,i*32+14,0,0,colors,TEXT_SKIP_DRAW,COMPOUND_STRING(">"));
    }
    CopyWindowToVram(win,COPYWIN_FULL);
    if (sMenu->preview < MAX_SPRITES)
    {
        u32 pic = gSaveBlock2Ptr->playerGender == FEMALE ? TRAINER_PIC_MAY : TRAINER_PIC_BRENDAN;
        LoadPalette(DynamicPal_TrainerPalette(pic,TRUE),OBJ_PLTT_ID(gSprites[sMenu->preview].oam.paletteNum),PLTT_SIZE_4BPP);
    }
    if (sMenu->field) RefreshPlayer();
}
static void CloseMenu(u8 taskId, bool32 accepted)
{
    TaskFunc next = accepted ? sMenu->done : sMenu->cancel;
    if (!accepted)
    {
        DynamicPal_SetSelection(sMenu->original);
        if (sMenu->preview < MAX_SPRITES)
            LoadPalette(DynamicPal_TrainerPalette(gSaveBlock2Ptr->playerGender==FEMALE?TRAINER_PIC_MAY:TRAINER_PIC_BRENDAN,TRUE),OBJ_PLTT_ID(gSprites[sMenu->preview].oam.paletteNum),PLTT_SIZE_4BPP);
    }
    if (sMenu->field) RefreshPlayer();
    ClearStdWindowAndFrameToTransparent(sMenu->window,TRUE);
    RemoveWindow(sMenu->window);
    if (sMenu->field && sMenu->preview<MAX_SPRITES) FreeAndDestroyTrainerPicSprite(sMenu->preview);
    FREE_AND_SET_NULL(sMenu);
    gTasks[taskId].func = next;
}
static void Task_DynamicPalMenu(u8 taskId)
{
    if (JOY_NEW(B_BUTTON)) {PlaySE(SE_SELECT);CloseMenu(taskId,FALSE);return;}
    if (JOY_NEW(A_BUTTON | START_BUTTON)) {PlaySE(SE_SELECT);CloseMenu(taskId,TRUE);return;}
    if (JOY_NEW(DPAD_UP)) {sMenu->cursor=(sMenu->cursor+2)%3;DrawMenu();}
    else if (JOY_NEW(DPAD_DOWN)) {sMenu->cursor=(sMenu->cursor+1)%3;DrawMenu();}
    else if (JOY_NEW(DPAD_LEFT | DPAD_RIGHT))
    {
        u32 shift=sMenu->cursor*4;
        u32 count=sMenu->cursor?DYNAMIC_PAL_COLOR_COUNT:DYNAMIC_PAL_SKIN_COUNT;
        u16 choice=DynamicPal_GetSelection();
        u32 value=(((choice>>shift)&15)+ (JOY_NEW(DPAD_RIGHT)?1:count-1))%count;
        DynamicPal_SetSelection((choice & ~(15<<shift)) | (value<<shift));
        PlaySE(SE_SELECT);DrawMenu();
    }
}
void DynamicPal_ShowMenu(u8 taskId, TaskFunc done, TaskFunc cancel, u8 previewSprite, bool32 field)
{
    struct WindowTemplate win={.bg=0,.tilemapLeft=2,.tilemapTop=1,.width=COLOR_WINDOW_WIDTH,.height=COLOR_WINDOW_HEIGHT,.paletteNum=15,.baseBlock=field ? 0x230 : COLOR_INTRO_BASE};
    if (sMenu) {gTasks[taskId].func=cancel;return;}
    sMenu=AllocZeroed(sizeof(*sMenu));
    if (!sMenu) {gTasks[taskId].func=cancel;return;}
    sMenu->window=AddWindow(&win);
    if (sMenu->window==WINDOW_NONE) {FREE_AND_SET_NULL(sMenu);gTasks[taskId].func=cancel;return;}
    sMenu->done=done;sMenu->cancel=cancel;sMenu->original=DynamicPal_GetSelection();sMenu->preview=previewSprite;sMenu->field=field;
    if (field)
    {
        u32 pic=gSaveBlock2Ptr->playerGender==FEMALE?TRAINER_PIC_MAY:TRAINER_PIC_BRENDAN;
        sMenu->preview=CreateTrainerPicSprite(pic,TRUE,184,62,0,GetTrainerPicTag(pic,TRUE));
    }
    if (field) SetStandardWindowBorderStyle(sMenu->window,FALSE);
    else DrawStdFrameWithCustomTileAndPalette(sMenu->window,FALSE,0xF3,2);
    PutWindowTilemap(sMenu->window);
    DrawMenu();
    gTasks[taskId].func=Task_DynamicPalMenu;
}
