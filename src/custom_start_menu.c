#include "global.h"
#include "custom_start_menu.h"
#include "bg.h"
#include "decompress.h"
#include "event_data.h"
#include "malloc.h"
#include "menu.h"
#include "palette.h"
#include "rtc.h"
#include "sprite.h"
#include "string_util.h"
#include "text.h"
#include "text_window.h"
#include "window.h"
#include "constants/characters.h"
#define ICON_TAG 0x7E30
static const u32 sTiles[] = INCGFX_U32("graphics/legends_start_menu/bg.png", ".4bpp.smol");
static const u32 sMap[] = INCGFX_U32("graphics/legends_start_menu/bg.bin", ".smolTM");
static const u32 sIcons[] = INCGFX_U32("graphics/legends_start_menu/icons.png", ".4bpp.smol", "-mwidth 4 -mheight 4");
static const u16 sIconPalette[] = INCGFX_U16("graphics/legends_start_menu/icons.pal", ".gbapal");
static const u16 sPalettes[][16] = {
    INCGFX_U16("graphics/legends_start_menu/bg1.pal", ".gbapal"),
    INCGFX_U16("graphics/legends_start_menu/bg.pal", ".gbapal"),
    INCGFX_U16("graphics/legends_start_menu/bg2.pal", ".gbapal"),
    INCGFX_U16("graphics/legends_start_menu/bg3.pal", ".gbapal"),
};
static const struct CompressedSpriteSheet sSheet={sIcons,8192,ICON_TAG};
static const struct SpritePalette sPal={sIconPalette,ICON_TAG};
static const struct OamData sOam={.shape=SPRITE_SHAPE(32x32),.size=SPRITE_SIZE(32x32),.priority=0};
#define ANIM(i) static const union AnimCmd sAnim##i[]={ANIMCMD_FRAME((i)*16,0),ANIMCMD_END};
ANIM(0) ANIM(1) ANIM(2) ANIM(3) ANIM(4) ANIM(5) ANIM(6) ANIM(7)
ANIM(8) ANIM(9) ANIM(10) ANIM(11) ANIM(12) ANIM(13) ANIM(14) ANIM(15)
static const union AnimCmd *const sAnims[]={sAnim0,sAnim1,sAnim2,sAnim3,sAnim4,sAnim5,sAnim6,sAnim7,sAnim8,sAnim9,sAnim10,sAnim11,sAnim12,sAnim13,sAnim14,sAnim15};
static const struct SpriteTemplate sTemplate={.tileTag=ICON_TAG,.paletteTag=ICON_TAG,.oam=&sOam,.anims=sAnims,.images=NULL,.affineAnims=gDummySpriteAffineAnimTable,.callback=SpriteCallbackDummy};
static EWRAM_DATA struct {u8 sprites[8],icons[8],count,clock,label;} *sCustomMenu=NULL;
static const struct WindowTemplate sClockWin={.bg=0,.tilemapLeft=1,.tilemapTop=17,.width=12,.height=3,.paletteNum=15,.baseBlock=0x30};
static const struct WindowTemplate sLabelWin={.bg=0,.tilemapLeft=14,.tilemapTop=17,.width=12,.height=3,.paletteNum=15,.baseBlock=0x54};
bool32 CustomStartMenu_IsActive(void){return sCustomMenu!=NULL;}
u8 CustomStartMenu_GetTheme(void){u16 value=VarGet(VAR_LEGENDS_MENU_THEME);return value<LEGENDS_MENU_THEME_COUNT?value:0;}
void CustomStartMenu_SetTheme(u8 theme){VarSet(VAR_LEGENDS_MENU_THEME,theme<LEGENDS_MENU_THEME_COUNT?theme:0);}
void CustomStartMenu_Select(u8 cursor,const u8 *label)
{
    u32 i;
    if(!sCustomMenu)return;
    for(i=0;i<sCustomMenu->count;i++)
        if(sCustomMenu->sprites[i]!=MAX_SPRITES)
            StartSpriteAnim(&gSprites[sCustomMenu->sprites[i]],sCustomMenu->icons[i]+(i==cursor?0:sCustomMenu->icons[i]==14?1:7));
    FillWindowPixelBuffer(sCustomMenu->label,PIXEL_FILL(1));
    AddTextPrinterParameterized(sCustomMenu->label,FONT_SMALL,label,0,3,TEXT_SKIP_DRAW,NULL);
    CopyWindowToVram(sCustomMenu->label,COPYWIN_FULL);
}
bool32 CustomStartMenu_Open(const u8 *icons,u8 count,u8 cursor,const u8 *label,u8 page)
{
    u32 i;u8 time[16];u8 *p;
    if(sCustomMenu)CustomStartMenu_Close();
    sCustomMenu=AllocZeroed(sizeof(*sCustomMenu));if(!sCustomMenu)return FALSE;
    sCustomMenu->count=min(count,8);
    for(i=0;i<8;i++)sCustomMenu->sprites[i]=MAX_SPRITES;
    sCustomMenu->clock=AddWindow(&sClockWin);sCustomMenu->label=AddWindow(&sLabelWin);
    if(sCustomMenu->clock==WINDOW_NONE || sCustomMenu->label==WINDOW_NONE){CustomStartMenu_Close();return FALSE;}
    DecompressAndCopyTileDataToVram(0,sTiles,0,0,0);
    DecompressDataWithHeaderWram(sMap,GetBgTilemapBuffer(0));
    LoadPalette(sPalettes[CustomStartMenu_GetTheme()],BG_PLTT_ID(14),PLTT_SIZE_4BPP);
    LoadPalette(gStandardMenuPalette,BG_PLTT_ID(15),PLTT_SIZE_4BPP);
    LoadCompressedSpriteSheet(&sSheet);LoadSpritePalette(&sPal);
    if(GetSpriteTileStartByTag(ICON_TAG)==0xFFFF || IndexOfSpritePaletteTag(ICON_TAG)==0xFF){CustomStartMenu_Close();return FALSE;}
    for(i=0;i<sCustomMenu->count;i++)
    {
        sCustomMenu->icons[i]=icons[i];
        sCustomMenu->sprites[i]=CreateSprite(&sTemplate,224,12+i*17,0);
        if(sCustomMenu->sprites[i]==MAX_SPRITES){CustomStartMenu_Close();return FALSE;}
    }
    RtcCalcLocalTime();p=ConvertIntToDecimalStringN(time,gLocalTime.hours,STR_CONV_MODE_LEADING_ZEROS,2);*p++=CHAR_COLON;ConvertIntToDecimalStringN(p,gLocalTime.minutes,STR_CONV_MODE_LEADING_ZEROS,2);
    FillWindowPixelBuffer(sCustomMenu->clock,PIXEL_FILL(1));
    AddTextPrinterParameterized(sCustomMenu->clock,FONT_SMALL,time,0,0,TEXT_SKIP_DRAW,NULL);
    AddTextPrinterParameterized(sCustomMenu->clock,FONT_SMALL,page?COMPOUND_STRING("L/R 2/2  SERVICES"):COMPOUND_STRING("L/R 1/2  ADVENTURE"),0,12,TEXT_SKIP_DRAW,NULL);
    PutWindowTilemap(sCustomMenu->clock);PutWindowTilemap(sCustomMenu->label);CopyWindowToVram(sCustomMenu->clock,COPYWIN_FULL);
    CustomStartMenu_Select(cursor,label);ScheduleBgCopyTilemapToVram(0);return TRUE;
}
void CustomStartMenu_Close(void)
{
    u32 i;if(!sCustomMenu)return;
    for(i=0;i<sCustomMenu->count;i++)if(sCustomMenu->sprites[i]!=MAX_SPRITES)DestroySprite(&gSprites[sCustomMenu->sprites[i]]);
    FreeSpriteTilesByTag(ICON_TAG);FreeSpritePaletteByTag(ICON_TAG);
    if(sCustomMenu->clock!=WINDOW_NONE)RemoveWindow(sCustomMenu->clock);
    if(sCustomMenu->label!=WINDOW_NONE)RemoveWindow(sCustomMenu->label);
    FREE_AND_SET_NULL(sCustomMenu);
    FillBgTilemapBufferRect(0,0,0,0,32,32,0);ScheduleBgCopyTilemapToVram(0);
}
