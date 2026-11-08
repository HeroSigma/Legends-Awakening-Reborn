from pathlib import Path
from collections import deque
from PIL import Image
import json,struct
P=Path(__file__).resolve().parents[2];D=P/'docs/la_world/unova_wesley';checks=[]
def check(cond,label):
 assert cond,label
 checks.append(label)
def readj(p):return json.loads(p.read_text())
def words(p):
 b=p.read_bytes();return struct.unpack('<'+str(len(b)//2)+'H',b)
r=readj(D/'report.json');layouts=readj(P/'data/layouts/layouts.json')['layouts'];town=next(l for l in layouts if l['id']=='LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT');route=next(l for l in layouts if l['id']=='LAYOUT_BWA_3_19_ROUTE_1')
pref=readj(D/'prefabs.json');attrs=[];used=[]
for bank,name,count in [(0,'primary/unova_general',r['primary_metatiles']),(1,'secondary/unova_nuvema',r['secondary_metatiles'])]:
 d=P/'data/tilesets'/name;raw=(d/'tiles.4bpp').read_bytes();meta=words(d/'metatiles.bin');att=words(d/'metatile_attributes.bin');attrs+=list(att)
 check(len(raw)==16384 and len(meta)==4096 and len(att)==512,f'Bank {bank}: padded GBA file sizes')
 im=Image.open(d/'tiles.png');check(im.mode=='P' and im.size==(128,256) and max(im.getdata())<=15,f'Bank {bank}: 4bpp indexed PNG')
 for n in range(count):
  for entry in meta[n*8:n*8+8]:
   tile=entry&1023;pal=entry>>12
   check(tile<1024 and (bank or tile<512) and pal<13,f'Bank {bank}: metatile {n} references valid')
 used+=list(range(bank*512,bank*512+count))
 for slot in range(16):check(len((d/'palettes'/f'{slot:02}.gbapal').read_bytes())==32,f'Bank {bank}: palette {slot} hardware size')
check(not any((P/'data/tilesets/primary/unova_general/tiles.4bpp').read_bytes()[:32]),'Transparent tile zero is blank')
blocks=words(P/town['blockdata_filepath']);kinds=readj(D/'collision_grid.json');w,h=town['width'],town['height'];check((w,h)==(40,40) and len(blocks)==w*h,'40x40 map dimensions')
check(all((b&1023) in used for b in blocks),'Map uses populated metatiles only')
def walking(x,y):return 0<=x<w and 0<=y<h and blocks[y*w+x]&0xC00==0 and blocks[y*w+x]>>12==3
for i,(b,k) in enumerate(zip(blocks,kinds['kind'])):
 if k in ['forest','building','hedge','mailbox','sign','railing','support','cliff']:check(b&0xC00!=0,f'Solid {k} at {i}')
 if k=='water':check(attrs[b&1023]&255==0x15 and b>>12==1,f'Ocean behavior/elevation at {i}')
 if k=='door':check(attrs[b&1023]&255==0x60 and walking(i%w,i//w),f'Door behavior/access at {i}')
seen={(19,23)};q=deque(seen)
while q:
 x,y=q.popleft()
 for pt in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
  if pt not in seen and walking(*pt):seen.add(pt);q.append(pt)
for target in [tuple(t) for t in kinds['doors']]+[(25,0),(26,0),(27,0),(19,29)]:check(target in seen,f'Arrival reaches {target}')
m=readj(P/'data/maps/Unova_NuvemaTown/map.json');orig=readj(P/'.la_work/unova_wesley/original/data/maps/Unova_NuvemaTown/map.json');rm=readj(P/'data/maps/Unova_Route1/map.json')
check(m['warp_events']==orig['warp_events']==[],'Original active warp list preserved')
check(len(m['object_events'])==len(orig['object_events']),'Object event count preserved')
check(len({(b['x'],b['y']) for b in m['object_events']})==len(m['object_events']),'NPC cells are distinct')
moves=[]
for a,b in zip(orig['object_events'],m['object_events']):
 check(all(a[k]==b[k] for k in ['local_id','flag','script','graphics_id','movement_type']),'Object identity/script/flags retained')
 check((b['x'],b['y']) in seen,'NPC on reachable ground')
 if (a['x'],a['y'])!=(b['x'],b['y']):moves.append({'local_id':b['local_id'],'old':[a['x'],a['y']],'new':[b['x'],b['y']]})
check(next(c for c in m['connections'] if c['map']==rm['id'])['offset']==3,'Nuvema north offset +3')
check(next(c for c in rm['connections'] if c['map']==m['id'])['offset']==-3,'Route1 south offset -3')
rb=words(P/route['blockdata_filepath']);rw=route['width'];trans=readj(D/'connection_translation.json')
check(all(str(b&1023) in trans['forward'] for b in rb[-rw*7:]),'Forward translation covers complete neighbor strip')
check(all(str(b&1023) in trans['reverse'] for b in blocks[:w*7]),'Reverse translation covers complete neighbor strip')
check(all(0<=n<1024 for side in ['forward','reverse'] for n in trans[side].values()),'Boundary translation indices valid')
for x in (22,23,24):check(rb[-rw+x]&0xC00==0 and walking(x+3,0),'North/south walkable road alignment')
check(len(words(P/town['border_filepath']))==4,'Porymap border is 2x2')
frames=[(P/f'data/tilesets/primary/unova_general/anim/water/{i}.4bpp').read_bytes() for i in range(4)]
check(all(len(f)==512 for f in frames) and len(set(frames))==4,'Four distinct 16-tile water frames')
check(384+16<=512,'Animation stays inside primary graphics bank')
catalog=readj(P/'data/tilesets/unova_wesley_prefabs.json');check(len(catalog)>0 and any('BlueHouse' in p['name'] for p in catalog) and any('Laboratory' in p['name'] for p in catalog),'Nuvema building prefabs registered')
for p in catalog:
 check(len(p['metatiles'])==p['width']*p['height'],'Prefab dimensions')
 if p['name'].startswith('Original sheet -'):
  source=readj(D/'complete_source_mapping.json');page=int(p['name'].rsplit(' ',1)[1]);valid={v['metatile_id'] for v in source['pieces'] if v['page']==page}
  check(all(t['metatile_id'] in valid for t in p['metatiles']),'Original sheet prefab references verified source pieces')
 else:check(all(t['metatile_id'] in used for t in p['metatiles']),'Prefab references populated metatiles')
check((P/'data/tilesets/unova_wesley_prefabs.json').is_file(),'Porymap prefab catalogue available for import')
check(all(r['source_crops'][f'StairTread_{n}_48x8']['native_size']==[48,8] for n in ['Top','Middle','Base']),'Native top/middle/base stair band dimensions')
check(r['source_crops']['NuvemaBlueHouse']['native_size']==[70,87] and r['source_crops']['NuvemaLaboratory']['native_size']==[142,110],'Native building proportions retained')
r['event_moves']=moves;(D/'report.json').write_text(json.dumps(r,indent=2)+'\n')
(D/'validation.json').write_text(json.dumps({'passed':True,'assertions':len(checks),'reachable_ground_tiles':len(seen),'runtime_playtested':False},indent=2)+'\n')
print(f'PASS: {len(checks)} asset, palette, geometry, event, prefab and connection assertions; {len(seen)} reachable ground tiles.')

