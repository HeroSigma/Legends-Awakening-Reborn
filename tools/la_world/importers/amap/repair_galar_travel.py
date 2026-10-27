#!/usr/bin/env python3
"""Repair editor sources, reject story warps on normal tiles, and anchor inspection arrivals."""
import json,struct,re,collections,shutil
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4];D=R/'docs/la_world/galar_import';S=R/'.la_work/amap/swsh_full_v11'
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def main():
 assert not (D/'travel_repair.json').exists(),'Already repaired'
 ledger=json.loads((D/'import_ledger.json').read_text());names={z['donor_id']:z['project_name'] for z in ledger};source={m['id']:m for m in json.loads((S/'manifest.json').read_text())['maps']};folders={json.loads((f/'map.json').read_text())['id']:f for f in (S/'maps').iterdir() if (f/'map.json').exists()};ls={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']};native=enums(R/'include/constants/metatile_behaviors.h');rows={};oldchanges=json.loads((D/'travel_cell_changes.json').read_text());changes=[];banks={};used={};clones={};issues=[];remaps=[]
 for f in (R/'data/galar_assets/tilesets').iterdir():
  original=S/'tilesets'/f.name;shutil.copy2(original/'tiles.png',f/'tiles.png')
  for i in range(13):
   pal=original/'palettes'/f'{i:02}.pal';target=f/f'palette_{i:02}.pal'
   if pal.exists():shutil.copy2(pal,target)
   else:target.write_text('JASC-PAL\n0100\n16\n'+'0 0 0\n'*16)
  banks[f.name]=(f,bytearray((f/'metatile_attributes.bin').read_bytes()),bytearray((f/'metatiles.bin').read_bytes()),(original/'source_frlg_metatile_attributes.bin').read_bytes());used[f.name]=set()
 for did,name in names.items():
  m=json.loads((R/'data/maps'/name/'map.json').read_text());l=ls[m['layout']];keys=[source[did][k] for k in ['primary_tileset','secondary_tileset']];blob=bytearray((folders[did]/'blockdata.bin').read_bytes())
  if next(z for z in ledger if z['donor_id']==did)['existing_import']:
   original_layouts=json.loads((R/'.la_work/amap/galar_import_backup/data/layouts/layouts.json').read_text())
   original_layout=next(z for z in original_layouts['layouts'] if z['id']==l['id'])
   blob=bytearray((R/original_layout['blockdata_filepath']).read_bytes())
  cells=list(struct.unpack('<'+'H'*(l['width']*l['height']),blob));m['object_events']=[o for o in m['object_events'] if o['script']!=name+'_GalarInspect'];rows[did]=(m,l,keys,cells)
  for b in [blob,(R/l['border_filepath']).read_bytes()]:
   for v, in struct.iter_unpack('<H',b):used[keys[(v&1023)//512]].add(v&511)
 def raw(keys,mid):return struct.unpack_from('<I',banks[keys[mid//512]][3],4*(mid%512))[0]&511
 def clone(keys,mid,behavior):
  key=keys[mid//512];f,a,t,r=banks[key];pair=(key,mid%512,behavior)
  if pair not in clones:
   slot=next(i for i in range(511,-1,-1) if i not in used[key]);used[key].add(slot);clones[pair]=slot;t[16*slot:16*slot+16]=t[16*(mid%512):16*(mid%512)+16];old=struct.unpack_from('<H',a,2*(mid%512))[0];struct.pack_into('<H',a,2*slot,(old&0xf000)|behavior)
  return mid//512*512+clones[pair]
 revision={'3.1':'5.6','3.2':'6.10','3.3':'7.11','3.4':'8.7','3.5':'9.10','3.6':'10.21','3.7':'11.10','3.8':'12.10','3.10':'14.10','4.6':'3.0'}
 warpbeh={0x60:'MB_NON_ANIMATED_DOOR',0x61:'MB_LADDER',0x62:'MB_EAST_ARROW_WARP',0x63:'MB_WEST_ARROW_WARP',0x64:'MB_NORTH_ARROW_WARP',0x65:'MB_SOUTH_ARROW_WARP',0x66:'MB_LADDER',0x67:'MB_AQUA_HIDEOUT_WARP',0x68:'MB_LADDER',0x69:'MB_NON_ANIMATED_DOOR',0x6a:'MB_UP_ESCALATOR',0x6b:'MB_DOWN_ESCALATOR',0x6c:'MB_UP_RIGHT_STAIR_WARP',0x6d:'MB_UP_LEFT_STAIR_WARP',0x6e:'MB_DOWN_RIGHT_STAIR_WARP',0x6f:'MB_DOWN_LEFT_STAIR_WARP',0x71:'MB_LADDER'}
 enabled={}
 for did,(m,l,keys,cells) in rows.items():
  enabled[did]={};m['warp_events']=[]
  for i,w in enumerate(source[did]['warps']):
   target=revision.get(w['target_id'],w['target_id']);wid=w['dest_warp_id'];reason=None
   if not (0<=w['x']<l['width'] and 0<=w['y']<l['height']):reason='source out of bounds'
   elif raw(keys,cells[w['y']*l['width']+w['x']]&1023) not in warpbeh:reason='non-warp tile: donor story transition not imported'
   elif w['dynamic_target'] or target not in names:reason='unresolved destination'
   if not reason:
    matches=[j for j,z in enumerate(source[target]['warps']) if revision.get(z['target_id'],z['target_id'])==did and z['dest_warp_id']==i]
    if matches and wid not in matches:
     points=[(source[target]['warps'][j]['x'],source[target]['warps'][j]['y']) for j in matches]
     if len(matches)==1 or (max(x for x,y in points)-min(x for x,y in points)<=1 and max(y for x,y in points)-min(y for x,y in points)<=1):
      remaps.append({'map':did,'warp':i,'old_target':w['target_id'],'old_index':wid,'target':target,'index':matches[0]});wid=matches[0]
    if not (0<=wid<len(source[target]['warps'])):reason='invalid destination index'
    elif w['target_id']!=target and not matches:reason='revision has no reciprocal doorway'
    else:
     dest=source[target]['warps'][wid];dl=rows[target][1]
     if not (0<=dest['x']<dl['width'] and 0<=dest['y']<dl['height']):reason='destination out of bounds'
   if reason:
    issues.append({'map':did,'warp':i,'reason':reason});m['warp_events'].append({'x':-1,'y':-1,'elevation':0,'dest_map':'MAP_LITTLEROOT_TOWN','dest_warp_id':'0'})
   else:
    enabled[did][i]=(target,wid);m['warp_events'].append({'x':w['x'],'y':w['y'],'elevation':3,'dest_map':rows[target][0]['id'],'dest_warp_id':str(wid)})
 while True:
  before=sum(map(len,enabled.values()))
  for did in rows:
   for i,(target,wid) in list(enabled[did].items()):
    if wid not in enabled[target]:
     rows[did][0]['warp_events'][i]={'x':-1,'y':-1,'elevation':0,'dest_map':'MAP_LITTLEROOT_TOWN','dest_warp_id':'0'};del enabled[did][i];issues.append({'map':did,'warp':i,'reason':'destination is an inactive story/invalid warp'})
  if sum(map(len,enabled.values()))==before:break
 tour=[];components_report=[]
 blocked={v for k,v in native.items() if k.startswith('MB_IMPASSABLE_') or k in ['MB_OCEAN_WATER','MB_POND_WATER','MB_DEEP_WATER','MB_WATERFALL','MB_SEMI_DEEP_WATER','MB_NO_SURFACING','MB_INTERIOR_DEEP_WATER']}
 for did,(m,l,keys,cells) in rows.items():
  original_cells=list(cells)
  for i in enabled[did]:
   w=m['warp_events'][i];pos=w['y']*l['width']+w['x'];old=cells[pos];new=0x3000|clone(keys,original_cells[pos]&1023,native[warpbeh[raw(keys,original_cells[pos]&1023)]]);cells[pos]=new;changes.append({'map':m['name'],'x':w['x'],'y':w['y'],'before':old,'after':new,'reason':'actual donor doorway/warp tile'})
  W=l['width'];H=l['height'];warp_positions={w['y']*W+w['x'] for w in m['warp_events'] if w['x']>=0}
  def behavior(v):return struct.unpack_from('<H',banks[keys[(v&1023)//512]][1],2*(v&511))[0]&255
  walk={i for i,v in enumerate(cells) if (v>>10&3)==0 and v>>12 not in [1,15] and behavior(v) not in blocked and i not in warp_positions}
  def adjacent(i):return [j for j in [i-W,i+W,i-1 if i%W else -1,i+1 if i%W<W-1 else -1] if 0<=j<W*H]
  # Match native elevation transitions; do not flatten unrelated height layers.
  def can_step(a,b):return cells[a]>>12==cells[b]>>12 or cells[a]>>12==0 or cells[b]>>12==0
  unseen=set(walk);components=[]
  while unseen:
   seed=next(iter(unseen));unseen.remove(seed);component={seed};queue=collections.deque([seed])
   while queue:
    i=queue.popleft()
    for j in adjacent(i):
     if j in unseen and can_step(i,j):unseen.remove(j);component.add(j);queue.append(j)
   components.append(component)
  anchor=None
  if did=='3.0':anchor=24*W+18
  # Preserve known-tested arrival for Postwick, otherwise prefer components reaching real exits.
  def score(c):
   exits=sum(any(j in c for j in adjacent(w)) for w in warp_positions)
   edges=sum(1 for i in c if i//W in [0,H-1] or i%W in [0,W-1]) if m['connections'] else 0
   return (1 if anchor in c else 0,1 if exits else 0,exits,1 if edges else 0,len(c))
  component=max(components,key=score) if components else set();occupied={(o['x'],o['y']) for o in m['object_events']};candidates=[]
  for i in component:
   x,y=i%W,i//W
   if not (0<x<W-1 and 0<y<H-1) or (x,y) in occupied or (x,y-1) in occupied:continue
   if all(j in component for j in [i-W,i+W,i-1,i+1]) and behavior(cells[i])==native['MB_NORMAL'] and behavior(cells[i-W])==native['MB_NORMAL'] and cells[i]>>12 in [0,3] and cells[i-W]>>12 in [0,3]:candidates.append(i)
  if candidates and len(component)>=12:
   if anchor in candidates:pos=anchor
   else:
    doors=[j for w in warp_positions for j in adjacent(w) if j in component]
    pos=min(candidates,key=lambda i:min([abs(i%W-j%W)+abs(i//W-j//W) for j in doors] or [abs(i%W-W//2)+abs(i//W-H//2)]))
   x,y=pos%W,pos//W;tour.append({'donor_id':did,'map':m['name'],'map_id':m['id'],'spawn':[x,y]});m['object_events'].append({'local_id':'LOCALID_'+m['name'].upper()+'_GALAR_INSPECTOR','graphics_id':'OBJ_EVENT_GFX_SCIENTIST_1','x':x,'y':y-1,'elevation':3,'movement_type':'MOVEMENT_TYPE_FACE_DOWN','movement_range_x':0,'movement_range_y':0,'trainer_type':'TRAINER_TYPE_NONE','trainer_sight_or_berry_tree_id':'0','script':m['name']+'_GalarInspect','flag':'0'})
  components_report.append({'map':did,'component_tiles':len(component),'door_access':score(component)[2] if component else 0,'inspection':bool(candidates and len(component)>=12)})
  (R/l['blockdata_filepath']).write_bytes(struct.pack('<'+'H'*len(cells),*cells));dump(R/'data/maps'/m['name']/'map.json',m)
 for f,a,t,r in banks.values():(f/'metatile_attributes.bin').write_bytes(a);(f/'metatiles.bin').write_bytes(t)
 oldtour=json.loads((D/'inspection_arrivals.json').read_text());rank={z['donor_id']:i for i,z in enumerate(oldtour)};tour.sort(key=lambda z:rank.get(z['donor_id'],1000+int(z['donor_id'].split('.')[0])*1000+int(z['donor_id'].split('.')[1])));assert tour[0]['donor_id']=='3.0'
 byid={z['donor_id']:z for z in tour}
 for did,(m,l,keys,cells) in rows.items():
  f=R/'data/maps'/m['name']/'scripts.inc';text=f.read_text();marker='\n'+m['name']+'_GalarInspect::';text=text[:text.index(marker)] if marker in text else text
  if did in byid:
   z=byid[did];nxt=tour[(tour.index(z)+1)%len(tour)];text+=f'\n{z["map"]}_GalarInspect::\n\tloadword 0, {z["map"]}_GalarInspectText\n\tcall Galar_InspectionPrompt\n\twarp {nxt["map_id"]}, {nxt["spawn"][0]}, {nxt["spawn"][1]}\n\tgoto Galar_InspectionFinish\n{z["map"]}_GalarInspectText:\n\t.string "Galar map {did}. Visit next?\\p"\n\t.string "YES: next. NO: Littleroot.$"\n'
  f.write_text(text)
 first=tour[0];f=R/'data/scripts/la_teleport_scientist.inc';text=f.read_text();text=re.sub(r'warp MAP_AMAP_3_0_POSTWICK, \d+, \d+',f'warp MAP_AMAP_3_0_POSTWICK, {first["spawn"][0]}, {first["spawn"][1]}',text);f.write_text(text)
 dump(D/'inspection_arrivals.json',tour);dump(D/'travel_cell_changes.json',changes);dump(D/'disabled_links.json',issues);dump(D/'arrival_components.json',components_report);dump(D/'editor_only_maps.json',[z for z in ledger if z['donor_id'] not in byid]);dump(D/'travel_repair.json',{'actual_tile_warps':sum(map(len,enabled.values())),'inspection_maps':len(tour),'postwick_arrival':first['spawn'],'reciprocal_repairs':remaps,'disabled_warps':len(issues),'runtime_verified':False})
 print((D/'travel_repair.json').read_text()[:1500])
if __name__=='__main__':main()
