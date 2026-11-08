// Ruby/Sapphire outfits: Modern Emerald / resetes12. See docs/features/player-outfits.
const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanNormal = {
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
    .images = sOutfitRsFrames_BrendanNormal,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanMachBike = {
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
    .images = sOutfitRsFrames_BrendanMachBike,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanAcroBike = {
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
    .images = sOutfitRsFrames_BrendanAcroBike,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanSurfing = {
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
    .images = sOutfitRsFrames_BrendanSurfing,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanUnderwater = {
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
    .images = sOutfitRsFrames_BrendanUnderwater,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanFieldMove = {
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
    .images = sOutfitRsFrames_BrendanFieldMove,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanFishing = {
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
    .images = sOutfitRsFrames_BrendanFishing,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanWatering = {
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
    .images = sOutfitRsFrames_BrendanWatering,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanDecorating = {
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
    .images = sOutfitRsFrames_BrendanDecorating,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_BrendanRiding = {
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
    .images = sOutfitRsFrames_BrendanRiding,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayNormal = {
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
    .images = sOutfitRsFrames_MayNormal,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayMachBike = {
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
    .images = sOutfitRsFrames_MayMachBike,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayAcroBike = {
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
    .images = sOutfitRsFrames_MayAcroBike,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MaySurfing = {
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
    .images = sOutfitRsFrames_MaySurfing,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayUnderwater = {
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
    .images = sOutfitRsFrames_MayUnderwater,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayFieldMove = {
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
    .images = sOutfitRsFrames_MayFieldMove,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayFishing = {
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
    .images = sOutfitRsFrames_MayFishing,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayWatering = {
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
    .images = sOutfitRsFrames_MayWatering,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayDecorating = {
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
    .images = sOutfitRsFrames_MayDecorating,
};

const struct ObjectEventGraphicsInfo gOutfitRsInfo_MayRiding = {
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
    .images = sOutfitRsFrames_MayRiding,
};

static const struct ObjectEventGraphicsInfo *GetPlayerOutfitGraphics(u16 graphicsId)
{
    if (!PlayerOutfit_Get()) return NULL;
    switch (graphicsId)
    {
    case OBJ_EVENT_GFX_BRENDAN_NORMAL: return &gOutfitRsInfo_BrendanNormal;
    case OBJ_EVENT_GFX_BRENDAN_MACH_BIKE: return &gOutfitRsInfo_BrendanMachBike;
    case OBJ_EVENT_GFX_BRENDAN_ACRO_BIKE: return &gOutfitRsInfo_BrendanAcroBike;
    case OBJ_EVENT_GFX_BRENDAN_SURFING: return &gOutfitRsInfo_BrendanSurfing;
    case OBJ_EVENT_GFX_BRENDAN_UNDERWATER: return &gOutfitRsInfo_BrendanUnderwater;
    case OBJ_EVENT_GFX_BRENDAN_FIELD_MOVE: return &gOutfitRsInfo_BrendanFieldMove;
    case OBJ_EVENT_GFX_BRENDAN_FISHING: return &gOutfitRsInfo_BrendanFishing;
    case OBJ_EVENT_GFX_BRENDAN_WATERING: return &gOutfitRsInfo_BrendanWatering;
    case OBJ_EVENT_GFX_BRENDAN_DECORATING: return &gOutfitRsInfo_BrendanDecorating;
    case OBJ_EVENT_GFX_LA_BRENDAN_RIDING:
    case OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING: return &gOutfitRsInfo_BrendanRiding;
    case OBJ_EVENT_GFX_MAY_NORMAL: return &gOutfitRsInfo_MayNormal;
    case OBJ_EVENT_GFX_MAY_MACH_BIKE: return &gOutfitRsInfo_MayMachBike;
    case OBJ_EVENT_GFX_MAY_ACRO_BIKE: return &gOutfitRsInfo_MayAcroBike;
    case OBJ_EVENT_GFX_MAY_SURFING: return &gOutfitRsInfo_MaySurfing;
    case OBJ_EVENT_GFX_MAY_UNDERWATER: return &gOutfitRsInfo_MayUnderwater;
    case OBJ_EVENT_GFX_MAY_FIELD_MOVE: return &gOutfitRsInfo_MayFieldMove;
    case OBJ_EVENT_GFX_MAY_FISHING: return &gOutfitRsInfo_MayFishing;
    case OBJ_EVENT_GFX_MAY_WATERING: return &gOutfitRsInfo_MayWatering;
    case OBJ_EVENT_GFX_MAY_DECORATING: return &gOutfitRsInfo_MayDecorating;
    case OBJ_EVENT_GFX_LA_MAY_RIDING:
    case OBJ_EVENT_GFX_LA_MAY_WATER_RIDING: return &gOutfitRsInfo_MayRiding;
    default: return NULL;
    }
}
