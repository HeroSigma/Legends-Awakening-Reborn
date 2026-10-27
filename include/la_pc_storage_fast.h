#ifndef GUARD_LA_PC_STORAGE_FAST_H
#define GUARD_LA_PC_STORAGE_FAST_H
bool32 StorageTryGetData(u32 box, u32 slot, s32 request, u32 *value);
void StorageHealCollectionCache(void);
#endif
