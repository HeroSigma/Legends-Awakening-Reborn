from pathlib import Path
import json,hashlib,struct,subprocess,re
P=Path(__file__).resolve().parents[2];D=P/'docs/la_world/triple_layer';B=P/'.la_work/triple_layer/original';m=json.loads((D/'conversion.json').read_text());checks=0
for rel,digest in json.loads((D/'protected_files.json').read_text()).items():assert hashlib.sha256((P/rel).read_bytes()).hexdigest()==digest,rel;checks+=1
for v in m['entries']:
 n=v['count'];old=struct.unpack('<'+str(n*8)+'H',(B/v['metatiles']).read_bytes());new=struct.unpack('<'+str(n*12)+'H',(P/v['metatiles']).read_bytes());a=struct.unpack('<'+str(n)+('H' if v['attribute_bytes']==2 else 'I'),(P/v['attributes']).read_bytes())
 for i,attr in enumerate(a):
  t=attr>>12&15 if v['attribute_bytes']==2 else attr>>29&3;lo=list(old[i*8:i*8+4]);hi=list(old[i*8+4:i*8+8]);actual=list(new[i*12:i*12+12]);expected=[0x3014]*4+lo+hi if t==0 else lo+hi+[0]*4 if t==1 or t>2 else lo+[0]*4+hi;assert actual==expected,(v['metatiles'],i);checks+=1
assert '#define NUM_TILES_PER_METATILE 12' in (P/'include/fieldmap.h').read_text();assert 'enable_triple_layer_metatiles=1' in (P/'porymap.project.cfg').read_text()
def function(src,signature):
 start=src.index(signature+'\n{');pos=start+len(signature)+1;depth=0
 for end in range(pos,len(src)):
  if src[end]=='{':depth+=1
  if src[end]=='}':
   depth-=1
   if not depth:return src[start:end+1]
fc=(P/'src/field_camera.c').read_text();shop=(P/'src/shop.c').read_text();deco=(P/'src/decoration.c').read_text()
harness='''#include <assert.h>
#include <stdint.h>
#include <stdio.h>
typedef uint8_t u8; typedef uint8_t bool8; typedef uint16_t u16; typedef uint32_t u32; typedef int32_t s32; typedef int16_t s16;
#define TRUE 1
#define FALSE 0
#define NUM_TILES_PER_METATILE 12
#define METATILE_LAYER_TYPE_NORMAL 0
#define METATILE_LAYER_TYPE_COVERED 1
#define METATILE_LAYER_TYPE_SPLIT 2
#define METATILE_ATTRIBUTE_LAYER_TYPE 6
u16 gOverworldTilemapBuffer_Bg1[1024], gOverworldTilemapBuffer_Bg2[1024],gOverworldTilemapBuffer_Bg3[1024];
int copies;void ScheduleBgCopyTilemapToVram(int bg){copies++;}
struct {int copyBGToVRAM;} sFieldCameraOffset; int MapPosToBgTilemapOffset(void *camera,int x,int y){return 65;}
struct {u16 tilemapBuffers[4][1024];} shopData,*sShopData=&shopData;
struct {const u16 *metatiles;const u16 *metatileAttributes;} decoData,*gTilesetPointer_SecretBaseRedCave=&decoData;
u32 ExtractMetatileAttribute(u32 a,u8 type,int frlg){return a>>12;}
static void BuyMenuDrawMapMetatileLayer(u16 *,s16,s16,const u16 *);
'''
for src,sig in [(fc,'static void DrawMetatile(s32 metatileLayerType, const u16 *tiles, u16 offset)'),(fc,'void DrawDoorMetatileAt(int x, int y, u16 *tiles)'),(shop,'static bool8 IsShopMetatileLayerEmpty(const u16 *src)'),(shop,'static void BuyMenuDrawMapMetatile(s16 x, s16 y, const u16 *src, u8 metatileLayerType)'),(shop,'static void BuyMenuDrawMapMetatileLayer(u16 *dest, s16 offset1, s16 offset2, const u16 *src)'),(deco,'static u16 GetDecorationMetatileEntry(u16 metatileId, u8 legacyIndex)'),(deco,'static u16 GetMetatile(u16 tile)')]:harness+=function(src,sig)+'\n'
harness+='''int main(void){
 u16 tiles[12]={1,2,3,4,5,6,7,8,9,10,11,12},door[8]={21,22,23,24,25,26,27,28};int i,t;
 DrawMetatile(0,tiles,65);assert(copies==3);
 for(i=0;i<4;i++){int pos=65+(i&1)+(i/2)*32;assert(gOverworldTilemapBuffer_Bg3[pos]==tiles[i]);assert(gOverworldTilemapBuffer_Bg2[pos]==tiles[i+4]);assert(gOverworldTilemapBuffer_Bg1[pos]==tiles[i+8]);}
 DrawMetatile(3,door,65);assert(copies==3);DrawDoorMetatileAt(0,0,door);assert(copies==6&&sFieldCameraOffset.copyBGToVRAM);
 for(i=0;i<4;i++){int pos=65+(i&1)+(i/2)*32;assert(gOverworldTilemapBuffer_Bg3[pos]==door[i]);assert(gOverworldTilemapBuffer_Bg2[pos]==door[i+4]);assert(gOverworldTilemapBuffer_Bg1[pos]==0);}
 BuyMenuDrawMapMetatile(1,1,tiles,0);for(i=0;i<4;i++){int pos=66+(i&1)+(i/2)*32;assert(shopData.tilemapBuffers[2][pos]==tiles[i]);assert(shopData.tilemapBuffers[3][pos]==tiles[i+4]);assert(shopData.tilemapBuffers[1][pos]==tiles[i+8]);}
 for(t=0;t<3;t++){u16 triple[12],attr=t<<12;for(i=0;i<12;i++)triple[i]=0;
 for(i=0;i<4;i++){if(t==0){triple[i]=0x3014;triple[i+4]=31+i;triple[i+8]=41+i;}else if(t==1){triple[i]=31+i;triple[i+4]=41+i;}else {triple[i]=31+i;triple[i+8]=41+i;}}
 BuyMenuDrawMapMetatile(1,1,triple,1);for(i=0;i<4;i++){int pos=66+(i&1)+(i/2)*32;assert(shopData.tilemapBuffers[2][pos]==31+i);assert(shopData.tilemapBuffers[3][pos]==41+i);}
 decoData.metatiles=triple;decoData.metatileAttributes=&attr;for(i=0;i<8;i++)assert(GetMetatile(i)==(i<4?31+i:41+i-4));}
 puts("PASS: actual renderer, legacy 8-entry animated doors, shop layers/UI compaction and decoration previews (ASan/UBSan).");return 0;}
'''
f=P/'.la_work/triple_layer/renderer_test.c';f.parent.mkdir(exist_ok=True);f.write_text(harness);exe=f.with_suffix('');subprocess.run(['gcc','-std=c99','-fsanitize=address,undefined','-fno-omit-frame-pointer','-g',str(f),'-o',str(exe)],check=True);subprocess.run([str(exe)],check=True)
(D/'validation.json').write_text(json.dumps({'passed':True,'data_assertions':checks,'metatile_records':m['metatiles'],'tileset_files':m['tilesets'],'native_renderer_sanitizers_passed':True,'runtime_emulator_playtested':False},indent=2)+'\n');print('PASS:',checks,'preservation and layer-placement assertions; map IDs, artwork, palettes, collisions and BWA Nuvema retained.')
