from pathlib import Path
from PIL import Image
import json,struct,shutil
P=Path('/home/allan/projects/Legends-Awakening-Reborn')
A=P/'data/tilesets/nuvema_recreation';A.mkdir(parents=True,exist_ok=True)
B=P/'.la_work/nuvema_recreation_backup';B.mkdir(parents=True,exist_ok=True)
def backup(f):
 q=B/f;q.parent.mkdir(parents=True,exist_ok=True)
 if not q.exists():shutil.copy2(P/f,q)
def edit(f,s):backup(f);(P/f).write_text(s)
source=Path('/mnt/c/Users/aadair/AppData/Local/Temp/codex-clipboard-86e3b6dd-4df2-4328-b076-76048b535216.png')
shutil.copy2(source,A/'reference.png')
shutil.copy2('/mnt/c/Users/aadair/AppData/Local/Temp/codex-clipboard-7be34133-d4ce-4f3a-b488-e691b4e45670.png',A/'reference_tilesheet.png')
im=Image.open(source).convert('RGB').resize((320,240),Image.Resampling.LANCZOS)
# Tile palettes follow materials; each 8x8 tile uses one hardware palette.
groups=[[] for _ in range(13)];tileinfo=[]
for y in range(30):
 for x in range(40):
  tile=im.crop((x*8,y*8,x*8+8,y*8+8));r,g,b=tuple(sum(c[i] for c in tile.getdata())//64 for i in range(3))
  if y>=24:k=0 if b>g else 1
  elif r>g*1.15:k=2
  elif b>r*1.35:k=3 if g<b*.8 else 4
  elif r>g*.92:k=5 if r>155 else 6
  elif g>r*1.45:k=7 if g<100 else 8 if g<145 else 9
  else:k=10 if g<110 else 11 if g<165 else 12
  groups[k].append(tile);tileinfo.append((x,y,k,tile))
pals=[]
for group in groups:
 canvas=Image.new('RGB',(8,max(8,len(group)*8)))
 for i,t in enumerate(group):canvas.paste(t,(0,i*8))
 q=canvas.quantize(colors=15,method=Image.Quantize.MEDIANCUT)
 colors=[tuple(v&248 for v in q.getpalette()[i:i+3]) for i in range(0,45,3)]
 pals.append([(0,0,0)]+colors)
preview=Image.new('RGB',(320,240));tiles=[bytes(64)];lookup={bytes(64):0};refs={};approximated=0
for x,y,k,t in tileinfo:
 pal=Image.new('P',(1,1));pal.putpalette(sum((list(c) for c in pals[k][1:]),[])+[0]*(768-45))
 q=t.quantize(palette=pal,dither=Image.Dither.NONE);pix=bytes(min(v,14)+1 for v in q.getdata())
 if pix not in lookup:
  if len(tiles)<1024:lookup[pix]=len(tiles);tiles.append(pix)
  else:
   # Reuse the closest existing pattern, preserving the selected material palette.
   candidates=sorted(range(1,len(tiles)),key=lambda i:abs(sum(tiles[i])-sum(pix)))[:32]
   lookup[pix]=min(candidates,key=lambda i:sum((a-b)**2 for a,b in zip(tiles[i],pix)));approximated+=1
 idx=lookup[pix];refs[x,y]=idx|(k<<12)
 rendered=Image.new('RGB',(8,8));rendered.putdata([pals[k][v] for v in tiles[idx]]);preview.paste(rendered,(x*8,y*8))
preview.resize((960,720),Image.Resampling.NEAREST).save(A/'preview.png')
# Collision follows structures and vegetation. Doors override structure collision.
blocked=set()
def rect(x0,y0,x1,y1):
 for y in range(y0,y1+1):
  for x in range(x0,x1+1):blocked.add((x,y))
rect(0,0,2,10);rect(17,0,19,10);rect(0,0,11,0);rect(14,0,19,0)
rect(4,1,8,3);rect(9,5,12,6);rect(7,6,8,7);rect(4,8,7,10);rect(12,8,15,10)
rect(0,12,19,14);rect(0,11,1,11);rect(18,11,19,11)
doors=[(6,3),(10,6),(6,10),(13,10)]
for d in doors:blocked.discard(d)
beh=(P/'include/constants/metatile_behaviors.h').read_text().split('enum {',1)[1].split('};',1)[0]
names=[s.strip().split(',')[0].split('//')[0].strip() for s in beh.splitlines() if s.strip().startswith('MB_')];doorbehavior=names.index('MB_NON_ANIMATED_DOOR')
meta=[];attr=[];blocks=[]
for y in range(15):
 for x in range(20):
  meta.extend([refs[x*2,y*2],refs[x*2+1,y*2],refs[x*2,y*2+1],refs[x*2+1,y*2+1],0,0,0,0]);attr.append(doorbehavior if (x,y) in doors else 0)
  blocks.append(y*20+x|0x3000|(0x400 if (x,y) in blocked else 0))
meta.extend([0]*(512*8-len(meta)));attr.extend([0]*(512-len(attr)))
for secondary in [False,True]:
 name='secondary' if secondary else 'primary';d=A/name;(d/'palettes').mkdir(parents=True,exist_ok=True)
 chunk=tiles[512:1024] if secondary else tiles[:512];chunk+= [bytes(64)]*(512-len(chunk))
 raw=bytes(a|(b<<4) for t in chunk for a,b in zip(t[::2],t[1::2]));(d/'tiles.4bpp').write_bytes(raw)
 png=Image.new('P',(128,256));png.putpalette([i*17 for i in range(16) for _ in range(3)]+[0]*720)
 for i,t in enumerate(chunk):tt=Image.new('P',(8,8));tt.putdata(t);png.paste(tt,((i%16)*8,(i//16)*8))
 png.save(d/'tiles.png')
 (d/'metatiles.bin').write_bytes(struct.pack('<4096H',*(meta if not secondary else [0]*4096)))
 (d/'metatile_attributes.bin').write_bytes(struct.pack('<512H',*(attr if not secondary else [0]*512)))
 for i,colors in enumerate(pals):
  (d/f'palettes/{i:02}.gbapal').write_bytes(struct.pack('<16H',*[r//8|((g//8)<<5)|((b//8)<<10) for r,g,b in colors]))
  (d/f'palettes/{i:02}.pal').write_text('JASC-PAL\n0100\n16\n'+'\n'.join(' '.join(map(str,c)) for c in colors)+'\n')
for f,kind in [('src/data/tilesets/graphics.h','graphics'),('src/data/tilesets/metatiles.h','meta'),('src/data/tilesets/headers.h','headers')]:
 s=(P/f).read_text()
 for name in ['primary','secondary']:
  symbol='gTileset_NuvemaRecreation_'+name;path='data/tilesets/nuvema_recreation/'+name
  if kind=='graphics':addition=f'\nconst u32 {symbol}_Tiles[] = INCBIN_U32("{path}/tiles.4bpp.lz");\nconst u16 {symbol}_Palettes[][16] = {{\n'+''.join(f' INCBIN_U16("{path}/palettes/{i:02}.gbapal"),\n' for i in range(13))+'};\n'
  elif kind=='meta':addition=f'\nconst u16 {symbol}_Metatiles[] = INCBIN_U16("{path}/metatiles.bin");\nconst u16 {symbol}_Attributes[] = INCBIN_U16("{path}/metatile_attributes.bin");\n'
  else:addition=f'\nconst struct Tileset {symbol} = {{ .isCompressed=TRUE, .isSecondary={"TRUE" if name=="secondary" else "FALSE"}, .tiles={symbol}_Tiles, .palettes={symbol}_Palettes, .metatiles={symbol}_Metatiles, .metatileAttributes={symbol}_Attributes, .callback=NULL }};\n'
  if symbol not in s:s+=addition
 edit(f,s)
f='data/layouts/layouts.json';data=json.loads((P/f).read_text());l=next(l for l in data['layouts'] if l['id']=='LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT');l.update(width=20,height=15,primary_tileset='gTileset_NuvemaRecreation_primary',secondary_tileset='gTileset_NuvemaRecreation_secondary');edit(f,json.dumps(data,indent=2)+'\n')
for f,raw in [(l['blockdata_filepath'],struct.pack('<300H',*blocks)),(l['border_filepath'],struct.pack('<4H',*([0x3400]*4)))]:backup(f);(P/f).write_bytes(raw)
f='data/maps/AMap_3_0_Nuvema_Town/map.json';data=json.loads((P/f).read_text());data.update(map_type='MAP_TYPE_TOWN',allow_running=True,object_events=[]);edit(f,json.dumps(data,indent=2)+'\n')
f='data/scripts/la_teleport_scientist.inc';edit(f,(P/f).read_text().replace('warp MAP_AMAP_3_0_NUVEMA_TOWN, 16, 22','warp MAP_AMAP_3_0_NUVEMA_TOWN, 9, 10'))
(A/'conversion.json').write_text(json.dumps({'map_size':[20,15],'tiles':len(tiles),'palettes':13,'approximate_tile_patterns':approximated,'doors':doors,'status':'visual and collision prototype; interiors not connected'},indent=2))
print('converted',len(tiles),'tiles; approximated',approximated)
