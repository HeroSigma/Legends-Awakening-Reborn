from pathlib import Path
from PIL import Image
import struct,json,shutil
p=Path('/home/allan/projects/Legends-Awakening-Reborn');a=p/'data/bwa_assets/tilesets/AccumulaTown';backup=p/'.la_work/accumula_wesley_pc_backup';backup.mkdir(exist_ok=True)
for fn in ['tiles.png','tiles.4bpp','metatiles.bin','metatile_attributes.bin']:
 if not (backup/fn).exists():shutil.copy2(a/fn,backup/fn)
mapfile=p/'data/layouts/Unova_AccumulaTown/map.bin'
if not (backup/'map.bin').exists():shutil.copy2(mapfile,backup/'map.bin')
source=Image.open(p/'graphics/unova_wesley/source/bw_buildings_tileset_by_wesleyfg_d45ygf8.png').convert('RGB');bg=source.getpixel((0,0));crop=source.crop((399,18,509,123)).convert('RGBA');crop.putdata([(*c[:3],0 if max(abs(c[i]-bg[i]) for i in range(3))<=8 else 255) for c in crop.getdata()]);pc=Image.new('RGBA',(112,112));pc.paste(crop,(1,0))
pals=[]
for slot in [1,2,3,5]:pals.append((slot,[tuple(map(int,l.split())) for l in (p/f'data/tilesets/primary/amap_primary_bwa_082d4a94/palettes/{slot:02}.pal').read_text().splitlines()[3:19]]))
pri=list(struct.unpack('<4096H',(p/'data/tilesets/primary/amap_primary_bwa_082d4a94/metatiles.bin').read_bytes()));sec=list(struct.unpack('<4096H',(a/'metatiles.bin').read_bytes()));attrs=list(struct.unpack('<512H',(a/'metatile_attributes.bin').read_bytes()));raw=bytearray((a/'tiles.4bpp').read_bytes());primary=(p/'data/tilesets/primary/amap_primary_bwa_082d4a94/tiles.4bpp').read_bytes();allraw=primary+raw;lookup={}
for idx in range(1024):
 packed=allraw[idx*32:(idx+1)*32];pix=bytes(v for b in packed for v in [b&15,b>>4]);lookup.setdefault(pix,idx)
# Reuse exact mirrored patterns through the GBA's hardware flip flags.
def flipped(pix,flag):
 rows=[pix[i:i+8] for i in range(0,64,8)]
 if flag&1024:rows=[r[::-1] for r in rows]
 if flag&2048:rows=rows[::-1]
 return b''.join(rows)
lookup={};remap={}
for idx in range(1024):
 packed=allraw[idx*32:(idx+1)*32];pix=bytes(v for b in packed for v in [b&15,b>>4])
 if pix in lookup:remap[idx]=lookup[pix]
 else:
  for flag in [0,1024,2048,3072]:lookup.setdefault(flipped(pix,flag),idx|flag)
for i,v in enumerate(sec):
 idx=v&1023
 if idx in remap:
  ref=remap[idx];sec[i]=(v&0xf000)|(ref&1023)|((v^ref)&3072)
used={v&1023 for v in pri+sec};free=[i for i in range(512,1024) if i not in used];refs={};preview=Image.new('RGBA',(112,112));newtiles=0;approximated=0
for y in range(14):
 for x in range(14):
  data=list(pc.crop((x*8,y*8,x*8+8,y*8+8)).getdata());options=[]
  for slot,colors in pals:
   inds=[];err=0
   for r,g,b,alpha in data:
    if not alpha:inds.append(0);continue
    idx=min(range(1,16),key=lambda i:sum((v-w)**2 for v,w in zip((r,g,b),colors[i])));inds.append(idx);err+=sum((v-w)**2 for v,w in zip((r,g,b),colors[idx]))
   options.append((err,slot,bytes(inds),colors))
  err,slot,pix,colors=min(options,key=lambda v:v[0])
  if not any(pix):idx=0
  elif pix in lookup:idx=lookup[pix]
  else:
   assert free,'Not enough unused tiles for lossless pattern packing';idx=free.pop(0);newtiles+=1;
   for flag in [0,1024,2048,3072]:lookup.setdefault(flipped(pix,flag),idx|flag)
   raw[(idx-512)*32:(idx-511)*32]=bytes(u|(v<<4) for u,v in zip(pix[::2],pix[1::2]))
  refs[x,y]=idx|slot<<12;t=Image.new('RGBA',(8,8));t.putdata([(*colors[i],255 if i else 0) for i in pix]);preview.paste(t,(x*8,y*8))
ids=list(range(0x355,0x360))+list(range(0x3b3,0x3c0))+list(range(0x3de,0x400));floor=sec[(0x28c-512)*8:(0x28c-512)*8+4];blocks=list(struct.unpack('<2400H',mapfile.read_bytes()));pattern=[]
for y in range(7):
 row=[]
 for x in range(7):
  n=ids[y*7+x];sec[(n-512)*8:(n-512)*8+8]=floor+[refs[x*2,y*2],refs[x*2+1,y*2],refs[x*2,y*2+1],refs[x*2+1,y*2+1]];attrs[n-512]=96 if (x,y)==(3,6) else 0
  collision=0 if (x,y)==(3,6) or (y==0 and x in [0,6]) else 0x400;blocks[(14+y)*60+44+x]=n|0x3000|collision;row.append(n)
 pattern.append(row)
for x in range(44,51):blocks[21*60+x]=0x328c
(a/'metatiles.bin').write_bytes(struct.pack('<4096H',*sec));(a/'metatile_attributes.bin').write_bytes(struct.pack('<512H',*attrs));(a/'tiles.4bpp').write_bytes(raw);png=Image.new('P',(128,256));png.putpalette([i*17 for i in range(16) for _ in range(3)]+[0]*720)
for i in range(512):
 t=Image.new('P',(8,8));t.putdata([v for b in raw[i*32:i*32+32] for v in [b&15,b>>4]]);png.paste(t,((i%16)*8,(i//16)*8))
png.save(a/'tiles.png');mapfile.write_bytes(struct.pack('<2400H',*blocks));preview.resize((448,448),Image.Resampling.NEAREST).save(p/'.la_work/accumula/Wesley-PC-preview.png');(a/'wesley_pc.json').write_text(json.dumps({'artist':'WesleyFG','source_crop':[399,18,509,123],'native_pixel_size':[110,105],'resized':False,'graphics_tiles_added':newtiles,'pattern':[[f'{n:03X}' for n in r] for r in pattern],'door':[47,20],'palette_conversion':'existing BWA material palettes; native pixel scale preserved'},indent=2)+'\n');print('PC installed with',newtiles,'new tiles, pavement background and original door coordinate.')
