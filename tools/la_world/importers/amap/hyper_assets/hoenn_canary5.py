#!/usr/bin/env python3
"""Northwest Hoenn canonical replacement and real, construction-gated Hyper extras."""
import copy,collections,csv,json,re,struct,sys,argparse,functools
from pathlib import Path
import hoenn_corridor_correction as P
C=P.C;ROOT=P.ROOT;load=P.load;dump=P.dump;digest=P.digest;words=P.words;OUT=ROOT/'.la_work/amap/hyper_hoenn_canary5'
SCOPE=load(OUT/'scope.json' if (OUT/'scope.json').exists() else Path(__file__).with_name('hoenn_canary5_scope.json'));ALL_TARGETS=SCOPE['canonical_targets'];KEEP={n:'Native Trainer Hill runtime owns generated floor layouts.' for n in ALL_TARGETS if n.startswith('TrainerHill_') and n not in ['TrainerHill_Entrance','TrainerHill_Elevator']};TARGETS={n:k for n,k in ALL_TARGETS.items() if n not in KEEP}
REMAP={'Route114':{15:(20,27)},'LavaridgeTown':{3:(14,10)},'Route111':{36:(25,120)},'Route112':{4:(15,39),10:(10,49),11:(18,45)},'Route115':{14:(29,51),19:(11,7),22:(11,14)},'VerdanturfTown_House':{0:(5,5),1:(5,4)}}
KINDS=P.KINDS
PREFIXES=['data','src','include','graphics']
def snapshot():
 OUT.mkdir(parents=True,exist_ok=True)
 if (OUT/'baseline.json').exists():return load(OUT/'baseline.json')
 b={str(f.relative_to(ROOT)):digest(f) for d in PREFIXES for f in (ROOT/d).rglob('*') if f.is_file() and not C.P.C.C.derived(str(f.relative_to(ROOT)))}
 # Snapshot only edited text/metadata and relevant original geometry for reproducible reconciliation.
 for f in b:
  if f.endswith(('.json','.c','.h','.inc','.txt')) and (f in ['data/layouts/layouts.json','data/maps/map_groups.json','include/constants/map_groups.h','include/constants/layouts.h','include/constants/region_map_sections.h','src/data/region_map/region_map_entries.h','src/data/region_map/region_map_sections.json','src/data/region_map/region_map_sections.constants.json.txt','src/data/heal_locations.json','src/data/heal_locations.h','src/data/tilesets/headers.h','src/data/tilesets/metatiles.h','src/data/object_events/hyper_assets.inc','src/hyper_asset_graphics_bindings.inc','src/region_map.c','src/map_name_popup.c','src/pokedex_area_screen.c','src/pokemon_summary_screen.c'] or f.startswith('data/maps/') and Path(f).name in ['map.json','scripts.inc']):
   p=OUT/'original'/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/f).read_bytes())
 dump(OUT/'baseline.json',b);return b

@functools.lru_cache(maxsize=None)
def source(k):return C.P.C.donor(k)[0]
def name(k):return 'HyperHoenn_'+k.replace('.','_')+'_'+re.sub(r'[^A-Za-z0-9]+','_',source(k)['name']).strip('_')
def special_type(d):
 types=['MAP_TYPE_NONE','MAP_TYPE_TOWN','MAP_TYPE_CITY','MAP_TYPE_ROUTE','MAP_TYPE_UNDERGROUND','MAP_TYPE_UNDERWATER','MAP_TYPE_OCEAN_ROUTE','MAP_TYPE_UNKNOWN','MAP_TYPE_INDOOR','MAP_TYPE_SECRET_BASE']
 if d['name']=='Route 106':return 'MAP_TYPE_OCEAN_ROUTE'
 return 'MAP_TYPE_INDOOR' if d['map_type']==0 and d['primary_tileset']=='primary_083DF884' else types[d['map_type']]
def const(n):return re.sub(r'(?<!^)(?=[A-Z])','_',n).upper().replace('__','_')
def from_layout(l):return P.grid_for(l)
def prepare():
 baseline=snapshot();cat=load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');by={z['donor_id']:z for z in cat['layouts']};ls=load(ROOT/'data/layouts/layouts.json');oldls=copy.deepcopy(ls);planner=load(ROOT/'.la_work/amap/hyper_hoenn_replacement/hyper_hoenn_replacement_manifest.json');canonical={z['hyper']['id']:z['canonical']['name'] for z in planner['maps']};maps={n:load(ROOT/f'data/maps/{n}/map.json') for n in TARGETS};oldmaps=copy.deepcopy(maps);grids={n:C.Grid(by[k]) for n,k in TARGETS.items()};ledger=[];patches=[];scripts={n:(ROOT/f'data/maps/{n}/scripts.inc').read_text() for n in TARGETS};files={};extras={k:name(k) for k in SCOPE['extras']};groups=load(ROOT/'data/maps/map_groups.json');oldgroups=copy.deepcopy(groups);sections=load(ROOT/'src/data/region_map/region_map_sections.json');old_section_ids=[z['id'] for z in sections['map_sections']];sections['map_sections'].append({'id':'MAPSEC_NONE','name':'NONE'});newsecs={};attr_sources={};variantids=[]
 def patch(n,x,y,after,reason):
  g=grids[n];before=g.blocks[y*g.w+x]
  if before!=after:g.blocks[y*g.w+x]=after;patches.append({'map':n,'x':x,'y':y,'before':before,'after':after,'reason':reason})
 def register(l,n,k,g):
  l.update(primary_tileset=by[k]['primary_tileset'],secondary_tileset=by[k]['secondary_tileset'],border_filepath=by[k]['border_path'],blockdata_filepath=f'data/hyper_assets/canary5_layouts/{n}/map.bin')
 for n,k in TARGETS.items():
  g=grids[n];m=maps[n];l=next(z for z in ls['layouts'] if z['id']==m['layout']);native=words(ROOT/l['blockdata_filepath']);assert (l['width'],l['height'])==(g.w,g.h),(n,'dimension mismatch');users=[f.parent.name for f in (ROOT/'data/maps').glob('*/map.json') if load(f)['layout']==l['id']]
  if len(users)>1:l=copy.deepcopy(l);l['id']='LAYOUT_HYPER_CANARY5_'+const(n);l['name']='HyperCanary5'+n+'_Layout';m['layout']=l['id'];ls['layouts'].append(l)
  # Match native land/ocean elevation at passable cells. Berry soil intentionally remains blocked.
  for y in range(g.h):
   for x in range(g.w):
    v=g.cell(x,y);el=native[y*g.w+x]>>12
    if v['collision']==0 and v['translated_behavior'] not in {0x10,0x11,0x12,0x13,0x14,0x15,0x19,0x22,0x2A} and el in [3,4,15] and v['elevation']!=el:patch(n,x,y,(v['block']&4095)|(el<<12),'Expansion elevation compatibility; Hyper art/metatile/collision retained.')
  # Keep the native Mt Chimney battle line and two-fossil chamber, rather than copying donor story placement.
  if n=='MtChimney':
   for x in [29,30,31,32]:patch(n,x,5,(g.cell(x,6)['block']&4095)|0x3000,'Native opposing actors remain on row5; inspected donor walkable row6 artwork extends their stage.')
  if n=='MirageTower_4F':
   floor=g.cell(6,7)['metatile']
   for y in range(3,6):
    for x in range(4,9):patch(n,x,y,floor|((native[y*g.w+x]>>12)<<12),'Two expansion fossils retain native coordinates and collapse scene; inspected Hyper floor artwork forms their platform.')
  if n in ['LavaridgeTown_Gym_1F','LavaridgeTown_Gym_B1F']:
   want=0x68 if n.endswith('_1F') else 0x29;tile=next(i+512*bi for bi,attrs in enumerate(g.attrs) for i,a in enumerate(attrs) if a&255==want)
   for e in m['warp_events']:
    v=g.cell(e['x'],e['y'])
    if 'GYM_' in e['dest_map'] and v['translated_behavior'] not in [0x29,*range(0x60,0x70)]:patch(n,e['x'],e['y'],tile|0x3000,'Native gym slot and destination retained; decorative donor cell replaced with inspected working Hyper steam-hole tile.')
  d=source(k)
  for kind,dkey in KINDS.items():
   probes={z['index']:z for z in d[dkey]}
   for i,e in enumerate(m[kind]):
    before=copy.deepcopy(e);probe=probes.get(i);reason='Native coordinate retained on inspected Hyper geometry.'
    if kind=='object_events' and i in REMAP.get(n,{}):e['x'],e['y']=REMAP[n][i];reason='Explicit native role/source geometry correspondence; coordinates only, no donor gameplay fields.'
    if n=='Route114' and kind=='bg_events' and i==1:e['x'],e['y']=30,6;reason='Inspected donor house sign location; native sign script retained.'
    if kind=='warp_events' and probe:
     counterpart=canonical.get(probe['target_id']);dest=load(ROOT/f'data/maps/{counterpart}/map.json')['id'] if counterpart else None
     if dest==e['dest_map'] and 'TERRA_CAVE' not in dest:e['x'],e['y']=probe['x'],probe['y'];reason='Destination-matched source doorway; native warp index/destination semantics preserved.'
    x,y=e['x'],e['y'];v=None
    if not(0<=x<g.w and 0<=y<g.h):assert e.get('script')=='0x0' and before==e,(n,kind,i,e);reason='Pre-existing dormant out-of-bounds null-script BG record; retained.'
    else:
     v=g.cell(x,y)
     if kind=='object_events' and v['collision'] and v['translated_behavior'] not in [0x60,0x69,0xA0]:
      old=native[before['y']*g.w+before['x']];assert before==e and ((old>>10)&3)==v['collision'] and (e['graphics_id'] in ['OBJ_EVENT_GFX_CABLE_CAR','OBJ_EVENT_GFX_GROUDON_FRONT','OBJ_EVENT_GFX_GROUDON_ASLEEP','OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE','OBJ_EVENT_GFX_BLACK_BELT']),(n,kind,i,v,e)
     if kind=='coord_events' and e.get('type')!='weather':assert v['collision']==0,(n,kind,i,v)
     if kind=='object_events' and e['graphics_id']=='OBJ_EVENT_GFX_BERRY_TREE':
      if v['translated_behavior']!=0xA0:
       near=[g.cell(a,b) for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if 0<=a<g.w and 0<=b<g.h and g.cell(a,b)['translated_behavior']==0xA0];assert near,(n,i,v);patch(n,x,y,near[0]['block'],'Native additional berry plot preserved by extending adjacent inspected Hyper berry-soil cell; native tree IDs/growth state retained.');v=g.cell(x,y)
      assert v['translated_behavior']==0xA0,(n,i,v)
    ledger.append({'map':n,'kind':kind,'index':i,'before':before,'after':copy.deepcopy(e),'donor_reference':probe,'cell':v,'reason':reason,'owner':'expansion/project'})
  register(l,n,k,g)
 # Preserve named expansion story walks against actual Hyper cells, repairing only original walkable cells.
 scene_paths=[]
 def trace(n,start,labels):
  g=grids[n];ol=next(z for z in oldls['layouts'] if z['id']==oldmaps[n]['layout']);nb=words(ROOT/ol['blockdata_filepath']);x,y=start;records=[];blocks=C.P.C.movement_blocks(scripts[n])
  for label in labels:
   for cmd in blocks[n+'_Movement_'+label]:
    match=re.search(r'_(up|down|left|right)$',cmd)
    if not match or not cmd.startswith(('walk_','jump_')) or 'in_place' in cmd:continue
    dx,dy={'up':(0,-1),'down':(0,1),'left':(-1,0),'right':(1,0)}[match[1]];x+=dx;y+=dy
    if not(0<=x<g.w and 0<=y<g.h):records.append({'x':x,'y':y,'native_offscreen':True});continue
    v=g.cell(x,y)
    if v['collision'] and v['translated_behavior'] not in [0x60,0x69]:
     old=nb[y*g.w+x]
     if ((old>>10)&3)==0:
      choices=[(abs(a-x)+abs(b-y),a,b) for b in range(max(0,y-3),min(g.h,y+4)) for a in range(max(0,x-3),min(g.w,x+4)) if g.walk(a,b) and g.cell(a,b)['translated_behavior'] in [0,2,6,0x21]];assert choices,(n,label,x,y,'no floor reference');_,a,b=min(choices);patch(n,x,y,(g.cell(a,b)['block']&4095)|((old>>12)<<12),'Named expansion story movement corridor reconciled using inspected nearby Hyper floor; native script/state unchanged.');v=g.cell(x,y)
     else:assert ((old>>10)&3)==v['collision'],(n,label,x,y,v)
    records.append(v)
  scene_paths.append({'map':n,'start':start,'labels':labels,'end':[x,y],'cells':records});return (x,y)
 for start,labels in [((12,9),['RivalApproachPlayer1']),((10,8),['RivalExit1']),((12,15),['RivalExitHerbShop','RivalApproachPlayer2']),((10,16),['RivalExit2'])]:trace('LavaridgeTown',start,labels)
 # A native scripted alternate layout must use the same Hyper world when Mirage Tower disappears.
 g=copy.deepcopy(grids['Route111']);grids['Route111_NoMirageTower']=g;l=next(z for z in ls['layouts'] if z['id']=='LAYOUT_ROUTE111_NO_MIRAGE_TOWER');native=words(ROOT/next(z for z in oldls['layouts'] if z['id']==l['id'])['blockdata_filepath']);variantids.append(l['id'])
 for y in range(56,59):
  for x in range(18,21):patch('Route111_NoMirageTower',x,y,native[y*g.w+x],'Native absent-tower footprint on Hyper route; same native flags/layout selector.')
 register(l,'Route111_NoMirageTower','0.26',g)
 # Native script operands only: PC exit column moved; Regi doorway and glass workshop coordinates changed.
 scripts['LavaridgeTown']=scripts['LavaridgeTown'].replace('LOCALID_LAVARIDGE_RIVAL, 11, 9','LOCALID_LAVARIDGE_RIVAL, 12, 9').replace('LOCALID_LAVARIDGE_RIVAL_ON_BIKE, 9, 8','LOCALID_LAVARIDGE_RIVAL_ON_BIKE, 10, 8').replace('VAR_0x8004, 9,','VAR_0x8004, 10,').replace('VAR_0x8008, 9,','VAR_0x8008, 10,')
 scripts['Route111']=scripts['Route111'].replace('setmetatile 29, 86, METATILE_General_RockWall_RockBase','setmetatile 29, 87, 0x09F').replace('setmetatile 29, 87, METATILE_General_RockWall_SandBase','setmetatile 29, 88, 0x09F')
 # All extra geometry is registered, including earlier entrance-only reservations.
 native_alias={'Route 106':'MAPSEC_ROUTE_106','Granite Cave':'MAPSEC_GRANITE_CAVE','Desert Ruins':'MAPSEC_DESERT_RUINS','Desert Underpass':'MAPSEC_DESERT_UNDERPASS','Basement':'MAPSEC_RUSTBORO_CITY'}
 roottemplate=load(ROOT/'data/maps/PetalburgWoods/map.json')
 for k,n in extras.items():
  d=source(k);nm=d['name'];sec=native_alias.get(nm)
  if not sec:
   sec='MAPSEC_HYPER_'+re.sub(r'[^A-Za-z0-9]+','_',nm).strip('_').upper()
   if sec not in newsecs:newsecs[sec]=nm;sections['map_sections'].append({'id':sec,'name':nm,'x':0,'y':0,'width':1,'height':1})
  m=copy.deepcopy(roottemplate);m.update(id='MAP_'+n.upper(),name=n,layout='LAYOUT_'+n.upper(),region_map_section=sec,music='MUS_ROUTE104',weather='WEATHER_NONE',map_type=special_type(d),requires_flash=False,show_map_name=True,allow_cycling=True,allow_escaping=False,allow_running=True,connections=None,object_events=[],warp_events=[],coord_events=[],bg_events=[])
  primary='gTileset_Hyper_'+d['primary_tileset'].replace('primary_','Primary_');secondary='gTileset_Hyper_'+d['secondary_tileset'].replace('secondary_','Secondary_');folder=ROOT/Path(SCOPE['extras'][k]['json']).parent
  l={'id':m['layout'],'name':n+'_Layout','width':d['width'],'height':d['height'],'primary_tileset':primary,'secondary_tileset':secondary,'border_filepath':f'data/hyper_assets/special_layouts/{k}/border.bin','blockdata_filepath':f'data/hyper_assets/canary5_layouts/{n}/map.bin','layout_version':'emerald'};ls['layouts'].append(l);files[l['border_filepath']]=(folder/'border.bin').read_bytes();grids[n]=C.Grid({'dimensions':[d['width'],d['height']],'primary_tileset':primary,'secondary_tileset':secondary,'blockdata_path':str((folder/'blockdata.bin').relative_to(ROOT))});maps[n]=m;scripts[n]=n+'_MapScripts::\n\t.byte 0\n'
  if k=='34.68':
   g=grids[n]
   for y in range(g.h):
    for x in range(g.w):
     v=g.cell(x,y)
     if v['collision']==0 and v['elevation'] in [0,1]:
      el=1 if v['translated_behavior'] in range(0x10,0x16) else 3
      patch(n,x,y,(v['block']&4095)|(el<<12),'Connected western Dewford coast matches inspected native land elevation 3 / water elevation 1; Hyper art/behavior retained.')
  group='gMapGroup_IndoorRustboro' if nm=='Basement' else 'gMapGroup_Dungeons' if nm in ['Granite Cave','Desert Ruins','Desert Underpass'] else 'gMapGroup_TownsAndRoutes' if nm=='Route 106' else 'gMapGroup_HyperHoenn_'+re.sub(r'[^A-Za-z0-9]+','_',nm).strip('_')
  if group not in groups:groups['group_order'].append(group);groups[group]=[]
  groups[group].append(n)
 # Resolve donor geometry edges to project/native destinations. Native slots never move.
 active={n:k for n,k in TARGETS.items()}
 for n in P.load(P.OUT/'sea_corridor_correction_manifest.json')['maps']:active[n['canonical_name']]=n['donor_id']
 for number in [1,2,3,4]:active.update(load(ROOT/f'.la_work/amap/hyper_hoenn_canary{number}/receipt.json')['donor_ids'])
 active.update({n:k for k,n in extras.items()});reverse={k:n for n,k in active.items()};warp_index={};pending=[];connections=[];gates=[];gatecounts=collections.Counter()
 def ensure(n):
  if n in maps:return
  maps[n]=load(ROOT/f'data/maps/{n}/map.json');scripts[n]=(ROOT/f'data/maps/{n}/scripts.inc').read_text();l=next(z for z in ls['layouts'] if z['id']==maps[n]['layout']);grids[n]=from_layout(l)
 def gate(n,x,y,reason,dest=None):
  ensure(n);g=grids[n]
  # Existing project blocker is retained; do not accumulate another scientist on it.
  existing=next((e for e in maps[n]['object_events'] if e['script'].startswith(n+'_EventScript_HyperConstruction') and abs(e['x']-x)+abs(e['y']-y)<=2),None)
  assert 0<=x<g.w and 0<=y<g.h,(n,x,y)
  v=g.cell(x,y)
  if v['translated_behavior'] in range(0x10,0x16) and reason.startswith('Exit outside'):
   valid=[(abs(a-x)+abs(b-y),a,b) for b in range(g.h) for a in range(g.w) if g.walk(a,b) and g.neighbors(a,b) and not any((e['x'],e['y'])==(a,b) for e in maps[n]['object_events'])];assert valid,(n,'No shore notice cell');_,x,y=min(valid);v=g.cell(x,y)
  if v['translated_behavior'] not in range(0x60,0x70) and not reason.startswith(('Registered western','Project notice','Exit outside')):
   assert v['translated_behavior'] not in range(0x10,0x16),(n,x,y,'water gate requires shore marker')
   # Exported static warp proves this is a map mouth. Open it with a known Hyper door tile.
   choices=[(abs((a&255)-0x60),bank*512+i) for bank,attrs in enumerate(g.attrs) for i,a in enumerate(attrs) if (a&255) in [0x60,0x61,0x69,0x6A]];assert choices,(n,x,y,'No native warp art available');idx=min(choices)[1];patch(n,x,y,idx|0x3000,'Registered donor map mouth repaired with inspected Hyper doorway behavior; no donor script copied.')
  if existing:
   if abs(existing['x']-x)+abs(existing['y']-y)==2:
    a,b=(existing['x']+x)//2,(existing['y']+y)//2
    if g.cell(a,b)['collision']:patch(n,a,b,(g.cell(existing['x'],existing['y'])['block']&0xF3FF),'Open the one inspected cell between existing construction approach marker and the registered donor mouth; Hyper approach-floor art retained.')
   gates.append({'map':n,'scientist':existing,'destination':dest,'reason':reason,'existing':True});return
  gatecounts[n]+=1;i=gatecounts[n];label=f'{n}_EventScript_HyperConstruction_Registered{i}';e=C.P.new_scientist(n,i,x,y,label);e['local_id']=e['local_id'].replace('_CONSTRUCTION_','_REGISTERED_CONSTRUCTION_');maps[n]['object_events'].append(e)
  scripts[n]+=f'\n@ Project-owned reservation; registered asset map, no donor gameplay.\n{label}::\n\tlock\n\tfaceplayer\n\tmsgbox {n}_Text_HyperConstruction_Registered{i}, MSGBOX_DEFAULT\n\trelease\n\tend\n\n{n}_Text_HyperConstruction_Registered{i}:\n\t.string "This area is under construction.\\p"\n\t.string "Please check back later!$"\n';gates.append({'map':n,'scientist':e,'destination':dest,'reason':reason,'existing':False})
 for n,k in list(active.items()):
  if n not in TARGETS and k not in extras:continue
  ensure(n);d=source(k)
  for w in d['warps']:
   if w['x']==w['y']==0 and (k in extras or w['index']>=len(oldmaps[n]['warp_events'])):continue # Placeholder slot requires donor script ownership; reference only.
   dest=reverse.get(w['target_id'])
   if k not in extras and w['index']<len(oldmaps[n]['warp_events']):warp_index[(k,w['index'])]=w['index'];continue
   if dest and not any(a['index']==w['dest_warp_id'] for a in source(w['target_id'])['warps']):
    gate(n,w['x'],w['y'],'Invalid donor destination slot held for manual review; no unsafe warp registered.',w['target_id']);continue
   if dest:
    idx=len(maps[n]['warp_events']);warp_index[(k,w['index'])]=idx;maps[n]['warp_events'].append({'x':w['x'],'y':w['y'],'elevation':w['elevation'],'dest_map':maps[dest]['id'] if dest in maps else load(ROOT/f'data/maps/{dest}/map.json')['id'],'dest_warp_id':'0'});pending.append((n,k,idx,w))
    if k not in extras:gate(n,w['x'],w['y'],'Extra map/shortcut entrance; static project warp registered.',w['target_id'])
   elif k in extras:gate(n,w['x'],w['y'],'Exit outside current Hoenn asset family scope remains closed.',w['target_id'])
 # Previous scientists get actual warps, including shared canonical shortcuts.
 for row in SCOPE['roots']:
  n=row['canonical_source'];k=row['source_donor_id'];ensure(n)
  if n in TARGETS:continue
  if row['entrance_kind']=='WARP':
   w=row['donor_warp'];dest=reverse.get(w['target_id']);assert dest,(n,w);idx=len(maps[n]['warp_events']);warp_index[(k,w['index'])]=idx;maps[n]['warp_events'].append({'x':w['x'],'y':w['y'],'elevation':w['elevation'],'dest_map':maps[dest]['id'] if dest in maps else load(ROOT/f'data/maps/{dest}/map.json')['id'],'dest_warp_id':'0'});pending.append((n,k,idx,w));gate(n,w['x'],w['y'],'Earlier reserved entrance now has registered destination.',w['target_id'])
 for n,k,idx,w in pending:
  destid=w['target_id'];dn=reverse[destid];ensure(dn);di=w['dest_warp_id'];key=(destid,di)
  if key not in warp_index:
   dw=next((a for a in source(destid)['warps'] if a['index']==di),None)
   if dn in TARGETS and di<len(oldmaps[dn]['warp_events']):warp_index[key]=di
   elif destid not in extras and dw and dw['target_id']==k:
    old=load(ROOT/f'data/maps/{dn}/map.json');count=len(old['warp_events'])
    if di<count and old['warp_events'][di]['dest_map']==maps[n]['id']:warp_index[key]=di
    else:
     warp_index[key]=len(maps[dn]['warp_events']);maps[dn]['warp_events'].append({'x':dw['x'],'y':dw['y'],'elevation':dw['elevation'],'dest_map':maps[n]['id'],'dest_warp_id':str(idx)});gate(dn,dw['x'],dw['y'],'New reciprocal entrance/shortcut, separate from native warp slots.',k)
   elif destid in extras and dw:
    # A donor arrival slot may point outward into a foreign region. Author a safe return to its Hoenn parent.
    warp_index[key]=len(maps[dn]['warp_events']);maps[dn]['warp_events'].append({'x':dw['x'],'y':dw['y'],'elevation':dw['elevation'],'dest_map':maps[n]['id'],'dest_warp_id':str(idx)})
   elif di<len(maps[dn]['warp_events']) and destid not in extras:warp_index[key]=di
   else:raise AssertionError(('Unresolved warp destination',n,w,dn))
  maps[n]['warp_events'][idx]['dest_warp_id']=str(warp_index[key])
 # Author static reciprocal returns only for a unique inspected same-room donor portal pair.
 project_warp_reconciliations=[]
 for n in extras.values():
  m=maps[n]
  for i,w in enumerate(m['warp_events']):
   if w['dest_map']==m['id'] and int(w['dest_warp_id'])==i:
    partners=[j for j,z in enumerate(m['warp_events']) if j!=i and z['dest_map']==m['id'] and int(z['dest_warp_id'])==i]
    assert len(partners)==1,(n,i,'Ambiguous same-room donor portal');before=copy.deepcopy(w);w['dest_warp_id']=str(partners[0]);project_warp_reconciliations.append({'map':n,'index':i,'before':before,'after':copy.deepcopy(w),'reason':'Project static reciprocal return for unique inspected same-room portal pair; no donor puzzle scripts.'})
 # Extra static connections are registered reciprocally; scientist-driven runtime guard blocks construction coast.
 for n,k in list(active.items()):
  if k not in extras and n not in ['DewfordTown','Route106']:continue
  ensure(n)
  for co in source(k)['connections']:
   dn=reverse.get(co['target_id'])
   if not dn or co['direction'] not in ['up','down','left','right']:continue
   opposite={'up':'down','down':'up','left':'right','right':'left'}[co['direction']]
   if not any(z['target_id']==k and z['direction']==opposite and z['offset']==-co['offset'] for z in source(active[dn])['connections']):continue # Copied donor headers are reference-only when they conflict with native reciprocal boundaries.
   ensure(dn);entry={'direction':co['direction'],'offset':co['offset'],'map':maps[dn]['id']};maps[n]['connections']=maps[n]['connections'] or []
   if entry not in maps[n]['connections']:maps[n]['connections'].append(entry);connections.append({'map':n,'added':entry})
   if k not in extras:
    g=grids[n];direction=co['direction'];lo=co['offset'];dg=grids[dn]
    points=[(0,y) for y in range(g.h)] if direction=='left' else[(x,g.h-1) for x in range(max(0,lo),min(g.w,lo+dg.w))]
    for x,y in points:
     v=g.cell(x,y)
     if v['collision']==0:
      if v['translated_behavior'] in range(0x10,0x16):continue # Runtime guard follows the scientist templates; removing scientists opens registered water boundary.
      elif C.Grid.walk(g,x,y) and g.neighbors(x,y):gate(n,x,y,'Registered western Dewford coastal extension boundary.',co['target_id'])
 # Construction connections stay registered/renderable. The blocker follows scientist templates,
 # so deleting those scientists in Porymap opens the entire coastline without collision cleanup.
 runtime=(ROOT/'src/fieldmap.c').read_text()
 runtime=runtime.replace('#include "constants/rgb.h"','#include "constants/rgb.h"\n#include "constants/event_objects.h"')
 guard='''static bool32 HyperHoennConstructionConnectionBlocked(const struct MapConnection *connection)
{
    const struct MapHeader *parent;
    const struct ObjectEventTemplate *objects;
    u32 i;
    bool32 isDewford;
    if (connection == NULL)
        return FALSE;
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_DEWFORD_TOWN)
     && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_DEWFORD_TOWN)
     && connection->mapGroup == MAP_GROUP(MAP_HYPERHOENN_34_68_ROUTE_106)
     && connection->mapNum == MAP_NUM(MAP_HYPERHOENN_34_68_ROUTE_106))
    {
        parent = &gMapHeader;
        isDewford = TRUE;
    }
    else if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_ROUTE106)
          && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_ROUTE106)
          && connection->mapGroup == MAP_GROUP(MAP_HYPERHOENN_34_68_ROUTE_106)
          && connection->mapNum == MAP_NUM(MAP_HYPERHOENN_34_68_ROUTE_106))
    {
        parent = &gMapHeader;
        isDewford = FALSE;
    }
    else
        return FALSE;
    objects = parent->events->objectEvents;
    for (i = 0; i < parent->events->objectEventCount; i++)
        if (objects[i].graphicsId == OBJ_EVENT_GFX_SCIENTIST_1
         && ((isDewford && objects[i].x == 0)
          || (!isDewford && objects[i].x == 50 && objects[i].y == 18)))
            return TRUE;
    return FALSE;
}

'''
 runtime=runtime.replace('enum Connection GetMapBorderIdAt(s32 x, s32 y)',guard+'enum Connection GetMapBorderIdAt(s32 x, s32 y)')
 runtime=runtime.replace('enum Connection GetMapBorderIdAt(s32 x, s32 y)\n{','enum Connection GetMapBorderIdAt(s32 x, s32 y)\n{\n    if (HyperHoennConstructionConnectionBlocked(GetMapConnectionAtPos(x, y)))\n        return CONNECTION_INVALID;')
 files['src/fieldmap.c']=runtime.encode()
 # Every extra area has a project-owned scientist, but no donor NPC/progression/events.
 for k,n in extras.items():
  if not maps[n]['object_events']:
   g=grids[n];candidates=[(w['x'],w['y']) for w in maps[n]['warp_events'] if 0<=w['x']<g.w and 0<=w['y']<g.h and C.Grid.walk(g,w['x'],w['y']) and g.neighbors(w['x'],w['y'])]
   if not candidates:candidates=[(x,y) for y in range(g.h) for x in range(g.w) if C.Grid.walk(g,x,y) and g.neighbors(x,y)]
   assert candidates,n;x,y=candidates[0];gate(n,x,y,'Project notice inside registered asset-only area.')
 # Write corrected private geometry for any earlier map whose newly registered entrance needed repairs/barriers.
 for n in maps:
  if n in grids and (n in TARGETS or n in extras.values() or any(p['map']==n for p in patches)):
   l=next(z for z in ls['layouts'] if z['id']==maps[n]['layout']);l['blockdata_filepath']=f'data/hyper_assets/canary5_layouts/{n}/map.bin'
 for n,g in grids.items():
  l=next((z for z in ls['layouts'] if z['name']==n+'_Layout' or z['blockdata_filepath']==f'data/hyper_assets/canary5_layouts/{n}/map.bin'),None)
  if l and '/canary5_layouts/' in l['blockdata_filepath']:files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(g.blocks),*g.blocks)
 # Expose map-local native script behavior derivatives directly in Porymap standard declarations.
 header=(ROOT/'src/data/tilesets/headers.h').read_text();metatiles=(ROOT/'src/data/tilesets/metatiles.h').read_text();native_headers=(OUT/'original/src/data/tilesets/headers.h').read_text();native_metatiles=(OUT/'original/src/data/tilesets/metatiles.h').read_text();labels={m[1]:int(m[2],16) for m in re.finditer(r'#define\s+(METATILE_\w+)\s+(0x[0-9A-Fa-f]+)',(ROOT/'include/constants/metatile_labels.h').read_text())};behavior_edits=[]
 for n,k in TARGETS.items():
  l=next(z for z in ls['layouts'] if z['id']==maps[n]['layout']);ol=next(z for z in oldls['layouts'] if z['id']==oldmaps[n]['layout']);tokens=set(re.findall(r'\bMETATILE_\w+',scripts[n]))
  if n.startswith('MirageTower') or n=='Route111':tokens.update(re.findall(r'\bMETATILE_\w+',(ROOT/'src/mirage_tower.c').read_text()))
  for role,bank in [('primary_tileset',0),('secondary_tileset',1)]:
   nativebody=re.search(r'const struct Tileset\s+'+ol[role]+r'\s*=\s*\{(.*?)\};',native_headers,re.S)[1];symbol=re.search(r'\.metatileAttributes\s*=\s*(\w+)',nativebody)[1];path=re.search(re.escape(symbol)+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',native_metatiles)[1];na=words(ROOT/path);a=list(grids[n].attrs[bank]);changed=[]
   for token in tokens:
    idx=labels.get(token,-1)-(512 if bank else 0)
    if 0<=idx<len(a) and idx<len(na) and (a[idx]&255)!=(na[idx]&255):before=a[idx];a[idx]=(a[idx]&0xFF00)|(na[idx]&255);changed.append({'map':n,'role':role,'token':token,'index':idx,'before':before,'after':a[idx]})
   if changed:
    base=l[role];derived='gTileset_Hyper_Canary5_'+n+('_Primary' if bank==0 else '_Secondary');sym='gMetatileAttributes_Hyper_Canary5_'+n+('_Primary' if bank==0 else '_Secondary');body=re.search(r'const struct Tileset\s+'+base+r'\s*=\s*\{(.*?)\};',header,re.S)[1];body=re.sub(r'(\.metatileAttributes\s*=\s*)\w+',lambda m:m[1]+sym,body);header+='\nconst struct Tileset '+derived+' = {'+body+'};\n';fp=f'data/hyper_assets/canary5_layouts/{n}/'+('primary' if bank==0 else 'secondary')+'_attributes.bin';metatiles+='\nconst u16 '+sym+'[] = INCBIN_U16("'+fp+'");\n';files[fp]=struct.pack('<'+'H'*len(a),*a);l[role]=derived;attr_sources[derived]={'base':base,'attributes_path':fp};behavior_edits+=changed
    if n=='Route111':next(z for z in ls['layouts'] if z['id']=='LAYOUT_ROUTE111_NO_MIRAGE_TOWER')[role]=derived
 import special_portal_assets
 header,metatiles=special_portal_assets.integrate(ROOT,maps,ls['layouts'],extras,grids,header,metatiles,files,attr_sources,patches)
 files['data/event_scripts.s']=((ROOT/'data/event_scripts.s').read_text()+'\n@ Hyper Hoenn construction-only asset maps.\n'+''.join('\t.include \"data/maps/'+n+'/scripts.inc\"\n' for n in extras.values())).encode()
 # Mapsecs retain all numeric IDs, including MAPSEC_NONE=218. New sections follow that sentinel.
 template=(ROOT/'src/data/region_map/region_map_sections.constants.json.txt').read_text();assert template.count('    MAPSEC_NONE,')==1;template=template.replace('    MAPSEC_NONE,\n','');assert len(sections['map_sections'])<0xFD
 files['src/data/region_map/region_map_sections.constants.json.txt']=template.encode();files['src/data/tilesets/headers.h']=header.encode();files['src/data/tilesets/metatiles.h']=metatiles.encode()
 for f in ['src/region_map.c','src/pokedex_area_screen.c','src/pokemon_summary_screen.c']:
  text=(ROOT/f).read_text();text=text.replace('regionMapId < MAPSEC_NONE','regionMapId < MAPSEC_COUNT && regionMapId != MAPSEC_NONE').replace('regionMapSectionId < MAPSEC_NONE','regionMapSectionId < MAPSEC_COUNT && regionMapSectionId != MAPSEC_NONE').replace('sum->metLocation < MAPSEC_NONE','sum->metLocation < MAPSEC_COUNT && sum->metLocation != MAPSEC_NONE').replace('sum->metLocation >= MAPSEC_NONE','(sum->metLocation >= MAPSEC_COUNT || sum->metLocation == MAPSEC_NONE)');files[f]=text.encode()
 text=(ROOT/'src/map_name_popup.c').read_text().replace('MAPSEC_COUNT - KANTO_MAPSEC_COUNT - 1','MAPSEC_COUNT - KANTO_MAPSEC_COUNT');files['src/map_name_popup.c']=text.encode()
 # Native art adapters from proven bank, preserving animation/dimensions/runtime; no donor NPCs.
 old=C.TARGETS;C.TARGETS={n:active[n] for n in maps if n in active}
 try:art,bind,ga,ret=C.graphics(cat,maps,ledger)
 finally:C.TARGETS=old
 art=art.replace('Canary #4','Canary #5').replace('gHyperCanary4Graphics','gHyperCanary5Graphics');bind=bind.replace('gHyperCanary4Graphics','gHyperCanary5Graphics');files['src/data/object_events/hyper_canary5_graphics.inc']=art.encode();files['src/hyper_asset_graphics_bindings.inc']=((ROOT/'src/hyper_asset_graphics_bindings.inc').read_text()+'\n/* Canonical northwest Hoenn and real asset-only special maps. */\n'+bind).encode();files['src/data/object_events/hyper_assets.inc']=(ROOT/'src/data/object_events/hyper_assets.inc').read_text().replace('struct HyperAssetGraphicsBinding\n','#include "hyper_canary5_graphics.inc"\n\nstruct HyperAssetGraphicsBinding\n').encode()
 return locals()

def apply():
 q=prepare();b=q['baseline'];assert all(digest(ROOT/f)==h for f,h in b.items()),'Workspace changed during review; no overwriting edits.'
 for n,m in q['maps'].items():dump(ROOT/f'data/maps/{n}/map.json',m)
 for n,t in q['scripts'].items():(ROOT/f'data/maps/{n}/scripts.inc').write_text(t)
 for f,data in q['files'].items():
  if f in b and not (OUT/'original'/f).exists():backup=OUT/'original'/f;backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes((ROOT/f).read_bytes())
  p=ROOT/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 dump(ROOT/'data/layouts/layouts.json',q['ls']);dump(ROOT/'data/maps/map_groups.json',q['groups']);dump(ROOT/'src/data/region_map/region_map_sections.json',q['sections'])
 changed={f:{'before':h,'after':digest(ROOT/f)} for f,h in b.items() if digest(ROOT/f)!=h};new={str(f.relative_to(ROOT)):digest(f) for d in PREFIXES for f in (ROOT/d).rglob('*') if f.is_file() and str(f.relative_to(ROOT)) not in b and not C.P.C.C.derived(str(f.relative_to(ROOT)))}
 dump(OUT/'receipt.json',{'schema':'hyper-hoenn-canary5-v1','canonical_maps_replaced':list(TARGETS),'donor_ids':TARGETS,'kept_native_dynamic_maps':KEEP,'registered_special_maps':q['extras'],'touched_maps':list(q['maps']),'changed_baseline_files':changed,'new_files':new,'attribute_derivatives':q['attr_sources'],'layout_count_before_after':[len(q['oldls']['layouts']),len(q['ls']['layouts'])],'original_group_order':q['oldgroups']['group_order'],'old_mapsec_ids':q['old_section_ids'],'graphics_binding_maps':sorted({a['map'] for a in q['ga']}),'hyper_gameplay_imported':False,'runtime_verified':False})
 dump(OUT/'coordinate_remap_ledger.json',{'events':q['ledger'],'geometry_patches':q['patches'],'construction_gates':q['gates'],'connections_added':q['connections'],'behavior_derivatives':q['behavior_edits'],'graphics_adapters':q['ga'],'native_graphics_retained':q['ret'],'native_scene_paths':q['scene_paths'],'warp_correspondence':{k+'.'+str(i):v for (k,i),v in q['warp_index'].items()},'blocked_external_links':SCOPE['blocked_external_links'],'project_warp_reconciliations':q['project_warp_reconciliations']})
 print('Applied',len(TARGETS),'canonical maps;',len(q['extras']),'real special maps;',len(q['ga']),'art adapters.')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--apply',action='store_true');v=a.parse_args()
 if v.apply:apply()
 else:q=prepare();print('Preflight passed:',len(TARGETS),'canonical maps,',len(q['extras']),'real special maps.')
