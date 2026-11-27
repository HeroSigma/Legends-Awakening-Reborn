// Ruby/Sapphire outfits: Modern Emerald / resetes12. See docs/features/player-outfits.
const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanNormal = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 16,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x32,
    .subspriteTables = sOamTables_16x32,
    .anims = sAnimTable_BrendanMayNormal,
    .images = sOutfitCrystalFrames_BrendanNormal,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanMachBike = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_BIKE_TIRE,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Standard,
    .images = sOutfitCrystalFrames_BrendanMachBike,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanAcroBike = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_BIKE_TIRE,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_AcroBike,
    .images = sOutfitCrystalFrames_BrendanAcroBike,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanSurfing = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Surfing,
    .images = sOutfitCrystalFrames_BrendanSurfing,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanUnderwater = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Standard,
    .images = sOutfitCrystalFrames_BrendanUnderwater,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanFieldMove = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_FieldMove,
    .images = sOutfitCrystalFrames_BrendanFieldMove,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanFishing = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Fishing,
    .images = sOutfitCrystalFrames_BrendanFishing,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanWatering = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Standard,
    .images = sOutfitCrystalFrames_BrendanWatering,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanDecorating = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 256,
    .width = 16,
    .height = 32,
    .paletteSlot = PALSLOT_NPC_SPECIAL,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = TRUE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x32,
    .subspriteTables = sOamTables_16x32,
    .anims = sAnimTable_Inanimate,
    .images = sOutfitCrystalFrames_BrendanDecorating,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_BrendanRiding = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_AREN,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 16,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x32,
    .subspriteTables = sOamTables_16x32,
    .anims = sAnimTable_BrendanMayNormal,
    .images = sOutfitCrystalFrames_BrendanRiding,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayNormal = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 16,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x32,
    .subspriteTables = sOamTables_16x32,
    .anims = sAnimTable_BrendanMayNormal,
    .images = sOutfitCrystalFrames_MayNormal,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayMachBike = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_BIKE_TIRE,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Standard,
    .images = sOutfitCrystalFrames_MayMachBike,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayAcroBike = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_BIKE_TIRE,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_AcroBike,
    .images = sOutfitCrystalFrames_MayAcroBike,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MaySurfing = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Surfing,
    .images = sOutfitCrystalFrames_MaySurfing,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayUnderwater = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_NPC_SPECIAL,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Standard,
    .images = sOutfitCrystalFrames_MayUnderwater,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayFieldMove = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_FieldMove,
    .images = sOutfitCrystalFrames_MayFieldMove,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayFishing = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Fishing,
    .images = sOutfitCrystalFrames_MayFishing,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayWatering = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = sOamTables_32x32,
    .anims = sAnimTable_Standard,
    .images = sOutfitCrystalFrames_MayWatering,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayDecorating = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 256,
    .width = 16,
    .height = 32,
    .paletteSlot = PALSLOT_NPC_SPECIAL,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = TRUE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x32,
    .subspriteTables = sOamTables_16x32,
    .anims = sAnimTable_Inanimate,
    .images = sOutfitCrystalFrames_MayDecorating,
};

const struct ObjectEventGraphicsInfo gOutfitCrystalInfo_MayRiding = {
    .tileTag = TAG_NONE,
    .paletteTag = OBJ_EVENT_PAL_TAG_ARIA,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_BRIDGE_REFLECTION,
    .size = 512,
    .width = 16,
    .height = 32,
    .paletteSlot = PALSLOT_PLAYER,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .compressed = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x32,
    .subspriteTables = sOamTables_16x32,
    .anims = sAnimTable_BrendanMayNormal,
    .images = sOutfitCrystalFrames_MayRiding,
};

static const struct ObjectEventGraphicsInfo *GetCrystalPlayerGraphics(u16 graphicsId)
{
    switch (graphicsId)
    {
    case OBJ_EVENT_GFX_BRENDAN_NORMAL: return &gOutfitCrystalInfo_BrendanNormal;
    case OBJ_EVENT_GFX_BRENDAN_MACH_BIKE: return &gOutfitCrystalInfo_BrendanMachBike;
    case OBJ_EVENT_GFX_BRENDAN_ACRO_BIKE: return &gOutfitCrystalInfo_BrendanAcroBike;
    case OBJ_EVENT_GFX_BRENDAN_SURFING: return &gOutfitCrystalInfo_BrendanSurfing;
    case OBJ_EVENT_GFX_BRENDAN_UNDERWATER: return &gOutfitCrystalInfo_BrendanUnderwater;
    case OBJ_EVENT_GFX_BRENDAN_FIELD_MOVE: return &gOutfitCrystalInfo_BrendanFieldMove;
    case OBJ_EVENT_GFX_BRENDAN_FISHING: return &gOutfitCrystalInfo_BrendanFishing;
    case OBJ_EVENT_GFX_BRENDAN_WATERING: return &gOutfitCrystalInfo_BrendanWatering;
    case OBJ_EVENT_GFX_BRENDAN_DECORATING: return &gOutfitCrystalInfo_BrendanDecorating;
    case OBJ_EVENT_GFX_LA_BRENDAN_RIDING:
    case OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING: return &gOutfitCrystalInfo_BrendanRiding;
    case OBJ_EVENT_GFX_MAY_NORMAL: return &gOutfitCrystalInfo_MayNormal;
    case OBJ_EVENT_GFX_MAY_MACH_BIKE: return &gOutfitCrystalInfo_MayMachBike;
    case OBJ_EVENT_GFX_MAY_ACRO_BIKE: return &gOutfitCrystalInfo_MayAcroBike;
    case OBJ_EVENT_GFX_MAY_SURFING: return &gOutfitCrystalInfo_MaySurfing;
    case OBJ_EVENT_GFX_MAY_UNDERWATER: return &gOutfitCrystalInfo_MayUnderwater;
    case OBJ_EVENT_GFX_MAY_FIELD_MOVE: return &gOutfitCrystalInfo_MayFieldMove;
    case OBJ_EVENT_GFX_MAY_FISHING: return &gOutfitCrystalInfo_MayFishing;
    case OBJ_EVENT_GFX_MAY_WATERING: return &gOutfitCrystalInfo_MayWatering;
    case OBJ_EVENT_GFX_MAY_DECORATING: return &gOutfitCrystalInfo_MayDecorating;
    case OBJ_EVENT_GFX_LA_MAY_RIDING:
    case OBJ_EVENT_GFX_LA_MAY_WATER_RIDING: return &gOutfitCrystalInfo_MayRiding;
    default: return NULL;
    }
}
