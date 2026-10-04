#!/usr/bin/env python3
"""Hash-guarded Rustboro progression assets and project-owned construction gates."""
import argparse,collections,copy,csv,importlib.util,json,re,struct
from pathlib import Path
s=importlib.util.spec_from_file_location('opening',Path(__file__).with_name('hoenn_canary2.py'));C=importlib.util.module_from_spec(s);s.loader.exec_module(C)
ROOT=C.ROOT;OUT=ROOT/'.la_work/amap/hyper_hoenn_canary3';load=C.load;dump=C.dump;digest=C.digest;words=C.words
TARGETS={'Route104':'0.19','PetalburgWoods':'24.11','RustboroCity':'0.3','Route116':'0.31','RusturfTunnel':'24.4','RustboroCity_DevonCorp_1F':'11.0','RustboroCity_DevonCorp_2F':'11.1','RustboroCity_DevonCorp_3F':'11.2','RustboroCity_Gym':'11.3','RustboroCity_CuttersHouse':'11.11','RustboroCity_PokemonCenter_1F':'11.5','RustboroCity_Mart':'11.7','RustboroCity_PokemonSchool':'11.4','Route104_MrBrineysHouse':'17.0','Route104_PrettyPetalFlowerShop':'17.1','Route116_TunnelersRestHouse':'21.0'}
GATE_ONLY={'Route102':'0.17','Route103':'0.18'}
PATCH={'map':'RustboroCity','x':30,'y':12,'before':0x160F,'after':0x32BB,'reason':'One Hyper hedge cell blocks the native south approach to the Devon employee. Extend the adjacent city floor by one cell, preserving both native help/return branch triggers and movement.'}
PATCH_PATH='data/hyper_assets/canary3_layouts/RustboroCity/map.bin'
TUNNEL_PATCHES=[{'map':'RusturfTunnel','x':23,'y':6,'before':0x4209,'after':0x1609,'reason':'Hyper side corridor bypasses native Rock Smash gate. Same metatile is a wall in native geometry; restore collision/elevation without changing artwork.'},{'map':'RusturfTunnel','x':19,'y':10,'before':0x4211,'after':0x1611,'reason':'Close the second native-wall bypass into the south annex; preserve two original rock objects and their native flags/HM scene.'}]
TUNNEL_PATCH_PATH='data/hyper_assets/canary3_layouts/RusturfTunnel/map.bin'
SCRIPT_MAPS=['RustboroCity_DevonCorp_1F','PetalburgWoods','RustboroCity','Route102','Route103','Route104','Route116','RusturfTunnel']
CHANGED=['data/layouts/layouts.json',*[f'data/maps/{n}/map.json' for n in {**TARGETS,**GATE_ONLY}],*[f'data/maps/{n}/scripts.inc' for n in SCRIPT_MAPS],'src/hyper_asset_graphics_bindings.inc','src/data/object_events/hyper_assets.inc','src/data/heal_locations.json','src/data/heal_locations.h']
class Grid(C.Grid):
 def walk(self,x,y):
  v=self.cell(x,y);return v["collision"]==0 and v["elevation"] in [0,3,4,15] and v["translated_behavior"] not in range(0x10,0x16)
 def neighbors(self,x,y):return [(a,b) for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if 0<=a<self.w and 0<=b<self.h and self.cell(a,b)['collision']==0 and self.cell(a,b)['translated_behavior'] not in range(0x10,0x16)]

def baseline():
 OUT.mkdir(parents=True,exist_ok=True)
 if (OUT/'baseline.json').exists():
  b=load(OUT/'baseline.json')
  for f in CHANGED:
   q=OUT/'original'/f
   if not q.exists():
    assert digest(ROOT/f)==b[f];q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes((ROOT/f).read_bytes())
  return b
 b={str(f.relative_to(ROOT)):digest(f) for d in ['data','src','include','graphics'] for f in (ROOT/d).rglob('*') if f.is_file() and not C.C.derived(str(f.relative_to(ROOT)))}
 for f in CHANGED:
  q=OUT/'original'/f;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes((ROOT/f).read_bytes())
 dump(OUT/'baseline.json',b);return b

def new_scientist(n,i,x,y,script):return {'local_id':f'LOCALID_{re.sub(r"(?<!^)(?=[A-Z])","_",n).upper()}_CONSTRUCTION_{i}','graphics_id':'OBJ_EVENT_GFX_SCIENTIST_1','x':x,'y':y,'elevation':0,'movement_type':'MOVEMENT_TYPE_FACE_DOWN','movement_range_x':0,'movement_range_y':0,'trainer_type':'TRAINER_TYPE_NONE','trainer_sight_or_berry_tree_id':'0','script':script,'flag':'0'}

def script_geometry():
 outputs={n:(OUT/'original'/f'data/maps/{n}/scripts.inc').read_text() for n in SCRIPT_MAPS};edits=[]
 def replace(n,old,new,reason):
  assert old in outputs[n],(n,old);count=outputs[n].count(old);outputs[n]=outputs[n].replace(old,new);edits.append({'map':n,'before':old,'after':new,'occurrences':count,'reason':reason,'kind':'native geometry operand only'})
 replace('RustboroCity','goto_if_eq VAR_TEMP_0, 11, RustboroCity_EventScript_PositionScientistLeftExit','goto_if_eq VAR_TEMP_0, 12, RustboroCity_EventScript_PositionScientistLeftExit','Devon left doorway moved from x11 to x12; preserve native exit branch.')
 for a,b in [('12, 15','13, 17'),('11, 15','12, 17')]:replace('RustboroCity','setobjectxyperm LOCALID_RUSTBORO_SCIENTIST, '+a,'setobjectxyperm LOCALID_RUSTBORO_SCIENTIST, '+b,'Native Match Call scientist follows the relocated Devon double door.')
 def reroute(label,steps,reason):
  n='PetalburgWoods';key=n+'_Movement_'+label;r=re.search(r'^'+key+r':\n(.*?)(?=^\w+:|\Z)',outputs[n],re.M|re.S);assert r;old=r[1];tail='\tdelay_16\n\tdelay_16\n' if label=='AquaRunAway' else '';new=''.join('\twalk_fast_'+direction+'\n' for direction in steps)+tail+'\tstep_end\n\n';outputs[n]=outputs[n][:r.start(1)]+new+outputs[n][r.end(1):];edits.append({'map':n,'label':key,'before':old,'after':new,'reason':reason,'kind':'native movement data only'})
 reroute('AquaRunAway',['up']*4+['left']*2+['up']*3,'Exit via inspected source clearing (33,11), beyond scene camera, avoiding blocked canopy (35,13); native removal/flags retained.')
 reroute('DevonResearcherExitLeft',['right']+['up']*7+['left']*3+['up']*3,'Native researcher leaves via source clearing (33,11), outside scene camera; route around canopy before native removal.')
 reroute('DevonResearcherExitRight',['left']+['up']*7+['left']*2+['up']*3,'Right-side encounter uses the same inspected clearing exit without crossing blocked canopy; native scene commands unchanged.')
 return outputs,edits

def prepare():
 b=baseline();assert all(digest(ROOT/f)==b[f] for f in CHANGED),'Inputs changed or batch already applied; validate receipt instead.'
 cat=load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');by={x['donor_id']:x for x in cat['layouts']};ls=load(ROOT/'data/layouts/layouts.json');maps={};ledger=[];grids={n:Grid(by[k]) for n,k in {**TARGETS,**GATE_ONLY}.items()};donors={n:C.donor(k)[0] for n,k in {**TARGETS,**GATE_ONLY}.items()}
 pg=grids['RustboroCity'];at=PATCH['y']*pg.w+PATCH['x'];assert pg.blocks[at]==PATCH['before'];pg.blocks[at]=PATCH['after']
 for patch in TUNNEL_PATCHES:
  g=grids[patch['map']];at=patch['y']*g.w+patch['x'];assert g.blocks[at]==patch['before'];g.blocks[at]=patch['after']
 # Every selected source coordinate is a reviewed role match, not a bulk donor-event copy.
 remaps={'Route104':{'object_events':[2,3,8,15,16,17,18,19,20,21,22,23,24,25,28,30,31],'warp_events':[1],'bg_events':[2,3,4,5,6]},'PetalburgWoods':{'object_events':list(range(13)),'warp_events':list(range(6)),'coord_events':[0,1],'bg_events':list(range(6))},'RustboroCity':{'object_events':[0,1,2,4,5,6,7,10,12,14,15],'warp_events':list(range(12)),'bg_events':list(range(10))},'Route116':{'object_events':[14],'bg_events':[3,7,10]},'RusturfTunnel':{'object_events':[2]},'RustboroCity_DevonCorp_1F':{'bg_events':[0]}}
 dk={'object_events':'npcs','warp_events':'warps','coord_events':'coord_events','bg_events':'bg_events'}
 for n,k in TARGETS.items():
  m=load(ROOT/f'data/maps/{n}/map.json');d=donors[n];g=grids[n]
  for key,donorkey in dk.items():
   for i,e in enumerate(m[key]):
    old=copy.deepcopy(e);probe=d[donorkey][i] if i<len(d[donorkey]) else None;reason='Retain native coordinate, checked against actual Hyper geometry and native scene paths.'
    if i in remaps.get(n,{}).get(key,[]):
     e['x'],e['y']=probe['x'],probe['y'];reason='Reviewed matching event role, source geometry and reciprocal entrance; copy x/y only.'
    if n=='PetalburgWoods' and key=='object_events' and i==11:
     e['x'],e['y']=30,17;reason='Native Elixir retains its item/flag; donor local12 is a woman, so use donor extra item clearing (30,17), not its NPC coordinate.'
    if n=='RustboroCity' and key=='object_events' and i==11:
     e['x'],e['y']=34,14;reason='Native X Defend moved to donor item clearing; donor actor art/gameplay at this local ID is unrelated.'
    if n=='Route104' and key=='object_events' and i==19:reason='Native Cheri tree maps to donor soil (9,18); its berry identity remains native.'
    if n=='RustboroCity' and key=='coord_events' and i in [3,4]:
     e['x']=22;reason='Move two native theft triggers from Hyper building cells to adjacent corridor x22; their native scene commands are identical apart from unused branch operand.'
    if n=='RustboroCity' and key=='coord_events' and i>=13:
     e['y']=55;reason='Native eight-branch rival approach translates two cells south onto open corridor; event states and native movement data unchanged.'
    if n=='RustboroCity' and key=='object_events' and i==13:
     e['y']=52;reason='Native rival approach starts two cells south to avoid source building at (14,51); all eight approach branches remain native.'
    v=g.cell(e['x'],e['y']);near=g.neighbors(e['x'],e['y'])
    if key=='coord_events':assert g.walk(e['x'],e['y']) and v['elevation']==e['elevation'],(n,key,i,v)
    elif key=='object_events':
     if e['graphics_id']=='OBJ_EVENT_GFX_BERRY_TREE':assert v['translated_behavior']==0xA0 and near,(n,i,v)
     elif e.get('local_id') in ['LOCALID_ROUTE104_BOAT','LOCALID_ROUTE104_BRINEY','LOCALID_ROUTE104_RIVAL'] or e['graphics_id'] in ['OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE','OBJ_EVENT_GFX_GENTLEMAN']:
      assert near or e['graphics_id'] in ['OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE'] and g.walk(e['x'],e['y']+2) or e.get('local_id')=='LOCALID_ROUTE104_BOAT' and v['collision']==0 and v['elevation']==1,(n,i,v)
     else:assert g.walk(e['x'],e['y']) and near,(n,key,i,v)
    elif key=='warp_events':
     if n=='Route116' and i in [3,4]:pass # Native weather callback owns dynamically opened Terra Cave.
     else:assert v['translated_behavior'] in [0x60,0x65,0x69,0x6A,0x6B,0x6C,0x6D,0x6E] and near,(n,i,v)
    elif key=='bg_events':assert near,(n,key,i,v)
    ledger.append({'map':n,'donor_id':k,'canonical_id':m['id'],'kind':key,'index':i,'before':old,'after':copy.deepcopy(e),'donor_reference':probe,'cell':v,'interaction_neighbors':near,'reason':reason,'owner':'expansion/project'})
  source=by[k];original=next(x for x in ls['layouts'] if x['id']==m['layout']);l=original
  users=[f.parent.name for f in (ROOT/'data/maps').glob('*/map.json') if load(f)['layout']==original['id']]
  if any(x not in TARGETS for x in users):
   l=copy.deepcopy(original);l['id']='LAYOUT_HYPER_CANARY3_'+re.sub(r'(?<!^)(?=[A-Z])','_',n).upper();l['name']='HyperCanary3'+n+'_Layout';ls['layouts'].append(l);m['layout']=l['id']
  assert [l['width'],l['height']]==source['dimensions'];l.update(primary_tileset=source['primary_tileset'],secondary_tileset=source['secondary_tileset'],blockdata_filepath=source['blockdata_path'],border_filepath=source['border_path']);maps[n]=m
  if n=='RustboroCity':l['blockdata_filepath']=PATCH_PATH
  if n=='RusturfTunnel':l['blockdata_filepath']=TUNNEL_PATCH_PATH
 for n in GATE_ONLY:maps[n]=load(ROOT/f'data/maps/{n}/map.json')
 scripts,edits=script_geometry();gates=[]
 # Donor-only warps are reserved, never connected to donor gameplay destinations.
 for n,k in {**TARGETS,**GATE_ONLY}.items():
  native_count=len(load(OUT/'original'/f'data/maps/{n}/map.json')['warp_events']);extra=donors[n]['warps'][native_count:]
  for i,w in enumerate(extra):
   target,dp=C.donor(w['target_id']);name=target['name'];label=f'{n}_EventScript_HyperConstruction_{i+1}';e=new_scientist(n,i+1,w['x'],w['y'],label);g=grids[n];assert g.walk(e['x'],e['y']) and g.neighbors(e['x'],e['y']),(n,w,g.cell(e['x'],e['y']))
   assert not any((x['x'],x['y'])==(e['x'],e['y']) for x in maps[n]['object_events']),(n,e)
   maps[n]['object_events'].append(e)
   safe=('Tunnel extension' if w['target_id'] in ['24.4','0.31'] else 'Tunnel shortcut' if n=='RusturfTunnel' and w['target_id']=='0.0' else name)
   safe=safe if len(safe)<=25 else 'This extra area'
   scripts[n]+=f'\n@ Project-owned reservation; no donor gameplay, flags or warp destination.\n{label}::\n\tlock\n\tfaceplayer\n\tmsgbox {n}_Text_HyperConstruction_{i+1}, MSGBOX_DEFAULT\n\trelease\n\tend\n\n{n}_Text_HyperConstruction_{i+1}:\n\t.string "{safe} is\\n"\n\t.string "under construction.\\p"\n\t.string "Please check back later!$"\n'
   gates.append({'map':n,'donor_id':k,'scientist':e,'source_warp':w,'reserved_donor_name':name,'display_name':safe,'reserved_donor_id':w['target_id'],'destination_reference_json':dp,'source_cell':g.cell(w['x'],w['y']),'source_interaction_neighbors':g.neighbors(w['x'],w['y']),'status':'ENTRANCE_RESERVED_BLOCKED_NO_WARP','reason':'Scientist occupies the actual donor-only entrance; no donor logic or region registration.'})
 return b,cat,ls,maps,ledger,grids,scripts,edits,gates

def trace(grids,scripts,n,start,labels,allow_door=False,boat=False):
 x,y=start;records=[];blocks=C.movement_blocks(scripts.get(n,(ROOT/f'data/maps/{n}/scripts.inc').read_text()))
 for label in labels:
  label=n+'_Movement_'+label if not label.startswith(n) else label
  for cmd in blocks[label]:
   r=re.search(r'_(up|down|left|right)$',cmd)
   if not r or not cmd.startswith(('walk_','jump_')) or 'in_place' in cmd:continue
   dx,dy={'up':(0,-1),'down':(0,1),'left':(-1,0),'right':(1,0)}[r[1]];x+=dx;y+=dy
   if not (0<=x<grids[n].w and 0<=y<grids[n].h):
    assert boat,(n,label,(x,y));records.append({'xy':[x,y],'native_boat_offscreen':True});continue
   v=grids[n].cell(x,y);permitted=grids[n].walk(x,y) or allow_door and v['translated_behavior'] in [0x60,0x69] or boat and v['collision']==0
   if not permitted and n=='RusturfTunnel' and label in ['RusturfTunnel_Movement_BrineyExit','RusturfTunnel_Movement_PeekoExit','RusturfTunnel_Movement_WandasBoyfriendExit']:
    m=load(OUT/'original'/f'data/maps/{n}/map.json');l=next(q for q in load(OUT/'original/data/layouts/layouts.json')['layouts'] if q['id']==m['layout']);old=words(ROOT/l['blockdata_filepath'])[y*l['width']+x];permitted=((old>>10)&3)==v['collision'] and v['collision']!=0;v['native_forced_actor_exit_original_block']=old
   assert permitted,(n,label,cmd,v);records.append(v)
 return {'map':n,'start':list(start),'labels':labels,'end':[x,y],'cells':records}

def scenes(grids,scripts):
 out=[]
 def add(n,xy,labels,**kw):r=trace(grids,scripts,n,xy,labels,**kw);out.append(r);return r['end']
 for branch in ['Left','Right']:
  end=add('PetalburgWoods',(35,17),['DevonResearcherApproachPlayer'+branch]);end=add('PetalburgWoods',end,['DevonResearcherFleeToPlayer'+branch]);add('PetalburgWoods',end,['DevonResearcherExit'+branch])
  end=add('PetalburgWoods',(35,14),['AquaEntrance','AquaApproachResearcher'+branch]);end=add('PetalburgWoods',end,['AquaApproachPlayer','AquaBackOff']);add('PetalburgWoods',end,['AquaRunAway'])
 add('RustboroCity',(13,21),['GruntEscape']);add('RustboroCity',(14,21),['EmployeeChaseGrunt1','EmployeeChaseGrunt2'])
 for x in [12,13]:
  add('RustboroCity',(x,18),['PlayerWalkDown']);end=add('RustboroCity',(x,17),['ScientistApproachPlayer']);add('RustboroCity',end,['ScientistLeave'],allow_door=True)
 for i in range(8):add('RustboroCity',(16,52),['RivalApproachPlayer'+str(i)])
 for n in ['RustboroCity_DevonCorp_3F']:
  add(n,(3,2),['EmployeeWalkOffscreen','EmployeeReturnToPlayer']);add(n,(3,2),['LeadPlayerToPresident']);add(n,(2,2),['PlayerFollowToPresident','PlayerApproachDesk'])
 n='RusturfTunnel';add(n,(13,4),['GruntAndPeekoBackUp']);add(n,(13,5),['GruntAndPeekoBackUp']);add(n,(14,5),['GruntEscape']);add(n,(13,5),['PushPlayerAsideForGrunt']);end=add(n,(5,4),['BrineyApproachPeeko1','BrineyApproachPeeko2']);add(n,end,['BrineyExit']);add(n,(14,4),['PeekoExit'])
 add(n,(23,5),['BoyfriendApproachWanda1','WandasBoyfriendExit1']);add(n,(23,5),['BoyfriendFaceRight','WandasBoyfriendApproachPlayer','BoyfriendApproachWanda','WandasBoyfriendExit']);add(n,(25,4),['WandaExit'])
 add('Route104',(17,50),['RivalExitBrineysCottage','RivalApproachPlayer']);add('Route104',(13,51),['PlayerBoardBoat'],boat=True);add('Route104',(12,51),['BrineyBoardBoat'],boat=True)
 # Boat movement is intentionally allowed on water, following the native forced sailing contract.
 add('Route104',(12,53),['SailToDewfordBeforeDadCalls'],boat=True)
 return out

def seam_checks(grids,maps):
 oldls=load(OUT/'original/data/layouts/layouts.json')['layouts'];new=[]
 for n in TARGETS:
  m=maps[n];g=grids[n]
  for conn in m['connections'] or []:
   dest=next(f.parent.name for f in (ROOT/'data/maps').glob('*/map.json') if load(f)['id']==conn['map']);dm=load(ROOT/f'data/maps/{dest}/map.json');dl=next(l for l in oldls if l['id']==dm['layout']);nl=next(l for l in oldls if l['id']==load(OUT/'original'/f'data/maps/{n}/map.json')['layout']);ob=words(ROOT/nl['blockdata_filepath']);db=words(ROOT/dl['blockdata_filepath']);direction=conn['direction'];off=conn['offset'];cells=[]
   coords=[(x,0 if direction=='up' else g.h-1) for x in range(g.w)] if direction in ['up','down'] else [(0 if direction=='left' else g.w-1,y) for y in range(g.h)]
   for x,y in coords:
    dx,dy=(x-off,dl['height']-1 if direction=='up' else 0) if direction in ['up','down'] else (dl['width']-1 if direction=='left' else 0,y-off)
    if not (0<=dx<dl['width'] and 0<=dy<dl['height']):continue
    a=ob[y*g.w+x];b=db[dy*dl['width']+dx];z=g.cell(x,y)['block'];w=grids[dest].cell(dx,dy)['block'] if dest in grids else b
    was=(a>>10)&3==0 and (b>>10)&3==0;now=(z>>10)&3==0 and (w>>10)&3==0;assert was==now or frozenset([n,dest]) in [frozenset(['Route104','RustboroCity']),frozenset(['Route104','Route105']),frozenset(['RustboroCity','Route115']),frozenset(['RustboroCity','Route116'])],(n,dest,x,y)
    if now:assert z>>12==w>>12,(n,dest,x,y,z,w)
    cells.append({'from':[x,y],'to':[dx,dy],'original_crossable':was,'crossable':now,'review':'Reviewed donor border crossability differs; canonical connection metadata and matching crossing elevations retained' if was!=now else 'unchanged crossability'})
   new.append({'from':n,'to':dest,'connection':conn,'cells':cells})
 return new

def graphics(cat,maps,ledger):
 native=(ROOT/'src/data/object_events/object_event_graphics_info.h').read_text();ptr=(ROOT/'src/data/object_events/object_event_graphics_info_pointers.h').read_text();anim=(ROOT/'src/data/object_events/object_event_anims.h').read_text();objects={x['source_graphics_id']:x for x in cat['object_graphics']};defs=[];bindings=[];audit=[];retained=[]
 skip={'OBJ_EVENT_GFX_BERRY_TREE','OBJ_EVENT_GFX_ITEM_BALL','OBJ_EVENT_GFX_MR_BRINEYS_BOAT','OBJ_EVENT_GFX_WINGULL','OBJ_EVENT_GFX_VAR_0','OBJ_EVENT_GFX_GAMEBOY_KID'}
 canonical={'OBJ_EVENT_GFX_DEVON_EMPLOYEE':23,'OBJ_EVENT_GFX_GENTLEMAN':48,'OBJ_EVENT_GFX_MAN_2':23,'OBJ_EVENT_GFX_SCIENTIST_1':46,'OBJ_EVENT_GFX_RIVAL_BRENDAN_NORMAL':100,'OBJ_EVENT_GFX_RIVAL_MAY_NORMAL':105}
 for n in TARGETS:
  roles={}
  for e in [x for x in ledger if x['map']==n and x['kind']=='object_events']:
   gfx=e['after']['graphics_id'];probe=e['donor_reference'];i=canonical.get(gfx,probe.get('graphics_id') if probe else None)
   if n=='RustboroCity_Gym' and gfx=='OBJ_EVENT_GFX_MAN_2':i=probe['graphics_id'] # Hyper gym guide art, not Devon staff uniform.
   if gfx in skip or gfx.startswith('OBJ_EVENT_GFX_VAR_') or gfx=='OBJ_EVENT_GFX_SS_TIDAL' or i not in objects:retained.append({'map':n,'graphics_id':gfx,'reason':'Native dynamic, species, boat, growth, reward or specialty rendering contract retained.'});continue
   roles.setdefault(gfx,i)
  if any(x['script'].startswith(n+'_EventScript_HyperConstruction') for x in maps[n]['object_events']):roles['OBJ_EVENT_GFX_SCIENTIST_1']=46
  if n in ['RustboroCity','Route104']:roles.update({x:canonical[x] for x in ['OBJ_EVENT_GFX_RIVAL_BRENDAN_NORMAL','OBJ_EVENT_GFX_RIVAL_MAY_NORMAL']})
  for gfx,i in roles.items():
   symbol=re.search(r'\['+gfx+r'\]\s*=\s*&(\w+)',ptr)[1];body=re.search(r'const struct ObjectEventGraphicsInfo '+symbol+r' = \{(.*?)\};',native,re.S)[1];obj=objects[i];dimensions=[int(re.search(r'\.'+f+r'\s*=\s*(\d+)',body)[1]) for f in ['width','height']]
   table=re.search(r'\.anims\s*=\s*(\w+)',body)[1];anims=re.search(re.escape(table)+r'\[\]\s*=\s*\{(.*?)\};',anim,re.S)[1];frames=[]
   for label in set(re.findall(r'=\s*(sAnim_\w+)',anims)):
    commands=re.search(re.escape(label)+r'\[\]\s*=\s*\{(.*?)\};',anim,re.S)[1];frames+=list(map(int,re.findall(r'ANIMCMD_FRAME\(\s*(\d+)',commands)))
   if dimensions!=[obj['width'],obj['height']] or max(frames,default=0)>=obj['frame_count']:
    retained.append({'map':n,'graphics_id':gfx,'source_graphics_id':i,'reason':'Donor art cannot satisfy native dimensions/animation; retain native graphic.'});continue
   adapter=f'gHyperCanary3Graphics_{n}_{gfx.removeprefix("OBJ_EVENT_GFX_")}';new=re.sub(r'(\.paletteTag\s*=\s*)[^,]+',lambda m:m[1]+f'0x{obj["palette_tag"]:04X}',body);new=re.sub(r'(\.images\s*=\s*)\w+',lambda m:m[1]+f'sPicTable_HyperAsset{i:03}',new);defs.append('static const struct ObjectEventGraphicsInfo '+adapter+' = {'+new+'};');bindings.append(f'    {{{maps[n]["id"]}, {gfx}, &{adapter}}},');audit.append({'map':n,'graphics_id':gfx,'source_graphics_id':i,'native_contract':body,'replacement':new,'source_frame_count':obj['frame_count'],'native_animation_frames':frames})
 return '/* Canary #3 art-only adapters. Native animation/runtime fields retained. */\n'+'\n\n'.join(defs)+'\n','\n'.join(bindings)+'\n',audit,retained

def extra_inventory():
 planner=load(ROOT/'.la_work/amap/hyper_hoenn_replacement/hyper_hoenn_replacement_manifest.json');matched={x['hyper']['id']:x['canonical']['name'] for x in planner['maps'] if x.get('hyper')};donors={}
 for f in (ROOT/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export/maps').glob('*/map.json'):
  d=load(f);k=f.parent.name.split('_')[0];a,b=k.split('.');donors[f'{int(a)}.{int(b)}']=(d,f)
 rows=[]
 for k,canonical in matched.items():
  d,f=donors[k];native=load(ROOT/f'data/maps/{canonical}/map.json');canonical_warps=len(native.get('warp_events',[]))
  for i,w in enumerate(d['warps']):
   if w['index']<canonical_warps and w['target_id'] in matched:continue
   if w['target_id'] not in donors:continue
   target,tf=donors[w['target_id']];rows.append({'canonical_source':canonical,'source_donor_id':k,'entrance_kind':'WARP','source_warp_index':w['index'],'entrance_x':w['x'],'entrance_y':w['y'],'destination_donor_id':w['target_id'],'destination_name':target['name'],'destination_json':str(tf.relative_to(ROOT)),'donor_warp':w,'status':'ENTRANCE_REVIEW_PENDING','classification':'EXTRA_ENTRANCE_TO_CANONICAL_MAP' if w['target_id'] in matched else 'HYPER_ONLY_DESTINATION_REFERENCE','ownership_policy':'Do not import donor gameplay; inspect/stage construction gate as canonical area is reached.'})
  for connection in d.get('connections',[]):
   k2=connection['target_id']
   if k2 in matched or k2 not in donors:continue
   target,tf=donors[k2];rows.append({'canonical_source':canonical,'source_donor_id':k,'entrance_kind':'CONNECTION','entrance_x':None,'entrance_y':None,'destination_donor_id':k2,'destination_name':target['name'],'destination_json':str(tf.relative_to(ROOT)),'donor_connection':connection,'status':'CONNECTION_BOUNDARY_REVIEW_PENDING','classification':'HYPER_ONLY_DESTINATION_REFERENCE','ownership_policy':'Inspect the full boundary; do not copy donor connection into canonical gameplay.'})
 # Broader extra package is reference only: these include other regions, so no claim that all are Hoenn.
 unmapped=[{'donor_id':k,'name':d['name'],'json':str(f.relative_to(ROOT)),'status':'UNASSIGNED_REFERENCE_ONLY_REGION_REVIEW_REQUIRED'} for k,(d,f) in donors.items() if k not in matched]
 return rows,unmapped

def apply():
 b,cat,ls,maps,ledger,grids,scripts,edits,gates=prepare();paths=scenes(grids,scripts);seams=seam_checks(grids,maps);gfx,bindings,gaudit,retained=graphics(cat,maps,ledger)
 patchfile=ROOT/PATCH_PATH;patchfile.parent.mkdir(parents=True,exist_ok=True);patchfile.write_bytes(struct.pack('<'+'H'*len(grids['RustboroCity'].blocks),*grids['RustboroCity'].blocks))
 heal=load(ROOT/'src/data/heal_locations.json');entries=heal if isinstance(heal,list) else heal['heal_locations'];h=next(x for x in entries if x['id']=='HEAL_LOCATION_RUSTBORO_CITY');assert (h['x'],h['y'])==(16,39);h['y']=47;dump(ROOT/'src/data/heal_locations.json',heal)
 hf=ROOT/'src/data/heal_locations.h';hs=hf.read_text();pat=r'(\[HEAL_LOCATION_RUSTBORO_CITY - 1\] = \{.*?\.y = )39(,.*?\},)';hs,count=re.subn(pat,lambda m:m[1]+'47'+m[2],hs,count=1,flags=re.S);assert count==1;hf.write_text(hs)
 tf=ROOT/TUNNEL_PATCH_PATH;tf.parent.mkdir(parents=True,exist_ok=True);tf.write_bytes(struct.pack('<'+'H'*len(grids['RusturfTunnel'].blocks),*grids['RusturfTunnel'].blocks))
 for n,m in maps.items():dump(ROOT/f'data/maps/{n}/map.json',m)
 dump(ROOT/'data/layouts/layouts.json',ls)
 for n,t in scripts.items():(ROOT/f'data/maps/{n}/scripts.inc').write_text(t)
 af='src/data/object_events/hyper_canary3_graphics.inc';(ROOT/af).write_text(gfx)
 p=ROOT/'src/hyper_asset_graphics_bindings.inc';p.write_text(p.read_text()+'\n/* Rustboro progression batch, native gameplay ownership. */\n'+bindings)
 p=ROOT/'src/data/object_events/hyper_assets.inc';p.write_text(p.read_text().replace('struct HyperAssetGraphicsBinding\n','#include "hyper_canary3_graphics.inc"\n\nstruct HyperAssetGraphicsBinding\n'))
 result={'schema':'hyper-hoenn-canary3-ledger-v1','events':ledger,'construction_gates':gates,'geometry_script_edits':edits,'native_scene_paths':paths,'connection_checks':seams,'graphics_adapters':gaudit,'native_graphics_retained':retained,'geometry_compatibility_patches':[PATCH,*TUNNEL_PATCHES],'hyper_gameplay_imported':False};dump(OUT/'coordinate_remap_ledger.json',result)
 with (OUT/'coordinate_remap_ledger.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['map','kind','index','role','old_x','old_y','new_x','new_y','reason'])
  for e in ledger:w.writerow([e['map'],e['kind'],e['index'],e['after'].get('script',e['after'].get('dest_map',e['after'].get('item'))),e['before']['x'],e['before']['y'],e['after']['x'],e['after']['y'],e['reason']])
 receipt={'schema':'hyper-hoenn-canary3-receipt-v1','canonical_maps_replaced':list(TARGETS),'donor_ids':TARGETS,'construction_only_maps':list(GATE_ONLY),'runtime_verified':False,'hyper_gameplay_imported':False,'changed_baseline_files':{f:{'before':b[f],'after':digest(ROOT/f)} for f in CHANGED},'new_files':{af:digest(ROOT/af),PATCH_PATH:digest(ROOT/PATCH_PATH),TUNNEL_PATCH_PATH:digest(ROOT/TUNNEL_PATCH_PATH)},'map_ids_header_sha256':digest(ROOT/'include/constants/map_groups.h'),'map_groups_json_sha256':digest(ROOT/'data/maps/map_groups.json'),'layout_count_before_after':[len(load(OUT/'original/data/layouts/layouts.json')['layouts']),len(ls['layouts'])]};dump(OUT/'receipt.json',receipt)
 reports(cat,ls,maps,gates)

def reports(cat,ls,maps,gates):
 groups=load(ROOT/'data/maps/map_groups.json');positions={n:(gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])}
 extra,unmapped=extra_inventory()
 for x in extra:
  match=next((g for g in gates if g['map']==x['canonical_source'] and (g['source_warp']['x'],g['source_warp']['y'])==(x['entrance_x'],x['entrance_y'])),None)
  if match:x['status']=match['status']
 dump(OUT/'hyper_extra_location_inventory.json',{'schema':1,'extra_entrances_from_canonical_hoenn':extra,'unassigned_donor_reference':unmapped,'note':'All exported warps/connections from matched canonical Hoenn counterparts are screened for unassigned destinations, including equal-count substitutions. Additional warps to canonical maps are also queued. Script-generated entrances and unassigned-region attribution still need manual archaeology; extraction is reference-only.'})
 with (OUT/'hyper_extra_location_inventory.csv').open('w',newline='') as f:
  fields=['canonical_source','source_donor_id','entrance_kind','entrance_x','entrance_y','destination_donor_id','destination_name','status','classification'];w=csv.DictWriter(f,fields,extrasaction='ignore');w.writeheader();w.writerows(extra)
 manifest=[]
 for n,k in TARGETS.items():
  m=maps[n];d=C.donor(k)[0];source=next(x for x in cat['layouts'] if x['donor_id']==k);l=next(x for x in ls['layouts'] if x['id']==m['layout']);manifest.append({'canonical_name':n,'canonical_id':m['id'],'canonical_group':positions[n][0],'canonical_map':positions[n][1],'donor_id':k,'donor_name':d['name'],'donor_identity':'HYPER_EMERALD_V5_7_EN_QOL','donor_group':d['group'],'donor_map':d['map'],'source_tileset_pair':[d['primary_tileset'],d['secondary_tileset']],'donor_script_table_reference_only':d['map_scripts'],'donor_event_counts':d['event_counts'],'donor_connections_reference_only':d['connections'],'dimensions':source['dimensions'],'map_type':m['map_type'],'tilesets':[l['primary_tileset'],l['secondary_tileset']],'layout':l,'blockdata_sha256':digest(ROOT/l['blockdata_filepath']),'border_sha256':digest(ROOT/l['border_filepath']),'donor_header_reference':{key:val for key,val in d.items() if 'pointer' in key or key in ['header','layout']},'event_counts':{key:len(m[key]) for key in ['object_events','warp_events','coord_events','bg_events']},'warps':m['warp_events'],'connections':m['connections'],'connection_count':len(m['connections'] or []),'reserved_extra_entrances':[g for g in gates if g['map']==n],'confidence':'HIGH','script_owner':n+'_MapScripts','replacement_mode':'LAYOUT_REPLACEMENT_WITH_NATIVE_EVENT_RECONCILIATION','runtime_verified':False})
 dump(OUT/'rustboro_spine_manifest.json',{'schema':1,'maps':manifest,'construction_only_maps':list(GATE_ONLY),'hyper_gameplay_imported':False,'runtime_verified':False})
 print('Applied 16 canonical asset replacements and',len(gates),'project-owned construction scientists; no donor destination registrations.')

def validate():
 b=load(OUT/'baseline.json');r=load(OUT/'receipt.json');assert set(r['changed_baseline_files'])==set(CHANGED)
 for f,h in b.items():assert digest(ROOT/f)==C.C.fourth_canary_hash(f,r['changed_baseline_files'].get(f,{}).get('after',h)),f
 for f,h in r['new_files'].items():assert digest(ROOT/f)==h,f
 for f,h in [('include/constants/map_groups.h',r['map_ids_header_sha256']),('data/maps/map_groups.json',r['map_groups_json_sha256'])]:assert digest(ROOT/f)==h
 ledger=load(OUT/'coordinate_remap_ledger.json');gates=ledger['construction_gates']
 for n in {**TARGETS,**GATE_ONLY}:
  a=load(OUT/'original'/f'data/maps/{n}/map.json');z=load(ROOT/f'data/maps/{n}/map.json')
  for key in a:
   if key=='layout':continue
   if key.endswith('_events'):
    native=z[key][:len(a[key])];assert len(native)==len(a[key]);assert [{k:v for k,v in x.items() if k not in ['x','y']} for x in a[key]]==[{k:v for k,v in x.items() if k not in ['x','y']} for x in native]
    assert z[key][len(a[key]):]==([g['scientist'] for g in gates if g['map']==n] if key=='object_events' else [])
   else:assert a[key]==z[key],(n,key)
  if n in GATE_ONLY:
   assert all(a[key]==z[key] for key in ['layout','warp_events','coord_events','bg_events','connections']);assert a['object_events']==z['object_events'][:len(a['object_events'])]
 for n in SCRIPT_MAPS:
  before=(OUT/'original'/f'data/maps/{n}/scripts.inc').read_text();after=(ROOT/f'data/maps/{n}/scripts.inc').read_text();after=after.split('\n@ Project-owned reservation;')[0]
  for edit in reversed([x for x in ledger['geometry_script_edits'] if x['map']==n]):
   if 'label' in edit:
    match=re.search(r'^'+edit['label']+r':\n(.*?)(?=^\w+:|\Z)',after,re.M|re.S);assert match[1]==edit['after'];after=after[:match.start(1)]+edit['before']+after[match.end(1):]
   else:assert after.count(edit['after'])==edit['occurrences'];after=after.replace(edit['after'],edit['before'])
  assert before==after,(n,'native script ownership/command mismatch')
 oldls=load(OUT/'original/data/layouts/layouts.json')['layouts'];newls=load(ROOT/'data/layouts/layouts.json')['layouts'];targetids={load(OUT/'original'/f'data/maps/{n}/map.json')['layout'] for n in TARGETS if load(ROOT/f'data/maps/{n}/map.json')['layout']==load(OUT/'original'/f'data/maps/{n}/map.json')['layout']}
 for a,z in zip(oldls,newls):
  assert a['id']==z['id']
  if a['id'] not in targetids and a['id'] not in C.C.fourth_layout_ids():assert a==z
  else:assert {k:v for k,v in a.items() if k not in ['primary_tileset','secondary_tileset','blockdata_filepath','border_filepath']}=={k:v for k,v in z.items() if k not in ['primary_tileset','secondary_tileset','blockdata_filepath','border_filepath']}
 result={'passed':True,'protected_files_checked':len(b),'canonical_maps_replaced':len(TARGETS),'construction_scientists':len(gates),'canonical_map_ids_unchanged':True,'native_story_flags_vars_save_warp_connections_ownership_preserved':True,'hyper_gameplay_imported':False,'runtime_verified':False};dump(OUT/'validation.json',result);print(json.dumps(result,indent=2));return result
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--apply',action='store_true');a.add_argument('--validate',action='store_true');v=a.parse_args()
 if v.apply:apply()
 elif v.validate:validate()
 else:
  b,cat,ls,maps,ledger,grids,scripts,edits,gates=prepare();scenes(grids,scripts);seam_checks(grids,maps);graphics(cat,maps,ledger);print('Preflight passed; no map writes.')
