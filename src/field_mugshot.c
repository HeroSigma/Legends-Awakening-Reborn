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
    {SP_NAME_FLANNERY, TRAINER_PIC_LEADER_FLANNERY},
    {SP_NAME_BRENDAN, TRAINER_PIC_HYPER_RIVAL_BRENDAN},
    {SP_NAME_MAY, TRAINER_PIC_HYPER_RIVAL_MAY},
    {SP_NAME_NORMAN, TRAINER_PIC_LEADER_NORMAN},
    {SP_NAME_OAK, TRAINER_PIC_PROFESSOR_OAK_FRLG},
    {SP_NAME_SHADOW_TRIAD, TRAINER_PIC_SHADOW_TRIAD},
    {SP_NAME_AQUA_GRUNT, TRAINER_PIC_DONOR_AQUA_GRUNT_MALE},
    {SP_NAME_AQUA_GRUNT_FEMALE, TRAINER_PIC_DONOR_AQUA_GRUNT_FEMALE},
    {SP_NAME_MAGMA_GRUNT_MALE, TRAINER_PIC_DONOR_MAGMA_GRUNT_MALE},
    {SP_NAME_AQUA_MATT, TRAINER_PIC_DONOR_AQUA_MATT},
    {SP_NAME_AQUA_SHELLY, TRAINER_PIC_DONOR_AQUA_SHELLY},
    {SP_NAME_ARCHIE, TRAINER_PIC_DONOR_ARCHIE},
    {SP_NAME_MAGMA_GRUNT_FEMALE, TRAINER_PIC_DONOR_MAGMA_GRUNT_FEMALE},
    {SP_NAME_REI, TRAINER_PIC_DONOR_REI},
    {SP_NAME_MAGMA_TABITHA, TRAINER_PIC_DONOR_MAGMA_TABITHA},
    {SP_NAME_WALLY, TRAINER_PIC_DONOR_WALLY},
    {SP_NAME_MAXIE, TRAINER_PIC_DONOR_MAXIE},
    {SP_NAME_STEVEN, TRAINER_PIC_DONOR_STEVEN},
    {SP_NAME_BLUE, TRAINER_PIC_DONOR_BLUE},
    {SP_NAME_PAST_RED, TRAINER_PIC_DONOR_PAST_RED},
    {SP_NAME_GREEN, TRAINER_PIC_DONOR_GREEN},
    {SP_NAME_ETHAN, TRAINER_PIC_DONOR_GOLD},
    {SP_NAME_SILVER, TRAINER_PIC_DONOR_SILVER},
    {SP_NAME_KRIS, TRAINER_PIC_DONOR_KRIS},
    {SP_NAME_LYRA, TRAINER_PIC_DONOR_LYRA},
    {SP_NAME_ZINNIA, TRAINER_PIC_DONOR_ZINNIA},
    {SP_NAME_DAWN, TRAINER_PIC_DONOR_DAWN},
    {SP_NAME_BARRY, TRAINER_PIC_DONOR_BARRY},
    {SP_NAME_LUCAS, TRAINER_PIC_DONOR_LUCAS},
    {SP_NAME_HILBERT, TRAINER_PIC_DONOR_HILBERT},
    {SP_NAME_HILDA, TRAINER_PIC_DONOR_HILDA},
    {SP_NAME_N, TRAINER_PIC_DONOR_N},
    {SP_NAME_NATE, TRAINER_PIC_DONOR_NATE},
    {SP_NAME_ROSA, TRAINER_PIC_DONOR_ROSA},
    {SP_NAME_HUGH, TRAINER_PIC_DONOR_HUGH},
    {SP_NAME_CALEM, TRAINER_PIC_DONOR_CALEM},
    {SP_NAME_SERENA, TRAINER_PIC_DONOR_SERENA},
    {SP_NAME_ELIO, TRAINER_PIC_DONOR_ELIO},
    {SP_NAME_SELENE, TRAINER_PIC_DONOR_SELENE},
    {SP_NAME_ASH, TRAINER_PIC_DONOR_ASH},
    {SP_NAME_ALAIN, TRAINER_PIC_DONOR_ALAINE},
    {SP_NAME_AKARI, TRAINER_PIC_DONOR_AKARI},
    {SP_NAME_GIOVANNI, TRAINER_PIC_DONOR_GIOVANNI},
    {SP_NAME_RAINBOW_ROCKET_GIOVANNI, TRAINER_PIC_DONOR_RAINBOW_ROCKET_GIOVANNI},
    {SP_NAME_PAST_MAXIE, TRAINER_PIC_DONOR_PAST_MAXIE},
    {SP_NAME_PAST_ARCHIE, TRAINER_PIC_DONOR_PAST_ARCHIE},
    {SP_NAME_CYRUS, TRAINER_PIC_DONOR_CYRUS},
    {SP_NAME_PAST_GHETSIS, TRAINER_PIC_DONOR_PAST_GHETSIS},
    {SP_NAME_LYSANDRE, TRAINER_PIC_DONOR_LYSANDRE},
    {SP_NAME_FABA, TRAINER_PIC_DONOR_FABA},
    {SP_NAME_GHETSIS, TRAINER_PIC_DONOR_GHETSIS},
    {SP_NAME_RED, TRAINER_PIC_DONOR_RED},
    {SP_NAME_GLADION, TRAINER_PIC_DONOR_GLADION},
    {SP_NAME_VICTOR, TRAINER_PIC_DONOR_VICTOR},
    {SP_NAME_GLORIA, TRAINER_PIC_DONOR_GLORIA},
    {SP_NAME_VOLO, TRAINER_PIC_DONOR_VOLO},
    {SP_NAME_NEW_MAY, TRAINER_PIC_DONOR_NEW_MAY},
    {SP_NAME_NEW_BRENDAN, TRAINER_PIC_DONOR_NEW_BRENDAN},
    {SP_NAME_MAGMA_COURTNEY, TRAINER_PIC_DONOR_MAGMA_COURTNEY},
    {SP_NAME_ROCKET_GRUNT_MALE, TRAINER_PIC_DONOR_ROCKET_GRUNT_MALE},
    {SP_NAME_ROCKET_GRUNT_FEMALE, TRAINER_PIC_DONOR_ROCKET_GRUNT_FEMALE},
    {SP_NAME_LUSAMINE, TRAINER_PIC_DONOR_LUSAMINE},
    {SP_NAME_CHEREN, TRAINER_PIC_DONOR_CHEREN},
    {SP_NAME_HAU, TRAINER_PIC_DONOR_HAO},
    {SP_NAME_LEON, TRAINER_PIC_DONOR_LEON},
    {SP_NAME_KUKUI, TRAINER_PIC_DONOR_KUKUI},
    {SP_NAME_RAINBOW_ROCKET_MALE, TRAINER_PIC_DONOR_RAINBOW_ROCKET_MALE},
    {SP_NAME_RAINBOW_ROCKET_FEMALE, TRAINER_PIC_DONOR_RAINBOW_ROCKET_FEMALE},
    {SP_NAME_LILY, TRAINER_PIC_DONOR_LILY},
    {SP_NAME_COLRESS, TRAINER_PIC_DONOR_COLRESS},
    {SP_NAME_GALACTIC_MALE, TRAINER_PIC_DONOR_GALACTIC_MALE},
    {SP_NAME_GALACTIC_FEMALE, TRAINER_PIC_DONOR_GALACTIC_FEMALE},
    {SP_NAME_PLASMA_MALE, TRAINER_PIC_DONOR_PLASMA_MALE},
    {SP_NAME_PLASMA_FEMALE, TRAINER_PIC_DONOR_PLASMA_FEMALE},
    {SP_NAME_FLARE_MALE, TRAINER_PIC_DONOR_FLARE_MALE},
    {SP_NAME_FLARE_FEMALE, TRAINER_PIC_DONOR_FLARE_FEMALE},
    {SP_NAME_CYNTHIA, TRAINER_PIC_DONOR_CYNTHIA},
    {SP_NAME_HOP, TRAINER_PIC_DONOR_HOP},
    {SP_NAME_PETREL, TRAINER_PIC_LA_PETREL},
    {SP_NAME_ARIANA, TRAINER_PIC_LA_ARIANA},
    {SP_NAME_PAST_GIOVANNI, TRAINER_PIC_DONOR_GIOVANNI},
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
