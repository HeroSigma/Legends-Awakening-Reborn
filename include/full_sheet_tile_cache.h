#ifndef GUARD_FULL_SHEET_TILE_CACHE_H
#define GUARD_FULL_SHEET_TILE_CACHE_H
#include <stdint.h>
#define FULL_SHEET_CACHE_SLOTS 1024
#define FULL_SHEET_TILE_NONE 65535
struct FullSheetTileCache
{
    uint16_t virtualIds[FULL_SHEET_CACHE_SLOTS];
    uint16_t references[FULL_SHEET_CACHE_SLOTS];
    uint32_t dirty[FULL_SHEET_CACHE_SLOTS / 32];
    uint16_t *mapping;
    uint16_t tileCount;
    uint16_t cursor;
};
void FullSheetCacheInit(struct FullSheetTileCache *cache, uint16_t *mapping, uint16_t count);
void FullSheetCacheRelease(struct FullSheetTileCache *cache, uint16_t slot);
uint16_t FullSheetCacheAcquire(struct FullSheetTileCache *cache, uint16_t virtualId);
#endif
