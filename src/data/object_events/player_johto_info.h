// Ruby/Sapphire outfits: Modern Emerald / resetes12. See docs/features/player-outfits.
const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanNormal = {
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
    .images = sOutfitJohtoFrames_BrendanNormal,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanMachBike = {
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
    .images = sOutfitJohtoFrames_BrendanMachBike,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanAcroBike = {
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
    .images = sOutfitJohtoFrames_BrendanAcroBike,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanSurfing = {
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
    .images = sOutfitJohtoFrames_BrendanSurfing,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanUnderwater = {
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
    .images = sOutfitJohtoFrames_BrendanUnderwater,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanFieldMove = {
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
    .images = sOutfitJohtoFrames_BrendanFieldMove,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanFishing = {
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
    .images = sOutfitJohtoFrames_BrendanFishing,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanWatering = {
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
    .images = sOutfitJohtoFrames_BrendanWatering,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanDecorating = {
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
    .images = sOutfitJohtoFrames_BrendanDecorating,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_BrendanRiding = {
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
    .images = sOutfitJohtoFrames_BrendanRiding,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayNormal = {
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
    .images = sOutfitJohtoFrames_MayNormal,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayMachBike = {
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
    .images = sOutfitJohtoFrames_MayMachBike,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayAcroBike = {
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
    .images = sOutfitJohtoFrames_MayAcroBike,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MaySurfing = {
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
    .images = sOutfitJohtoFrames_MaySurfing,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayUnderwater = {
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
    .images = sOutfitJohtoFrames_MayUnderwater,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayFieldMove = {
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
    .images = sOutfitJohtoFrames_MayFieldMove,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayFishing = {
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
    .images = sOutfitJohtoFrames_MayFishing,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayWatering = {
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
    .images = sOutfitJohtoFrames_MayWatering,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayDecorating = {
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
    .images = sOutfitJohtoFrames_MayDecorating,
};

const struct ObjectEventGraphicsInfo gOutfitJohtoInfo_MayRiding = {
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
    .images = sOutfitJohtoFrames_MayRiding,
};

static const struct ObjectEventGraphicsInfo *GetJohtoPlayerGraphics(u16 graphicsId)
{
    switch (graphicsId)
    {
    case OBJ_EVENT_GFX_BRENDAN_NORMAL: return &gOutfitJohtoInfo_BrendanNormal;
    case OBJ_EVENT_GFX_BRENDAN_MACH_BIKE: return &gOutfitJohtoInfo_BrendanMachBike;
    case OBJ_EVENT_GFX_BRENDAN_ACRO_BIKE: return &gOutfitJohtoInfo_BrendanAcroBike;
    case OBJ_EVENT_GFX_BRENDAN_SURFING: return &gOutfitJohtoInfo_BrendanSurfing;
    case OBJ_EVENT_GFX_BRENDAN_UNDERWATER: return &gOutfitJohtoInfo_BrendanUnderwater;
    case OBJ_EVENT_GFX_BRENDAN_FIELD_MOVE: return &gOutfitJohtoInfo_BrendanFieldMove;
    case OBJ_EVENT_GFX_BRENDAN_FISHING: return &gOutfitJohtoInfo_BrendanFishing;
    case OBJ_EVENT_GFX_BRENDAN_WATERING: return &gOutfitJohtoInfo_BrendanWatering;
    case OBJ_EVENT_GFX_BRENDAN_DECORATING: return &gOutfitJohtoInfo_BrendanDecorating;
    case OBJ_EVENT_GFX_LA_BRENDAN_RIDING:
    case OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING: return &gOutfitJohtoInfo_BrendanRiding;
    case OBJ_EVENT_GFX_MAY_NORMAL: return &gOutfitJohtoInfo_MayNormal;
    case OBJ_EVENT_GFX_MAY_MACH_BIKE: return &gOutfitJohtoInfo_MayMachBike;
    case OBJ_EVENT_GFX_MAY_ACRO_BIKE: return &gOutfitJohtoInfo_MayAcroBike;
    case OBJ_EVENT_GFX_MAY_SURFING: return &gOutfitJohtoInfo_MaySurfing;
    case OBJ_EVENT_GFX_MAY_UNDERWATER: return &gOutfitJohtoInfo_MayUnderwater;
    case OBJ_EVENT_GFX_MAY_FIELD_MOVE: return &gOutfitJohtoInfo_MayFieldMove;
    case OBJ_EVENT_GFX_MAY_FISHING: return &gOutfitJohtoInfo_MayFishing;
    case OBJ_EVENT_GFX_MAY_WATERING: return &gOutfitJohtoInfo_MayWatering;
    case OBJ_EVENT_GFX_MAY_DECORATING: return &gOutfitJohtoInfo_MayDecorating;
    case OBJ_EVENT_GFX_LA_MAY_RIDING:
    case OBJ_EVENT_GFX_LA_MAY_WATER_RIDING: return &gOutfitJohtoInfo_MayRiding;
    default: return NULL;
    }
}
