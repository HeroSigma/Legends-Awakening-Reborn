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
static EWRAM_DATA struct {u8 sprites[8],icons[8],count,clock,label;u16 backdrops[2][36];} *sCustomMenu=NULL;
static const struct WindowTemplate sClockWin={.bg=0,.tilemapLeft=2,.tilemapTop=17,.width=12,.height=2,.paletteNum=14,.baseBlock=0x30};
static const struct WindowTemplate sLabelWin={.bg=0,.tilemapLeft=16,.tilemapTop=17,.width=10,.height=2,.paletteNum=14,.baseBlock=0x48};
bool32 CustomStartMenu_IsActive(void){return sCustomMenu!=NULL;}
u8 CustomStartMenu_GetTheme(void){u16 value=VarGet(VAR_LEGENDS_MENU_THEME);return value<LEGENDS_MENU_THEME_COUNT?value:0;}
void CustomStartMenu_SetTheme(u8 theme){VarSet(VAR_LEGENDS_MENU_THEME,theme<LEGENDS_MENU_THEME_COUNT?theme:0);}
// Restore the exact footer pixels under each window instead of painting a rectangle.
static void RestoreFooter(u8 win, u8 backdrop)
{
    u8 tiles[1024], tile[32];
    u32 i,x,y;
    DecompressDataWithHeaderWram(sTiles,tiles);
    for(i=0;i<GetWindowAttribute(win,WINDOW_WIDTH)*GetWindowAttribute(win,WINDOW_HEIGHT);i++)
    {
        u32 width=GetWindowAttribute(win,WINDOW_WIDTH);
        u16 entry=sCustomMenu->backdrops[backdrop][i];
        u32 index=entry&0x3FF;
        if(index>=32)index=0;
        for(y=0;y<8;y++)for(x=0;x<8;x+=2)
        {
            u32 a=(entry&0x400)?7-x:x, b=(entry&0x400)?6-x:x+1;
            u32 sy=(entry&0x800)?7-y:y;
            u8 pa=tiles[index*32+sy*4+a/2]>>((a&1)*4)&15;
            u8 pb=tiles[index*32+sy*4+b/2]>>((b&1)*4)&15;
            tile[y*4+x/2]=pa|(pb<<4);
        }
        BlitBitmapToWindow(win,tile,(i%width)*8,(i/width)*8,8,8);
    }
}
static const u8 sFooterColors[]={TEXT_COLOR_TRANSPARENT,5,1};
void CustomStartMenu_Select(u8 cursor,const u8 *label)
{
    u32 i;
    if(!sCustomMenu)return;
    for(i=0;i<sCustomMenu->count;i++)
        if(sCustomMenu->sprites[i]!=MAX_SPRITES)
            StartSpriteAnim(&gSprites[sCustomMenu->sprites[i]],sCustomMenu->icons[i]+(i==cursor?0:sCustomMenu->icons[i]==14?1:7));
    RestoreFooter(sCustomMenu->label,1);
    AddTextPrinterParameterized4(sCustomMenu->label,FONT_SMALL,0,1,0,0,sFooterColors,TEXT_SKIP_DRAW,label);
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
    for(i=0;i<24;i++)sCustomMenu->backdrops[0][i]=((u16 *)GetBgTilemapBuffer(0))[(17+i/12)*32+2+i%12];
    for(i=0;i<20;i++)sCustomMenu->backdrops[1][i]=((u16 *)GetBgTilemapBuffer(0))[(17+i/10)*32+16+i%10];
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
    RestoreFooter(sCustomMenu->clock,0);
    AddTextPrinterParameterized4(sCustomMenu->clock,FONT_SMALL,0,1,0,0,sFooterColors,TEXT_SKIP_DRAW,time);
    AddTextPrinterParameterized4(sCustomMenu->clock,FONT_SMALL,38,1,0,0,sFooterColors,TEXT_SKIP_DRAW,page?COMPOUND_STRING("L/R 2/2"):COMPOUND_STRING("L/R 1/2"));
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
