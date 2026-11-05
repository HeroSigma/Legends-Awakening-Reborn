// Speaker-driven adaptation of Mudskip's field-mugshot presentation.
#include "global.h"
#include "field_mugshot.h"
#include "field_name_box.h"
#include "match_call.h"
#include "event_data.h"
#include "script.h"
#include "sprite.h"
#include "palette.h"
#include "data.h"
#include "decompress.h"
#include "dynamic_palettes.h"
#include "malloc.h"
#include "gpu_regs.h"
#include "battle_pyramid.h"
#include "overworld.h"
#include "constants/speaker_names.h"
#include "constants/trainers.h"

static EWRAM_INIT u8 sPortrait = MAX_SPRITES;
static EWRAM_INIT u8 sMask = MAX_SPRITES;
static EWRAM_DATA u16 sWindowBits = 0;
static EWRAM_DATA u16 sOutBits = 0;
static const u32 sBirchGfx[] = INCGFX_U32("graphics/birch_speech/birch.png", ".4bpp");
static const u16 sBirchPal[] = INCGFX_U16("graphics/birch_speech/birch.png", ".gbapal");
static const struct OamData sOam = {
    .shape = SPRITE_SHAPE(64x64), .size = SPRITE_SIZE(64x64), .priority = 0,
};
static void PortraitCallback(struct Sprite *sprite) {}
static const struct SpriteTemplate sFieldPortraitTemplate = {
    .tileTag = FIELD_MUGSHOT_TAG, .paletteTag = FIELD_MUGSHOT_TAG,
    .oam = &sOam, .anims = gDummySpriteAnimTable,
    .affineAnims = gDummySpriteAffineAnimTable, .callback = PortraitCallback,
};
static const struct {u16 speaker, pic;} sPortraits[] = {
    {SP_NAME_BRENDAN, TRAINER_PIC_BRENDAN},
    {SP_NAME_MAY, TRAINER_PIC_MAY},
    {SP_NAME_RED, TRAINER_PIC_RED},
    {SP_NAME_SILVER, TRAINER_PIC_SILVER_HNS},
    {SP_NAME_WALLY, TRAINER_PIC_WALLY},
    {SP_NAME_NORMAN, TRAINER_PIC_LEADER_NORMAN},
    {SP_NAME_GIOVANNI, TRAINER_PIC_LEADER_GIOVANNI_FRLG},
    {SP_NAME_OAK, TRAINER_PIC_PROFESSOR_OAK_FRLG},
    {SP_NAME_BLUE, TRAINER_PIC_RIVAL_LATE_FRLG},
    {SP_NAME_GREEN, TRAINER_PIC_LEAF},
    {SP_NAME_SHADOW_TRIAD, TRAINER_PIC_SHADOW_TRIAD},
    {SP_NAME_AQUA_GRUNT, TRAINER_PIC_AQUA_GRUNT_M},
};

bool32 __attribute__((noinline)) IsFieldMugshotActive(void)
{
    return sPortrait < MAX_SPRITES && gSprites[sPortrait].inUse
        && gSprites[sPortrait].callback == PortraitCallback;
}

void RemoveFieldMugshot(void)
{
    // A map/menu may already have reset all sprites. Never destroy a reused ID.
    if (IsFieldMugshotActive())
    {
        if (sMask < MAX_SPRITES && gSprites[sMask].inUse
            && gSprites[sMask].callback == PortraitCallback)
        {
            DestroySprite(&gSprites[sMask]);
            SetGpuReg(REG_OFFSET_DISPCNT, (GetGpuReg(REG_OFFSET_DISPCNT) & ~DISPCNT_OBJWIN_ON) | sWindowBits);
            SetGpuReg(REG_OFFSET_WINOUT, (GetGpuReg(REG_OFFSET_WINOUT) & ~WINOUT_WINOBJ_OBJ) | sOutBits);
        }
        DestroySprite(&gSprites[sPortrait]);
    }
    FreeSpriteTilesByTag(FIELD_MUGSHOT_TAG);
    FreeSpritePaletteByTag(FIELD_MUGSHOT_TAG);
    sPortrait = sMask = MAX_SPRITES;
}

void UpdateFieldMugshot(void)
{
    u16 pic = TRAINER_PIC_NONE;
    bool32 birch = gSpeakerName == gSpeakerNamesTable[SP_NAME_BIRCH];
    bool32 player = gSpeakerName == gSpeakerNamesTable[SP_NAME_PLAYER];
    RemoveFieldMugshot();
    if (!gSpeakerName || IsMatchCallTaskActive() || gMsgIsSignPost
        || FlagGet(OW_FLAG_SUPPRESS_NAME_BOX)) return;
    if (player)
        pic = PlayerOutfit_TrainerPic(gSaveBlock2Ptr->playerGender == FEMALE ? TRAINER_PIC_MAY : TRAINER_PIC_BRENDAN);
    else
        for (u32 i = 0; i < ARRAY_COUNT(sPortraits); i++)
            if (gSpeakerName == gSpeakerNamesTable[sPortraits[i].speaker])
                pic = sPortraits[i].pic;
    if (!birch && pic == TRAINER_PIC_NONE) return;

    u8 *buffer = AllocZeroed(0x800);
    if (!buffer) return;
    if (birch) CpuCopy32(sBirchGfx, buffer, 0x800);
    else DecompressDataWithHeaderWram(GetTrainerFrontPicData(pic), buffer);
    struct SpriteSheet sheet = {buffer, 0x800, FIELD_MUGSHOT_TAG};
    struct SpritePalette pal = {birch ? sBirchPal : player ? DynamicPal_TrainerPalette(pic, TRUE) : GetTrainerFrontPicPalette(pic), FIELD_MUGSHOT_TAG};
    LoadSpriteSheet(&sheet);
    Free(buffer);
    if (GetSpriteTileStartByTag(FIELD_MUGSHOT_TAG) == 0xFFFF) return;
    // Portraits must never evict overworld encounters to obtain a palette.
    u32 paletteSlot = AllocSpritePalette(FIELD_MUGSHOT_TAG);
    if (paletteSlot == 0xFF)
    {
        RemoveFieldMugshot();
        return;
    }
    LoadSpritePaletteInSlot(&pal, paletteSlot);
    sPortrait = CreateSpriteUnchecked(&sFieldPortraitTemplate, 200, 64, 0);
    if (sPortrait == MAX_SPRITES)
    {
        RemoveFieldMugshot();
        return;
    }
    if (GetFlashLevel() || InBattlePyramid())
    {
        sMask = CreateSpriteUnchecked(&sFieldPortraitTemplate, 200, 64, 0);
        if (sMask < MAX_SPRITES)
        {
            sWindowBits = GetGpuReg(REG_OFFSET_DISPCNT) & DISPCNT_OBJWIN_ON;
            sOutBits = GetGpuReg(REG_OFFSET_WINOUT) & WINOUT_WINOBJ_OBJ;
            SetGpuRegBits(REG_OFFSET_DISPCNT, DISPCNT_OBJWIN_ON);
            SetGpuRegBits(REG_OFFSET_WINOUT, WINOUT_WINOBJ_OBJ);
            gSprites[sMask].oam.objMode = ST_OAM_OBJ_WINDOW;
        }
    }
}
