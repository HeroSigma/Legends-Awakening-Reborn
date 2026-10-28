#ifndef GUARD_BAG_CATEGORIES_H
#define GUARD_BAG_CATEGORIES_H
#include "item.h"
// First five values retain native pocket IDs. These are UI views, not save fields.
enum BagCategory {
    BAG_REGULAR = POCKET_ITEMS, BAG_BALLS = POCKET_POKE_BALLS,
    BAG_MACHINES = POCKET_TM_HM, BAG_BERRIES = POCKET_BERRIES,
    BAG_KEYS = POCKET_KEY_ITEMS,
    BAG_MEDICINE = POCKETS_COUNT, BAG_EQUIPMENT, BAG_TRAINING,
    BAG_EVOLUTION, BAG_MEGA_STONES, BAG_Z_CRYSTALS, BAG_TERA_SHARDS,
    BAG_TREASURES, BAG_CATEGORIES_COUNT
};
u32 GetItemBagCategory(enum Item item);
u32 BagCategory_StoragePocket(u32 category);
u32 BagCategory_Count(u32 category);
u32 BagCategory_Slot(u32 category, u32 position);
struct ItemSlot BagCategory_GetSlot(u32 category, u32 position);
enum Item BagCategory_GetItem(u32 category, u32 position);
void BagCategory_Move(u32 category, u32 from, u32 to);
void BagCategory_Sort(u32 category, u32 sort);
bool32 LegendsStore_CategoryAllowed(u32 category);
extern const u8 *const gBagCategoryNames[BAG_CATEGORIES_COUNT];
#endif
