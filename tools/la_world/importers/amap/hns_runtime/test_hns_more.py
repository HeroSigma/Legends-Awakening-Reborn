from probe import *
M=json.loads((R/'docs/la_world/hns_canary/manifest.json').read_text());G=json.loads((R/'data/maps/map_groups.json').read_text());group=G['group_order'].index('gMapGroup_HnS_Canary');maps={m['name']:json.loads((R/'data/maps'/m['name']/'map.json').read_text()) for m in M['maps']};byid={m['id']:n for n,m in maps.items()};L={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']};results=[]
def loc():
 p=rd(symbols['gSaveBlock1Ptr']);return rd(p+4,1),rd(p+5,1)
def target(n):return group,G['gMapGroup_HnS_Canary'].index(n)
def visit(n,x,y):warp(*target(n),x,y)
def check(n,ok,d):results.append(dict(test=n,passed=bool(ok),details=d));print(n,ok,d)
def cell(n,x,y):
 l=L[maps[n]['layout']];b=(R/l['blockdata_filepath']).read_bytes();v=struct.unpack_from('<H',b,(y*l['width']+x)*2)[0];key=l['primary_tileset' if (v&1023)<512 else 'secondary_tileset'].replace('gTileset_HnSCanary_','');attrs=(R/M['banks'][key]['path']/'metatile_attributes.bin').read_bytes();return v,struct.unpack_from('<H',attrs,(v&511)*2)[0]
def land(n,x,y):
 v,a=cell(n,x,y);return (v>>10&3)==0 and a in [0,2,79]
assert lib.boot(str(R/'pokeemerald.gba').encode());state('hns_newbark',True)
for n,m in maps.items():
 l=L[m['layout']];w,h=l['width'],l['height']
 for c in m.get('connections') or []:
  dn=byid[c['map']];dl=L[maps[dn]['layout']];dw,dh=dl['width'],dl['height'];o=c['offset'];dr=c['direction'];candidates=[]
  for i in range(h if dr in ['left','right'] else w):
   if dr=='left':x,y,dx,dy,k=0,i,dw-1,i-o,32
   elif dr=='right':x,y,dx,dy,k=w-1,i,0,i-o,16
   elif dr=='up':x,y,dx,dy,k=i,0,i-o,dh-1,64
   else:x,y,dx,dy,k=i,h-1,i-o,0,128
   if 0<=dx<dw and 0<=dy<dh and land(n,x,y) and land(dn,dx,dy):candidates.append((x,y,k))
  if candidates:
   x,y,k=candidates[len(candidates)//2];visit(n,x,y);frames(24,k);frames(120);check('boundary_'+n+'_'+dn,loc()==target(dn),dict(map=loc(),pos=pos()))
# Stair movements for both avatar genders, using same native routine.
for gender in [0,1]:
 state('hns_newbark',True);wr(rd(symbols['gSaveBlock2Ptr'])+8,gender,1);visit('HnSTest_Route31',24,13);frames(64,16);frames(20);high=pos();frames(64,32);frames(20);check('stairs_gender_'+str(gender),high[0]>26 and pos()==(24,13),dict(high=high,low=pos()));shot('hns_stairs_gender_'+str(gender))
# Animation callbacks must change the actual VRAM payload.
visit('HnSTest_CherrygroveCity',41,8)
def data(a,n):return bytes(rd(a+i,1) for i in range(n))
a=data(0x6000000+508*32,128);frames(16);b=data(0x6000000+508*32,128);check('outdoor_flower_animation',a!=b,dict(before=__import__('hashlib').sha256(a).hexdigest(),after=__import__('hashlib').sha256(b).hexdigest()))
visit('HnSTest_VioletCity_Gym',9,18);a=data(0x6000000+744*32,128);frames(10);b=data(0x6000000+744*32,128);check('gym_flower_animation',a!=b,dict(before=__import__('hashlib').sha256(a).hexdigest(),after=__import__('hashlib').sha256(b).hexdigest()))
# Find a land-to-water shoreline and attempt a normal walking step.
n='HnSTest_CherrygroveCity';l=L[maps[n]['layout']];found=None
for y in range(2,l['height']-2):
 for x in range(2,l['width']-2):
  if not land(n,x,y):continue
  for dx,dy,k in [(1,0,16),(-1,0,32),(0,1,128),(0,-1,64)]:
   v,a=cell(n,x+dx,y+dy)
   if a in [16,17,21] and (v>>10&3)==0:found=(x,y,k);break
  if found:break
 if found:break
assert found
x,y,k=found;visit(n,x,y);frames(24,k);frames(20);check('shoreline_blocks_walking',pos()==(x,y),dict(start=(x,y),after=pos(),key=k));shot('hns_shoreline_test')
(HERE/'hns_more_results.json').write_text(json.dumps(results,indent=2)+'\n')
