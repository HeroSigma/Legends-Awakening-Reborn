#!/usr/bin/env python3
"""Independent pre-apply checks of native doors, puzzles, Dive pairs and alternate states."""
import collections,re,struct
import hoenn_canary9 as C

def review(q):
 oldlayouts={z['id']:z for z in q['oldls']['layouts']};decl=dict(re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',(C.ROOT/'src/data/tilesets/headers.h').read_text(),re.S));meta=(C.ROOT/'src/data/tilesets/metatiles.h').read_text();nativeattrs={}
 def oldgrid(n):
  l=oldlayouts[q['original'][n]['layout']];a=[]
  for role in ['primary_tileset','secondary_tileset']:
   sy=re.search(r'\.metatileAttributes\s*=\s*(\w+)',decl[l[role]])[1];p=re.search(re.escape(sy)+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',meta)[1];a.append(C.words(C.ROOT/p))
  return l,C.words(C.ROOT/l['blockdata_filepath']),a
 water=doors=0;dormant=[];native_event_positions=[];puzzles=[];dive=[];ids={m['id']:n for n,m in q['maps'].items()}
 for n in C.TARGETS:
  m=q['maps'][n];g=q['grids'][n];l,b,a=oldgrid(n)
  for i,w in enumerate(m['warp_events'][:len(q['original'][n]['warp_events'])]):
   old=q['original'][n]['warp_events'][i];v=b[old['y']*l['width']+old['x']];omb=a[(v&1023)//512][v&511]&255;now=g.cell(w['x'],w['y'])
   if omb in [0x29,*range(0x60,0x70),0x1B,0x1C]:assert now['translated_behavior'] in [0x29,*range(0x60,0x70),0x1B,0x1C],(n,i,omb,now)
   else:dormant.append({'map':n,'index':i,'native_behavior':omb,'source_behavior':now['translated_behavior']})
   doors+=1
  for y in range(g.h):
   for x in range(g.w):
    v=g.cell(x,y)
    if m['map_type'] in ['MAP_TYPE_CITY','MAP_TYPE_TOWN','MAP_TYPE_ROUTE','MAP_TYPE_OCEAN_ROUTE'] and v['collision']==0 and v['translated_behavior'] in [0x10,0x11,0x12,0x13,0x14,0x15]:assert v['elevation']==1,(n,v);water+=1
  for e in q['events']:
   if e['map']!=n:continue
   assert {k:v for k,v in e['before'].items() if k not in ['x','y','elevation']}=={k:v for k,v in e['after'].items() if k not in ['x','y','elevation']}
   if e['kind']=='object_events':
    v=g.cell(e['after']['x'],e['after']['y']);assert not v['collision'] or e['original_cell']['collision'],(n,e['index'],v)
  # Actor reset coordinates must still refer to valid cells; scene branching/scripts are unchanged.
  for line in q['scripts'][n].splitlines():
   mo=re.search(r'\bsetobjectxy(?:perm)?\s+([^,]+),\s*(\d+),\s*(\d+)',line)
   if mo:
    v=g.cell(int(mo[2]),int(mo[3]));assert v['collision']==0,(n,line,v);native_event_positions.append({'map':n,'command':line.strip(),'cell':v})
  if n in ['MossdeepCity_Gym','SootopolisCity_Gym_1F','SootopolisCity_Gym_B1F']:
   for y in range(g.h):
    for x in range(g.w):
     v=b[y*l['width']+x];now=g.cell(x,y);assert ((v>>10)&3,a[(v&1023)//512][v&511]&255)==(now['collision'],now['translated_behavior']),(n,x,y)
   puzzles.append({'map':n,'cells':g.w*g.h,'native_collision_and_behavior_equal':True})
  for co in m['connections'] or []:
   if co['direction'] not in ['dive','emerge'] or ids.get(co['map']) not in q['grids']:continue
   dg=q['grids'][ids[co['map']]];tested=0
   for y in range(g.h):
    for x in range(g.w):
     v=g.cell(x,y)
     if v['collision']:continue
     dv=dg.cell(x,y)
     if co['direction']=='dive' and v['translated_behavior'] in [0x11,0x12,0x14]:assert dv['collision']==0,(n,x,y,dv);tested+=1
     if co['direction']=='emerge' and v['translated_behavior'] not in [0x19,0x2A,0x6C]:assert dv['collision']==0 and dv['translated_behavior'] in [0x10,0x11,0x12,0x13,0x14,0x15],(n,x,y,dv);tested+=1
   dive.append({'map':n,'direction':co['direction'],'destination':ids[co['map']],'valid_cells':tested})
 for n,below in [('SkyPillar_2F','SkyPillar_1F'),('SkyPillar_4F','SkyPillar_3F')]:
  g=q['grids'][n];dg=q['grids'][below]
  for y in range(g.h):
   for x in range(g.w):
    if g.cell(x,y)['translated_behavior']==0xD2:assert dg.cell(x,y)['collision']==0,(n,x,y)
 heals=[]
 for h in C.load(C.ROOT/'src/data/heal_locations.json')['heal_locations']:
  if h['map'] not in ids:continue
  n=ids[h['map']];v=q['grids'][n].cell(h['x'],h['y']);assert v['collision']==0 and v['translated_behavior'] not in range(0x10,0x16);heals.append({'id':h['id'],'map':n,'cell':v})
 result={'passed':True,'native_warps':doors,'surface_water_cells':water,'native_puzzles':puzzles,'native_scripted_actor_positions':native_event_positions,'dive_emerge_pairs':dive,'heal_fly_arrivals':heals,'arrival_only_slots':dormant,'alternate_layouts':q['alternate_layouts'],'scope':'Static geometry and ownership checks; progression and emulator rendering require runtime testing.'};C.dump(C.OUT/'geometry_validation.json',result);print({k:v for k,v in result.items() if k in ['passed','native_warps','surface_water_cells']});return result
if __name__=='__main__':review(C.prepare())
