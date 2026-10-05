#!/usr/bin/env python3
"""Render current Hyper interiors and audit preserved expansion event cells."""
import re,struct,collections,argparse
from PIL import Image,ImageDraw
import hoenn_finalization as F
R=F.R
parser=argparse.ArgumentParser();parser.add_argument('--batch',type=int,choices=[1,2,3,4,5,6,7,8,9,10],default=1);args=parser.parse_args()
O=R/f'.la_work/amap/hoenn_interior_polish{args.batch}';O.mkdir(parents=True,exist_ok=True)
FAMILIES={1:('LittlerootTown_','OldaleTown_','PetalburgCity_','RustboroCity_'),2:('DewfordTown_','SlateportCity_','MauvilleCity_'),3:('VerdanturfTown_','FallarborTown_','LavaridgeTown_','Route111_','Route113_','Route114_'),4:('FortreeCity_','Route119_','LilycoveCity_','Route121_','Route123_'),5:('MossdeepCity_','SootopolisCity_','PacifidlogTown_','EverGrandeCity_'),6:('BattleFrontier_','PetalburgCity_Gym','RustboroCity_Gym','DewfordTown_Gym','MauvilleCity_Gym','LavaridgeTown_Gym','FortreeCity_Gym','MossdeepCity_Gym','SootopolisCity_Gym'),7:('InsideOfTruck','Route104_','Route109_','Route110_','Route112_CableCarStation','MtChimney_CableCarStation','Route116_','Route117_','Route124_','SSTidal','SafariZone_RestHouse','TrainerHill_'),8:('AquaHideout_','MtPyre_'),9:('BirthIsland_','FarawayIsland_','NavelRock_','SouthernIsland_'),10:('HyperHoenn_',)}[args.batch]
ls={l['id']:l for l in F.load(R/'data/layouts/layouts.json')['layouts']};headers=(R/'src/data/tilesets/headers.h').read_text();meta=(R/'src/data/tilesets/metatiles.h').read_text();graphics=(R/'src/data/tilesets/graphics.h').read_text()+'\n'+(R/'src/graphics.c').read_text();cache={}
def bank(s):
 if s in cache:return cache[s]
 body=re.search(r'const struct Tileset '+s+r'.*?\};',headers,re.S)[0];ts=re.search(r'\.tiles\s*=\s*(\w+)',body)[1];path=re.search(ts+r'\[\].*?"([^"]+)"',graphics)[1];png=Image.open((R/path).with_name('tiles.png'));ms=re.search(r'\.metatiles\s*=\s*(\w+)',body)[1];mp=re.search(ms+r'\[\].*?"([^"]+)"',meta)[1];ps=re.search(r'\.palettes\s*=\s*(\w+)',body)[1];pb=re.search(ps+r'\[\]\[16\].*?\};',graphics,re.S)[0];pals=[]
 for p in re.findall(r'"([^"]+/(?:[^"]+)\.(?:pal|gbapal))"',pb):
  pbdata=(R/p).read_bytes()
  if pbdata.startswith(b'JASC-PAL'):pals.append([tuple(map(int,line.split())) for line in pbdata.decode().splitlines()[3:19]])
  else:
   assert len(pbdata)==32,(s,p,len(pbdata));vs=struct.unpack('<16H',pbdata);pals.append([((v&31)*255//31,((v>>5)&31)*255//31,((v>>10)&31)*255//31) for v in vs])
 result=(png,F.words(R/mp),pals);cache[s]=result;return result
rows=[];pictures=[]
for p in sorted((R/'data/maps').glob('*/map.json')):
 n=p.parent.name
 if not n.startswith(FAMILIES) or (args.batch!=6 and '_Gym' in n) or (args.batch==6 and n in ('BattleFrontier_OutsideEast','BattleFrontier_OutsideWest')):continue
 m=F.load(p)
 if args.batch==7 and (m.get('map_type')!='MAP_TYPE_INDOOR' or 'Prototype' in n):continue
 if args.batch==8 and 'Unused' in n:continue
 if args.batch==9 and n.endswith('_Frlg'):continue
 l=ls[m['layout']];g=F.grid(l,headers,meta);banks=[bank(l[k]) for k in ['primary_tileset','secondary_tileset']];out=Image.new('RGB',(g.w*16,g.h*16));bad=[]
 for y in range(g.h):
  for x in range(g.w):
   t=g.cell(x,y)['metatile'];entries=banks[t//512][1][t%512*8:t%512*8+8]
   for layer in range(2):
    for q in range(4):
     v=entries[layer*4+q];ti=v&1023;bi=int(ti>=512);idx=ti-bi*512;png=banks[bi][0];pn=v>>12
     if pn>=13:bad.append([x,y,t,pn])
     pal=banks[int(pn>=6)][2][min(pn,12)]
     for py in range(8):
      for px in range(8):
       tx=idx%(png.width//8)*8+(7-px if v&1024 else px);ty=idx//(png.width//8)*8+(7-py if v&2048 else py)
       if ty>=png.height:continue
       ci=png.getpixel((tx,ty))%16
       if layer==0 or ci:out.putpixel((x*16+q%2*8+px,y*16+q//2*8+py),pal[ci])
 out.save(O/(n+'.png'));pic=out.resize((g.w*32,g.h*32));draw=ImageDraw.Draw(pic);actors=[]
 for i,e in enumerate(m['object_events']):
  virtual='graphics_id' not in e or e.get('movement_type')=='MOVEMENT_TYPE_INVISIBLE' or e.get('type')=='clone' or e.get('script')=='0x0';cell=g.cell(e['x'],e['y']);actors.append({'index':i,'event':e,'cell':cell,'virtual_or_decorative':virtual})
  x,y=e['x']*32,e['y']*32;draw.ellipse((x+6,y+6,x+26,y+26),fill='gray' if virtual else 'orange',outline='black');draw.text((x+10,y+9),str(i+1),fill='black')
 for i,w in enumerate(m['warp_events']):
  x,y=w['x']*32,w['y']*32;draw.rectangle((x+2,y+2,x+29,y+29),outline='cyan',width=2)
 pictures.append((n,pic));rows.append({'map':n,'layout':l,'actors':actors,'warps':m['warp_events'],'coord_events':m['coord_events'],'bg_events':m['bg_events'],'invalid_palette_refs':bad})
for start in range(0,len(pictures),8):
 sheet=Image.new('RGB',(1280,800),'#eeeeee');d=ImageDraw.Draw(sheet)
 for j,(n,pic) in enumerate(pictures[start:start+8]):
  x=j%4*320;y=j//4*400;d.text((x+3,y+3),n.replace('Town_','_').replace('City_','_'),fill='black');pic.thumbnail((310,365));sheet.paste(pic,(x+3,y+25))
 sheet.save(O/f'contact_{start//8+1}.png')
F.dump(O/'inventory.json',rows);print('Rendered',len(rows),'rooms;',(len(pictures)+7)//8,'contact sheets; invalid palette references',sum(len(z['invalid_palette_refs']) for z in rows))
