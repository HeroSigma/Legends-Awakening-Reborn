from probe import *
M=json.loads((R/'docs/la_world/hns_canary/manifest.json').read_text());G=json.loads((R/'data/maps/map_groups.json').read_text());group=G['group_order'].index('gMapGroup_HnS_Canary');maps={m['name']:json.loads((R/'data/maps'/m['name']/'map.json').read_text()) for m in M['maps']};byid={m['id']:n for n,m in maps.items()};L={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']};results=[]
def loc():
 p=rd(symbols['gSaveBlock1Ptr']);return rd(p+4,1),rd(p+5,1)
def target(n):return group,G['gMapGroup_HnS_Canary'].index(n)
def passable(n,x,y):
 l=L[maps[n]['layout']]
 if not(0<=x<l['width'] and 0<=y<l['height']):return False
 b=(R/l['blockdata_filepath']).read_bytes();v=struct.unpack_from('<H',b,(y*l['width']+x)*2)[0];return (v>>10&3)==0
assert lib.boot(str(R/'pokeemerald.gba').encode());state('hns_newbark',True)
for n,m in maps.items():
 for i,w in enumerate(m['warp_events']):
  dn=byid[w['dest_map']];ok=False;attempts=[]
  for dx,dy,k in [(0,1,64),(1,0,32),(-1,0,16),(0,-1,128)]:
   x,y=w['x']+dx,w['y']+dy
   if not passable(n,x,y):continue
   warp(*target(n),x,y);frames(80,k);frames(180);attempts.append(dict(from_cell=(x,y),map=loc(),pos=pos()))
   if loc()==target(dn):ok=True;break
  results.append(dict(test='warp_'+n+'_'+str(i),passed=ok,destination=dn,attempts=attempts));print(n,i,'->',dn,ok)
(HERE/'hns_warp_results.json').write_text(json.dumps(results,indent=2)+'\n');assert all(x['passed'] for x in results)
