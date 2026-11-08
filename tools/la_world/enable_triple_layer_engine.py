from pathlib import Path
P=Path('/home/allan/projects/Legends-Awakening-Reborn')
f=P/'include/fieldmap.h';s=f.read_text().replace('#define NUM_TILES_PER_METATILE 8','#define NUM_TILES_PER_METATILE 12');f.write_text(s)
f=P/'src/field_camera.c';s=f.read_text();s=s.replace('        DrawMetatile(METATILE_LAYER_TYPE_COVERED, tiles, offset);','''        // Door animation frames still contain eight entries: bottom and middle.
        // Expand only this legacy frame; never read a nonexistent third layer.
        u16 doorTiles[NUM_TILES_PER_METATILE];
        u32 i;
        for (i = 0; i < 8; i++)
            doorTiles[i] = tiles[i];
        for (; i < NUM_TILES_PER_METATILE; i++)
            doorTiles[i] = 0;
        DrawMetatile(METATILE_LAYER_TYPE_COVERED, doorTiles, offset);''');s=s.replace('if (metatileId > NUM_METATILES_TOTAL)','if (metatileId >= NUM_METATILES_TOTAL)')
a=s.index('static void DrawMetatile(s32 metatileLayerType, const u16 *tiles, u16 offset)\n{');b=s.index('\nstatic s32 MapPosToBgTilemapOffset',a)
s=s[:a]+'''static void DrawMetatile(s32 metatileLayerType, const u16 *tiles, u16 offset)
{
    u32 i;
    // Some donor records have undefined legacy layer types. Preserve their old
    // no-draw behavior; valid records now explicitly provide all three layers.
    if (metatileLayerType > METATILE_LAYER_TYPE_SPLIT)
        return;

    for (i = 0; i < 4; i++)
    {
        u16 pos = offset + (i & 1) + (i / 2) * 32;
        gOverworldTilemapBuffer_Bg3[pos] = tiles[i];
        gOverworldTilemapBuffer_Bg2[pos] = tiles[i + 4];
        gOverworldTilemapBuffer_Bg1[pos] = tiles[i + 8];
    }
    ScheduleBgCopyTilemapToVram(1);
    ScheduleBgCopyTilemapToVram(2);
    ScheduleBgCopyTilemapToVram(3);
}
''' +s[b:];f.write_text(s)
f=P/'src/shop.c';s=f.read_text().replace('metatileLayerType = MapGridGetMetatileLayerTypeAt(x + i, y + j);','metatileLayerType = METATILE_LAYER_TYPE_NORMAL;');a=s.index('static void BuyMenuDrawMapMetatile(s16 x, s16 y, const u16 *src, u8 metatileLayerType)\n{');b=s.index('\nstatic void BuyMenuDrawMapMetatileLayer(u16 *dest',a)
s=s[:a]+'''static bool8 IsShopMetatileLayerEmpty(const u16 *src)
{
    u32 i;
    for (i = 0; i < 4; i++)
    {
        // 0x3014 is the stock NORMAL metatile's unused bottom-layer filler.
        if ((src[i] & 0x3FF) != 0 && src[i] != 0x3014)
            return FALSE;
    }
    return TRUE;
}

static void BuyMenuDrawMapMetatile(s16 x, s16 y, const u16 *src, u8 metatileLayerType)
{
    u16 offset1 = x * 2;
    u16 offset2 = y * 64;
    const u16 *bottom = src;
    const u16 *middle = src + 4;

    if (metatileLayerType == METATILE_LAYER_TYPE_NORMAL)
    {
        BuyMenuDrawMapMetatileLayer(sShopData->tilemapBuffers[2], offset1, offset2, src);
        BuyMenuDrawMapMetatileLayer(sShopData->tilemapBuffers[3], offset1, offset2, src + 4);
        BuyMenuDrawMapMetatileLayer(sShopData->tilemapBuffers[1], offset1, offset2, src + 8);
    }
    else
    {
        // The menu occupies BG1. Compact the two occupied layers beneath it.
        // Converted legacy tiles always have an empty (or stock filler) layer.
        if (IsShopMetatileLayerEmpty(src))
        {
            bottom = src + 4;
            middle = src + 8;
        }
        else if (IsShopMetatileLayerEmpty(src + 4))
        {
            middle = src + 8;
        }
        BuyMenuDrawMapMetatileLayer(sShopData->tilemapBuffers[2], offset1, offset2, bottom);
        BuyMenuDrawMapMetatileLayer(sShopData->tilemapBuffers[3], offset1, offset2, middle);
    }
}
''' +s[b:];f.write_text(s)
f=P/'src/decoration.c';s=f.read_text();old='''static u16 GetMetatile(u16 tile)
{
    return gTilesetPointer_SecretBaseRedCave->metatiles[tile] & 0xFFF;
}''';new='''static u16 GetDecorationMetatileEntry(u16 metatileId, u8 legacyIndex)
{
    u32 layerType = ExtractMetatileAttribute(gTilesetPointer_SecretBaseRedCave->metatileAttributes[metatileId], METATILE_ATTRIBUTE_LAYER_TYPE, FALSE);
    u8 index = legacyIndex;
    // Decoration selection sprites still describe the two original layers.
    if (layerType == METATILE_LAYER_TYPE_NORMAL)
        index += 4;
    else if (layerType == METATILE_LAYER_TYPE_SPLIT && index >= 4)
        index += 4;
    return gTilesetPointer_SecretBaseRedCave->metatiles[metatileId * NUM_TILES_PER_METATILE + index];
}

static u16 GetMetatile(u16 tile)
{
    return GetDecorationMetatileEntry(tile / NUM_TILES_PER_METATILE, tile % NUM_TILES_PER_METATILE) & 0xFFF;
}''';assert old in s;s=s.replace(old,new);s=s.replace('gTilesetPointer_SecretBaseRedCave->metatiles[(data->decoration->tiles[0] * NUM_TILES_PER_METATILE) + 7]','GetDecorationMetatileEntry(data->decoration->tiles[0], 7)').replace('gTilesetPointer_SecretBaseRedCave->metatiles[(sPlaceDecorationGraphicsDataBuffer.decoration->tiles[0] * NUM_TILES_PER_METATILE) + 7]','GetDecorationMetatileEntry(sPlaceDecorationGraphicsDataBuffer.decoration->tiles[0], 7)');f.write_text(s)
f=P/'porymap.project.cfg';s=f.read_text().replace('enable_triple_layer_metatiles=0','enable_triple_layer_metatiles=1');f.write_text(s)
print('Engine, animated doors, shops, decoration previews and Porymap configured for 12-entry metatiles.')
