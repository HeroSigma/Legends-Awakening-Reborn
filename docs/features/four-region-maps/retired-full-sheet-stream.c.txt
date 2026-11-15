#include "global.h"
#include "malloc.h"
#include "fieldmap.h"
#include "full_sheet_stream.h"
#include "full_sheet_tile_cache.h"
#include "menu.h"
#include "overworld.h"

extern const struct Tileset gTileset_AccumulaFullSheetTest_Primary;
extern const struct Tileset gTileset_AccumulaFullSheetTest_Secondary;

static const u32 sAccumulaGraphics[] = INCBIN_U32("data/full_sheet/accumula_test/tiles.4bpp");
static const u32 sAccumulaPrimary[] = INCBIN_U32("data/tilesets/primary/accumula_fullsheet_test/metatiles.extended.bin");
static const u32 sAccumulaSecondary[] = INCBIN_U32("data/tilesets/secondary/accumula_fullsheet_test/metatiles.extended.bin");

extern const struct Tileset gTileset_NuvemaFullSheetTest_Primary;
extern const struct Tileset gTileset_NuvemaFullSheetTest_Secondary;

static const u32 sNuvemaGraphics[] = INCBIN_U32("data/full_sheet/nuvema_test/tiles.4bpp");
static const u32 sNuvemaPrimary[] = INCBIN_U32("data/tilesets/primary/nuvema_fullsheet_test/metatiles.extended.bin");
static const u32 sNuvemaSecondary[] = INCBIN_U32("data/tilesets/secondary/nuvema_fullsheet_test/metatiles.extended.bin");

// A virtual tile ID is 16 bits. Flip bits are 16/17; palette occupies 18..21.
// Hardware references are generated only for the resident camera buffer.
struct FullSheetStreamData
{
    const struct Tileset *primary;
    const struct Tileset *secondary;
    const u32 *graphics;
    const u32 *primaryMetatiles;
    const u32 *secondaryMetatiles;
    u16 tileCount;
    u16 primaryCount;
    u16 secondaryCount;
};
static const struct FullSheetStreamData sStreams[] =
{
    { &gTileset_AccumulaFullSheetTest_Primary, &gTileset_AccumulaFullSheetTest_Secondary,
      sAccumulaGraphics, sAccumulaPrimary, sAccumulaSecondary,
      sizeof(sAccumulaGraphics) / 32, sizeof(sAccumulaPrimary) / 48, sizeof(sAccumulaSecondary) / 48 },
    { &gTileset_NuvemaFullSheetTest_Primary, &gTileset_NuvemaFullSheetTest_Secondary,
      sNuvemaGraphics, sNuvemaPrimary, sNuvemaSecondary,
      sizeof(sNuvemaGraphics) / 32, sizeof(sNuvemaPrimary) / 48, sizeof(sNuvemaSecondary) / 48 },
};
static EWRAM_DATA struct FullSheetTileCache sCache = {0};
static EWRAM_DATA const struct FullSheetStreamData *sStream = NULL;
static EWRAM_DATA bool8 sReady = FALSE;
// Exposed in the ELF for emulator/debugger validation. An export must pass its
// camera residency check; a nonzero value signals an invalid runtime package.
EWRAM_DATA u32 gFullSheetStreamFailures = 0;
EWRAM_DATA u32 gFullSheetStreamUploads = 0;

bool8 FullSheetStreamActive(void)
{
    return sStream != NULL;
}

bool8 FullSheetStreamOwnsTileset(const struct Tileset *tileset)
{
    unsigned i;
    for (i = 0; i < ARRAY_COUNT(sStreams); i++)
        if (tileset == sStreams[i].primary || tileset == sStreams[i].secondary)
            return TRUE;
    return FALSE;
}

// Call before resetting the heap: cached tile mappings belong to that heap.
void FullSheetStreamRelease(void)
{
    sReady = FALSE;
    sStream = NULL;
    if (sCache.mapping)
    {
        Free(sCache.mapping);
        sCache.mapping = NULL;
    }
}

bool8 FullSheetStreamLoad(const struct MapLayout *layout)
{
    unsigned i;
    u16 *mapping;
    sReady = FALSE;
    sStream = NULL;
    if (sCache.mapping)
    {
        Free(sCache.mapping);
        sCache.mapping = NULL;
    }
    for (i = 0; i < ARRAY_COUNT(sStreams); i++)
    {
        if (layout && layout->primaryTileset == sStreams[i].primary && layout->secondaryTileset == sStreams[i].secondary)
        {
            mapping = Alloc(sStreams[i].tileCount * sizeof(u16));
            if (!mapping)
            {
                gFullSheetStreamFailures++;
                return TRUE;
            }
            FullSheetCacheInit(&sCache, mapping, sStreams[i].tileCount);
            sStream = &sStreams[i];
            return TRUE;
        }
    }
    return FALSE;
}

bool8 FullSheetStreamDraw(const struct MapLayout *layout, u16 metatileId, u16 offset)
{
    const u32 *record;
    u16 *buffers[3];
    unsigned layer, q;
    u16 pos, slot;
    u32 ref;
    if (!sStream || layout->primaryTileset != sStream->primary || layout->secondaryTileset != sStream->secondary)
        return FALSE;
    if (metatileId < sStream->primaryCount)
        record = sStream->primaryMetatiles + metatileId * 12;
    else if (metatileId - sStream->primaryCount < sStream->secondaryCount)
        record = sStream->secondaryMetatiles + (metatileId - sStream->primaryCount) * 12;
    else
        record = sStream->primaryMetatiles;
    buffers[0] = gOverworldTilemapBuffer_Bg3;
    buffers[1] = gOverworldTilemapBuffer_Bg2;
    buffers[2] = gOverworldTilemapBuffer_Bg1;
    for (layer = 0; layer < 3; layer++)
        for (q = 0; q < 4; q++)
        {
            pos = offset + (q & 1) + (q / 2) * 32;
            FullSheetCacheRelease(&sCache, buffers[layer][pos] & 1023);
        }
    for (layer = 0; layer < 3; layer++)
        for (q = 0; q < 4; q++)
        {
            pos = offset + (q & 1) + (q / 2) * 32;
            ref = record[layer * 4 + q];
            slot = FullSheetCacheAcquire(&sCache, ref & 65535);
            if (slot == FULL_SHEET_TILE_NONE)
            {
                gFullSheetStreamFailures++;
                slot = 0;
            }
            buffers[layer][pos] = slot | ((ref >> 6) & 0xFC00);
        }
    ScheduleBgCopyTilemapToVram(1);
    ScheduleBgCopyTilemapToVram(2);
    ScheduleBgCopyTilemapToVram(3);
    return TRUE;
}

void FullSheetStreamCommit(void)
{
    if (sStream)
        sReady = TRUE;
}

void FullSheetStreamVBlank(void)
{
    unsigned word, bit, slot;
    u32 dirty;
    if (!sStream || !sReady)
        return;
    sReady = FALSE;
    // Runs before the engine's queued tilemap DMA, so graphics and references
    // become visible together. Only changed 32-byte slots are transferred.
    for (word = 0; word < FULL_SHEET_CACHE_SLOTS / 32; word++)
    {
        dirty = sCache.dirty[word];
        sCache.dirty[word] = 0;
        if (!dirty)
            continue;
        for (bit = 0; bit < 32; bit++)
            if (dirty & ((u32)1 << bit))
            {
                slot = word * 32 + bit;
                DmaCopy32(3, sStream->graphics + sCache.virtualIds[slot] * 8, (void *)(VRAM + slot * 32), 32);
                gFullSheetStreamUploads++;
            }
    }
}
