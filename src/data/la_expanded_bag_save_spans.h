/* V3 preserves all live story fields. Omit native bag/PC item arrays (packed separately)
 * and unused SB2 Pokedex filler bytes. V2 spans remain untouched for migration. */
static const struct CollectionSpan sBagCollectionSpans[] = {
 {1,0,1176},
 {1,2500,4312},
 {1,10186,2},
 {1,11152,768},
 {1,12336,288},
 {1,12712,80},
 {1,13720,260},
 {1,15016,64},
 {1,15530,2},
 {1,15544,24},
 {2,0,40},
 {2,152,24},
 };
#define BAG_PC_BYTES ((PC_ITEMS_COUNT * 20 + 7) / 8)
#define COLLECTION_BAG_USED (64 + 7040 + BAG_PC_BYTES + EXPANDED_BAG_BYTES + sizeof(struct PokemonStorage) + sizeof(struct SaveBlock3))
STATIC_ASSERT(offsetof(struct SaveBlock1, pcItems) == 1176, BagPcItemsOffset);
STATIC_ASSERT(offsetof(struct SaveBlock1, bag) == 1376, BagInventoryOffset);
STATIC_ASSERT(offsetof(struct SaveBlock2, pokedex.filler) == 40, BagUnusedDexOffset);
STATIC_ASSERT(sizeof(gSaveBlock2Ptr->pokedex.filler) == 104, BagUnusedDexSize);
STATIC_ASSERT(offsetof(struct SaveBlock2, filler_90) == 144, BagUnusedOffset);
STATIC_ASSERT(COLLECTION_BAG_USED <= 16 * CHUNK, ExpandedBagCollectionFits);
