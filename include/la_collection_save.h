#ifndef GUARD_LA_COLLECTION_SAVE_H
#define GUARD_LA_COLLECTION_SAVE_H
bool32 LaCollectionFind(u32 *counter, u32 *bank);
bool32 LaCollectionLoad(u32 bank);
bool32 LaCollectionWrite(u32 counter, u32 bank);
bool32 LaCollectionCopyToBank1(u32 counter);
#endif
