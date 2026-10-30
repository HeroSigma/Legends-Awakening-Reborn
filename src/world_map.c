#include "global.h"
#include "bg.h"
#include "decompress.h"
#include "gpu_regs.h"
#include "main.h"
#include "malloc.h"
#include "menu.h"
#include "overworld.h"
#include "palette.h"
#include "region_map.h"
#include "regional_map_names.h"
#include "sound.h"
#include "sprite.h"
#include "string_util.h"
#include "text.h"
#include "text_window.h"
#include "window.h"
#include "world_map.h"
#include "constants/rgb.h"
#include "constants/characters.h"
#include "constants/songs.h"

struct WorldLocation { u8 x, y, region; const u8 *name; };
#include "data/world_map_locations.h"
#include "data/world_map_sinnoh.h"
static const u8 sTiles[] = INCBIN_U8("data/world_map/tiles.bin");
static const u16 sTilemap[] = INCBIN_U16("data/world_map/tilemap.bin");
static const u16 sPalette[] = INCBIN_U16("data/world_map/palette.bin");
static const u8 sOcean[] = _("Open Sea");
static const u8 sHoenn[] = _("Hoenn");
static const u8 sJohto[] = _("Johto");
static const u8 sKanto[] = _("Kanto");
static const u8 sSinnoh[] = _("Sinnoh");
static const u8 sWorld[] = _("World Map");
static const u8 sHelp[] = _("D-Pad: Explore   B: Back");
static EWRAM_DATA struct {
    MainCallback callback;
    u8 state, x, y, playerX, playerY, cursor, player, playerKnown;
    u16 bg0[1024];
} *sWorldMap;
static const struct BgTemplate sBgs[] = {
    {.bg=0, .charBaseIndex=2, .mapBaseIndex=31, .screenSize=0, .priority=0},
    {.bg=2, .charBaseIndex=0, .mapBaseIndex=24, .screenSize=3, .paletteMode=0, .priority=2},
};
static const struct WindowTemplate sWindows[] = {
    {.bg=0,.tilemapLeft=1,.tilemapTop=0,.width=28,.height=2,.paletteNum=15,.baseBlock=1},
    {.bg=0,.tilemapLeft=1,.tilemapTop=16,.width=28,.height=4,.paletteNum=15,.baseBlock=57},
    DUMMY_WIN_TEMPLATE
};
static const u32 sCursorTiles[] = {0x11111111,0x10000001,0x10200201,0x10022001,0x10022001,0x10200201,0x10000001,0x11111111};
static const u16 sCursorPal[16] = {RGB_BLACK,RGB_WHITE,RGB_RED,RGB_YELLOW};
static const struct SpriteSheet sCursorSheet = {sCursorTiles,sizeof(sCursorTiles),0x7E10};
static const struct SpritePalette sCursorPalette = {sCursorPal,0x7E10};
static const struct OamData sOam = {.shape=SPRITE_SHAPE(8x8),.size=SPRITE_SIZE(8x8),.priority=0};
static const struct SpriteTemplate sCursorTemplate = {.tileTag=0x7E10,.paletteTag=0x7E10,.oam=&sOam,.anims=gDummySpriteAnimTable,.images=NULL,.affineAnims=gDummySpriteAffineAnimTable,.callback=SpriteCallbackDummy};
__attribute__((noinline)) const u8 *WorldMap_LocationAt(u16 x, u16 y)
{
    u32 i;
    for(i=0;i<ARRAY_COUNT(sWorldLocations);i++)
        if(sWorldLocations[i].x==x && sWorldLocations[i].y==y) return sWorldLocations[i].name;
    for(i=0;i<ARRAY_COUNT(sSinnohLocations);i++)
        if(sSinnohLocations[i].x==x && sSinnohLocations[i].y==y) return sSinnohLocations[i].name;
    return sOcean;
}
__attribute__((noinline)) u8 WorldMap_RegionAt(u16 x, u16 y)
{
    u32 i;
    for(i=0;i<ARRAY_COUNT(sWorldLocations);i++)
        if(sWorldLocations[i].x==x && sWorldLocations[i].y==y) return sWorldLocations[i].region;
    for(i=0;i<ARRAY_COUNT(sSinnohLocations);i++)
        if(sSinnohLocations[i].x==x && sSinnohLocations[i].y==y) return 4;
    if(x>=2 && x<29 && y>=3 && y<24)return 4;
    if(x>=31 && x<61 && y>=3 && y<23) return x<48 ? 2 : 1;
    if(x>=2 && x<32 && y>=28 && y<48) return 3;
    return 0;
}
__attribute__((noinline)) static void WorldMap_Refresh(void)
{
    s16 sx=sWorldMap->x*8-120, sy=sWorldMap->y*8-72;
    u8 r=WorldMap_RegionAt(sWorldMap->x,sWorldMap->y);
    const u8 *region=r==1?sKanto:r==2?sJohto:r==3?sHoenn:r==4?sSinnoh:sWorld;
    if(sx<0)sx=0;if(sx>256)sx=256;if(sy<0)sy=0;if(sy>240)sy=240;
    ChangeBgX(2,sx<<8,BG_COORD_SET);ChangeBgY(2,sy<<8,BG_COORD_SET);
    gSprites[sWorldMap->cursor].x=sWorldMap->x*8+4-sx;
    gSprites[sWorldMap->cursor].y=sWorldMap->y*8+4-sy;
    gSprites[sWorldMap->player].x=sWorldMap->playerX*8+4-sx;
    gSprites[sWorldMap->player].y=sWorldMap->playerY*8+4-sy;
    gSprites[sWorldMap->player].invisible=(!sWorldMap->playerKnown || sWorldMap->playerX*8<sx || sWorldMap->playerX*8>sx+232 || sWorldMap->playerY*8<sy+16 || sWorldMap->playerY*8>sy+120);
    FillWindowPixelBuffer(0,PIXEL_FILL(1));
    AddTextPrinterParameterized(0,FONT_NORMAL,region,4,0,TEXT_SKIP_DRAW,NULL);
    CopyWindowToVram(0,COPYWIN_FULL);
    FillWindowPixelBuffer(1,PIXEL_FILL(1));
    AddTextPrinterParameterized(1,FONT_NORMAL,WorldMap_LocationAt(sWorldMap->x,sWorldMap->y),4,0,TEXT_SKIP_DRAW,NULL);
    AddTextPrinterParameterized(1,FONT_SMALL,sHelp,4,18,TEXT_SKIP_DRAW,NULL);
    CopyWindowToVram(1,COPYWIN_FULL);
}
static bool32 SameName(const u8 *a, const u8 *b)
{
    while (*a != EOS && *b != EOS)
    {
        u8 ca=*a++, cb=*b++;
        if(ca>=CHAR_a && ca<=CHAR_z)ca-=CHAR_a-CHAR_A;
        if(cb>=CHAR_a && cb<=CHAR_z)cb-=CHAR_a-CHAR_A;
        if(ca!=cb)return FALSE;
    }
    return *a==*b;
}
static void WorldMap_VBlank(void){LoadOam();ProcessSpriteCopyRequests();TransferPlttBuffer();}
static void WorldMap_Update(void)
{
    if(sWorldMap->state==0 && !gPaletteFade.active)
    {
        u8 x=sWorldMap->x,y=sWorldMap->y;
        if(JOY_NEW(B_BUTTON)) {BeginNormalPaletteFade(PALETTES_ALL,0,0,16,RGB_BLACK);sWorldMap->state=1;}
        else {
            if(JOY_REPEAT(DPAD_LEFT) && x>1)x--;else if(JOY_REPEAT(DPAD_RIGHT) && x<61)x++;
            if(JOY_REPEAT(DPAD_UP) && y>3)y--;else if(JOY_REPEAT(DPAD_DOWN) && y<47)y++;
            if(x!=sWorldMap->x || y!=sWorldMap->y){sWorldMap->x=x;sWorldMap->y=y;WorldMap_Refresh();}
        }
    }
    else if(sWorldMap->state==1 && !gPaletteFade.active)
    {
        MainCallback cb=sWorldMap->callback;
        SetVBlankCallback(NULL);FreeAllWindowBuffers();FreeAllSpritePalettes();ResetSpriteData();
        UnsetBgTilemapBuffer(0);FREE_AND_SET_NULL(sWorldMap);SetMainCallback2(cb);return;
    }
    AnimateSprites();BuildOamBuffer();UpdatePaletteFade();
}
void WorldMap_Open(MainCallback callback)
{
    u32 i;u8 name[40];const u8 *current=RegionalMapDisplayName(&gMapHeader);
    SetVBlankCallback(NULL);SetGpuReg(REG_OFFSET_DISPCNT,0);
    sWorldMap=AllocZeroed(sizeof(*sWorldMap));
    if(!sWorldMap){SetMainCallback2(callback);return;}
    sWorldMap->callback=callback;sWorldMap->x=7;sWorldMap->y=41;
    if(!current){GetMapName(name,gMapHeader.regionMapSectionId,0);current=name;}
    for(i=0;i<ARRAY_COUNT(sWorldLocations);i++)
        if(SameName(current,sWorldLocations[i].name)){sWorldMap->x=sWorldLocations[i].x;sWorldMap->y=sWorldLocations[i].y;sWorldMap->playerKnown=TRUE;break;}
    if(!sWorldMap->playerKnown)
        for(i=0;i<ARRAY_COUNT(sSinnohLocations);i++)
            if(SameName(current,sSinnohLocations[i].name)){sWorldMap->x=sSinnohLocations[i].x;sWorldMap->y=sSinnohLocations[i].y;sWorldMap->playerKnown=TRUE;break;}
    sWorldMap->playerX=sWorldMap->x;sWorldMap->playerY=sWorldMap->y;
    ResetSpriteData();FreeAllSpritePalettes();ResetBgsAndClearDma3BusyFlags(0);InitBgsFromTemplates(0,sBgs,ARRAY_COUNT(sBgs));
    SetBgTilemapBuffer(0,sWorldMap->bg0);InitWindows(sWindows);DeactivateAllTextPrinters();
    LoadPalette(sPalette,0,sizeof(sPalette));LoadPalette(GetTextWindowPalette(0),BG_PLTT_ID(15),PLTT_SIZE_4BPP);
    LoadBgTiles(2,sTiles,sizeof(sTiles),0);LoadBgTilemap(2,sTilemap,sizeof(sTilemap),0);
    PutWindowTilemap(0);PutWindowTilemap(1);CopyBgTilemapBufferToVram(0);
    LoadSpriteSheet(&sCursorSheet);LoadSpritePalette(&sCursorPalette);
    sWorldMap->cursor=CreateSprite(&sCursorTemplate,0,0,0);sWorldMap->player=CreateSprite(&sCursorTemplate,0,0,1);
    gSprites[sWorldMap->player].oam.objMode=ST_OAM_OBJ_NORMAL;
    WorldMap_Refresh();BeginNormalPaletteFade(PALETTES_ALL,0,16,0,RGB_BLACK);
    SetGpuReg(REG_OFFSET_DISPCNT,DISPCNT_MODE_0|DISPCNT_OBJ_1D_MAP|DISPCNT_OBJ_ON);ShowBg(0);ShowBg(2);
    SetVBlankCallback(WorldMap_VBlank);SetMainCallback2(WorldMap_Update);
}
