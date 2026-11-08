// WesleyFG ocean texture: four native-pixel phases, isolated from all other tile banks.
static const u16 sUnovaOceanFrame0[] = INCBIN_U16("data/tilesets/primary/unova_general/anim/water/0.4bpp");
static const u16 sUnovaOceanFrame1[] = INCBIN_U16("data/tilesets/primary/unova_general/anim/water/1.4bpp");
static const u16 sUnovaOceanFrame2[] = INCBIN_U16("data/tilesets/primary/unova_general/anim/water/2.4bpp");
static const u16 sUnovaOceanFrame3[] = INCBIN_U16("data/tilesets/primary/unova_general/anim/water/3.4bpp");

static const u16 *const sUnovaOceanFrames[] = {
    sUnovaOceanFrame0, sUnovaOceanFrame1, sUnovaOceanFrame2, sUnovaOceanFrame3
};

static void TilesetAnim_UnovaGeneral(u16 timer)
{
    if (timer % 16 == 0)
        AppendTilesetAnimToBuffer(sUnovaOceanFrames[(timer / 16) % 4],
            (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(384)), 16 * TILE_SIZE_4BPP);
}

void InitTilesetAnim_UnovaGeneral(void)
{
    sPrimaryTilesetAnimCounter = 0;
    sPrimaryTilesetAnimCounterMax = 64;
    sPrimaryTilesetAnimCallback = TilesetAnim_UnovaGeneral;
}
