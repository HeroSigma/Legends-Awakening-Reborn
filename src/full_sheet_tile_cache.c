#include "full_sheet_tile_cache.h"

void FullSheetCacheInit(struct FullSheetTileCache *cache, uint16_t *mapping, uint16_t count)
{
    unsigned i;
    cache->mapping = mapping;
    cache->tileCount = count;
    cache->cursor = 1;
    for (i = 0; i < count; i++)
        mapping[i] = FULL_SHEET_TILE_NONE;
    for (i = 0; i < FULL_SHEET_CACHE_SLOTS; i++)
    {
        cache->virtualIds[i] = FULL_SHEET_TILE_NONE;
        cache->references[i] = 0;
    }
    for (i = 0; i < FULL_SHEET_CACHE_SLOTS / 32; i++)
        cache->dirty[i] = 0;
    mapping[0] = 0;
    cache->virtualIds[0] = 0;
    cache->dirty[0] = 1;
}

void FullSheetCacheRelease(struct FullSheetTileCache *cache, uint16_t slot)
{
    if (slot && slot < FULL_SHEET_CACHE_SLOTS && cache->references[slot])
        cache->references[slot]--;
}

uint16_t FullSheetCacheAcquire(struct FullSheetTileCache *cache, uint16_t virtualId)
{
    unsigned i;
    uint16_t slot, old;
    if (!virtualId)
        return 0;
    if (virtualId >= cache->tileCount)
        return FULL_SHEET_TILE_NONE;
    slot = cache->mapping[virtualId];
    if (slot != FULL_SHEET_TILE_NONE)
    {
        cache->references[slot]++;
        return slot;
    }
    for (i = 0; i < FULL_SHEET_CACHE_SLOTS - 1; i++)
    {
        slot = cache->cursor++;
        if (cache->cursor == FULL_SHEET_CACHE_SLOTS)
            cache->cursor = 1;
        if (cache->references[slot])
            continue;
        old = cache->virtualIds[slot];
        if (old != FULL_SHEET_TILE_NONE)
            cache->mapping[old] = FULL_SHEET_TILE_NONE;
        cache->mapping[virtualId] = slot;
        cache->virtualIds[slot] = virtualId;
        cache->references[slot] = 1;
        cache->dirty[slot / 32] |= (uint32_t)1 << (slot % 32);
        return slot;
    }
    return FULL_SHEET_TILE_NONE;
}
