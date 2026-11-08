#ifndef GUARD_EXPANDED_BAG_H
#define GUARD_EXPANDED_BAG_H
#include "item.h"
#define EXPANDED_BAG_BYTES (((ITEMS_COUNT - 1) * 10 + 7) / 8)
extern u8 gExpandedBagData[EXPANDED_BAG_BYTES];
bool32 ExpandedBag_Active(void);
bool32 ExpandedBag_UsesPocket(struct BagPocket *pocket);
void ExpandedBag_Rebind(void);
void ExpandedBag_Clear(void);
void ExpandedBag_BeginLoad(void);
bool32 ExpandedBag_ImportLegacy(void);
void ExpandedBag_LoadPacked(void);
void ExpandedBag_Suspend(void);
void ExpandedBag_Resume(void);
u32 ExpandedBag_Quantity(u32 item);
struct ItemSlot ExpandedBag_GetSlot(struct BagPocket *pocket, u32 slot);
void ExpandedBag_SetSlot(struct BagPocket *pocket, u32 slot, struct ItemSlot data);
u16 ExpandedBag_SectorSize(u32 id, const u8 *data, u16 size);
void ExpandedBag_WriteSector(u32 id, u8 *data, u16 size);
void ExpandedBag_ReadSector(u32 id, const u8 *data, u16 size);
#endif
