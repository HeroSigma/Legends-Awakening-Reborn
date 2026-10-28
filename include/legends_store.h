#ifndef GUARD_LEGENDS_STORE_H
#define GUARD_LEGENDS_STORE_H
#include "item.h"
void LegendsStore_Open(void);
bool32 LegendsStore_ItemAllowed(enum Item item);
u32 LegendsStore_Price(enum Item item, u32 saleCategory);
u32 LegendsStore_Buy(enum Item item, u32 quantity, u32 saleCategory);
#endif
