#ifndef GUARD_ITEM_ACQUISITION_H
#define GUARD_ITEM_ACQUISITION_H
#include "item.h"

// A future quest or dedicated vendor may award these explicitly; ordinary
// Marts and Legends Store must exclude them from display and purchase.
bool32 Item_IsQuestRelic(enum Item item);
#endif
