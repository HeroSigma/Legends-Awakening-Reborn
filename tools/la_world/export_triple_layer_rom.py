from pathlib import Path
from PIL import Image
import json,struct,shutil
P=Path('/home/allan/projects/Legends-Awakening-Reborn');B=P/'.la_work/triple_layer/original';D=P/'docs/la_world/triple_layer';out=Path('/mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Triple-Layer');out.mkdir(parents=True,exist_ok=True)
l=next(v for v in json.loads((P/'data/layouts/layouts.json').read_text())['layouts'] if v['id']=='LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT');dirs=[P/'data/tilesets/primary/amap_primary_bwa_082d4a94',P/'data/tilesets/secondary/amap_secondary_bwa_p082d4a94s082d4aac'];raw=b''.join((d/'tiles.4bpp').read_bytes() for d in dirs);tiles=[bytes(v for b in raw[i:i+32] for v in [b&15,b>>4]) for i in range(0,len(raw),32)];pals=[]
for i in range(13):pals.append([tuple(map(int,s.split())) for s in (dirs[int(i>=6)]/'palettes'/f'{i:02}.pal').read_text().splitlines()[3:19]])
def render(old):
 cache=[]
 for d in dirs:
  path=d/'metatiles.bin';data=(B/path.relative_to(P)).read_bytes() if old else path.read_bytes();stride=8 if old else 12;words=struct.unpack('<'+str(len(data)//2)+'H',data);attrs=struct.unpack('<'+str((d/'metatile_attributes.bin').stat().st_size//2)+'H',(d/'metatile_attributes.bin').read_bytes())
  for n in range(len(words)//stride):
   refs=list(words[n*stride:(n+1)*stride]);kind=attrs[n]>>12&15
   if old:refs=[0x3014]*4+refs if kind==0 else refs+[0]*4 if kind==1 or kind>2 else refs[:4]+[0]*4+refs[4:]
   im=Image.new('RGBA',(16,16))
   for j,v in enumerate(refs):
    q=Image.new('RGBA',(8,8));pal=pals[v>>12] if v>>12<len(pals) else [(0,0,0)]*16;q.putdata([(*pal[i],255 if i else 0) for i in tiles[v&1023]])
    if v&1024:q=q.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if v&2048:q=q.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    im.alpha_composite(q,((j%2)*8,(j%4//2)*8))
   cache.append(im)
 im=Image.new('RGBA',(l['width']*16,l['height']*16));blocks=struct.unpack('<'+str(l['width']*l['height'])+'H',(P/l['blockdata_filepath']).read_bytes())
 for i,v in enumerate(blocks):im.paste(cache[v&1023],((i%l['width'])*16,(i//l['width'])*16))
 return im
before=render(True);after=render(False);assert before.tobytes()==after.tobytes(),'Nuvema visual changed';after.save(out/'Nuvema-BWA-triple-layer.png')
shutil.copy2(P/'pokeemerald.gba',out/'Legends-Awakening-Reborn-Triple-Layer.gba')
for f in D.glob('*.json'):shutil.copy2(f,out/f.name)
shutil.copy2(D/'README.md',out/'README.md');print('BWA Nuvema before/after rendered pixels identical; exported verified triple-layer ROM and migration reports.')
