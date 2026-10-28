#include "global.h"
#include "expanded_bag.h"
#include "save.h"
#include "load_save.h"
#include "pokemon_storage_system.h"
#include "la_collection_save.h"
#include "agb_flash.h"
#include "gba/flash_internal.h"
#include <stddef.h>
#include <string.h>
#define COLLECTION_SIGNATURE 0x3243504C
#define CHUNK 4072
struct CollectionSpan { u8 block; u16 offset; u16 size; };
#include "data/la_collection_save_spans.h"
#include "data/la_expanded_bag_save_spans.h"
static EWRAM_DATA u8 sPackedPcItems[BAG_PC_BYTES] = {0};
static u32 Read32(const u8 *p) { return p[0] | p[1]<<8 | p[2]<<16 | (u32)p[3]<<24; }
static void Put32(u8 *p, u32 v) { u32 i; for(i=0;i<4;i++) p[i]=v>>(i*8); }
static bool32 Equal(const u8 *a,const u8 *b,u32 n) { while(n--) if(*a++!=*b++) return FALSE; return TRUE; }
static const u32 sCrcTable[256] = {
    0x00000000,0x77073096,0xee0e612c,0x990951ba,0x076dc419,0x706af48f,0xe963a535,0x9e6495a3,
    0x0edb8832,0x79dcb8a4,0xe0d5e91e,0x97d2d988,0x09b64c2b,0x7eb17cbd,0xe7b82d07,0x90bf1d91,
    0x1db71064,0x6ab020f2,0xf3b97148,0x84be41de,0x1adad47d,0x6ddde4eb,0xf4d4b551,0x83d385c7,
    0x136c9856,0x646ba8c0,0xfd62f97a,0x8a65c9ec,0x14015c4f,0x63066cd9,0xfa0f3d63,0x8d080df5,
    0x3b6e20c8,0x4c69105e,0xd56041e4,0xa2677172,0x3c03e4d1,0x4b04d447,0xd20d85fd,0xa50ab56b,
    0x35b5a8fa,0x42b2986c,0xdbbbc9d6,0xacbcf940,0x32d86ce3,0x45df5c75,0xdcd60dcf,0xabd13d59,
    0x26d930ac,0x51de003a,0xc8d75180,0xbfd06116,0x21b4f4b5,0x56b3c423,0xcfba9599,0xb8bda50f,
    0x2802b89e,0x5f058808,0xc60cd9b2,0xb10be924,0x2f6f7c87,0x58684c11,0xc1611dab,0xb6662d3d,
    0x76dc4190,0x01db7106,0x98d220bc,0xefd5102a,0x71b18589,0x06b6b51f,0x9fbfe4a5,0xe8b8d433,
    0x7807c9a2,0x0f00f934,0x9609a88e,0xe10e9818,0x7f6a0dbb,0x086d3d2d,0x91646c97,0xe6635c01,
    0x6b6b51f4,0x1c6c6162,0x856530d8,0xf262004e,0x6c0695ed,0x1b01a57b,0x8208f4c1,0xf50fc457,
    0x65b0d9c6,0x12b7e950,0x8bbeb8ea,0xfcb9887c,0x62dd1ddf,0x15da2d49,0x8cd37cf3,0xfbd44c65,
    0x4db26158,0x3ab551ce,0xa3bc0074,0xd4bb30e2,0x4adfa541,0x3dd895d7,0xa4d1c46d,0xd3d6f4fb,
    0x4369e96a,0x346ed9fc,0xad678846,0xda60b8d0,0x44042d73,0x33031de5,0xaa0a4c5f,0xdd0d7cc9,
    0x5005713c,0x270241aa,0xbe0b1010,0xc90c2086,0x5768b525,0x206f85b3,0xb966d409,0xce61e49f,
    0x5edef90e,0x29d9c998,0xb0d09822,0xc7d7a8b4,0x59b33d17,0x2eb40d81,0xb7bd5c3b,0xc0ba6cad,
    0xedb88320,0x9abfb3b6,0x03b6e20c,0x74b1d29a,0xead54739,0x9dd277af,0x04db2615,0x73dc1683,
    0xe3630b12,0x94643b84,0x0d6d6a3e,0x7a6a5aa8,0xe40ecf0b,0x9309ff9d,0x0a00ae27,0x7d079eb1,
    0xf00f9344,0x8708a3d2,0x1e01f268,0x6906c2fe,0xf762575d,0x806567cb,0x196c3671,0x6e6b06e7,
    0xfed41b76,0x89d32be0,0x10da7a5a,0x67dd4acc,0xf9b9df6f,0x8ebeeff9,0x17b7be43,0x60b08ed5,
    0xd6d6a3e8,0xa1d1937e,0x38d8c2c4,0x4fdff252,0xd1bb67f1,0xa6bc5767,0x3fb506dd,0x48b2364b,
    0xd80d2bda,0xaf0a1b4c,0x36034af6,0x41047a60,0xdf60efc3,0xa867df55,0x316e8eef,0x4669be79,
    0xcb61b38c,0xbc66831a,0x256fd2a0,0x5268e236,0xcc0c7795,0xbb0b4703,0x220216b9,0x5505262f,
    0xc5ba3bbe,0xb2bd0b28,0x2bb45a92,0x5cb36a04,0xc2d7ffa7,0xb5d0cf31,0x2cd99e8b,0x5bdeae1d,
    0x9b64c2b0,0xec63f226,0x756aa39c,0x026d930a,0x9c0906a9,0xeb0e363f,0x72076785,0x05005713,
    0x95bf4a82,0xe2b87a14,0x7bb12bae,0x0cb61b38,0x92d28e9b,0xe5d5be0d,0x7cdcefb7,0x0bdbdf21,
    0x86d3d2d4,0xf1d4e242,0x68ddb3f8,0x1fda836e,0x81be16cd,0xf6b9265b,0x6fb077e1,0x18b74777,
    0x88085ae6,0xff0f6a70,0x66063bca,0x11010b5c,0x8f659eff,0xf862ae69,0x616bffd3,0x166ccf45,
    0xa00ae278,0xd70dd2ee,0x4e048354,0x3903b3c2,0xa7672661,0xd06016f7,0x4969474d,0x3e6e77db,
    0xaed16a4a,0xd9d65adc,0x40df0b66,0x37d83bf0,0xa9bcae53,0xdebb9ec5,0x47b2cf7f,0x30b5ffe9,
    0xbdbdf21c,0xcabac28a,0x53b39330,0x24b4a3a6,0xbad03605,0xcdd70693,0x54de5729,0x23d967bf,
    0xb3667a2e,0xc4614ab8,0x5d681b02,0x2a6f2b94,0xb40bbe37,0xc30c8ea1,0x5a05df1b,0x2d02ef8d,
};
static u32 Crc(u32 state,const u8 *data,u32 n)
{
    while(n--) state=(state>>8)^sCrcTable[(state^*data++)&255];
    return state;
}
static u16 Sum(const u8 *p)
{
    u32 sum=0,i;
    for(i=0;i<4084;i+=4) sum+=Read32(p+i);
    return (sum>>16)+sum;
}
static u32 SectorCrc(const struct SaveSector *s)
{
    u8 prefix[6]; u32 c;
    prefix[0]=s->id; prefix[1]=s->id>>8; Put32(prefix+2,s->counter);
    c=Crc(0xffffffff,prefix,6);
    c=Crc(c,s->data,8);
    return ~Crc(c,(const u8 *)s+12,CHUNK);
}
static void Transfer(void *buffer,u32 offset,u32 size,bool32 write)
{
    u32 i,n; u8 *b=buffer;
    for(i=0;i<ARRAY_COUNT(sCollectionSpans)+2 && size;i++)
    {
        u8 *p; u32 length;
        if(i<ARRAY_COUNT(sCollectionSpans)) {
            const struct CollectionSpan *s=&sCollectionSpans[i];
            p=(s->block==1?(u8 *)gSaveBlock1Ptr:(u8 *)gSaveBlock2Ptr)+s->offset;
            length=s->size;
        } else if(i==ARRAY_COUNT(sCollectionSpans)) {
            p=(u8 *)gPokemonStoragePtr; length=sizeof(*gPokemonStoragePtr);
        } else { p=(u8 *)gSaveBlock3Ptr; length=sizeof(*gSaveBlock3Ptr); }
        if(offset>=length) { offset-=length; continue; }
        n=min(size,length-offset);
        if(write) memcpy(p+offset,b,n); else memcpy(b,p+offset,n);
        b+=n;size-=n;offset=0;
    }
}
static void PcItemsPack(bool32 load)
{
    u32 bit=0;
    if(!load)memset(sPackedPcItems,0,sizeof(sPackedPcItems));
    for(u32 i=0;i<PC_ITEMS_COUNT;i++) {
        u32 value=0;
        if(!load)value=gSaveBlock1Ptr->pcItems[i].itemId|((u32)gSaveBlock1Ptr->pcItems[i].quantity<<10);
        for(u32 j=0;j<20;j++,bit++) {
            if(load) {if(sPackedPcItems[bit>>3]&(1<<(bit&7)))value|=1<<j;}
            else if(value&(1<<j))sPackedPcItems[bit>>3]|=1<<(bit&7);
        }
        if(load)gSaveBlock1Ptr->pcItems[i]=(struct ItemSlot){.itemId=value&1023,.quantity=value>>10};
    }
}
static void TransferBag(void *buffer,u32 offset,u32 size,bool32 write)
{
    u8 *b=buffer;
    for(u32 i=0;i<ARRAY_COUNT(sBagCollectionSpans)+4 && size;i++) {
        u8 *p;u32 length;
        if(i<ARRAY_COUNT(sBagCollectionSpans)) {
            const struct CollectionSpan *s=&sBagCollectionSpans[i];
            p=(s->block==1?(u8 *)gSaveBlock1Ptr:(u8 *)gSaveBlock2Ptr)+s->offset;length=s->size;
        } else switch(i-ARRAY_COUNT(sBagCollectionSpans)) {
            case 0:p=sPackedPcItems;length=sizeof(sPackedPcItems);break;
            case 1:p=gExpandedBagData;length=EXPANDED_BAG_BYTES;break;
            case 2:p=(u8 *)gPokemonStoragePtr;length=sizeof(*gPokemonStoragePtr);break;
            default:p=(u8 *)gSaveBlock3Ptr;length=sizeof(*gSaveBlock3Ptr);break;
        }
        if(offset>=length){offset-=length;continue;}
        u32 n=min(size,length-offset);
        if(write)memcpy(p+offset,b,n);else memcpy(b,p+offset,n);
        b+=n;size-=n;offset=0;
    }
}
static void TransferVersion(void *b,u32 offset,u32 n,bool32 write,u32 version)
{
    if(version==3)TransferBag(b,offset,n,write);else Transfer(b,offset,n,write);
}
static u32 Used(u32 version) {return version==3?COLLECTION_BAG_USED:COLLECTION_USED;}
static bool32 Inspect(u32 bank,u32 *generation,u8 positions[16],u32 *outVersion)
{
    struct SaveSector *s=&gSaveDataBuffer;
    u32 i,seen=0,counter=0,crc=0xffffffff,version=0;
    u8 header[64];
    for(i=0;i<16;i++) {
        ReadFlash(bank*16+i,0,(u8 *)s,4096);
        if(s->signature!=COLLECTION_SIGNATURE || s->id>=16 || (seen&(1u<<s->id))) return FALSE;
        if(i==0) counter=s->counter;
        if(i==0)version=Read32(s->data+4)&0xffff;
        if((version!=2 && version!=3) || s->counter!=counter || Read32(s->data)!=0x5343414c || Read32(s->data+4)!=(0x0fe80000|version))return FALSE;
        if(s->checksum!=Sum((u8 *)s) || Read32(s->data+8)!=SectorCrc(s)) return FALSE;
        seen|=1u<<s->id;positions[s->id]=i;
    }
    for(i=0;i<16;i++) {
        u32 start=i*CHUNK,end=min((i+1)*CHUNK,Used(version)),skip= i==0?64:0;
        ReadFlash(bank*16+positions[i],0,(u8 *)s,4096);
        if(i==0) memcpy(header,s->data+12,64);
        if(end>start+skip) crc=Crc(crc,(u8 *)s+12+skip,end-start-skip);
    }
    if(Read32(header)!=0x4f43414c || Read32(header+4)!=0x00324c4c || Read32(header+8)!=version
        || Read32(header+12)!=Used(version)-64 || Read32(header+16)!=sizeof(*gPokemonStoragePtr)
        || Read32(header+20)!=~crc || !Equal(header+24,sCollectionAbi,32)
        || Read32(header+56)!=~Crc(0xffffffff,header,56)) return FALSE;
    if(version==3 && Read32(header+60)!=ITEMS_COUNT)return FALSE;
    if(outVersion)*outVersion=version;
    *generation=counter;
    return TRUE;
}
bool32 LaCollectionFind(u32 *counter,u32 *bank)
{
    u8 positions[16];u32 a=0,b=0;bool32 va=Inspect(0,&a,positions,NULL),vb=Inspect(1,&b,positions,NULL);
    if(!va&&!vb) return FALSE;
    *bank=vb&&(!va||(s32)(b-a)>0)?1:0;
    *counter=*bank?b:a;
    return TRUE;
}
bool32 LaCollectionWrite(u32 counter,u32 bank)
{
    struct SaveSector *s=&gSaveDataBuffer;
    u32 i,offset,crc=0xffffffff,version=ExpandedBag_Active()?3:2;u8 header[64]={0};
    if(bank>1 || !StorageIsCollectionMode() || !StorageFlush()) return FALSE;
    if(version==3)PcItemsPack(FALSE);
    for(offset=0;offset<Used(version)-64;offset+=4096) {
        u32 n=min(4096,Used(version)-64-offset);
        TransferVersion(s,offset,n,FALSE,version);crc=Crc(crc,(u8 *)s,n);
    }
    Put32(header,0x4f43414c);Put32(header+4,0x00324c4c);Put32(header+8,version);
    Put32(header+12,Used(version)-64);Put32(header+16,sizeof(*gPokemonStoragePtr));Put32(header+20,~crc);
    memcpy(header+24,sCollectionAbi,32);Put32(header+56,~Crc(0xffffffff,header,56));
    if(version==3)Put32(header+60,ITEMS_COUNT);
    for(i=0;i<16;i++) {
        u32 start=i*CHUNK,skip=i==0?64:0,end=min((i+1)*CHUNK,Used(version));
        memset(s,0,4096);
        Put32(s->data,0x5343414c);Put32(s->data+4,0x0fe80000|version);
        if(i==0) memcpy(s->data+12,header,64);
        if(end>start+skip) TransferVersion((u8 *)s+12+skip,start+skip-64,end-start-skip,FALSE,version);
        s->id=i;s->signature=COLLECTION_SIGNATURE;s->counter=counter;
        Put32(s->data+8,SectorCrc(s));s->checksum=Sum((u8 *)s);
        if(ProgramFlashSectorAndVerify(bank*16+(i+counter)%16,(u8 *)s)) return FALSE;
    }
    return TRUE;
}
bool32 LaCollectionLoad(u32 bank)
{
    struct SaveSector *s=&gSaveDataBuffer;u8 positions[16];u32 counter,i,version;
    if(bank>1 || !Inspect(bank,&counter,positions,&version)) return FALSE;
    memset(gSaveBlock1Ptr,0,sizeof(*gSaveBlock1Ptr));
    memset(gSaveBlock2Ptr,0,sizeof(*gSaveBlock2Ptr));
    StorageInitialize();
    for(i=0;i<16;i++) {
        u32 start=i*CHUNK,skip=i==0?64:0,end=min((i+1)*CHUNK,Used(version));
        ReadFlash(bank*16+positions[i],0,(u8 *)s,4096);
        if(end>start+skip) TransferVersion((u8 *)s+12+skip,start+skip-64,end-start-skip,TRUE,version);
    }
    if(version==3){PcItemsPack(TRUE);ExpandedBag_LoadPacked();}
    StorageInvalidateCache();gSaveCounter=counter;
    return StorageIsCollectionMode() && gPokemonStoragePtr->currentBox<60;
}
bool32 LaCollectionCopyToBank1(u32 counter)
{
    struct SaveSector *s=&gSaveDataBuffer;u8 positions[16];u32 old,i;
    if(!Inspect(0,&old,positions,NULL)) return FALSE;
    for(i=0;i<16;i++) {
        ReadFlash(positions[i],0,(u8 *)s,4096);
        s->counter=counter;Put32(s->data+8,SectorCrc(s));s->checksum=Sum((u8 *)s);
        if(ProgramFlashSectorAndVerify(16+(i+counter)%16,(u8 *)s)) return FALSE;
    }
    return TRUE;
}
