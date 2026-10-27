#include "global.h"
#include "pokemon_storage_system.h"
#include "../tools/la_world/storage/reborn_pc_bank.h"
#include <string.h>
#include <stddef.h>
#include "la_pc_storage_fast.h"
#include "constants/species.h"
EWRAM_DATA static struct LaPcBankContext sStorageContext = {0};
struct LegacyStorage {
    u8 currentBox;
    struct BoxPokemon boxes[14][30];
    u8 names[14][9];
    u8 wallpapers[14];
    struct Pokemon fusions[4];
};
STATIC_ASSERT(sizeof(struct PokemonStorage) == sizeof(struct LaPcBank), PcBankSize);
STATIC_ASSERT(offsetof(struct PokemonStorage, boxes) == offsetof(struct LaPcBank, records), PcBankRecords);
STATIC_ASSERT(offsetof(struct PokemonStorage, boxNames) == offsetof(struct LaPcBank, names), PcBankNames);
STATIC_ASSERT(offsetof(struct PokemonStorage, fusions) == offsetof(struct LaPcBank, fusions), PcBankFusions);
STATIC_ASSERT(sizeof(struct LegacyStorage) == 34144, PcLegacySize);
static struct LaPcBankContext *Context(void)
{
    if (sStorageContext.bank != (struct LaPcBank *)gPokemonStoragePtr)
        LaPcBankBind(&sStorageContext, (struct LaPcBank *)gPokemonStoragePtr);
    return &sStorageContext;
}
u32 GetStorageBoxCount(void) { return StorageIsCollectionMode() ? 60 : 14; }
bool32 StorageIsCollectionMode(void) { return gPokemonStoragePtr != NULL && gPokemonStoragePtr->version == 2 && gPokemonStoragePtr->mode == 1; }
bool32 StorageFlush(void) { return gPokemonStoragePtr->version != 2 || LaPcBankFlush(Context()); }
void StorageInvalidateCache(void) { LaPcBankBind(&sStorageContext, (struct LaPcBank *)gPokemonStoragePtr); }
void StorageInitialize(void) { LaPcBankClear(Context(), LA_PC_NORMAL_MODE); }
bool32 StorageHasBoxedFusion(void)
{
    u32 i, box, slot;
    bool32 active = FALSE;
    for (i = 0; i < 4; i++) if (gPokemonStoragePtr->fusions[i].level) active = TRUE;
    if (!active) return FALSE;
    for (box = 0; box < GetStorageBoxCount(); box++) for (slot = 0; slot < 30; slot++) {
        enum Species species = GetBoxMonDataAt(box, slot, MON_DATA_SPECIES);
        enum Species base;
        if (!species) continue;
        base = GET_BASE_SPECIES_ID(species);
        if (species != base && (base == SPECIES_KYUREM || base == SPECIES_NECROZMA || base == SPECIES_CALYREX)) return TRUE;
    }
    return FALSE;
}
bool32 StorageChangeMode(u32 mode, bool32 confirmed)
{
    if (confirmed && mode != gPokemonStoragePtr->mode && StorageHasBoxedFusion()) return FALSE;
    return LaPcBankChangeMode(Context(), mode, confirmed);
}
bool32 StorageReadMon(u32 box, u32 slot, struct BoxPokemon *out) { return LaPcBankRead(Context(), box, slot, out); }
bool32 StorageWriteMon(u32 box, u32 slot, const struct BoxPokemon *in) { return LaPcBankSet(Context(), box, slot, in); }
struct BoxPokemon *StorageGetMon(u32 box, u32 slot) { return LaPcBankGet(Context(), box, slot); }
bool32 StorageIsBoxPointer(const void *ptr)
{
    u32 address = (u32)ptr;
    u32 native = (u32)gPokemonStoragePtr->boxes;
    u32 cache = (u32)&sStorageContext.cache[0];
    if (StorageIsCollectionMode()) return address >= cache && address < cache + sizeof(sStorageContext.cache);
    return address >= native && address < native + sizeof(gPokemonStoragePtr->boxes);
}
u32 StorageLegacySize(void) { return sizeof(struct LegacyStorage); }
static u8 *LegacyByte(u32 offset)
{
    if (offset == 0) return &gPokemonStoragePtr->currentBox;
    if (offset >= offsetof(struct LegacyStorage, boxes) && offset < offsetof(struct LegacyStorage, names))
        return (u8 *)gPokemonStoragePtr->boxes + offset - offsetof(struct LegacyStorage, boxes);
    if (offset >= offsetof(struct LegacyStorage, names) && offset < offsetof(struct LegacyStorage, wallpapers))
        return (u8 *)gPokemonStoragePtr->boxNames + offset - offsetof(struct LegacyStorage, names);
    if (offset >= offsetof(struct LegacyStorage, wallpapers) && offset < offsetof(struct LegacyStorage, wallpapers) + 14)
        return gPokemonStoragePtr->boxWallpapers + offset - offsetof(struct LegacyStorage, wallpapers);
    if (offset >= offsetof(struct LegacyStorage, fusions) && offset < sizeof(struct LegacyStorage))
        return (u8 *)gPokemonStoragePtr->fusions + offset - offsetof(struct LegacyStorage, fusions);
    return NULL;
}
void StorageLegacyRead(void *out, u32 offset, u32 size)
{
    u8 *dst = out;
    while (size--) { u8 *p = LegacyByte(offset++); *dst++ = p == NULL ? 0 : *p; }
}
void StorageLegacyWrite(const void *in, u32 offset, u32 size)
{
    const u8 *src = in;
    while (size--) { u8 *p = LegacyByte(offset++); if (p != NULL) *p = *src; src++; }
}

bool32 StorageTryGetData(u32 box, u32 slot, s32 request, u32 *value)
{
    struct LaPcBankContext *ctx;
    const u8 *record;
    u32 species;
    bool32 egg;
    if (!StorageIsCollectionMode()) return FALSE;
    switch (request) {
    case MON_DATA_SPECIES: case MON_DATA_SPECIES_OR_EGG:
    case MON_DATA_SANITY_HAS_SPECIES: case MON_DATA_SANITY_IS_BAD_EGG:
    case MON_DATA_SANITY_IS_EGG: case MON_DATA_IS_EGG:
    case MON_DATA_MOVE1: case MON_DATA_MOVE2: case MON_DATA_MOVE3: case MON_DATA_MOVE4:
    case MON_DATA_HELD_ITEM:
        break;
    default: return FALSE;
    }
    if (box >= 60 || slot >= 30) { *value = 0; return TRUE; }
    ctx = Context();
    if (ctx->cacheValid && ctx->cachedBox == box) {
        *value = GetBoxMonData(&ctx->cache[slot], request);
        return TRUE;
    }
    record = ctx->bank->records.compact[box][slot];
    species = LaPcPeekSpecies(record);
    if (species >= NUM_SPECIES) return FALSE;
    egg = LaPcPeekEgg(record);
    switch (request) {
    case MON_DATA_SPECIES: *value = species; break;
    case MON_DATA_SPECIES_OR_EGG: *value = egg ? SPECIES_EGG : species; break;
    case MON_DATA_SANITY_HAS_SPECIES: *value = species != 0; break;
    case MON_DATA_SANITY_IS_BAD_EGG: *value = 0; break;
    case MON_DATA_IS_EGG: case MON_DATA_SANITY_IS_EGG: *value = egg; break;
    case MON_DATA_HELD_ITEM: *value = LaPcPeekItem(record); break;
    default: *value = LaPcPeekMove(record, request - MON_DATA_MOVE1); break;
    }
    return TRUE;
}
void StorageHealCollectionCache(void)
{
    struct LaPcBankContext *ctx = Context();
    u32 slot;
    if (ctx->cacheValid) for (slot = 0; slot < 30; slot++) HealBoxPokemon(&ctx->cache[slot]);
    StorageFlush();
}
