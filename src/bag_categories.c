#include "global.h"
#include "bag_categories.h"
#include "item_menu.h"
#include "malloc.h"
#include "string_util.h"

const u8 *const gBagCategoryNames[BAG_CATEGORIES_COUNT] = {
    [BAG_REGULAR] = COMPOUND_STRING("ITEMS"),
    [BAG_BALLS] = COMPOUND_STRING("POKE BALLS"),
    [BAG_MACHINES] = COMPOUND_STRING("TMs & HMs"),
    [BAG_BERRIES] = COMPOUND_STRING("BERRIES"),
    [BAG_KEYS] = COMPOUND_STRING("KEY ITEMS"),
    [BAG_MEDICINE] = COMPOUND_STRING("MEDICINE"),
    [BAG_EQUIPMENT] = COMPOUND_STRING("HELD ITEMS"),
    [BAG_TRAINING] = COMPOUND_STRING("TRAINING"),
    [BAG_EVOLUTION] = COMPOUND_STRING("EVOLUTION"),
    [BAG_MEGA_STONES] = COMPOUND_STRING("MEGA STONES"),
    [BAG_Z_CRYSTALS] = COMPOUND_STRING("Z-CRYSTALS"),
    [BAG_TERA_SHARDS] = COMPOUND_STRING("TERA SHARDS"),
    [BAG_TREASURES] = COMPOUND_STRING("TREASURES"),
};

u32 __attribute__((noinline)) GetItemBagCategory(enum Item item)
{
    u32 pocket = GetItemPocket(item);
    if (pocket != POCKET_ITEMS)
        return pocket;
    if (item == ITEM_ABILITY_PATCH || item == ITEM_ABILITY_CAPSULE)
        return BAG_TRAINING;
    switch (gItemsInfo[item].sortType)
    {
    case ITEM_TYPE_HEALTH_RECOVERY:
    case ITEM_TYPE_STATUS_RECOVERY:
    case ITEM_TYPE_PP_RECOVERY: return BAG_MEDICINE;
    case ITEM_TYPE_LEVEL_UP_ITEM:
    case ITEM_TYPE_NATURE_MINT:
    case ITEM_TYPE_STAT_BOOST_DRINK:
    case ITEM_TYPE_STAT_BOOST_FEATHER:
    case ITEM_TYPE_STAT_BOOST_MOCHI:
    case ITEM_TYPE_EV_BOOST_HELD_ITEM: return BAG_TRAINING;
    case ITEM_TYPE_EVOLUTION_STONE:
    case ITEM_TYPE_EVOLUTION_ITEM:
    case ITEM_TYPE_NECTAR: return BAG_EVOLUTION;
    case ITEM_TYPE_MEGA_STONE: return BAG_MEGA_STONES;
    case ITEM_TYPE_Z_CRYSTAL: return BAG_Z_CRYSTALS;
    case ITEM_TYPE_TERA_SHARD: return BAG_TERA_SHARDS;
    case ITEM_TYPE_SELLABLE:
    case ITEM_TYPE_RELIC:
    case ITEM_TYPE_FOSSIL: return BAG_TREASURES;
    case ITEM_TYPE_X_ITEM: return BAG_REGULAR;
    case ITEM_TYPE_BATTLE_ITEM:
    case ITEM_TYPE_SPECIAL_HELD_ITEM:
    case ITEM_TYPE_HELD_ITEM:
    case ITEM_TYPE_TYPE_BOOST_HELD_ITEM:
    case ITEM_TYPE_CONTEST_HELD_ITEM:
    case ITEM_TYPE_GEM:
    case ITEM_TYPE_PLATE:
    case ITEM_TYPE_MEMORY:
    case ITEM_TYPE_DRIVE:
    case ITEM_TYPE_INCENSE: return BAG_EQUIPMENT;
    default: return BAG_REGULAR;
    }
}

u32 BagCategory_StoragePocket(u32 category)
{
    return category < POCKETS_COUNT ? category : POCKET_ITEMS;
}

u32 BagCategory_Count(u32 category)
{
    struct BagPocket *pocket = &gBagPockets[BagCategory_StoragePocket(category)];
    u32 count = 0;
    for (u32 i = 0; i < pocket->capacity; i++)
    {
        enum Item item = BagPocket_GetSlotData(pocket, i).itemId;
        if (item != ITEM_NONE && GetItemBagCategory(item) == category)
            count++;
    }
    return count;
}

u32 BagCategory_Slot(u32 category, u32 position)
{
    struct BagPocket *pocket = &gBagPockets[BagCategory_StoragePocket(category)];
    for (u32 i = 0; i < pocket->capacity; i++)
    {
        enum Item item = BagPocket_GetSlotData(pocket, i).itemId;
        if (item != ITEM_NONE && GetItemBagCategory(item) == category && position-- == 0)
            return i;
    }
    return pocket->capacity;
}

struct ItemSlot BagCategory_GetSlot(u32 category, u32 position)
{
    struct BagPocket *pocket = &gBagPockets[BagCategory_StoragePocket(category)];
    u32 slot = BagCategory_Slot(category, position);
    return slot < pocket->capacity ? BagPocket_GetSlotData(pocket, slot) : (struct ItemSlot){0};
}

enum Item BagCategory_GetItem(u32 category, u32 position)
{
    return BagCategory_GetSlot(category, position).itemId;
}

void BagCategory_Move(u32 category, u32 from, u32 to)
{
    struct BagPocket *pocket = &gBagPockets[BagCategory_StoragePocket(category)];
    if (from == to || from >= BagCategory_Count(category))
        return;
    s32 shift = to > from ? 1 : -1;
    if (to > from) to--;
    struct ItemSlot saved = BagCategory_GetSlot(category, from);
    for (u32 i = from; i != to; i += shift)
        BagPocket_SetSlotData(pocket, BagCategory_Slot(category, i), BagCategory_GetSlot(category, i + shift));
    BagPocket_SetSlotData(pocket, BagCategory_Slot(category, to), saved);
}

void BagCategory_Sort(u32 category, u32 sort)
{
    u32 storage = BagCategory_StoragePocket(category);
    struct BagPocket *pocket = &gBagPockets[storage];
    if (storage != POCKET_ITEMS)
    {
        SortItemsInBag(pocket, sort);
        return;
    }
    // Sort only this category; preserve the placement/order of all other items.
    struct ItemSlot *slots = Alloc(pocket->capacity * sizeof(*slots));
    u16 *indices = Alloc(pocket->capacity * sizeof(*indices));
    if (!slots || !indices) {Free(slots);Free(indices);return;}
    u32 count = 0;
    for (u32 i = 0; i < pocket->capacity; i++)
    {
        enum Item item = BagPocket_GetSlotData(pocket, i).itemId;
        if (item != ITEM_NONE && GetItemBagCategory(item) == category)
        {
            indices[count] = i;
            slots[count] = BagPocket_GetSlotData(pocket, i);
            slots[count++].quantity ^= gSaveBlock2Ptr->encryptionKey;
        }
    }
    if (count < 2) {Free(slots);Free(indices);return;}
    struct BagPocket view = {.itemSlots = slots, .capacity = count, .id = POCKET_ITEMS};
    SortItemsInBag(&view, sort);
    for (u32 i = 0; i < count; i++) BagPocket_SetSlotData(pocket, indices[i], BagPocket_GetSlotData(&view, i));
    Free(slots);Free(indices);
}

bool32 LegendsStore_CategoryAllowed(u32 category)
{
    return category < BAG_CATEGORIES_COUNT && category != BAG_KEYS && category != BAG_TERA_SHARDS;
}
