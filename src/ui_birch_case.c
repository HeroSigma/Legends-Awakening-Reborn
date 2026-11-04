// Briefcase artwork by Mudskip; UI design by Archie, Team Aqua.
// Selection-only adaptation: the native rescue callback owns the reward/battle.
#include "global.h"
#include "bg.h"
#include "battle_main.h"
#include "data.h"
#include "decompress.h"
#include "gpu_regs.h"
#include "main.h"
#include "malloc.h"
#include "menu.h"
#include "menu_helpers.h"
#include "palette.h"
#include "pokemon.h"
#include "scanline_effect.h"
#include "sound.h"
#include "sprite.h"
#include "starter_choose.h"
#include "string_util.h"
#include "task.h"
#include "text.h"
#include "trainer_pokemon_sprites.h"
#include "trig.h"
#include "window.h"
#include "text_window.h"
#include "overworld.h"
#include "event_data.h"
#include "constants/rgb.h"
#include "constants/songs.h"

#define CASE_SPRITE_TAG 20001
struct StarterCase
{
    MainCallback callback;
    u16 *caseMap, *barMap;
    u8 selected, balls[3], hand, mon, phase;
    bool8 confirming;
};
static EWRAM_DATA struct StarterCase *sStarterCase;
static const u32 sCaseTiles[] = INCGFX_U32("graphics/ui_birch_case/case_tiles.png", ".4bpp.smol");
static const u32 sCaseMap[] = INCGFX_U32("graphics/ui_birch_case/case_tiles.bin", ".smolTM");
static const u16 sCasePal[] = INCGFX_U16("graphics/ui_birch_case/case_tiles.pal", ".gbapal");
static const u32 sBarTiles[] = INCGFX_U32("graphics/ui_birch_case/text_bg_tiles.png", ".4bpp.smol");
static const u32 sBarMap[] = INCGFX_U32("graphics/ui_birch_case/text_bg_tiles.bin", ".smolTM");
static const u16 sBarPal[] = INCGFX_U16("graphics/ui_birch_case/text_bg_tiles.pal", ".gbapal");
static const u32 sBallTiles[] = INCGFX_U32("graphics/ui_birch_case/pokeball_hand.png", ".4bpp.smol");
static const u16 sBallPal[] = INCGFX_U16("graphics/ui_birch_case/pokeball_hand.pal", ".gbapal");
static const struct CompressedSpriteSheet sSheet={sBallTiles,2048,CASE_SPRITE_TAG};
static const struct SpritePalette sPal={sBallPal,CASE_SPRITE_TAG};
static const struct OamData sOam={.shape=SPRITE_SHAPE(32x32),.size=SPRITE_SIZE(32x32),.priority=1};
static const union AnimCmd sBallStill[]={ANIMCMD_FRAME(0,32),ANIMCMD_JUMP(0)};
static const union AnimCmd sBallRock[]={ANIMCMD_FRAME(0,16),ANIMCMD_FRAME(16,16),ANIMCMD_FRAME(0,16),ANIMCMD_FRAME(32,16),ANIMCMD_JUMP(0)};
static const union AnimCmd sHandAnim[]={ANIMCMD_FRAME(48,32),ANIMCMD_JUMP(0)};
static const union AnimCmd *const sAnims[]={sBallStill,sBallRock,sHandAnim};
static const struct SpriteTemplate sTemplate={.tileTag=CASE_SPRITE_TAG,.paletteTag=CASE_SPRITE_TAG,.oam=&sOam,.anims=sAnims,.images=NULL,.affineAnims=gDummySpriteAffineAnimTable,.callback=SpriteCallbackDummy};
static const struct BgTemplate sBgs[]={
    {.bg=0,.charBaseIndex=0,.mapBaseIndex=31,.priority=0},
    {.bg=1,.charBaseIndex=3,.mapBaseIndex=30,.priority=2},
    {.bg=2,.charBaseIndex=2,.mapBaseIndex=28,.priority=1},
};
static const struct WindowTemplate sWindows[]={
    {.bg=0,.tilemapLeft=0,.tilemapTop=14,.width=30,.height=6,.paletteNum=15,.baseBlock=1},DUMMY_WIN_TEMPLATE,
};
static void Case_VBlank(void) {LoadOam();ProcessSpriteCopyRequests();TransferPlttBuffer();}
static void Case_Main(void) {RunTasks();AnimateSprites();BuildOamBuffer();DoScheduledBgTilemapCopiesToVram();UpdatePaletteFade();}
static void Case_Hand(struct Sprite *sprite)
{
    sprite->data[0]=(sprite->data[0]+1)&63;
    sprite->y2=Sin(sprite->data[0]*4,2);
}
static void Case_Text(void)
{
    static const u8 colors[]={0,TEXT_COLOR_WHITE,TEXT_COLOR_DARK_GRAY};
    u16 species=GetStarterPokemon(sStarterCase->selected);
    u32 type1=gSpeciesInfo[species].types[0],type2=gSpeciesInfo[species].types[1];
    u8 text[80];
    FillWindowPixelBuffer(0,PIXEL_FILL(0));
    if (sStarterCase->confirming)
    {
        StringCopy(gStringVar1,GetSpeciesName(species));
        StringExpandPlaceholders(text,COMPOUND_STRING("Choose {STR_VAR_1}?"));
        AddTextPrinterParameterized4(0,FONT_NORMAL,5,3,0,0,colors,TEXT_SKIP_DRAW,text);
        AddTextPrinterParameterized4(0,FONT_SMALL,5,25,0,0,colors,TEXT_SKIP_DRAW,COMPOUND_STRING("A: Yes   B: Back"));
    }
    else
    {
        AddTextPrinterParameterized4(0,FONT_NORMAL,5,3,0,0,colors,TEXT_SKIP_DRAW,GetSpeciesName(species));
        StringCopy(text,gTypesInfo[type1].name);
        if (type2!=type1) {StringAppend(text,COMPOUND_STRING(" / "));StringAppend(text,gTypesInfo[type2].name);}
        AddTextPrinterParameterized4(0,FONT_SMALL,5,19,0,0,colors,TEXT_SKIP_DRAW,text);
        AddTextPrinterParameterized4(0,FONT_SMALL,5,33,0,0,colors,TEXT_SKIP_DRAW,COMPOUND_STRING("Left/Right: browse   A: choose"));
    }
    PutWindowTilemap(0);CopyWindowToVram(0,COPYWIN_FULL);
}
static void Case_Refresh(void)
{
    for (u32 i=0;i<3;i++)
        if (sStarterCase->balls[i]<MAX_SPRITES) StartSpriteAnim(&gSprites[sStarterCase->balls[i]],i==sStarterCase->selected?1:0);
    if (sStarterCase->hand<MAX_SPRITES) gSprites[sStarterCase->hand].x=64+sStarterCase->selected*56;
    if (sStarterCase->mon<MAX_SPRITES) FreeAndDestroyMonPicSprite(sStarterCase->mon);
    sStarterCase->mon=CreateMonPicSprite(GetStarterPokemon(sStarterCase->selected),FALSE,0x8000,TRUE,208,104,5,TAG_NONE);
    if (sStarterCase->mon<MAX_SPRITES) gSprites[sStarterCase->mon].oam.priority=0;
    Case_Text();
}
static void Case_Free(void)
{
    if (!sStarterCase) return;
    if (sStarterCase->mon<MAX_SPRITES) FreeAndDestroyMonPicSprite(sStarterCase->mon);
    for(u32 i=0;i<3;i++) if (sStarterCase->balls[i]<MAX_SPRITES) DestroySprite(&gSprites[sStarterCase->balls[i]]);
    if (sStarterCase->hand<MAX_SPRITES) DestroySprite(&gSprites[sStarterCase->hand]);
    FreeSpriteTilesByTag(CASE_SPRITE_TAG);FreeSpritePaletteByTag(CASE_SPRITE_TAG);
    FreeAllWindowBuffers();UnsetBgTilemapBuffer(0);UnsetBgTilemapBuffer(1);UnsetBgTilemapBuffer(2);
    FREE_AND_SET_NULL(sStarterCase->caseMap);FREE_AND_SET_NULL(sStarterCase->barMap);FREE_AND_SET_NULL(sStarterCase);
}
static void Task_StarterCase(u8 taskId)
{
    if (gPaletteFade.active) return;
    if (sStarterCase->phase)
    {
        MainCallback next=sStarterCase->callback;
        Case_Free();DestroyTask(taskId);SetMainCallback2(next);return;
    }
    if (JOY_NEW(A_BUTTON))
    {
        PlaySE(SE_SELECT);
        if (!sStarterCase->confirming)
        {
            sStarterCase->confirming=TRUE;PlayCry_Normal(GetStarterPokemon(sStarterCase->selected),0);Case_Text();
        }
        else
        {
            gSpecialVar_Result=sStarterCase->selected;sStarterCase->phase=1;
            BeginNormalPaletteFade(PALETTES_ALL,0,0,16,RGB_BLACK);
        }
    }
    else if (JOY_NEW(B_BUTTON) && sStarterCase->confirming)
    {
        PlaySE(SE_SELECT);sStarterCase->confirming=FALSE;Case_Text();
    }
    else if (!sStarterCase->confirming && JOY_NEW(DPAD_LEFT|DPAD_RIGHT))
    {
        PlaySE(SE_SELECT);sStarterCase->selected=(sStarterCase->selected+(JOY_NEW(DPAD_RIGHT)?1:2))%3;Case_Refresh();
    }
}
static void Case_Load(void)
{
    switch (gMain.state)
    {
    case 0:
        ResetTempTileDataBuffers();
        DecompressAndCopyTileDataToVram(1,sCaseTiles,0,0,0);DecompressAndCopyTileDataToVram(2,sBarTiles,0,0,0);
        gMain.state++;break;
    case 1:
        if (FreeTempTileDataBuffersIfPossible()) return;
        DecompressDataWithHeaderWram(sCaseMap,sStarterCase->caseMap);DecompressDataWithHeaderWram(sBarMap,sStarterCase->barMap);
        CopyBgTilemapBufferToVram(1);CopyBgTilemapBufferToVram(2);
        LoadPalette(sCasePal,32,sizeof(sCasePal));LoadPalette(sBarPal,16,sizeof(sBarPal));
        LoadPalette(GetOverworldTextboxPalettePtr(),BG_PLTT_ID(15),PLTT_SIZE_4BPP);
        LoadCompressedSpriteSheet(&sSheet);LoadSpritePalette(&sPal);
        for(u32 i=0;i<3;i++) sStarterCase->balls[i]=CreateSprite(&sTemplate,64+i*56,58,1);
        sStarterCase->hand=CreateSprite(&sTemplate,120,52,0);
        if(sStarterCase->hand<MAX_SPRITES) {StartSpriteAnim(&gSprites[sStarterCase->hand],2);gSprites[sStarterCase->hand].callback=Case_Hand;}
        Case_Refresh();BeginNormalPaletteFade(PALETTES_ALL,0,16,0,RGB_BLACK);
        CreateTask(Task_StarterCase,0);SetVBlankCallback(Case_VBlank);SetMainCallback2(Case_Main);break;
    }
}
void CB2_ChooseStarter(void)
{
    MainCallback next=gMain.savedCallback;
    SetVBlankCallback(NULL);SetHBlankCallback(NULL);SetGpuReg(REG_OFFSET_DISPCNT,0);
    CleanupOverworldWindowsAndTilemaps();ScanlineEffect_Stop();ResetTasks();ResetSpriteData();ResetAllPicSprites();FreeAllSpritePalettes();ResetPaletteFade();
    sStarterCase=AllocZeroed(sizeof(*sStarterCase));
    if (!sStarterCase) {gSpecialVar_Result=1;SetVBlankCallback(Case_VBlank);SetMainCallback2(next);return;}
    sStarterCase->callback=next;sStarterCase->selected=1;sStarterCase->hand=SPRITE_NONE;sStarterCase->mon=SPRITE_NONE;
    for(u32 i=0;i<3;i++) sStarterCase->balls[i]=SPRITE_NONE;
    sStarterCase->caseMap=AllocZeroed(BG_SCREEN_SIZE);sStarterCase->barMap=AllocZeroed(BG_SCREEN_SIZE);
    if(!sStarterCase->caseMap || !sStarterCase->barMap) {gSpecialVar_Result=1;Case_Free();SetVBlankCallback(Case_VBlank);SetMainCallback2(next);return;}
    DmaFill16(3,0,(void *)VRAM,VRAM_SIZE);DmaFill32(3,0,(void *)OAM,OAM_SIZE);
    ResetBgsAndClearDma3BusyFlags(0);InitBgsFromTemplates(0,sBgs,ARRAY_COUNT(sBgs));ResetAllBgsCoordinates();
    SetBgTilemapBuffer(1,sStarterCase->caseMap);SetBgTilemapBuffer(2,sStarterCase->barMap);InitWindows(sWindows);DeactivateAllTextPrinters();
    SetGpuReg(REG_OFFSET_WIN0H,0);SetGpuReg(REG_OFFSET_WIN0V,0);SetGpuReg(REG_OFFSET_WININ,0);SetGpuReg(REG_OFFSET_WINOUT,0);
    SetGpuReg(REG_OFFSET_BLDCNT,BLDCNT_TGT2_ALL|BLDCNT_EFFECT_BLEND|BLDCNT_TGT1_BG2);SetGpuReg(REG_OFFSET_BLDALPHA,BLDALPHA_BLEND(1,8));SetGpuReg(REG_OFFSET_BLDY,0);
    SetGpuReg(REG_OFFSET_DISPCNT,DISPCNT_OBJ_ON|DISPCNT_OBJ_1D_MAP);ShowBg(0);ShowBg(1);ShowBg(2);
    gMain.state=0;SetMainCallback2(Case_Load);
}
