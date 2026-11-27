// Ruby/Sapphire outfits: Modern Emerald / resetes12. See docs/features/player-outfits.
const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanNormal = {
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
    .images = sOutfitClassicFrames_BrendanNormal,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanMachBike = {
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
    .images = sOutfitClassicFrames_BrendanMachBike,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanAcroBike = {
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
    .images = sOutfitClassicFrames_BrendanAcroBike,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanSurfing = {
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
    .images = sOutfitClassicFrames_BrendanSurfing,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanUnderwater = {
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
    .images = sOutfitClassicFrames_BrendanUnderwater,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanFieldMove = {
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
    .images = sOutfitClassicFrames_BrendanFieldMove,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanFishing = {
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
    .images = sOutfitClassicFrames_BrendanFishing,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanWatering = {
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
    .images = sOutfitClassicFrames_BrendanWatering,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanDecorating = {
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
    .images = sOutfitClassicFrames_BrendanDecorating,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_BrendanRiding = {
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
    .images = sOutfitClassicFrames_BrendanRiding,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayNormal = {
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
    .images = sOutfitClassicFrames_MayNormal,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayMachBike = {
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
    .images = sOutfitClassicFrames_MayMachBike,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayAcroBike = {
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
    .images = sOutfitClassicFrames_MayAcroBike,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MaySurfing = {
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
    .images = sOutfitClassicFrames_MaySurfing,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayUnderwater = {
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
    .images = sOutfitClassicFrames_MayUnderwater,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayFieldMove = {
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
    .images = sOutfitClassicFrames_MayFieldMove,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayFishing = {
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
    .images = sOutfitClassicFrames_MayFishing,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayWatering = {
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
    .images = sOutfitClassicFrames_MayWatering,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayDecorating = {
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
    .images = sOutfitClassicFrames_MayDecorating,
};

const struct ObjectEventGraphicsInfo gOutfitClassicInfo_MayRiding = {
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
    .images = sOutfitClassicFrames_MayRiding,
};

static const struct ObjectEventGraphicsInfo *GetClassicPlayerGraphics(u16 graphicsId)
{
    switch (graphicsId)
    {
    case OBJ_EVENT_GFX_BRENDAN_NORMAL: return &gOutfitClassicInfo_BrendanNormal;
    case OBJ_EVENT_GFX_BRENDAN_MACH_BIKE: return &gOutfitClassicInfo_BrendanMachBike;
    case OBJ_EVENT_GFX_BRENDAN_ACRO_BIKE: return &gOutfitClassicInfo_BrendanAcroBike;
    case OBJ_EVENT_GFX_BRENDAN_SURFING: return &gOutfitClassicInfo_BrendanSurfing;
    case OBJ_EVENT_GFX_BRENDAN_UNDERWATER: return &gOutfitClassicInfo_BrendanUnderwater;
    case OBJ_EVENT_GFX_BRENDAN_FIELD_MOVE: return &gOutfitClassicInfo_BrendanFieldMove;
    case OBJ_EVENT_GFX_BRENDAN_FISHING: return &gOutfitClassicInfo_BrendanFishing;
    case OBJ_EVENT_GFX_BRENDAN_WATERING: return &gOutfitClassicInfo_BrendanWatering;
    case OBJ_EVENT_GFX_BRENDAN_DECORATING: return &gOutfitClassicInfo_BrendanDecorating;
    case OBJ_EVENT_GFX_LA_BRENDAN_RIDING:
    case OBJ_EVENT_GFX_LA_BRENDAN_WATER_RIDING: return &gOutfitClassicInfo_BrendanRiding;
    case OBJ_EVENT_GFX_MAY_NORMAL: return &gOutfitClassicInfo_MayNormal;
    case OBJ_EVENT_GFX_MAY_MACH_BIKE: return &gOutfitClassicInfo_MayMachBike;
    case OBJ_EVENT_GFX_MAY_ACRO_BIKE: return &gOutfitClassicInfo_MayAcroBike;
    case OBJ_EVENT_GFX_MAY_SURFING: return &gOutfitClassicInfo_MaySurfing;
    case OBJ_EVENT_GFX_MAY_UNDERWATER: return &gOutfitClassicInfo_MayUnderwater;
    case OBJ_EVENT_GFX_MAY_FIELD_MOVE: return &gOutfitClassicInfo_MayFieldMove;
    case OBJ_EVENT_GFX_MAY_FISHING: return &gOutfitClassicInfo_MayFishing;
    case OBJ_EVENT_GFX_MAY_WATERING: return &gOutfitClassicInfo_MayWatering;
    case OBJ_EVENT_GFX_MAY_DECORATING: return &gOutfitClassicInfo_MayDecorating;
    case OBJ_EVENT_GFX_LA_MAY_RIDING:
    case OBJ_EVENT_GFX_LA_MAY_WATER_RIDING: return &gOutfitClassicInfo_MayRiding;
    default: return NULL;
    }
}
