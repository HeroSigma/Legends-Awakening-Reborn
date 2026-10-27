"""Stage pinned HnS Kanto/Johto assets and project-owned placeholder travel.

One-shot staging refuses an existing manifest, protecting subsequent Porymap edits.
No donor scripts are emitted. Original event records are reference-only in the ledger.
"""
import copy,csv,hashlib,json,re,shutil,struct,tarfile
from collections import Counter,defaultdict
from pathlib import Path
from hns_region_assets import R,S,A,AssetPort,dump,blob
from hns_region_objects import ObjectPort
D=R/'docs/la_world/hns_regions'
B=R/'.la_work/amap/hns_regions_backup'
def read(p):return json.loads(p.read_text())
def append(path,text):
 p=R/path;p.write_text(p.read_text()+'\n/* HNS_REGION_GENERATED: visual assets only. */\n'+text+'\n')
def replace(path,old,new):
 p=R/path;t=p.read_text();assert old in t,(path,old[:80]);p.write_text(t.replace(old,new,1))
def main():
 assert not (D/'manifest.json').exists(),'Already staged. Do not overwrite Porymap edits.'
 assert __import__('subprocess').check_output(['git','-C',str(S),'rev-parse','HEAD'],text=True).strip()=='167aa6d537b109bb229c231ddce4616974c4da71'
 D.mkdir(parents=True,exist_ok=True);B.mkdir(parents=True,exist_ok=True)
 groups=read(R/'data/maps/map_groups.json');layouts=read(R/'data/layouts/layouts.json')
 sg=read(S/'data/maps/map_groups.json');sl={x['id']:x for x in read(S/'data/layouts/layouts.json')['layouts']}
 sources={};meta={}
 for gi,g in enumerate(sg['group_order']):
  if gi<=24 or gi in (27,30):
   for mi,n in enumerate(sg[g]):
    sources[n]=read(S/'data/maps'/n/'map.json');meta[n]=(gi,mi,g)
 for n in ['ArtisanCave_1F','ArtisanCave_B1F']:
  sources[n]=read(S/'data/maps'/n/'map.json');meta[n]=(30,-1,'associated_artisan_cave')
 oldnine=groups['gMapGroup_HnS_Canary']
 aliases={n.removeprefix('HnSTest_')+'_hns':n for n in oldnine}
 refs={n for n in sources if re.search(r'TestMap|^Trees_hns$|UnusedContest|Saffron_Temp',n)}
 sourceid={v['id']:n for n,v in sources.items()}
 sourceid.update(MAP_BATTLE_FRONTIER_OUTSIDE_EAST='BattleFrontier_OutsideEast_hns',MAP_BATTLE_FRONTIER_OUTSIDE_WEST='BattleFrontier_OutsideWest_hns',MAP_UNION_ROOM='UnionRoom_hns',MAP_TRADE_CENTER='TradeCenter_hns')
 target={n:aliases.get(n,'HnS_'+n.removesuffix('_hns')) for n in sources}
 ids={n:read(R/'data/maps'/target[n]/'map.json')['id'] if n in aliases else 'MAP_HNS_REGION_'+re.sub(r'\W','_',n.removesuffix('_hns')).upper() for n in sources}
 lids={n:read(R/'data/maps'/target[n]/'map.json')['layout'] if n in aliases else 'LAYOUT_HNS_REGION_'+re.sub(r'\W','_',n.removesuffix('_hns')).upper() for n in sources}
 assert len(set(target.values()))==len(sources)
 # Back up every file this tool is authorized to edit, plus preserve existing map/layout hashes.
 files=['data/maps/map_groups.json','data/layouts/layouts.json','data/event_scripts.s','src/data/tilesets/headers.h','src/data/tilesets/graphics.h','src/data/tilesets/metatiles.h','src/tileset_anims.c','include/constants/event_objects.h','include/constants/flags.h','src/data/object_events/object_event_graphics.h','src/data/object_events/object_event_pic_tables.h','src/data/object_events/object_event_graphics_info.h','src/data/object_events/object_event_graphics_info_pointers.h','src/event_object_movement.c','src/regional_map_names.c']
 for n in oldnine:
  files += [str(p.relative_to(R)) for p in (R/'data/maps'/n).rglob('*') if p.is_file()]
 with tarfile.open(B/'before.tar.gz','w:gz') as z:
  for f in files:z.add(R/f,arcname=f)
 protected={}
 for root in ['data/maps','data/layouts','data/bwa_assets','data/swsh_assets','data/hyper_assets']:
  for p in (R/root).rglob('*'):
   if p.is_file() and p.name not in ['map_groups.json','layouts.json'] and not any(n in p.parts for n in oldnine):
    protected[str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
 dump(B/'protected.json',protected)
 # Build all graphics before mutating the canonical registries.
 ap=AssetPort();op=ObjectPort();banks={};geometry={};safe={};ledger=[];review=[]
 for n,m in sources.items():
  lay=sl[m['layout']];base=640 if lay.get('layout_version')=='hns' else 512
  primary=ap.bank(lay['primary_tileset'],lay['secondary_tileset'],base,False)
  secondary=ap.bank(lay['primary_tileset'],lay['secondary_tileset'],base,True)
  banks[n]=(primary,secondary)
  raw=(S/lay['blockdata_filepath']).read_bytes();w,h=lay['width'],lay['height'];assert len(raw)==w*h*2,(n,w,h,len(raw))
  cells=list(struct.unpack('<'+'H'*(w*h),raw));geometry[n]=(lay,raw,cells)
  occupied={(e['x'],e['y']) for e in m.get('object_events',[])}
  warps={(e['x'],e['y']) for e in m.get('warp_events',[])}
  attrs=struct.unpack('<512H',(R/primary['attributes']['path']).read_bytes())+struct.unpack('<512H',(R/secondary['attributes']['path']).read_bytes())
  candidates=[]
  for y in range(1,h-1):
   for x in range(1,w-1):
    cell=cells[y*w+x];beh=attrs[cell&1023]&255
    if cell&1023 and cell&0xc00==0 and beh in {ap.native[k] for k in ['MB_NORMAL','MB_CAVE','MB_INDOOR_ENCOUNTER','MB_SHORT_GRASS','MB_MOUNTAIN_TOP','MB_HOLDS_LARGE_DECORATION','MB_HOLDS_SMALL_DECORATION']} and (x,y) not in occupied|warps:
     candidates.append((abs(x-w//2)+abs(y-h//2),x,y))
  if not candidates:
   review.append(dict(map=n,issue='No plain floor arrival; source warp fallback requires review'))
   candidates=[(0,e['x'],e['y']) for e in m.get('warp_events',[]) if 0<=e['x']<w and 0<=e['y']<h]
  if not candidates and n in refs:candidates=[(0,w//2,h//2)]
  assert candidates,('No arrival point',n)
  pair=[]
  for distance,x,y in candidates:
   if y>1:
    above=cells[(y-1)*w+x]
    if above&1023 and above&0xc00==0 and attrs[above&1023]&255 in {ap.native[k] for k in ['MB_NORMAL','MB_CAVE','MB_INDOOR_ENCOUNTER','MB_SHORT_GRASS','MB_MOUNTAIN_TOP','MB_HOLDS_LARGE_DECORATION','MB_HOLDS_SMALL_DECORATION']} and (x,y-1) not in occupied|warps and above>>12==cells[y*w+x]>>12:pair.append((distance,x,y))
  _,x,y=min(pair or candidates);safe[n]=(x,y)
  if n=='PokemonLeague_HallOfFame_hns':safe[n]=(4,11)
 # Resolve donor dynamic artwork only from explicit graphical assignments; unresolved actors stay dormant.
 dynamic={}
 for n,m in sources.items():
  script=(S/'data/maps'/n/'scripts.inc')
  text=script.read_text() if script.exists() else ''
  dynamic[n]=dict(re.findall(r'setvar\s+(VAR_OBJ_GFX_ID_[0-9A-F]),\s*(OBJ_EVENT_GFX_\w+)',text))
  for e in m.get('object_events',[]):
   gfx=e['graphics_id']
   if gfx.startswith(('VAR_','OBJ_EVENT_GFX_VAR_')):
    suffix=gfx.rsplit('_',1)[-1];gfx=dynamic[n].get('VAR_OBJ_GFX_ID_'+suffix)
   if gfx:op.gfx(gfx)
 animations,closure=ap.animations();out=op.output()
 dump(D/'object_assets.json',dict(assets=op.assets,mapping=op.mapping))
 dump(D/'animation_closure.json',closure)
 # Register new groups without changing any preexisting numeric identity.
 categories={}
 for n in sources:
  gi=meta[n][0]
  if n in refs:category='References'
  elif gi==0:category='Johto_World' if list(sg[sg['group_order'][0]]).index(n)<31 else 'Kanto_World'
  elif gi in list(range(1,11))+[22]:category='Johto_Interiors'
  elif gi in list(range(11,22))+[23]:category='Kanto_Interiors'
  elif gi==24 or n.startswith('ArtisanCave'):category='Dungeons'
  else:category='SpecialAreas'
  categories[n]=category
  if n in aliases:continue
  group='gMapGroup_HnS_'+category
  if group not in groups:groups['group_order'].append(group);groups[group]=[]
  assert len(groups[group])<127,(group,len(groups[group]))
  groups[group].append(target[n])
 assert len(groups['group_order'])<=128
 positions={n:(groups['group_order'].index(g),groups[g].index(target[n])) for n in sources for g in groups['group_order'] if target[n] in groups[g]}
 # Keep only static in-scope travel; replace dynamic exits with a reviewed incoming parent link.
 warp_source={};blocked=[];incoming=defaultdict(list)
 for n,m in sources.items():
  for i,e in enumerate(m.get('warp_events',[])):
   dn=sourceid.get(e['dest_map'])
   if dn and dn not in refs:incoming[dn].append((n,i))
 for n,m in sources.items():
  retained=[]
  for i,e in enumerate(m.get('warp_events',[])):
   dn=sourceid.get(e['dest_map'])
   if e['dest_map']=='MAP_UNION_ROOM':dn='UnionRoom_hns'
   if e['dest_map']=='MAP_TRADE_CENTER':dn=next((v for v in sources if v.lower()=='tradecenter_hns'),None)
   if dn and (dn not in refs or n in refs):
    retained.append((i,copy.deepcopy(e),dn,int(e['dest_warp_id'])))
   elif e['dest_map']=='MAP_DYNAMIC':
    parents=[x for x in incoming[n] if x[0] not in refs]
    if parents:
     parent,pi=sorted(parents)[0];retained.append((i,copy.deepcopy(e),parent,pi))
     review.append(dict(map=n,issue='Dynamic exit replaced with project static return',destination=parent))
    else:blocked.append(dict(map=n,index=i,event=e,reason='Dynamic destination needs project service logic'))
   else:blocked.append(dict(map=n,index=i,event=e,reason='Out-of-scope or reference destination'))
  warp_source[n]=retained
 # Resolve retained indices recursively; reject destination references to removed warps.
 while True:
  wi={n:{old:i for i,(old,e,dn,di) in enumerate(v)} for n,v in warp_source.items()}
  removed=0
  for n,v in warp_source.items():
   valid=[]
   for old,e,dn,di in v:
    if di not in wi[dn]:
     blocked.append(dict(map=n,index=old,event=e,reason='Source references nonexistent or held destination warp',destination=dn,destination_index=di));removed+=1
    else:valid.append((old,e,dn,di))
   warp_source[n]=valid
  if not removed:break
 # Emit maps with one project-owned map callback and harmless placeholder event scripts.
 maps=[];all_events=[]
 for n,m in sources.items():
  name=target[n];lay,raw,cells=geometry[n];w,h=lay['width'],lay['height'];p,s=banks[n];folder=A/'layouts'/name
  blob(folder/'map.bin',raw);border=(S/lay['border_filepath']).read_bytes();blob(folder/'border.bin',border)
  nl=dict(id=lids[n],name=name+'_Layout',width=w,height=h,primary_tileset=p['symbol'],secondary_tileset=s['symbol'],blockdata_filepath=str((folder/'map.bin').relative_to(R)),border_filepath=str((folder/'border.bin').relative_to(R)),border_width=lay.get('border_width',2),border_height=lay.get('border_height',2),layout_version='emerald')
  existing=next((i for i,x in enumerate(layouts['layouts']) if x['id']==lids[n]),None)
  if existing is None:layouts['layouts'].append(nl)
  else:layouts['layouts'][existing]=nl
  nm={k:copy.deepcopy(v) for k,v in m.items() if k in ['requires_flash','weather','map_type','allow_cycling','allow_escaping','allow_running','show_map_name','battle_scene']}
  nm.update(id=ids[n],name=name,layout=lids[n],music='MUS_ROUTE104',region_map_section='MAPSEC_KANTO_AR' if categories[n].startswith('Kanto') or m.get('region')=='REGION_KANTO' else 'MAPSEC_GS_JOHTO')
  nm['requires_flash']=False
  if nm['battle_scene'].endswith('_HNS'):nm['battle_scene']='MAP_BATTLE_SCENE_NORMAL'
  if nm['weather']=='WEATHER_LEAVES':nm['weather']='WEATHER_NONE'
  nm['connections']=[dict(e,map=ids[sourceid[e['map']]]) for e in m.get('connections') or [] if e['map'] in sourceid and sourceid[e['map']] not in refs]
  objects=[];seen=set()
  ranked=sorted(enumerate(m.get('object_events',[])),key=lambda z:(str(z[1].get('flag','0'))!='0',z[0]))
  visible_choice={}
  for i,e in ranked:visible_choice.setdefault((e['x'],e['y']),i)
  for i,e in enumerate(m.get('object_events',[])):
   gfx=e['graphics_id'];resolved=gfx;reason=[]
   if gfx.startswith(('VAR_','OBJ_EVENT_GFX_VAR_')):
    resolved=dynamic[n].get('VAR_OBJ_GFX_ID_'+gfx.rsplit('_',1)[-1])
    if not resolved:reason.append('uninitialized dynamic artwork slot')
   if visible_choice[(e['x'],e['y'])]!=i:reason.append('overlapping story alternative')
   if not (0<=e['x']<w and 0<=e['y']<h):reason.append('off-map staging actor')
   ne=copy.deepcopy(e);ne['local_id']='LOCALID_'+name.upper()+'_ACTOR_'+str(i+1)
   ne['graphics_id']=op.gfx(resolved) if resolved else 'OBJ_EVENT_GFX_SCIENTIST_1'
   ne.update(script='HnsRegion_Placeholder',flag='FLAG_HIDE_HNS_PLACEHOLDER_VARIANTS' if reason else '0',trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0')
   # Static face preserves placement without donor movement callbacks, disguises, berry state, or path blockers.
   face=e.get('movement_type','')
   ne['movement_type']=face if face in ['MOVEMENT_TYPE_FACE_UP','MOVEMENT_TYPE_FACE_DOWN','MOVEMENT_TYPE_FACE_LEFT','MOVEMENT_TYPE_FACE_RIGHT','MOVEMENT_TYPE_NONE'] else 'MOVEMENT_TYPE_FACE_DOWN'
   ne['movement_range_x']=ne['movement_range_y']=0
   objects.append(ne)
   ledger.append(dict(map=name,source_map=n,index=i,source=e,target=ne,visible=not reason,reason=reason or ['visible placeholder']))
  # Dedicated inspection guide doubles as safe traversal for unsupported side systems.
  x,y=safe[n]
  if len(objects)<64:
   objects.append(dict(local_id='LOCALID_'+name.upper()+'_INSPECTOR',graphics_id='OBJ_EVENT_GFX_SCIENTIST_1',x=x,y=y-1 if y>1 else y+1,elevation=cells[(y-1 if y>1 else y+1)*w+x]>>12,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script=name+'_Inspect',flag='0'))
  else:
   ix=next((i for i,o in enumerate(objects) if o['flag']=='0'),0);objects[ix]['script']=name+'_Inspect'
  if n=='PokemonLeague_HallOfFame_hns':objects[-1].update(x=4,y=10)
  nm['object_events']=objects
  nm['warp_events']=[dict(e,dest_map=ids[dn],dest_warp_id=str(wi[dn][di])) for old,e,dn,di in warp_source[n]]
  nm['coord_events']=[dict(type='trigger',x=e['x'],y=e['y'],elevation=e.get('elevation',0),var='VAR_TEMP_1',var_value='65535',script='HnsRegion_NoOp') for e in m.get('coord_events',[])]
  nm['bg_events']=[dict(type='sign',x=e['x'],y=e['y'],elevation=e.get('elevation',0),player_facing_dir='BG_EVENT_PLAYER_FACING_ANY',script='HnsRegion_Sign') for e in m.get('bg_events',[])]
  all_events.append(dict(map=name,source_map=n,source_objects=m.get('object_events',[]),source_warps=m.get('warp_events',[]),source_coord_events=m.get('coord_events',[]),source_bg_events=m.get('bg_events',[])))
  dump(R/'data/maps'/name/'map.json',nm)
  active=[v for v in sources if v not in refs];nxt=active[(active.index(n)+1)%len(active)] if n in active else active[0];nx,ny=safe[nxt]
  scripts=f"""{name}_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

{name}_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, {name}_Next
 release
 end
{name}_Next::
 warp {ids[nxt]}, {nx}, {ny}
 waitstate
 release
 end
"""
  (R/'data/maps'/name/'scripts.inc').write_text(scripts)
  maps.append(dict(source=n,name=name,id=ids[n],layout=lids[n],source_group=meta[n][0],source_map=meta[n][1],group=positions[n][0],map=positions[n][1],category=categories[n],reference_only=n in refs,width=w,height=h,source_layout=lay,source_mapsec=m.get('region_map_section'),source_region=m.get('region'),arrival=[x,y],objects=len(m.get('object_events',[])),visible_objects=sum(e['flag']=='0' for e in objects),warps=len(nm['warp_events']),connections=len(nm['connections']),blockdata_sha256=hashlib.sha256(raw).hexdigest(),border_sha256=hashlib.sha256(border).hexdigest(),primary=p['symbol'],secondary=s['symbol']))
 # Rebuild output after dynamic artwork resolution (no late imports expected).
 out=op.output()
 append('src/data/tilesets/graphics.h',ap.decls['graphics'])
 append('src/data/tilesets/metatiles.h',ap.decls['metatiles'])
 append('src/data/tilesets/headers.h',ap.decls['headers'])
 append('src/tileset_anims.c',animations)
 blob(R/'include/constants/hns_object_graphics.h',out['constants'].encode())
 append('include/constants/event_objects.h','#include "constants/hns_object_graphics.h"')
 append('include/constants/flags.h','#define FLAG_HIDE_HNS_PLACEHOLDER_VARIANTS FLAG_UNUSED_0x020')
 append('src/data/object_events/object_event_graphics.h',out['graphics'])
 append('src/data/object_events/object_event_pic_tables.h',out['picdefs'])
 append('src/data/object_events/object_event_graphics_info.h',out['infos'])
 pp='src/data/object_events/object_event_graphics_info_pointers.h'
 replace(pp,'const struct ObjectEventGraphicsInfo *const gObjectEventGraphicsInfoPointers[NUM_OBJ_EVENT_GFX] = {',out['externs']+'\nconst struct ObjectEventGraphicsInfo *const gObjectEventGraphicsInfoPointers[] = {\n'+out['pointers'])
 replace('src/event_object_movement.c','    /* Visual-only opt-in after expansion dynamic/species resolution. */','    if (graphicsId >= OBJ_EVENT_GFX_HNS_BASE && graphicsId < OBJ_EVENT_GFX_HNS_END)\n        return gObjectEventGraphicsInfoPointers[graphicsId];\n\n    /* Visual-only opt-in after expansion dynamic/species resolution. */')
 replace('src/event_object_movement.c','#include "data/object_events/hyper_palettes.inc"','#include "data/object_events/hyper_palettes.inc"\n'+out['palettes'])
 common=r"""HnsRegion_OnTransition::
 setflag FLAG_HIDE_HNS_PLACEHOLDER_VARIANTS
 end
HnsRegion_NoOp::
 end
HnsRegion_Placeholder::
 lock
 faceplayer
 msgbox HnsRegion_PlaceholderText, MSGBOX_DEFAULT
 release
 end
HnsRegion_Sign::
 msgbox HnsRegion_PlaceholderText, MSGBOX_SIGN
 end
HnsRegion_PlaceholderText:
 .string "This area is under construction.\p"
 .string "Story and services are coming later.$"
HnsRegion_InspectText:
 .string "Regional map inspection.\p"
 .string "Visit the next preserved map?$"
"""
 blob(R/'data/scripts/hns_region_placeholders.inc',common.encode())
 append('data/event_scripts.s','.include "data/scripts/hns_region_placeholders.inc"\n'+''.join(f'.include "data/maps/{target[n]}/scripts.inc"\n' for n in sources if n not in aliases))
 # Display names are presentation-only; canonical mapsec/met-location ABI is unchanged.
 names=[];entry=[]
 for i,row in enumerate(maps):
  label=row['source_mapsec'] or row['source']
  label=label.removeprefix('MAPSEC_').replace('_',' ').title().replace('Pokemon','Pokemon')
  names.append(f'static const u8 sHnsRegionName{i}[] = _("{label}");')
  entry.append(f' case {row["layout"]}: return sHnsRegionName{i};')
 text='\n'.join(names)+'\nstatic const u8 *HnsRegionDisplayName(u16 layout)\n{\n switch (layout) {\n'+'\n'.join(entry)+'\n default: return NULL;\n }\n}\n'
 blob(R/'src/hns_region_names.inc',text.encode())
 replace('src/regional_map_names.c','#include "mercury_johto_names.inc"','#include "mercury_johto_names.inc"\n#include "hns_region_names.inc"')
 replace('src/regional_map_names.c','    const u8 *mercuryName = MercuryJohtoDisplayName(header->mapLayoutId);','    const u8 *hnsName = HnsRegionDisplayName(header->mapLayoutId);\n    if (hnsName != NULL)\n        return hnsName;\n    const u8 *mercuryName = MercuryJohtoDisplayName(header->mapLayoutId);')
 dump(R/'data/maps/map_groups.json',groups);dump(R/'data/layouts/layouts.json',layouts)
 dump(D/'manifest.json',dict(source_commit='167aa6d537b109bb229c231ddce4616974c4da71',policy='assets/travel/placeholders only; no donor gameplay',maps=maps,banks=list(ap.banks.values()),deferred_regions=['Alola','Sinjoh']))
 dump(D/'object_event_ledger.json',ledger);dump(D/'source_event_reference.json',all_events);dump(D/'blocked_travel.json',blocked);dump(D/'manual_review.json',review);dump(D/'behavior_translation.json',ap.behaviors)
 with (D/'inventory.csv').open('w',newline='') as f:
  fields=['name','source','group','map','category','reference_only','width','height','objects','visible_objects','warps','connections','source_mapsec']
  cw=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');cw.writeheader();cw.writerows(maps)
 print(json.dumps(dict(maps=len(maps),references=len(refs),objects=len(ledger),art=len(op.assets),banks=len(ap.banks),groups=len(groups['group_order']),blocked=len(blocked),review=len(review))))
if __name__=='__main__':main()
