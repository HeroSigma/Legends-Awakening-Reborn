// Wardrobe layout/preview concept and background by Mudskip, adapted to LA's
// outfit variables, unified trainer pictures and dynamic player palettes.
#include "global.h"
#include "outfit_box.h"
#include "dynamic_palettes.h"
#include "bg.h"
#include "data.h"
#include "decompress.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "gpu_regs.h"
#include "graphics.h"
#include "item.h"
#include "main.h"
#include "malloc.h"
#include "menu.h"
#include "overworld.h"
#include "palette.h"
#include "scanline_effect.h"
#include "sound.h"
#include "sprite.h"
#include "string_util.h"
#include "task.h"
#include "text.h"
#include "trainer.h"
#include "trainer_pokemon_sprites.h"
#include "window.h"
#include "constants/event_objects.h"
#include "constants/event_object_movement.h"
#include "constants/flags.h"
#include "constants/items.h"
#include "constants/rgb.h"
#include "constants/songs.h"
#include "constants/trainers.h"

struct OutfitBox
{
    u16 tilemap[0x400];
    u16 originalColors, colors;
    u8 originalStyle, style, top, colorRow;
    u8 front, back, avatars[4];
    bool8 colorMode;
};
static EWRAM_DATA struct OutfitBox *sBox;
static const u32 sTiles[] = INCGFX_U32("graphics/outfit_menu/main.png", ".4bpp.smol");
static const u16 sPalette[] = INCBIN_U16("graphics/outfit_menu/main.gbapal");
static const u16 sTilemap[] = INCBIN_U16("graphics/outfit_menu/main.bin");
static const struct BgTemplate sBgs[] = {
    {.bg=0,.charBaseIndex=1,.mapBaseIndex=28,.priority=0},
    {.bg=1,.charBaseIndex=0,.mapBaseIndex=30,.priority=1},
};
static const struct WindowTemplate sWindows[] = {
    {.bg=0,.tilemapLeft=1,.tilemapTop=14,.width=24,.height=6,.paletteNum=15,.baseBlock=1},
    DUMMY_WIN_TEMPLATE,
};
static const u16 sTextPalette[] = {RGB(16,7,8),RGB_WHITE,RGB(7,23,25),RGB(4,13,15)};
static const u8 *const sLabels[] = {COMPOUND_STRING("Skin"),COMPOUND_STRING("Clothes"),COMPOUND_STRING("Accent")};
static const u8 *const sDescriptions[2][PLAYER_OUTFIT_STYLE_COUNT] = {
    {COMPOUND_STRING("Your original Hoenn outfit."),COMPOUND_STRING("A classic Hoenn adventure look."),COMPOUND_STRING("A red vest with white sleeves."),COMPOUND_STRING("A gold jacket for the road."),COMPOUND_STRING("A dark jacket with red trim.")},
    {COMPOUND_STRING("Your original Hoenn outfit."),COMPOUND_STRING("A classic Hoenn adventure look."),COMPOUND_STRING("A blue top and bright skirt."),COMPOUND_STRING("Overalls for a Johto adventure."),COMPOUND_STRING("A sporty jacket and shorts.")},
};
static void CB2_OutfitBoxSetup(void);
static void Task_OutfitBox(u8 taskId);
static void CB2_OutfitBox(void)
{
    RunTasks(); AnimateSprites(); BuildOamBuffer();
    DoScheduledBgTilemapCopiesToVram(); UpdatePaletteFade();
}
static void VBlank_OutfitBox(void)
{
    LoadOam(); ProcessSpriteCopyRequests(); TransferPlttBuffer();
}
static void Print(const u8 *text, u32 x, u32 y)
{
    static const u8 colors[] = {TEXT_COLOR_TRANSPARENT,1,3};
    AddTextPrinterParameterized4(0,FONT_SMALL,x,y,0,0,colors,TEXT_SKIP_DRAW,text);
}
static void DrawInfo(void)
{
    u32 gender=gSaveBlock2Ptr->playerGender==FEMALE;
    FillWindowPixelBuffer(0,PIXEL_FILL(0));
    if (sBox->colorMode)
    {
        for (u32 i=0;i<3;i++)
        {
            Print(sLabels[i],12,i*12);
            Print(DynamicPal_ColorName((sBox->colors>>(i*4))&15,i==0),72,i*12);
            if (i==sBox->colorRow) Print(COMPOUND_STRING(">"),0,i*12);
        }
        Print(COMPOUND_STRING("Left/Right: change  B: back"),0,36);
    }
    else
    {
        Print(PlayerOutfit_Name(gender,sBox->style),0,0);
        if (sBox->style==sBox->originalStyle) Print(COMPOUND_STRING("Worn"),145,0);
        Print(sDescriptions[gender][sBox->style],0,14);
        Print(COMPOUND_STRING("R: colors   A: wear   B: cancel"),0,30);
    }
    PutWindowTilemap(0); CopyWindowToVram(0,COPYWIN_FULL);
}
static void SpriteCB_OutfitAvatar(struct Sprite *sprite)
{
    StartSpriteAnimIfDifferent(sprite,sprite->data[0]==sBox->style ? ANIM_STD_GO_SOUTH : ANIM_STD_FACE_SOUTH);
    sprite->x2 = sprite->data[0]==sBox->style ? -3 : 0;
}
static void DestroyPreviews(void)
{
    if (sBox->front<MAX_SPRITES) FreeAndDestroyTrainerPicSprite(sBox->front);
    if (sBox->back<MAX_SPRITES) FreeAndDestroyTrainerPicSprite(sBox->back);
    // Object preview templates are temporary; DestroySprite releases their
    // untagged image tiles without dereferencing the freed template pointer.
    for (u32 i=0;i<4;i++)
        if (sBox->avatars[i]<MAX_SPRITES) DestroySprite(&gSprites[sBox->avatars[i]]);
    sBox->front=sBox->back=SPRITE_NONE;
    memset(sBox->avatars,SPRITE_NONE,sizeof(sBox->avatars));
}
static void RefreshPreviews(void)
{
    u32 gender=gSaveBlock2Ptr->playerGender==FEMALE, pic;
    u16 savedColors=DynamicPal_GetSelection();
    u32 savedStyle=PlayerOutfit_Get();
    DestroyPreviews();
    // Resolvers read existing variables. Restore them within this call: browsing
    // never commits an outfit, and a later B leaves the save untouched.
    DynamicPal_SetSelection(sBox->colors);
    PlayerOutfit_Set(sBox->style);
    pic=PlayerOutfit_TrainerPic(gender ? TRAINER_PIC_MAY : TRAINER_PIC_BRENDAN);
    sBox->front=CreateTrainerPicSprite(pic,TRUE,59,64,9,TAG_NONE);
    sBox->back=CreateTrainerPicSprite(pic,FALSE,149,64,10,TAG_NONE);
    if (sBox->front<MAX_SPRITES)
        LoadPalette(DynamicPal_TrainerPalette(pic,TRUE),OBJ_PLTT_ID(9),PLTT_SIZE_4BPP);
    if (sBox->back<MAX_SPRITES)
        LoadPalette(DynamicPal_TrainerPalette(pic,FALSE),OBJ_PLTT_ID(10),PLTT_SIZE_4BPP);
    for (u32 i=0;i<4 && sBox->top+i<PLAYER_OUTFIT_STYLE_COUNT;i++)
    {
        u32 style=sBox->top+i;
        u8 id;
        PlayerOutfit_Set(style);
        id=CreateObjectGraphicsSprite(gender ? OBJ_EVENT_GFX_MAY_NORMAL : OBJ_EVENT_GFX_BRENDAN_NORMAL,SpriteCB_OutfitAvatar,224,35+i*32,0);
        sBox->avatars[i]=id;
        if (id>=MAX_SPRITES) continue;
        gSprites[id].data[0]=style;
        gSprites[id].oam.paletteNum=4+i;
        gSprites[id].oam.priority=0;
        LoadPalette(DynamicPal_ObjectPalette(gender ? OBJ_EVENT_PAL_TAG_ARIA : OBJ_EVENT_PAL_TAG_AREN,gender ? gObjectEventPal_May : gObjectEventPal_Brendan),OBJ_PLTT_ID(4+i),PLTT_SIZE_4BPP);
    }
    PlayerOutfit_Set(savedStyle);
    DynamicPal_SetSelection(savedColors);
    DrawInfo();
}
static void Task_OutfitBoxClose(u8 taskId)
{
    if (gPaletteFade.active) return;
    SetVBlankCallback(NULL);
    DestroyPreviews(); FreeAllSpritePalettes(); FreeAllWindowBuffers();
    UnsetBgTilemapBuffer(1);
    FREE_AND_SET_NULL(sBox);
    DestroyTask(taskId);
    gFieldCallback=NULL;
    SetMainCallback2(CB2_ReturnToFieldFadeFromBlack);
}
static void CloseBox(u8 taskId, bool32 accepted)
{
    if (accepted)
    {
        PlayerOutfit_Set(sBox->style);
        DynamicPal_SetSelection(sBox->colors);
    }
    PlaySE(SE_SELECT);
    BeginNormalPaletteFade(PALETTES_ALL,0,0,16,RGB_BLACK);
    gTasks[taskId].func=Task_OutfitBoxClose;
}
static void Task_OutfitBox(u8 taskId)
{
    if (gPaletteFade.active) return;
    if (JOY_NEW(A_BUTTON | START_BUTTON)) {CloseBox(taskId,TRUE);return;}
    if (JOY_NEW(B_BUTTON))
    {
        if (sBox->colorMode) {sBox->colorMode=FALSE;DrawInfo();}
        else CloseBox(taskId,FALSE);
        return;
    }
    if (JOY_NEW(L_BUTTON | R_BUTTON))
    {
        sBox->colorMode=!sBox->colorMode;
        PlaySE(SE_SELECT);DrawInfo();return;
    }
    if (sBox->colorMode)
    {
        if (JOY_NEW(DPAD_UP | DPAD_DOWN))
            sBox->colorRow=(sBox->colorRow+(JOY_NEW(DPAD_UP)?2:1))%3;
        else if (JOY_NEW(DPAD_LEFT | DPAD_RIGHT))
        {
            u32 shift=sBox->colorRow*4,count=sBox->colorRow?DYNAMIC_PAL_COLOR_COUNT:DYNAMIC_PAL_SKIN_COUNT;
            u32 value=(((sBox->colors>>shift)&15)+(JOY_NEW(DPAD_RIGHT)?1:count-1))%count;
            sBox->colors=(sBox->colors&~(15<<shift))|(value<<shift);
            RefreshPreviews();
        }
        else return;
    }
    else if (JOY_NEW(DPAD_UP | DPAD_DOWN))
    {
        sBox->style=(sBox->style+(JOY_NEW(DPAD_UP)?PLAYER_OUTFIT_STYLE_COUNT-1:1))%PLAYER_OUTFIT_STYLE_COUNT;
        if (sBox->style<sBox->top) sBox->top=sBox->style;
        if (sBox->style>=sBox->top+4) sBox->top=sBox->style-3;
        RefreshPreviews();
    }
    else return;
    PlaySE(SE_SELECT);DrawInfo();
}
static void CB2_OutfitBoxSetup(void)
{
    switch (gMain.state)
    {
    case 0:
        SetVBlankCallback(NULL); SetHBlankCallback(NULL);
        SetGpuReg(REG_OFFSET_DISPCNT,0);
        ScanlineEffect_Stop();
        ResetTasks(); ResetSpriteData(); FreeAllSpritePalettes(); ResetPaletteFade();
        ClearScheduledBgCopiesToVram();
        CpuFill16(0,(void *)VRAM,VRAM_SIZE);
        ResetBgsAndClearDma3BusyFlags(0);
        for (u32 i=0;i<4;i++) {ChangeBgX(i,0,BG_COORD_SET);ChangeBgY(i,0,BG_COORD_SET);}
        InitBgsFromTemplates(0,sBgs,ARRAY_COUNT(sBgs));
        SetBgTilemapBuffer(1,sBox->tilemap);
        CpuCopy16(sTilemap,sBox->tilemap,sizeof(sTilemap));
        ScheduleBgCopyTilemapToVram(1);
        DecompressAndCopyTileDataToVram(1,sTiles,0,0,0);
        LoadPalette(sPalette,0,PLTT_SIZE_4BPP);
        LoadPalette(sTextPalette,BG_PLTT_ID(15),sizeof(sTextPalette));
        InitWindows(sWindows); DeactivateAllTextPrinters();
        gMain.state++;
        break;
    case 1:
        if (IsDma3ManagerBusyWithBgCopy()) return;
        RefreshPreviews();
        CreateTask(Task_OutfitBox,0);
        BlendPalettes(PALETTES_ALL,16,RGB_BLACK);
        BeginNormalPaletteFade(PALETTES_ALL,0,16,0,RGB_BLACK);
        SetGpuReg(REG_OFFSET_DISPCNT,DISPCNT_OBJ_ON | DISPCNT_OBJ_1D_MAP);
        ShowBg(0); ShowBg(1);
        SetVBlankCallback(VBlank_OutfitBox);
        SetMainCallback2(CB2_OutfitBox);
        break;
    }
}
void OutfitBox_Open(void)
{
    if (sBox) return;
    sBox=AllocZeroed(sizeof(*sBox));
    if (!sBox) {SetMainCallback2(CB2_ReturnToFieldFadeFromBlack);return;}
    sBox->originalStyle=sBox->style=PlayerOutfit_Get();
    sBox->originalColors=sBox->colors=DynamicPal_GetSelection();
    sBox->top=sBox->style>=4 ? sBox->style-3 : 0;
    sBox->front=sBox->back=SPRITE_NONE;
    memset(sBox->avatars,SPRITE_NONE,sizeof(sBox->avatars));
    SetMainCallback2(CB2_OutfitBoxSetup);
}
void OutfitBox_EnsureOwned(void)
{
    // New item is appended, so existing item IDs and save layout remain stable.
    if (FlagGet(FLAG_RECEIVED_RUNNING_SHOES) && !CheckBagHasItem(ITEM_OUTFIT_BOX,1))
        AddBagItem(ITEM_OUTFIT_BOX,1);
}
