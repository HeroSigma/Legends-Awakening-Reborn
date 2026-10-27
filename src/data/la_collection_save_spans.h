/* Generated against current save ABI by the compact-PC layout audit. */
static const u8 sCollectionAbi[32] = {58,75,160,116,215,29,127,46,161,135,220,90,167,175,101,97,189,208,7,198,81,159,231,137,75,12,152,240,146,64,54,54};
static const struct CollectionSpan sCollectionSpans[] = {
 {1,0,2120},
 {1,2500,4312},
 {1,10186,2},
 {1,11152,768},
 {1,12336,288},
 {1,12712,80},
 {1,13720,260},
 {1,15016,64},
 {1,15530,2},
 {1,15544,24},
 {2,0,176},
};
#define COLLECTION_STORY_SIZE 8096
#define COLLECTION_USED 64968
STATIC_ASSERT(sizeof(struct SaveBlock1) == 15568, Collection_SaveBlock1_Size);
STATIC_ASSERT(sizeof(struct SaveBlock2) == 3884, Collection_SaveBlock2_Size);
STATIC_ASSERT(sizeof(struct SaveBlock3) == 4, Collection_SaveBlock3_Size);
STATIC_ASSERT(sizeof(struct PokemonStorage) == 56804, Collection_PokemonStorage_Size);
STATIC_ASSERT(offsetof(struct SaveBlock1, pokeblocks) == 2120, CollectionField0);
STATIC_ASSERT(offsetof(struct SaveBlock1, filler1) == 2440, CollectionField1);
STATIC_ASSERT(offsetof(struct SaveBlock1, berryBlenderRecords) == 2492, CollectionField2);
STATIC_ASSERT(offsetof(struct SaveBlock1, unused_9C2) == 2498, CollectionField3);
STATIC_ASSERT(offsetof(struct SaveBlock1, tvShows) == 10188, CollectionField4);
STATIC_ASSERT(offsetof(struct SaveBlock1, pokeNews) == 11088, CollectionField5);
STATIC_ASSERT(offsetof(struct SaveBlock1, contestWinners) == 11920, CollectionField6);
STATIC_ASSERT(offsetof(struct SaveBlock1, linkBattleRecords) == 12624, CollectionField7);
STATIC_ASSERT(offsetof(struct SaveBlock1, enigmaBerry) == 12792, CollectionField8);
STATIC_ASSERT(offsetof(struct SaveBlock1, mysteryGift) == 12844, CollectionField9);
STATIC_ASSERT(offsetof(struct SaveBlock1, trainerHillTimes) == 13980, CollectionField10);
STATIC_ASSERT(offsetof(struct SaveBlock1, ramScript) == 13996, CollectionField11);
STATIC_ASSERT(offsetof(struct SaveBlock1, recordMixingGift) == 15000, CollectionField12);
STATIC_ASSERT(offsetof(struct SaveBlock1, trainerNameRecords) == 15080, CollectionField13);
STATIC_ASSERT(offsetof(struct SaveBlock1, registeredTexts) == 15320, CollectionField14);
STATIC_ASSERT(offsetof(struct SaveBlock1, trainerHill) == 15532, CollectionField15);
STATIC_ASSERT(offsetof(struct SaveBlock1, secretBases) == 6812, CollectionField16);
STATIC_ASSERT(offsetof(struct SaveBlock1, playerRoomDecorations) == 10012, CollectionField17);
STATIC_ASSERT(offsetof(struct SaveBlock1, playerRoomDecorationPositions) == 10024, CollectionField18);
STATIC_ASSERT(offsetof(struct SaveBlock1, decorationDesks) == 10036, CollectionField19);
STATIC_ASSERT(offsetof(struct SaveBlock1, decorationChairs) == 10046, CollectionField20);
STATIC_ASSERT(offsetof(struct SaveBlock1, decorationPlants) == 10056, CollectionField21);
STATIC_ASSERT(offsetof(struct SaveBlock1, decorationOrnaments) == 10066, CollectionField22);
STATIC_ASSERT(offsetof(struct SaveBlock1, decorationMats) == 10096, CollectionField23);
STATIC_ASSERT(offsetof(struct SaveBlock1, decorationPosters) == 10126, CollectionField24);
STATIC_ASSERT(offsetof(struct SaveBlock1, decorationDolls) == 10136, CollectionField25);
STATIC_ASSERT(offsetof(struct SaveBlock1, decorationCushions) == 10176, CollectionField26);
STATIC_ASSERT(offsetof(struct SaveBlock2, playerApprentice) == 176, CollectionField27);
