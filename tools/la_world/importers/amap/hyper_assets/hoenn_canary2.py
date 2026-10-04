#!/usr/bin/env python3
"""Opening-spine canary #2: four new canonical layouts; retain confirmed #1."""
import collections,copy,csv,hashlib,importlib.util,json,re,struct
from pathlib import Path
SPEC=importlib.util.spec_from_file_location('first',Path(__file__).with_name('hoenn_canary1.py'));C=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(C)
ROOT=C.ROOT;OUT=ROOT/'.la_work/amap/hyper_hoenn_canary2'
TARGETS={'LittlerootTown':'0.9','Route101':'0.16','Route103':'0.18','PetalburgCity':'0.0'}
RETAINED={'OldaleTown':'0.10','Route102':'0.17','OldaleTown_Mart':'2.4'}
CHANGED=['data/layouts/layouts.json',*[f'data/maps/{n}/map.json' for n in TARGETS],'data/maps/Route103/scripts.inc','data/maps/PetalburgCity/scripts.inc','src/hyper_asset_graphics_bindings.inc','src/data/object_events/hyper_assets.inc']
load=C.load;dump=C.dump;digest=C.digest;words=C.words
PATCH={'map':'Route101','x':7,'y':18,'before':0x140F,'after':0x3001,'reason':'Native west rescue-containment trigger at (6,18) steps player right. Hyper shrub blocks (7,18); replace this one landing cell with Hyper normal grass/elevation3, preserving all native rescue scripts.'}
PATCH_PATH='data/hyper_assets/canary2_layouts/Route101/map.bin'
class Grid(C.Grid):
 def walk(self,x,y):
  v=self.cell(x,y);return v['collision']==0 and v['elevation'] in [0,3,15] and v['translated_behavior'] not in range(0x10,0x16)
 def surface(self,x,y):return self.cell(x,y)['collision']==0

def baseline():
 OUT.mkdir(exist_ok=True);p=OUT/'baseline.json'
 if p.exists():return load(p)
 b={str(p.relative_to(ROOT)):digest(p) for d in ['data','src','include','graphics'] for p in (ROOT/d).rglob('*') if p.is_file() and not C.derived(str(p.relative_to(ROOT)))}
 for f in CHANGED:
  p=OUT/'original'/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/f).read_bytes())
 dump(OUT/'baseline.json',b);return b

def donor(k):
 a,b=k.split('.');p=next((ROOT/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export/maps').glob(f'{int(a):02}.{int(b):02}_*/map.json'));return load(p),str(p.relative_to(ROOT))
def prepare():
 b=baseline();assert all(digest(ROOT/f)==b[f] for f in CHANGED),'Applied batch or changed inputs: validate receipt, do not overwrite.'
 cat=load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');byid={x['donor_id']:x for x in cat['layouts']};ls=load(ROOT/'data/layouts/layouts.json');maps={};ledger=[];grids={n:Grid(byid[k]) for n,k in {**TARGETS,**RETAINED}.items()}
 pg=grids['Route101'];at=PATCH['y']*pg.w+PATCH['x'];assert pg.blocks[at]==PATCH['before'];pg.blocks[at]=PATCH['after']
 remaps={'LittlerootTown':{'object_events':{2:None},'warp_events':{2:None},'bg_events':{0:None,1:None,2:None,3:None}},'Route101':{'object_events':{1:(4,13),3:(5,13)},'bg_events':{0:None}},'Route103':{'object_events':{0:None,5:None,6:None,7:None,8:None,11:None,13:None,14:None,15:None,16:None},'bg_events':{0:None}},'PetalburgCity':{'object_events':{7:None},'warp_events':{0:None,3:None,4:None},'bg_events':{i:None for i in range(8)}}}
 dk={'object_events':'npcs','warp_events':'warps','coord_events':'coord_events','bg_events':'bg_events'}
 for name,k in TARGETS.items():
  m=load(ROOT/f'data/maps/{name}/map.json');d,dp=donor(k);g=grids[name]
  for key in dk:
   for i,e in enumerate(m[key]):
    before=copy.deepcopy(e);probe=d[dk[key]][i] if i<len(d[dk[key]]) else None;choice=remaps.get(name,{}).get(key,{})
    reason='Retain native coordinate, valid Hyper cell; native script/state/role remains authoritative.'
    if i in choice:
     xy=choice[i] if choice[i] is not None else (probe['x'],probe['y']);e['x'],e['y']=xy
     reason='Role-matched source event and actual geometry: copy only x/y; preserve native gameplay fields.'
     if name=='Route101' and key=='object_events':reason='Native chase final positions (Birch 4,13; Zigzagoon 5,13) are valid Hyper cells. Donor/default 9/10,13 lie in trees; rescue script already overrides both starts and is unchanged.'
    if name=='LittlerootTown' and key=='object_events' and i==8:probe=None;reason='Existing LA teleport scientist is project-owned, not donor local9. Preserve hook, art, flag and valid original (10,16) placement.'
    if name=='PetalburgCity' and key=='object_events' and i in [5,6]:reason='Keep native item positions and persistent item flags; donor local6/7 are not trusted as identical reward roles.'
    c=g.cell(e['x'],e['y']);neighbors=[g.cell(x,y) for x,y in [(e['x']+1,e['y']),(e['x']-1,e['y']),(e['x'],e['y']+1),(e['x'],e['y']-1)] if 0<=x<g.w and 0<=y<g.h and g.surface(x,y)]
    if key=='object_events':
     if e['graphics_id']=='OBJ_EVENT_GFX_MOM':assert c['translated_behavior']==0x69 # Native doorway staging, then scripted exit.
     elif e['graphics_id']=='OBJ_EVENT_GFX_BERRY_TREE':assert c['translated_behavior']==0xA0 and g.walk(e['x'],e['y']+1),c
     elif e['graphics_id'].startswith('OBJ_EVENT_GFX_SWIMMER'):assert c['translated_behavior'] in range(0x10,0x16),c
     else:assert g.walk(e['x'],e['y']),(name,key,i,c)
    elif key=='coord_events':assert g.walk(e['x'],e['y']) and c['elevation']==e['elevation']
    elif key=='warp_events':
     if name=='Route103':assert (e['x'],e['y'])==(45,6) # Native postgame OnLoad opens the closed cave.
     else:assert c['translated_behavior']==0x69 and g.walk(e['x'],e['y']+1),(name,i,c)
    elif key=='bg_events':assert neighbors
    ledger.append({'map':name,'donor_id':k,'canonical_id':m['id'],'kind':key,'index':i,'role':e.get('script',e.get('item',e.get('dest_map'))),'before':before,'after':copy.deepcopy(e),'cell':c,'interaction_neighbors':neighbors,'donor_reference':probe,'donor_json':dp,'reason':reason,'owner':'pokeemerald-expansion/project'})
  l=next(x for x in ls['layouts'] if x['id']==m['layout']);source=byid[k];l.update(primary_tileset=source['primary_tileset'],secondary_tileset=source['secondary_tileset'],blockdata_filepath=source['blockdata_path'],border_filepath=source['border_path']);assert [l['width'],l['height']]==source['dimensions'];maps[name]=m
  if name=='Route101':l['blockdata_filepath']=PATCH_PATH
 return b,cat,ls,maps,ledger,grids

def movement_blocks(text):return {m[1]:[x.strip() for x in m[2].splitlines() if x.strip() and not x.strip().startswith('@')] for m in re.finditer(r'^(\w+_Movement_\w+):\n(.*?)(?=^\w+:|\Z)',text,re.M|re.S)}
def scripts():
 outputs={};edits=[]
 for n in ['Route103','PetalburgCity']:
  p=f'data/maps/{n}/scripts.inc';s=(ROOT/p).read_text();blocks=movement_blocks(s)
  labels=['Route103_Movement_RivalExitFacingNorth2'] if n=='Route103' else [f'PetalburgCity_Movement_{actor}WalkToGym{i}' for actor in ['Boy','Player'] for i in range(4)]+['PetalburgCity_Movement_BoyWalkAway']
  for label in labels:
   m=re.search(r'^'+label+r':\n(.*?)(?=^\w+:|\Z)',s,re.M|re.S);old=m[1]
   if n=='Route103':
    pos=old.rfind('\twalk_down\n');assert pos>=0;new=old[:pos]+old[pos:].replace('\twalk_down\n','',1);reason='North-facing rival ends at (9,9), before Hyper tree (9,10); retain ledge jump, native removal, battles and flags.'
   elif 'BoyWalkAway' in label:
    new=old.replace('\twalk_down\n','\twalk_down\n\twalk_down\n',1);reason='Return guide from remapped (16,9) via native row11 to unchanged (5,11).'
   elif '_Boy' in label:
    at=old.rfind('\twalk_right\n');assert at>=0;new=old[:at]+'\twalk_up\n'+old[at:];reason='Native gym guide now ends at (16,9), beside actual Hyper gym sign (17,9).'
   else:new=old.replace('\tstep_end','\twalk_up\n\tstep_end');reason='Player follows native guide to (15,9), in front of the same canonical Gym door.'
   s=s[:m.start(1)]+new+s[m.end(1):];edits.append({'file':p,'label':label,'before':old,'after':new,'reason':reason,'ownership':'native expansion movement data; no story command changes'})
  outputs[p]=s
 return outputs,edits
def trace(grids,name,xy,labels,script_text,allow_door=False,offscreen=False):
 blocks=movement_blocks(script_text);x,y=xy;steps=[]
 for label in labels:
  assert label in blocks,label
  for command in blocks[label]:
   direction=re.search(r'_(up|down|left|right)$',command)
   moving=direction and command.startswith(('walk_','jump_')) and 'in_place' not in command
   if not moving:continue
   dx,dy={'up':(0,-1),'down':(0,1),'left':(-1,0),'right':(1,0)}[direction[1]];distance=2 if command.startswith('jump_2_') else 1
   x+=dx*distance;y+=dy*distance;current=name;cx,cy=x,y
   g=grids[name]
   if name=='PetalburgCity' and x>=g.w:current='Route102';cx=x-g.w;cy=y-10
   if name=='PetalburgCity' and x<0 and offscreen:steps.append({'xy':[x,y],'command':command,'native_offscreen_exit':True});continue
   cell=grids[current].cell(cx,cy)
   # Explicit native doorway entry and original twin forest staging are allowed.
   permitted=grids[current].walk(cx,cy) or (allow_door and cell['translated_behavior']==0x69) 
   if not permitted and name=='LittlerootTown' and 'TwinReturn' in label:
    native=next(l for l in load(OUT/'original/data/layouts/layouts.json')['layouts'] if l['id']=='LAYOUT_LITTLEROOT_TOWN');before=words(ROOT/native['blockdata_filepath'])[cy*native['width']+cx];permitted=((before>>10)&3)!=0;cell['native_forced_forest_staging_block']=before
   assert permitted,(name,label,command,cell)
   steps.append({'map':current,'cell':cell,'command':command})
 return {'map':name,'start':list(xy),'labels':labels,'end':[x,y],'steps':steps,'owner':'native expansion movement data'}

def scene_checks(grids,script_output):
 records=[]
 def text(n):return script_output.get(f'data/maps/{n}/scripts.inc',(ROOT/f'data/maps/{n}/scripts.inc').read_text())
 def add(n,xy,labels,**kw):v=trace(grids,n,xy,labels,text(n),**kw);records.append(v);return tuple(v['end'])
 for shift in [0,9]:
  add('LittlerootTown',(3+shift,10),['LittlerootTown_Movement_PlayerStepOffTruck','LittlerootTown_Movement_PlayerApproachDoor','LittlerootTown_Movement_PlayerEnterHouse'],allow_door=True)
  add('LittlerootTown',(5+shift,8),['LittlerootTown_Movement_MomExitHouse','LittlerootTown_Movement_MomApproachPlayerAtTruck','LittlerootTown_Movement_MomApproachDoor','LittlerootTown_Movement_MomEnterHouse'],allow_door=True)
 for side in ['Left','Right']:
  end=add('LittlerootTown',(7,2),['LittlerootTown_Movement_TwinApproachPlayer'+side]);add('LittlerootTown',end,['LittlerootTown_Movement_TwinReturn'+side])
 for i,x in [(0,10),(1,11)]:
  end=add('LittlerootTown',(x,9),['LittlerootTown_Movement_MomApproachPlayer'+str(i)]);add('LittlerootTown',end,['LittlerootTown_Movement_MomReturnHome'+str(i)])
 for gender,start in [('Male',(5,9)),('Female',(14,9))]:
  for i in range(2,6):
   end=add('LittlerootTown',start,[f'LittlerootTown_Movement_MomApproachPlayer{gender}{i}']);add('LittlerootTown',end,[f'LittlerootTown_Movement_MomReturnHome{gender}{i}','LittlerootTown_Movement_MomExitThroughDoor'],allow_door=True)
 for x in [10,11]:add('Route101',(x,19),['Route101_Movement_EnterScene'])
 end=add('Route101',(0,15),['Route101_Movement_BirchRunAway1','Route101_Movement_BirchRunInCircles']);assert end==(4,13);add('Route101',end,['Route101_Movement_BirchApproachPlayer'])
 end=add('Route101',(0,16),['Route101_Movement_ZigzagoonChase1','Route101_Movement_ZigzagoonChaseInCircles']);assert end==(5,13)
 for x in [10,11]:add('Route101',(x,18),['Route101_Movement_PreventExitSouth'])
 for y in range(15,19):add('Route101',(6,y),['Route101_Movement_PreventExitWest'])
 add('Route101',(7,13),['Route101_Movement_PreventExitNorth'])
 add('Route103',(10,3),['Route103_Movement_RivalExitFacingNorth1','Route103_Movement_RivalExitFacingNorth2']);add('Route103',(10,3),['Route103_Movement_RivalExit1','Route103_Movement_RivalExit2'])
 for i in range(4):
  end=add('PetalburgCity',(5,11),[f'PetalburgCity_Movement_BoyApproachPlayer{i}',f'PetalburgCity_Movement_BoyWalkToGym{i}']);assert end==(16,9);add('PetalburgCity',end,['PetalburgCity_Movement_BoyWalkAway'])
  end=add('PetalburgCity',(8,10+i),[f'PetalburgCity_Movement_PlayerWalkToGym{i}']);assert end==(15,9)
 add('PetalburgCity',(15,9),['PetalburgCity_Movement_WallyTutorialPlayer']);add('PetalburgCity',(15,10),['PetalburgCity_Movement_WallyTutorialWally'])
 add('PetalburgCity',(15,9),['PetalburgCity_Movement_WalkToWallyHousePlayer','PetalburgCity_Movement_WalkInsideHousePlayer'],allow_door=True)
 add('PetalburgCity',(15,10),['PetalburgCity_Movement_WalkToWallyHouseWallysDad','PetalburgCity_Movement_WalkInsideHouseWallysDad'],allow_door=True)
 for y in range(10,14):
  end=add('PetalburgCity',(13,y),['PetalburgCity_Movement_ScottStartWalkLeft','PetalburgCity_Movement_ScottApproachPlayer']);add('PetalburgCity',end,[f'PetalburgCity_Movement_ScottExit{y-10}'],offscreen=True)
 return records

def seam_checks(grids):
 # Compare actual crossability, not decorative canopy or blocked-cell elevation.
 ls=load(OUT/'original/data/layouts/layouts.json')['layouts'];old={}
 for n in {**TARGETS,**RETAINED,'Route104':'0.19','Route110':'0.25'}:
  m=load(ROOT/f'data/maps/{n}/map.json');l=next(x for x in ls if x['id']==m['layout']);old[n]=(l,words(ROOT/l['blockdata_filepath']))
 def cell(n,x,y,new):
  if new and n in grids:return grids[n].cell(x,y)['block']
  l,b=old[n];return b[y*l['width']+x]
 reports=[]
 for n in TARGETS:
  m=load(ROOT/f'data/maps/{n}/map.json');g=grids[n]
  for connection in m['connections']:
   target=next(k for k in old if load(ROOT/f'data/maps/{k}/map.json')['id']==connection['map']);tl=old[target][0];d=connection['direction'];off=connection['offset'];points=[]
   coords=[(x,0 if d=='up' else g.h-1) for x in range(g.w)] if d in ['up','down'] else [(0 if d=='left' else g.w-1,y) for y in range(g.h)]
   for x,y in coords:
    nx,ny=(x-off,tl['height']-1 if d=='up' else 0) if d in ['up','down'] else (tl['width']-1 if d=='left' else 0,y-off)
    if not(0<=nx<tl['width'] and 0<=ny<tl['height']):continue
    a,b=cell(n,x,y,False),cell(target,nx,ny,False);z,w=cell(n,x,y,True),cell(target,nx,ny,True)
    was=((a>>10)&3)==0 and ((b>>10)&3)==0;now=((z>>10)&3)==0 and ((w>>10)&3)==0
    assert was==now,(n,target,(x,y),(nx,ny),hex(a),hex(b),hex(z),hex(w))
    if now:assert z>>12==w>>12
    points.append({'from_xy':[x,y],'to_xy':[nx,ny],'original_crossable':was,'replacement_crossable':now})
   reports.append({'from':n,'to':target,'direction':d,'offset':off,'cells':points})
 return reports

STATIC={'LittlerootTown':{'TWIN':6,'FAT_MAN':17,'BOY_2':7,'MOM':215,'PROF_BIRCH':64,'RIVAL_BRENDAN_NORMAL':100,'RIVAL_MAY_NORMAL':105},'Route101':{'YOUNGSTER':35,'PROF_BIRCH':64,'BOY_2':9},'Route103':{'MAN_3':33,'WOMAN_2':20,'TWIN':6,'FISHERMAN':50,'BOY_1':7,'PROF_BIRCH':64,'POKEFAN_M':19,'CUTTABLE_TREE':82,'BLACK_BELT':44,'MAN_5':99,'SWIMMER_F':43,'SWIMMER_M':42,'RIVAL_BRENDAN_NORMAL':100,'RIVAL_MAY_NORMAL':105},'PetalburgCity':{'WOMAN_4':26,'WALLY':135,'BOY_1':7,'GENTLEMAN':48,'POKEFAN_M':19,'BOY_2':9,'SCOTT':219}}
def graphics(cat):
 native=(ROOT/'src/data/object_events/object_event_graphics_info.h').read_text();ptr=(ROOT/'src/data/object_events/object_event_graphics_info_pointers.h').read_text();objects={x['source_graphics_id']:x for x in cat['object_graphics']};defs=[];bindings=[];audit=[]
 for n,entries in STATIC.items():
  for role,i in entries.items():
   gfx='OBJ_EVENT_GFX_'+role;symbol=re.search(r'\['+gfx+r'\]\s*=\s*&(\w+)',ptr)[1];body=re.search(r'const struct ObjectEventGraphicsInfo '+symbol+r' = \{(.*?)\};',native,re.S)[1];obj=objects[i]
   assert all(int(re.search(r'\.'+f+r'\s*=\s*(\d+)',body)[1])==obj[f] for f in ['width','height']),(n,role,i)
   adapter=f'gHyperCanary2Graphics_{n}_{role}';new=re.sub(r'(\.paletteTag\s*=\s*)[^,]+',lambda m:m[1]+f'0x{obj["palette_tag"]:04X}',body);new=re.sub(r'(\.images\s*=\s*)\w+',lambda m:m[1]+f'sPicTable_HyperAsset{i:03}',new);defs.append('static const struct ObjectEventGraphicsInfo '+adapter+' = {'+new+'};');bindings.append(f'    {{{load(ROOT/f"data/maps/{n}/map.json")["id"]}, {gfx}, &{adapter}}},');audit.append({'map':n,'expansion_symbol':gfx,'source_graphics_id':i,'native_contract':body,'replacement':new,'source_frame_count':obj['frame_count'],'adapter':adapter})
 bindings.append('    {MAP_ROUTE102, OBJ_EVENT_GFX_WALLY, &gHyperCanary2Graphics_PetalburgCity_WALLY}, /* native tutorial crosses this connection */')
 return '/* Canary #2 art-only adapters: retain all native runtime/animation fields. */\n'+'\n\n'.join(defs)+'\n','\n'.join(bindings)+'\n',audit

def apply():
 b,cat,ls,maps,ledger,grids=prepare();script_out,edits=scripts();scenes=scene_checks(grids,script_out);seams=seam_checks(grids);gfx,bindings,gaudit=graphics(cat)
 patchfile=ROOT/PATCH_PATH;patchfile.parent.mkdir(parents=True,exist_ok=True);patchfile.write_bytes(struct.pack('<'+'H'*len(grids['Route101'].blocks),*grids['Route101'].blocks))
 for n,m in maps.items():dump(ROOT/f'data/maps/{n}/map.json',m)
 dump(ROOT/'data/layouts/layouts.json',ls)
 for f,s in script_out.items():(ROOT/f).write_text(s)
 af='src/data/object_events/hyper_canary2_graphics.inc';(ROOT/af).write_text(gfx)
 p=ROOT/'src/hyper_asset_graphics_bindings.inc';p.write_text(p.read_text()+'\n/* Opening spine: four new maps plus Wally art during the retained Route102 tutorial. */\n'+bindings)
 p=ROOT/'src/data/object_events/hyper_assets.inc';s=p.read_text();s=s.replace('struct HyperAssetGraphicsBinding\n','#include "hyper_canary2_graphics.inc"\n\nstruct HyperAssetGraphicsBinding\n');p.write_text(s)
 result={'schema':'hyper-hoenn-canary2-ledger-v1','events':ledger,'movement_edits':edits,'native_scene_paths':scenes,'connection_checks':seams,'graphics_adapters':gaudit,'native_renderers_retained':['player','trucks','Birchs bag / ChooseStarter','species Zigzagoon','berry growth','item/follower PokeBall','LA teleport scientist'],'hyper_gameplay_imported':False,'geometry_compatibility_patches':[PATCH]}
 dump(OUT/'coordinate_remap_ledger.json',result)
 with (OUT/'coordinate_remap_ledger.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['map','kind','index','role','old_x','old_y','new_x','new_y','reason'])
  for e in ledger:w.writerow([e['map'],e['kind'],e['index'],e['role'],e['before']['x'],e['before']['y'],e['after']['x'],e['after']['y'],e['reason']])
 receipt={'schema':'hyper-hoenn-canary2-receipt-v1','canonical_maps_replaced':list(TARGETS),'donor_ids':TARGETS,'retained_confirmed_canary1':RETAINED,'runtime_verified':False,'hyper_gameplay_imported':False,'changed_baseline_files':{f:{'before':b[f],'after':digest(ROOT/f)} for f in CHANGED},'new_files':{af:digest(ROOT/af),PATCH_PATH:digest(ROOT/PATCH_PATH)},'map_ids_header_sha256':digest(ROOT/'include/constants/map_groups.h'),'map_groups_json_sha256':digest(ROOT/'data/maps/map_groups.json'),'layout_count_before_after':[len(load(OUT/'original/data/layouts/layouts.json')['layouts']),len(ls['layouts'])]}
 dump(OUT/'receipt.json',receipt);print('Applied four new canonical maps; confirmed Canary #1 maps retain geometry/events/scripts.')

def validate():
 b=load(OUT/'baseline.json');receipt=load(OUT/'receipt.json');changes=receipt['changed_baseline_files'];assert set(changes)==set(CHANGED)
 for f,h in b.items():assert digest(ROOT/f)==C.third_canary_hash(f,changes[f]['after'] if f in changes else h),f
 for f,h in receipt['new_files'].items():assert digest(ROOT/f)==h
 oldls=load(OUT/'original/data/layouts/layouts.json');newls=load(ROOT/'data/layouts/layouts.json');assert len(oldls['layouts'])+(3 if C.third_receipt() else 0)+C.fourth_layout_delta()==len(newls['layouts']);changedids={load(OUT/'original'/f'data/maps/{n}/map.json')['layout'] for n in TARGETS}
 for a,z in zip(oldls['layouts'],newls['layouts']):
  assert a['id']==z['id']
  if a['id'] not in changedids and a['id'] not in ([load(ROOT/f'data/maps/{n}/map.json')['layout'] for n in C.THIRD_TARGETS] if C.third_receipt() else []) and a['id'] not in C.fourth_layout_ids():assert a==z
  else:assert {k:v for k,v in a.items() if k not in ['primary_tileset','secondary_tileset','blockdata_filepath','border_filepath']}=={k:v for k,v in z.items() if k not in ['primary_tileset','secondary_tileset','blockdata_filepath','border_filepath']}
 for n in TARGETS:
  a=load(OUT/'original'/f'data/maps/{n}/map.json');z=load(ROOT/f'data/maps/{n}/map.json')
  for key in a:
   if key.endswith('_events'):
    assert len(a[key])+len(C.third_gates(n) if key=='object_events' else [])==len(z[key]);assert [{k:v for k,v in e.items() if k not in ['x','y']} for e in a[key]]==[{k:v for k,v in e.items() if k not in ['x','y']} for e in z[key][:len(a[key])]]
   else:assert a[key]==z[key],(n,key)
 # Reconstruct the two reviewed movement-data edits; everything outside those
 # movement blocks, including story commands and text, must match original.
 ledger=load(OUT/'coordinate_remap_ledger.json')
 for f in ['data/maps/Route103/scripts.inc','data/maps/PetalburgCity/scripts.inc']:
  s=(ROOT/f).read_text().split('\n@ Project-owned reservation;')[0]
  for edit in reversed([x for x in ledger['movement_edits'] if x['file']==f]):
   match=re.search(r'^'+edit['label']+r':\n(.*?)(?=^\w+:|\Z)',s,re.M|re.S);assert match[1]==edit['after'];s=s[:match.start(1)]+edit['before']+s[match.end(1):]
  assert s==(OUT/'original'/f).read_text(),f
 assert digest(ROOT/'include/constants/map_groups.h')==receipt['map_ids_header_sha256'];assert digest(ROOT/'data/maps/map_groups.json')==receipt['map_groups_json_sha256']
 result={'passed':True,'protected_files_checked':len(b),'new_maps':list(TARGETS),'retained_maps':list(RETAINED),'canonical_ids_layout_ids_unchanged':True,'hyper_gameplay_imported':False,'native_story_commands_unchanged':True,'runtime_verified':False};dump(OUT/'validation.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--apply',action='store_true');p.add_argument('--validate',action='store_true');a=p.parse_args()
 if a.apply:apply()
 elif a.validate:validate()
 else:
  _,cat,_,_,_,grids=prepare();s,_=scripts();scene_checks(grids,s);seam_checks(grids);graphics(cat);print('All opening-spine preflight checks passed; no maps changed.')
