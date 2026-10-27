from pathlib import Path
from PIL import Image,ImageDraw
import struct,json
P=Path(__file__).resolve().parents[2];OUT=P/'.la_work/unova_wesley'
def load(dirs):
 raw=b''.join((d/'tiles.4bpp').read_bytes() for d in dirs);metas=[];pals=[[(0,0,0)]*16 for _ in range(16)]
 for bank,d in enumerate(dirs):
  metas.extend(struct.unpack('<4096H',(d/'metatiles.bin').read_bytes()))
  for f in (d/'palettes').glob('*.pal'):
   slot=int(f.stem)
   if (bank==0 and slot>=6) or (bank==1 and not 6<=slot<13):continue
   pals[slot]=[tuple(map(int,l.split())) for l in f.read_text().splitlines()[3:19]]
 tiles=[bytes(v for b in raw[i:i+32] for v in (b&15,b>>4)) for i in range(0,len(raw),32)];cache=[]
 for n in range(1024):
  im=Image.new('RGBA',(16,16))
  for j,v in enumerate(metas[n*8:n*8+8]):
   colors=pals[v>>12];q=Image.new('RGBA',(8,8));q.putdata([(*colors[i],255 if i else 0) for i in tiles[v&1023]])
   if v&1024:q=q.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
   if v&2048:q=q.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
   im.alpha_composite(q,((j%2)*8,(j//2%2)*8))
  cache.append(im)
 return cache

def render(cache,blocks,w,h,path):
 im=Image.new('RGBA',(w*16,h*16))
 for i,v in enumerate(blocks):im.paste(cache[v&1023],((i%w)*16,(i//w)*16))
 im.convert('RGB').save(path);return im
old=json.loads((OUT/'original/data/layouts/layouts.json').read_text());l=next(x for x in old['layouts'] if x['id']=='LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT')
cache=load([P/'data/tilesets/primary/amap_primary_bwa_082d4a94',P/'data/tilesets/secondary/amap_secondary_bwa_p082d4a94s082d4aac']);raw=(OUT/'original'/l['blockdata_filepath']).read_bytes();before=render(cache,struct.unpack('<'+str(len(raw)//2)+'H',raw),l['width'],l['height'],OUT/'Nuvema-before.png')
l=next(x for x in json.loads((P/'data/layouts/layouts.json').read_text())['layouts'] if x['id']=='LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT');cache=load([P/'data/tilesets/primary/unova_general',P/'data/tilesets/secondary/unova_nuvema']);raw=(P/l['blockdata_filepath']).read_bytes();after=render(cache,struct.unpack('<'+str(len(raw)//2)+'H',raw),l['width'],l['height'],OUT/'Nuvema-after.png')
report=json.loads((P/'docs/la_world/unova_wesley/report.json').read_text())
for bank,count in enumerate([report['primary_metatiles'],report['secondary_metatiles']]):
 w=512;h=((count+15)//16)*48;atlas=Image.new('RGB',(w,h),(30,30,35));d=ImageDraw.Draw(atlas)
 for i in range(count):
  x=(i%16)*32;y=(i//16)*48;t=cache[i+bank*512].resize((32,32),Image.Resampling.NEAREST);atlas.paste(t,(x,y),t);d.text((x,y+32),f'{i+bank*512:03X}',fill='white')
 atlas.save(OUT/('Unova-primary-metatiles.png' if bank==0 else 'Unova-Nuvema-metatiles.png'))
compare=Image.new('RGB',(before.width+after.width+32,max(before.height,after.height)+32),(30,30,35));compare.paste(before,(0,32));compare.paste(after,(before.width+32,32));d=ImageDraw.Draw(compare);d.text((8,8),'BWA ORIGINAL',fill='white');d.text((before.width+40,8),'WESLEY UNOVA',fill='white');compare.save(OUT/'Nuvema-before-after.png')
print('Rendered map, before/after and both metatile atlases.')
