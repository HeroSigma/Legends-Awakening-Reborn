#include "global.h"
#include "expanded_bag.h"
#include "save.h"
#include "pokemon_storage_system.h"
#include <string.h>

EWRAM_DATA u8 gExpandedBagData[EXPANDED_BAG_BYTES] = {0};
static EWRAM_DATA u16 sSlots[ITEMS_COUNT - 1] = {0};
static EWRAM_DATA u16 sBases[POCKETS_COUNT] = {0};
static EWRAM_DATA bool8 sActive = FALSE;
STATIC_ASSERT(ITEMS_COUNT <= 1024, ExpandedBagItemBits);
STATIC_ASSERT(MAX_BAG_ITEM_CAPACITY <= 1023, ExpandedBagQuantityBits);
STATIC_ASSERT(MAX_PC_ITEM_CAPACITY <= 1023, ExpandedBagPcQuantityBits);
#define BAG_MAGIC 0x33474142u
#define BAG_HEADER 16

static u32 Read32(const u8 *p) {return p[0]|p[1]<<8|p[2]<<16|(u32)p[3]<<24;}
static void Put32(u8 *p,u32 v) {for(u32 i=0;i<4;i++)p[i]=v>>(8*i);}
static u32 BagCrc(const u8 *p,u32 n)
{
    u32 crc=0xffffffff;
    while(n--) {crc^=*p++;for(u32 i=0;i<8;i++)crc=(crc>>1)^((crc&1)?0xedb88320:0);}
    return ~crc;
}
static void SetQuantity(u32 item,u32 quantity)
{
    if(item==0 || item>=ITEMS_COUNT)return;
    u32 bit=(item-1)*10,byte=bit/8,shift=bit%8;
    u32 word=gExpandedBagData[byte]|gExpandedBagData[byte+1]<<8;
    word=(word&~(1023u<<shift))|(quantity<<shift);
    gExpandedBagData[byte]=word;gExpandedBagData[byte+1]=word>>8;
}
u32 ExpandedBag_Quantity(u32 item)
{
    if(item==0 || item>=ITEMS_COUNT)return 0;
    u32 bit=(item-1)*10,byte=bit/8;
    return ((gExpandedBagData[byte]|gExpandedBagData[byte+1]<<8)>>(bit%8))&1023;
}

bool32 ExpandedBag_Active(void) {return sActive;}
bool32 ExpandedBag_UsesPocket(struct BagPocket *pocket)
{
    return sActive && pocket->id<POCKETS_COUNT && pocket==&gBagPockets[pocket->id];
}
void ExpandedBag_Rebind(void)
{
    if(!sActive)return;
    u32 base=0;
    for(u32 pocket=0;pocket<POCKETS_COUNT;pocket++) {
        u32 count=0;
        for(u32 item=1;item<ITEMS_COUNT;item++)if(GetItemPocket(item)==pocket)count++;
        sBases[pocket]=base;gBagPockets[pocket].capacity=count;base+=count;
    }
}
void ExpandedBag_LoadPacked(void)
{
    u16 positions[POCKETS_COUNT]={0};
    sActive=TRUE;ExpandedBag_Rebind();memset(sSlots,0,sizeof(sSlots));
    for(u32 item=1;item<ITEMS_COUNT;item++)if(ExpandedBag_Quantity(item)) {
        u32 pocket=GetItemPocket(item);
        if(pocket<POCKETS_COUNT)sSlots[sBases[pocket]+positions[pocket]++]=item;
    }
}
void ExpandedBag_BeginLoad(void) {sActive=FALSE;memset(gExpandedBagData,0,sizeof(gExpandedBagData));SetBagItemsPointers();}
void ExpandedBag_Clear(void) {memset(gExpandedBagData,0,sizeof(gExpandedBagData));ExpandedBag_LoadPacked();}
void ExpandedBag_Suspend(void) {sActive=FALSE;SetBagItemsPointers();}
void ExpandedBag_Resume(void) {sActive=TRUE;SetBagItemsPointers();}
bool32 ExpandedBag_ImportLegacy(void)
{
    memset(gExpandedBagData,0,sizeof(gExpandedBagData));
    for(u32 pocket=0;pocket<POCKETS_COUNT;pocket++) {
        for(u32 slot=0;slot<gBagPockets[pocket].capacity;slot++) {
            struct ItemSlot data=BagPocket_GetSlotData(&gBagPockets[pocket],slot);
            if(data.itemId==ITEM_NONE)continue;
            u32 total=ExpandedBag_Quantity(data.itemId)+data.quantity;
            // Keep an unusual legacy inventory intact rather than discard excess.
            if(total>MAX_BAG_ITEM_CAPACITY) {memset(gExpandedBagData,0,sizeof(gExpandedBagData));return FALSE;}
            SetQuantity(data.itemId,total);
        }
    }
    ExpandedBag_LoadPacked();return TRUE;
}
struct ItemSlot ExpandedBag_GetSlot(struct BagPocket *pocket,u32 slot)
{
    if(slot>=pocket->capacity)return (struct ItemSlot){0};
    enum Item item=sSlots[sBases[pocket->id]+slot];
    return (struct ItemSlot){.itemId=item,.quantity=ExpandedBag_Quantity(item)};
}
void ExpandedBag_SetSlot(struct BagPocket *pocket,u32 slot,struct ItemSlot data)
{
    if(slot>=pocket->capacity)return;
    u32 base=sBases[pocket->id];enum Item old=sSlots[base+slot];
    sSlots[base+slot]=data.itemId;
    if(data.itemId!=ITEM_NONE)SetQuantity(data.itemId,data.quantity);
    if(old!=ITEM_NONE && old!=data.itemId) {
        for(u32 i=0;i<pocket->capacity;i++)if(sSlots[base+i]==old)return;
        SetQuantity(old,0);
    }
}
u16 ExpandedBag_SectorSize(u32 id,const u8 *data,u16 size)
{
    if(id==SECTOR_ID_PKMN_STORAGE_END && Read32(data+size)==BAG_MAGIC)
        return size+BAG_HEADER+((EXPANDED_BAG_BYTES+3)&~3);
    return size;
}
void ExpandedBag_WriteSector(u32 id,u8 *data,u16 size)
{
    if(id!=SECTOR_ID_PKMN_STORAGE_END || !sActive)return;
    u8 *p=data+size;Put32(p,BAG_MAGIC);Put32(p+4,ITEMS_COUNT);Put32(p+8,EXPANDED_BAG_BYTES);
    Put32(p+12,BagCrc(gExpandedBagData,EXPANDED_BAG_BYTES));memcpy(p+BAG_HEADER,gExpandedBagData,EXPANDED_BAG_BYTES);
}
void ExpandedBag_ReadSector(u32 id,const u8 *data,u16 size)
{
    if(id!=SECTOR_ID_PKMN_STORAGE_END)return;
    const u8 *p=data+size;
    if(Read32(p)!=BAG_MAGIC || Read32(p+4)!=ITEMS_COUNT || Read32(p+8)!=EXPANDED_BAG_BYTES
      || Read32(p+12)!=BagCrc(p+BAG_HEADER,EXPANDED_BAG_BYTES))return;
    memcpy(gExpandedBagData,p+BAG_HEADER,EXPANDED_BAG_BYTES);ExpandedBag_LoadPacked();
}
STATIC_ASSERT(sizeof(struct PokemonStorageLegacy)-8*SECTOR_DATA_SIZE+BAG_HEADER+((EXPANDED_BAG_BYTES+3)&~3)<=SECTOR_DATA_SIZE, ExpandedBagNormalSectorFits);
