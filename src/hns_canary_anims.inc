// Graphical callbacks adapted from Heart & Soul; no gameplay.
static void HnSCanary_TilesetAnim_JohtoGeneral(u16);
static void HnSCanary_QueueAnimTiles_JohtoGeneral_Flower(u16);
static void HnSCanary_QueueAnimTiles_JohtoGeneral_SandWaterEdge(u16);
static void HnSCanary_QueueAnimTiles_JohtoGeneral_Waterfall(u16);
static void HnSCanary_QueueAnimTiles_JohtoGeneral_LandWaterEdge(u16);
static void HnSCanary_TilesetAnim_EcruteakTheater(u16);
static void HnSCanary_QueueAnimTiles_EcruteakTheater_Flower(u16);
// Johto General primary tileset frame data

static const u16 HnSCanary_sJohtoGeneral_Flower_Frame0[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/flower/0.4bpp");
static const u16 HnSCanary_sJohtoGeneral_Flower_Frame1[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/flower/1.4bpp");
static const u16 HnSCanary_sJohtoGeneral_Flower_Frame2[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/flower/2.4bpp");
static const u16 HnSCanary_sJohtoGeneral_Flower_Frame3[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/flower/3.4bpp");
static const u16 HnSCanary_sJohtoGeneral_Flower_Frame4[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/flower/4.4bpp");

static const u16 *const HnSCanary_sJohtoGeneral_Flower[] = {
    HnSCanary_sJohtoGeneral_Flower_Frame0,
    HnSCanary_sJohtoGeneral_Flower_Frame1,
    HnSCanary_sJohtoGeneral_Flower_Frame2,
    HnSCanary_sJohtoGeneral_Flower_Frame3,
    HnSCanary_sJohtoGeneral_Flower_Frame4
};

static const u16 HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame0[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/water_current_landwatersedge/0.4bpp");
static const u16 HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame1[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/water_current_landwatersedge/1.4bpp");
static const u16 HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame2[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/water_current_landwatersedge/2.4bpp");
static const u16 HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame3[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/water_current_landwatersedge/3.4bpp");
static const u16 HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame4[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/water_current_landwatersedge/4.4bpp");
static const u16 HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame5[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/water_current_landwatersedge/5.4bpp");
static const u16 HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame6[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/water_current_landwatersedge/6.4bpp");
static const u16 HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame7[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/water_current_landwatersedge/7.4bpp");

static const u16 *const HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge[] = {
    HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame0,
    HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame1,
    HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame2,
    HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame3,
    HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame4,
    HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame5,
    HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame6,
    HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge_Frame7
};

static const u16 HnSCanary_sJohtoGeneral_SandWatersEdge_Frame0[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/sandwatersedge/0.4bpp");
static const u16 HnSCanary_sJohtoGeneral_SandWatersEdge_Frame1[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/sandwatersedge/1.4bpp");
static const u16 HnSCanary_sJohtoGeneral_SandWatersEdge_Frame2[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/sandwatersedge/2.4bpp");
static const u16 HnSCanary_sJohtoGeneral_SandWatersEdge_Frame3[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/sandwatersedge/3.4bpp");
static const u16 HnSCanary_sJohtoGeneral_SandWatersEdge_Frame4[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/sandwatersedge/4.4bpp");
static const u16 HnSCanary_sJohtoGeneral_SandWatersEdge_Frame5[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/sandwatersedge/5.4bpp");
static const u16 HnSCanary_sJohtoGeneral_SandWatersEdge_Frame6[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/sandwatersedge/6.4bpp");
static const u16 HnSCanary_sJohtoGeneral_SandWatersEdge_Frame7[] = INCBIN_U16("data/hns_canary_assets/anim/primary/johto_general_hns/anim/sandwatersedge/7.4bpp");

static const u16 *const HnSCanary_sJohtoGeneral_SandWatersEdge[] = {
    HnSCanary_sJohtoGeneral_SandWatersEdge_Frame0,
    HnSCanary_sJohtoGeneral_SandWatersEdge_Frame1,
    HnSCanary_sJohtoGeneral_SandWatersEdge_Frame2,
    HnSCanary_sJohtoGeneral_SandWatersEdge_Frame3,
    HnSCanary_sJohtoGeneral_SandWatersEdge_Frame4,
    HnSCanary_sJohtoGeneral_SandWatersEdge_Frame5,
    HnSCanary_sJohtoGeneral_SandWatersEdge_Frame6,
    HnSCanary_sJohtoGeneral_SandWatersEdge_Frame7
};

static const u16 HnSCanary_sEcruteakTheater_Flower_Frame0[] = INCBIN_U16("data/hns_canary_assets/anim/secondary/ecruteak_theater_hns/anim/flower/0.4bpp");
static const u16 HnSCanary_sEcruteakTheater_Flower_Frame1[] = INCBIN_U16("data/hns_canary_assets/anim/secondary/ecruteak_theater_hns/anim/flower/1.4bpp");
static const u16 HnSCanary_sEcruteakTheater_Flower_Frame2[] = INCBIN_U16("data/hns_canary_assets/anim/secondary/ecruteak_theater_hns/anim/flower/2.4bpp");
static const u16 HnSCanary_sEcruteakTheater_Flower_Frame3[] = INCBIN_U16("data/hns_canary_assets/anim/secondary/ecruteak_theater_hns/anim/flower/3.4bpp");
static const u16 HnSCanary_sEcruteakTheater_Flower_Frame4[] = INCBIN_U16("data/hns_canary_assets/anim/secondary/ecruteak_theater_hns/anim/flower/4.4bpp");

static const u16 *const HnSCanary_sEcruteakTheater_Flower[] = {
    HnSCanary_sEcruteakTheater_Flower_Frame0,
    HnSCanary_sEcruteakTheater_Flower_Frame1,
    HnSCanary_sEcruteakTheater_Flower_Frame2,
    HnSCanary_sEcruteakTheater_Flower_Frame3,
    HnSCanary_sEcruteakTheater_Flower_Frame4
};

// Johto General primary tileset callbacks

void HnSCanary_InitTilesetAnim_JohtoGeneral(void)
{
    sPrimaryTilesetAnimCounter = 0;
    sPrimaryTilesetAnimCounterMax = 256;
    sPrimaryTilesetAnimCallback = HnSCanary_TilesetAnim_JohtoGeneral;
}

static void HnSCanary_TilesetAnim_JohtoGeneral(u16 timer)
{
    if (timer % 8 == 0)
        HnSCanary_QueueAnimTiles_JohtoGeneral_SandWaterEdge(timer >> 3);
    if (timer % 16 == 1)
        HnSCanary_QueueAnimTiles_JohtoGeneral_LandWaterEdge(timer >> 4);
    if (timer % 16 == 2)
        HnSCanary_QueueAnimTiles_JohtoGeneral_Flower(timer >> 4);
    if (timer % 16 == 3)
        HnSCanary_QueueAnimTiles_JohtoGeneral_Waterfall(timer / 16);
}

static void HnSCanary_QueueAnimTiles_JohtoGeneral_Flower(u16 timer)
{
    u16 i = timer % ARRAY_COUNT(HnSCanary_sJohtoGeneral_Flower);
    AppendTilesetAnimToBuffer(HnSCanary_sJohtoGeneral_Flower[i], (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(508)), 4 * TILE_SIZE_4BPP);
}

static void HnSCanary_QueueAnimTiles_JohtoGeneral_SandWaterEdge(u16 timer)
{
    u16 i = timer % ARRAY_COUNT(HnSCanary_sJohtoGeneral_SandWatersEdge);
    AppendTilesetAnimToBuffer(HnSCanary_sJohtoGeneral_SandWatersEdge[i], (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(416)), 18 * TILE_SIZE_4BPP);
}

static void HnSCanary_QueueAnimTiles_JohtoGeneral_Waterfall(u16 timer)
{
    u16 i = timer % ARRAY_COUNT(HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge);
    const u16 *frame = HnSCanary_sJohtoGeneral_WaterCurrentLandWatersEdge[i];
    const u16 *src = frame + (34 * (TILE_SIZE_4BPP / 2));
    AppendTilesetAnimToBuffer(src, (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(450)), 12 * TILE_SIZE_4BPP);
}

static void HnSCanary_QueueAnimTiles_JohtoGeneral_LandWaterEdge(u16 timer)
{
    return;
}

// Ecruteak Theater secondary tileset callbacks

void HnSCanary_InitTilesetAnim_EcruteakTheater(void)
{
    sSecondaryTilesetAnimCounter = 0;
    sSecondaryTilesetAnimCounterMax = 960;
    sSecondaryTilesetAnimCallback = HnSCanary_TilesetAnim_EcruteakTheater;
}

static void HnSCanary_TilesetAnim_EcruteakTheater(u16 timer)
{
    if (timer % 10 == 0)
        HnSCanary_QueueAnimTiles_EcruteakTheater_Flower(timer / 10);
}

static void HnSCanary_QueueAnimTiles_EcruteakTheater_Flower(u16 timer)
{
    AppendTilesetAnimToBuffer(HnSCanary_sEcruteakTheater_Flower[timer % ARRAY_COUNT(HnSCanary_sEcruteakTheater_Flower)], (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(640 + 104)), 0x80);
}

