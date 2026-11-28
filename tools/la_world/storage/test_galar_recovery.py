"""Native reviewed Galar recovery and stable Unova retirement; isolated battery."""
from pathlib import Path
import json,struct,hashlib,subprocess
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/la_world/galar_recovery';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
G=json.loads((R/'data/maps/map_groups.json').read_text());L={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']}
def mapid(name):
 for group,key in enumerate(G['group_order']):
  if name in G[key]:return group,G[key].index(name)
 raise KeyError(name)
ledger=json.loads((D/'import_ledger.json').read_text());arrivals=json.loads((D/'runtime_arrivals.json').read_text())
check('56_reviewed_maps',len(ledger)==56 and len(arrivals)==56)
check('Unova_removed_from_active_map_groups',not any('Unova' in k for k in G['group_order']))
# Preserve every unrelated map's numerical bank and index.
old=json.loads(subprocess.check_output(['git','show','bfa6112e58:data/maps/map_groups.json'],text=True))
for group,key in enumerate(old['group_order']):
 if 'Unova' in key:continue
 check('stable_'+key,G['group_order'].index(key)==group and G[key]==old[key])
for row in ledger:
 name=row['project_name'];m=json.loads((R/'data/maps'/name/'map.json').read_text());l=L[m['layout']]
 check(name+'_registered',mapid(name)[0]<127)
 check(name+'_layout_size',len((R/l['blockdata_filepath']).read_bytes())==l['width']*l['height']*2)
 check(name+'_no_donor_actors_or_scripts',not m['object_events'] and not m['coord_events'] and not m['bg_events'] and (R/'data/maps'/name/'scripts.inc').read_text()==name+'_MapScripts::\n\t.byte 0\n')
 for w in m['warp_events']:
  if w['x']<0:continue
  target=next(z['project_name'] for z in ledger if 'MAP_'+z['project_name'].upper()==w['dest_map'])
  dest=json.loads((R/'data/maps'/target/'map.json').read_text())['warp_events'][int(w['dest_warp_id'])]
  check(name+'_warp_'+str((w['x'],w['y']))+'_valid_target',dest['x']>=0)
start(0)
for row in arrivals:
 group,mid=mapid(row['map']);x,y=row['spawn'];warp(group,mid,x,y);frames(30)
 check(row['map']+'_native_location',location()==(group,mid))
 check(row['map']+'_field_loop',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 check(row['map']+'_spawn_position',pos()==(x,y))
 check(row['map']+'_walkable_floor',invoke('MapGridGetCollisionAt',x+7,y+7)==0)
 header=invoke('Overworld_GetMapHeaderByGroupAndId',group,mid) if 'Overworld_GetMapHeaderByGroupAndId' in symbols else invoke('GetMapHeaderFromGroupAndId',group,mid)
 check(row['map']+'_native_name',invoke('RegionalMapDisplayName',header)!=0)
 if row['donor_id'] in ['3.0','5.6','6.10','7.11','8.7','9.10','10.21','11.10','12.10','14.10','3.9']:
  shutil.copy2(shot('Galar_'+row['donor_id']),D/(row['donor_id'].replace('.','_')+'.png'))
print('PASS map arrivals',flush=True)
# Exercise every active warp destination via native entry handling.
warps=0
for row in ledger:
 m=json.loads((R/'data/maps'/row['project_name']/'map.json').read_text())
 for index,w in enumerate(m['warp_events']):
  if w['x']<0:continue
  target=next(z['project_name'] for z in ledger if 'MAP_'+z['project_name'].upper()==w['dest_map']);group,mid=mapid(target)
  a=symbols['sWarpDestination']
  for i,v in enumerate(struct.pack('<BBbxhh',group,mid,int(w['dest_warp_id']),-1,-1)):wr(a+i,v,1)
  wr(symbols['gMain']+4,symbols['WarpIntoMap']|1);frames(2);wr(symbols['gMain']+4,symbols['CB2_LoadMap']|1);frames(210)
  check(row['project_name']+'_native_warp_'+str(index),location()==(group,mid) and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
  x,y=pos();check(row['project_name']+'_native_warp_floor_'+str(index),invoke('MapGridGetCollisionAt',x+7,y+7)==0)
  warps+=1
print('PASS warps',warps,flush=True)
# The selected Postwick version and Route 1 must connect in both directions.
post=next(z for z in arrivals if z['donor_id']=='3.0');route=next(z for z in arrivals if z['donor_id']=='3.19')
pg,pm=mapid(post['map']);rg,rm=mapid(route['map'])
route_map=json.loads((R/'data/maps'/route['map']/'map.json').read_text());route_height=L[route_map['layout']]['height']
warp(pg,pm,23,0);frames(32,64);frames(60)
check('Postwick_to_Route1_walk',location()==(rg,rm))
warp(rg,rm,22,route_height-1);frames(32,128);frames(60)
check('Route1_to_Postwick_walk',location()==(pg,pm))

# Old Unova numeric banks continue to redirect safely through the existing guard.
for group in range(104,109):
 warp(group,0,1,1);check('retired_bank_'+str(group)+'_redirects',location()==mapid('LittlerootTown'))
post=next(z for z in arrivals if z['donor_id']=='3.0');group,mid=mapid(post['map']);warp(group,mid,*post['spawn'])
invoke('ScriptGiveMon',25,10,0)
check('save_Galar',invoke('TrySavingData',0)==1)
check('reload_Galar',invoke('LoadGameSave',0)==1)
check('Galar_location_persists',location()==(group,mid))
check('party_persists',rd(symbols['gPartiesCount'],1)==1)
lib.shutdown()
(D/'runtime-validation.json').write_text(json.dumps(dict(checks=checks,maps_tested=len(arrivals),warp_destinations_tested=warps,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'Galar recovery checks',flush=True)
