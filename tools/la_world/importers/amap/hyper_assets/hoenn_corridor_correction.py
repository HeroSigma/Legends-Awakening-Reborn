#!/usr/bin/env python3
"""Correct the missing western Hoenn sea corridor; expansion owns gameplay."""
import argparse,copy,csv,json,re,struct,collections,sys
from pathlib import Path
import hoenn_canary4 as C
ROOT=C.ROOT; load=C.load;dump=C.dump;digest=C.digest;words=C.words
OUT=ROOT/'.la_work/amap/hyper_hoenn_corridor_correction'
TARGETS={'Route105':'0.20','Route107':'0.22','Route108':'0.23'}
RESERVATIONS=[('DewfordTown',0,6,'34.68'),('DewfordTown',0,7,'34.68'),('DewfordTown',0,11,'34.68'),('DewfordTown',0,12,'34.68'),('Route106',50,18,'34.68'),('Route105',32,45,'35.6')]
SCOPE=['data/layouts/layouts.json',*[f'data/maps/{n}/map.json' for n in [*TARGETS,'DewfordTown','Route106']],*[f'data/maps/{n}/scripts.inc' for n in ['Route105','DewfordTown','Route106']],'src/overworld.c','src/data/tilesets/headers.h','src/data/tilesets/metatiles.h','src/data/object_events/hyper_assets.inc','src/hyper_asset_graphics_bindings.inc']
REMAP={'Route105':{'object_events':{4:(33,33)},'warp_events':{0:(9,21)}}}
KINDS={'object_events':'npcs','warp_events':'warps','coord_events':'coord_events','bg_events':'bg_events'}
def baseline():
 OUT.mkdir(parents=True,exist_ok=True)
 if (OUT/'baseline.json').exists():return load(OUT/'baseline.json')
 b={str(f.relative_to(ROOT)):digest(f) for d in ['data','src','include','graphics'] for f in (ROOT/d).rglob('*') if f.is_file() and not C.P.C.C.derived(str(f.relative_to(ROOT)))}
 for f in set(SCOPE+[f'data/maps/{n}/scripts.inc' for n in TARGETS]):
  p=OUT/'original'/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/f).read_bytes())
 dump(OUT/'baseline.json',b);return b

def grid_for(layout):
 primary=layout['primary_tileset'];g=C.Grid({'dimensions':[layout['width'],layout['height']],'blockdata_path':layout['blockdata_filepath'],'primary_tileset':'gTileset_Hyper_Primary_083DF704' if primary=='gTileset_Hyper_Primary_Route105' else primary,'secondary_tileset':layout['secondary_tileset']})
 if primary=='gTileset_Hyper_Primary_Route105':g.attrs[0]=words(ROOT/'data/hyper_assets/corridor_correction/Route105/metatile_attributes.bin')
 return g
def prepare():
 b=baseline();assert all(digest(ROOT/f)==b[f] for f in SCOPE),'Inputs changed; inspect receipt, never reapply blindly.'
 cat=load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');by={x['donor_id']:x for x in cat['layouts']};ls=load(ROOT/'data/layouts/layouts.json');oldls=copy.deepcopy(ls);maps={n:load(ROOT/f'data/maps/{n}/map.json') for n in [*TARGETS,'DewfordTown','Route106']};oldmaps=copy.deepcopy(maps);grids={n:C.Grid(by[k]) for n,k in TARGETS.items()};patches=[];ledger=[]
 for n,k in TARGETS.items():
  m=maps[n];g=grids[n];l=next(x for x in ls['layouts'] if x['id']==m['layout']);assert [l['width'],l['height']]==by[k]['dimensions'];assert sum(load(f)['layout']==l['id'] for f in (ROOT/'data/maps').glob('*/map.json'))==1
  native=words(ROOT/l['blockdata_filepath'])
  for y in range(g.h):
   for x in range(g.w):
    v=g.cell(x,y);el=native[y*g.w+x]>>12
    if v['collision']==0 and v['translated_behavior'] in range(0x10,0x16) and el in [1,3] and v['elevation']!=el:
     after=(v['block']&4095)|(el<<12);g.blocks[y*g.w+x]=after;patches.append({'map':n,'x':x,'y':y,'before':v['block'],'after':after,'reason':'Retain native per-cell ocean elevation; Hyper art and collision unchanged.'})
  d=C.P.C.donor(k)[0]
  for kind,dkey in KINDS.items():
   probes={z['index']:z for z in d[dkey]}
   for i,e in enumerate(m[kind]):
    a=copy.deepcopy(e);xy=REMAP.get(n,{}).get(kind,{}).get(i)
    if xy:e['x'],e['y']=xy
    v=g.cell(e['x'],e['y']);near=g.neighbors(e['x'],e['y'])
    if kind=='object_events':
     water=e['graphics_id'].startswith(('OBJ_EVENT_GFX_SWIMMER','OBJ_EVENT_GFX_TUBER_M_SWIMMING'))
     assert v['collision']==0 and (v['translated_behavior'] in range(0x10,0x16) if water else g.walk(e['x'],e['y'])),(n,kind,i,v)
    elif kind=='warp_events':assert v['collision']==0 and v['translated_behavior'] in [0x60,0x64] and near,(n,i,v)
    elif kind=='bg_events':assert near or any(0<=x<g.w and 0<=y<g.h and g.cell(x,y)['collision']==0 for x,y in [(e['x']-1,e['y']),(e['x']+1,e['y']),(e['x'],e['y']-1),(e['x'],e['y']+1)]),(n,i,v)
    ledger.append({'map':n,'donor_id':k,'kind':kind,'index':i,'before':a,'after':copy.deepcopy(e),'donor_reference':probes.get(i),'cell':v,'interaction_neighbors':near,'owner':'expansion/project','reason':'Native role/state retained; inspected actual Hyper cell.' if not xy else 'Reviewed native Iron role/source item clearing or source Island Cave doorway; coordinates only.'})
  l.update(primary_tileset=by[k]['primary_tileset'],secondary_tileset=by[k]['secondary_tileset'],blockdata_filepath=f'data/hyper_assets/corridor_correction/{n}/map.bin',border_filepath=by[k]['border_path'])
 # Close only newly opened incompatible seam corners that were blocked natively.
 names={load(f)['id']:f.parent.name for f in (ROOT/'data/maps').glob('*/map.json')};seams=[]
 for n,g in grids.items():
  oldl=next(z for z in oldls['layouts'] if z['id']==oldmaps[n]['layout']);ob=words(ROOT/oldl['blockdata_filepath'])
  for co in maps[n]['connections'] or []:
   if co['direction'] not in ['left','right','up','down']:continue
   dn=names[co['map']];dm=maps.get(dn,load(ROOT/f'data/maps/{dn}/map.json'));dl=next(z for z in oldls['layouts'] if z['id']==dm['layout']);dg=grids.get(dn) or grid_for(dl);direct=co['direction'];off=co['offset'];cross=[]
   for x,y in ([(x,0 if direct=='up' else g.h-1) for x in range(g.w)] if direct in ['up','down'] else [(0 if direct=='left' else g.w-1,y) for y in range(g.h)]):
    dx,dy=(x-off,dg.h-1 if direct=='up' else 0) if direct in ['up','down'] else(dg.w-1 if direct=='left' else 0,y-off)
    if not(0<=dx<dg.w and 0<=dy<dg.h):continue
    a=g.cell(x,y);z=dg.cell(dx,dy)
    if a['collision']==z['collision']==0:
     good=a['elevation']==z['elevation'] or a['elevation'] in [0,15] or z['elevation'] in [0,15]
     if not good and (ob[y*g.w+x]>>10)&3:
      g.blocks[y*g.w+x]=a['block']|1024;patches.append({'map':n,'x':x,'y':y,'before':a['block'],'after':a['block']|1024,'reason':'Native-closed corner stays closed across incompatible sea seam; same artwork.'});continue
     assert good,(n,dn,a,z);cross.append({'from':[x,y],'to':[dx,dy],'elevation':a['elevation']})
   assert cross,(n,dn);seams.append({'map':n,'destination':dn,'connection':co,'crossing_cells':cross})
 # Source extra connection is absent from canonical headers, including its water boundary.
 # Four paired land mouths were verified on both Dewford and extra 34.68; R106 is a shore notice, not a invented warp.
 for n in ['DewfordTown','Route106']:grids[n]=grid_for(next(z for z in ls['layouts'] if z['id']==maps[n]['layout']))
 gates=[];scripts={n:(ROOT/f'data/maps/{n}/scripts.inc').read_text() for n in ['Route105','DewfordTown','Route106']};counts=collections.Counter()
 for n,x,y,dest in RESERVATIONS:
  counts[n]+=1;i=counts[n];g=grids[n];assert g.walk(x,y) and g.neighbors(x,y),(n,x,y);assert not any((e['x'],e['y'])==(x,y) for e in maps[n]['object_events'])
  label=f'{n}_EventScript_HyperConstruction_Corridor{i}';e=C.P.new_scientist(n,i,x,y,label);e['local_id']=e['local_id'].replace('_CONSTRUCTION_', '_CORRIDOR_CONSTRUCTION_');maps[n]['object_events'].append(e)
  display='Western Dewford extension' if dest=='34.68' else 'Champion Island'
  scripts[n]+=f'\n@ Project-owned reservation; no donor gameplay, flags or warp destination.\n{label}::\n\tlock\n\tfaceplayer\n\tmsgbox {n}_Text_HyperConstruction_Corridor{i}, MSGBOX_DEFAULT\n\trelease\n\tend\n\n{n}_Text_HyperConstruction_Corridor{i}:\n\t.string "{display} is\\n"\n\t.string "under construction.\\p"\n\t.string "Please check back later!$"\n'
  gates.append({'map':n,'scientist':e,'reserved_donor_id':dest,'reserved_donor_name':C.P.C.donor(dest)[0]['name'],'source_cell':g.cell(x,y),'status':'RESERVED_NO_DONOR_WARP_OR_CONNECTION','kind':'SHORE_NOTICE_WITH_ABSENT_CONNECTION' if n=='Route106' else 'LAND_CONNECTION_GATE' if n=='DewfordTown' else 'WARP_GATE'})
 # Hyper doorway is one row lower. Flags and calls stay native; only art/coordinate operands change.
 scripts['Route105']=scripts['Route105'].replace('setmetatile 9, 19, METATILE_General_RockWall_RockBase, TRUE','setmetatile 9, 20, 0x09F, TRUE').replace('setmetatile 9, 20, METATILE_General_RockWall_SandBase, TRUE','setmetatile 9, 21, 0x09F, TRUE')
 # Local primary attribute derivative restores expansion rough/deep-water Dive semantics without mutating the bank.
 source=ROOT/'data/tilesets/primary/hyper_primary_083df704/metatile_attributes.bin'
 if not source.exists():source=ROOT/'data/tilesets/primary/hyper_primary_083DF704/metatile_attributes.bin'
 attrs=words(source);native=words(ROOT/'data/tilesets/primary/general/metatile_attributes.bin');attr_edits=[]
 for idx in [0x14E,0x14F]:
  before=attrs[idx];attrs[idx]=(before&0xFF00)|(native[idx]&255);attr_edits.append({'metatile':idx,'before':before,'after':attrs[idx],'reason':'Expansion Route105 abnormal-weather Dive ownership; donor graphics unchanged.'})
 primary='gTileset_Hyper_Primary_Route105';next(z for z in ls['layouts'] if z['id']==maps['Route105']['layout'])['primary_tileset']=primary
 h=(ROOT/'src/data/tilesets/headers.h').read_text();body=re.search(r'const struct Tileset gTileset_Hyper_Primary_083DF704\s*=\s*\{(.*?)\};',h,re.S)[1];body=re.sub(r'(\.metatileAttributes\s*=\s*)\w+',r'\1gMetatileAttributes_Hyper_Route105',body);header=h+'\n/* Canonical Route105 weather/Dive behavior derivative; shared Hyper graphics. */\nconst struct Tileset '+primary+' = {'+body+'};\n'
 metatiles=(ROOT/'src/data/tilesets/metatiles.h').read_text()+'\nconst u16 gMetatileAttributes_Hyper_Route105[] = INCBIN_U16("data/hyper_assets/corridor_correction/Route105/metatile_attributes.bin");\n'
 # Curated scientist art only for already active towns; native swimming and item renderers retained.
 safe=[e for e in ledger if e['kind']=='object_events' and not any(k in e['after']['graphics_id'] for k in ['SWIMMER','TUBER','ITEM_BALL'])]
 old=C.TARGETS;C.TARGETS={**TARGETS,'DewfordTown':'0.11','Route106':'0.21'}
 try:text,bind,ga,ret=C.graphics(cat,maps,safe)
 finally:C.TARGETS=old
 text=text.replace('Canary #4','Corridor correction').replace('gHyperCanary4Graphics','gHyperCorridorGraphics');bind=bind.replace('gHyperCanary4Graphics','gHyperCorridorGraphics')
 return b,ls,maps,grids,ledger,patches,seams,gates,scripts,attrs,attr_edits,header,metatiles,text,bind,ga,ret

def apply():
 q=prepare();b,ls,maps,grids,ledger,patches,seams,gates,scripts,attrs,ae,header,metatiles,text,bind,ga,ret=q
 new={}
 def write(f,data):
  p=ROOT/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data if isinstance(data,bytes) else data.encode());
  if f not in b:new[f]=digest(p)
 for n in TARGETS:write(f'data/hyper_assets/corridor_correction/{n}/map.bin',struct.pack('<'+'H'*len(grids[n].blocks),*grids[n].blocks))
 write('data/hyper_assets/corridor_correction/Route105/metatile_attributes.bin',struct.pack('<'+'H'*len(attrs),*attrs));dump(ROOT/'data/layouts/layouts.json',ls)
 for n,m in maps.items():dump(ROOT/f'data/maps/{n}/map.json',m)
 for n,t in scripts.items():write(f'data/maps/{n}/scripts.inc',t)
 write('src/data/tilesets/headers.h',header);write('src/data/tilesets/metatiles.h',metatiles);write('src/data/object_events/hyper_corridor_graphics.inc',text)
 p=ROOT/'src/hyper_asset_graphics_bindings.inc';write(str(p.relative_to(ROOT)),p.read_text()+'\n/* Missing canonical sea corridor and construction notices. */\n'+bind)
 p=ROOT/'src/data/object_events/hyper_assets.inc';write(str(p.relative_to(ROOT)),p.read_text().replace('struct HyperAssetGraphicsBinding\n','#include "hyper_corridor_graphics.inc"\n\nstruct HyperAssetGraphicsBinding\n'))
 p=ROOT/'src/overworld.c';t=p.read_text();start=t.index('void LoadMapFromCameraTransition(');end=t.index('static void LoadMapFromWarp(',start);part=t[start:end];part=part.replace('{\n    SetWarpDestination','{\n    const struct Tileset *previousPrimaryTileset = gMapHeader.mapLayout->primaryTileset;\n\n    SetWarpDestination',1);a=part.index('    CopySecondaryTilesetToVramUsingHeap');z=part.index('    UpdateLocationHistoryForRoamer();',a);old=part[a:z];branch='''    // Connected canonical maps may use different primary asset banks.
    if (previousPrimaryTileset != gMapHeader.mapLayout->primaryTileset)
    {
        CopyMapTilesetsToVram(gMapHeader.mapLayout);
        LoadMapTilesetPalettes(gMapHeader.mapLayout);
        ApplyWeatherColorMapToPals(0, NUM_PALS_TOTAL);
        InitTilesetAnimations();
    }
    else
    {
'''+''.join(('    '+line if line else '')+'\n' for line in old.rstrip().splitlines())+'''    }
''';part=part[:a]+branch+part[z:];write('src/overworld.c',t[:start]+part+t[end:])
 dump(OUT/'coordinate_remap_ledger.json',{'events':ledger,'geometry_patches':patches,'connection_checks':seams,'construction_gates':gates,'behavior_derivative':ae,'native_script_geometry_edits':[{'map':'Route105','old':[9,19,9,20],'new':[9,20,9,21],'closed_metatile':'0x09F','ownership':'Expansion FLAG_REGI_DOORS_OPENED and OnLoad calls retained.'}],'graphics_adapters':ga,'native_graphics_retained':ret})
 dump(OUT/'receipt.json',{'schema':'hyper-hoenn-corridor-correction-v1','canonical_maps_replaced':list(TARGETS),'donor_ids':TARGETS,'construction_only_maps':['DewfordTown','Route106'],'hyper_gameplay_imported':False,'runtime_verified':False,'graphics_binding_maps':sorted({a['map'] for a in ga}),'changed_baseline_files':{f:{'before':b[f],'after':digest(ROOT/f)} for f in SCOPE},'new_files':new,'map_ids_header_sha256':digest(ROOT/'include/constants/map_groups.h'),'map_groups_json_sha256':digest(ROOT/'data/maps/map_groups.json')})
 print('Applied three sea routes, six construction scientists, asset-only connected-map reload correction.')

def validate():
 b=load(OUT/'baseline.json');r=load(OUT/'receipt.json');assert set(r['changed_baseline_files'])==set(SCOPE)
 for f,h in b.items():assert digest(ROOT/f)==r['changed_baseline_files'].get(f,{}).get('after',h),f
 for f,h in r['new_files'].items():assert digest(ROOT/f)==h,f
 assert digest(ROOT/'include/constants/map_groups.h')==r['map_ids_header_sha256'];assert digest(ROOT/'data/maps/map_groups.json')==r['map_groups_json_sha256']
 ledger=load(OUT/'coordinate_remap_ledger.json')
 for n in [*TARGETS,'DewfordTown','Route106']:
  a=load(OUT/'original'/f'data/maps/{n}/map.json');z=load(ROOT/f'data/maps/{n}/map.json')
  for key in a:
   if key=='layout':assert a[key]==z[key];continue
   if key in KINDS:
    assert [{k:v for k,v in e.items() if k not in ['x','y']} for e in a[key]]==[{k:v for k,v in e.items() if k not in ['x','y']} for e in z[key][:len(a[key])]],(n,key)
    assert z[key][len(a[key]):]==([g['scientist'] for g in ledger['construction_gates'] if g['map']==n] if key=='object_events' else [])
   else:assert a[key]==z[key],(n,key)
  old=(OUT/'original'/f'data/maps/{n}/scripts.inc').read_text() if (OUT/'original'/f'data/maps/{n}/scripts.inc').exists() else (ROOT/f'data/maps/{n}/scripts.inc').read_text();now=(ROOT/f'data/maps/{n}/scripts.inc').read_text().split('\n@ Project-owned reservation;')[0]
  if n=='Route105':now=now.replace('setmetatile 9, 20, 0x09F, TRUE','setmetatile 9, 19, METATILE_General_RockWall_RockBase, TRUE').replace('setmetatile 9, 21, 0x09F, TRUE','setmetatile 9, 20, METATILE_General_RockWall_SandBase, TRUE')
  assert now==old.split('\n@ Project-owned reservation;')[0],n
 old=load(OUT/'original/data/layouts/layouts.json');new=load(ROOT/'data/layouts/layouts.json');ids={load(ROOT/f'data/maps/{n}/map.json')['layout'] for n in TARGETS};assert len(old['layouts'])==len(new['layouts'])
 for a,z in zip(old['layouts'],new['layouts']):
  if a['id'] not in ids:assert a==z,a['id']
  else:assert {k:v for k,v in a.items() if k not in ['primary_tileset','secondary_tileset','blockdata_filepath','border_filepath']}=={k:v for k,v in z.items() if k not in ['primary_tileset','secondary_tileset','blockdata_filepath','border_filepath']}
 result={'passed':True,'protected_files_checked':len(b),'maps_replaced':3,'construction_scientists_added':6,'canonical_map_ids_unchanged':True,'native_event_script_flags_items_warps_connections_save_ownership_preserved':True,'bwa_swsh_imports_byte_identical':True,'hyper_gameplay_imported':False,'runtime_verified':False};dump(OUT/'validation.json',result);print(json.dumps(result,indent=2));return result
def audit_and_report():
 r=load(OUT/'receipt.json');ledger=load(OUT/'coordinate_remap_ledger.json');ls=load(ROOT/'data/layouts/layouts.json')['layouts'];active={f.parent.name for f in (ROOT/'data/maps').glob('*/map.json') if next(l for l in ls if l['id']==load(f)['layout'])['primary_tileset'].startswith('gTileset_Hyper_')}
 inventory=load(ROOT/'.la_work/amap/hyper_hoenn_canary4/hyper_extra_location_inventory.json');rows=inventory['extra_entrances_from_canonical_hoenn']
 for row in rows:
  gates=[g for g in ledger['construction_gates'] if g['map']==row['canonical_source'] and g['reserved_donor_id']==row['destination_donor_id']]
  if gates:
   row['status']='ENTRANCE_RESERVED_BLOCKED_NO_WARP' if row['entrance_kind']=='WARP' else 'CONNECTION_RESERVED_ABSENT_WITH_SCIENTISTS'
   row['scientist_coordinates']=[[g['scientist']['x'],g['scientist']['y']] for g in gates]
   row['boundary_policy']='Canonical connection remains absent, including water portion; scientists cover paired Dewford land mouths or reachable Route106 shore notice.' if row['entrance_kind']=='CONNECTION' else 'Scientist occupies source extra warp cell; donor warp not imported.'
 pending=[z for z in rows if z['canonical_source'] in active and 'RESERVED' not in z['status']];assert not pending,pending
 inventory.update(active_canonical_hyper_maps=sorted(active),pending_extra_entrances_from_active_maps=pending,reserved_entrances_from_active_maps=sum(z['canonical_source'] in active and 'RESERVED' in z['status'] for z in rows),construction_scientists_total=26,scope='All exported extra warps and connections from the 54 activated canonical maps audited. Future Hoenn entrances remain queued; not every unassigned donor map is Hoenn.')
 dump(OUT/'hyper_extra_location_inventory.json',inventory)
 fields=['canonical_source','source_donor_id','entrance_kind','source_warp_index','entrance_x','entrance_y','destination_donor_id','destination_name','status','scientist_coordinates']
 with (OUT/'hyper_extra_location_inventory.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
 family=[]
 for k in ['34.68','34.69','34.71','34.73','35.6']:
  d,rel=C.P.C.donor(k);folder=ROOT/Path(rel).parent
  family.append({'donor_id':k,'name':d['name'],'dimensions':[d['width'],d['height']],'source_json':rel,'header_pointer':d['header_pointer'],'layout_pointer':d['layout_pointer'],'tileset_pair':[d['primary_tileset'],d['secondary_tileset']],'blockdata_sha256':digest(folder/'blockdata.bin'),'border_sha256':digest(folder/'border.bin'),'event_counts_reference_only':d['event_counts'],'warps_reference_only':d['warps'],'connections_reference_only':d['connections'],'status':'SOURCE_GEOMETRY_PRESERVED_FOR_LATER; ENTRANCE_RESERVED; NO_CANONICAL_REGISTRATION_OR_GAMEPLAY_IMPORT'})
 dump(OUT/'reserved_special_area_families.json',{'maps':family,'note':'34.68 is the western Dewford extension, not canonical Route106 (0.21); extra Granite Cave 34.69/34.71/34.73 is distinct from canonical 24.7–24.10. Champion Island downstream destinations retained in source metadata only.'})
 maps=[]
 for n,k in TARGETS.items():
  m=load(ROOT/f'data/maps/{n}/map.json');d,_=C.P.C.donor(k);l=next(z for z in ls if z['id']==m['layout'])
  maps.append({'canonical_name':n,'canonical_id':m['id'],'donor_identity':'HYPER_EMERALD_V5_7_EN_QOL','donor_id':k,'donor_name':d['name'],'donor_header_pointer':d['header_pointer'],'donor_layout_pointer':d['layout_pointer'],'dimensions':[l['width'],l['height']],'map_type':m['map_type'],'tilesets':[l['primary_tileset'],l['secondary_tileset']],'layout':l,'blockdata_sha256':digest(ROOT/l['blockdata_filepath']),'border_sha256':digest(ROOT/l['border_filepath']),'event_counts':{kind:len(m[kind]) for kind in KINDS},'donor_event_counts_reference_only':d['event_counts'],'warps':m['warp_events'],'connections':m['connections'],'script_owner':n+'_MapScripts','confidence':'HIGH','runtime_verified':False})
 dump(OUT/'sea_corridor_correction_manifest.json',{'maps':maps,'hyper_gameplay_imported':False,'runtime_verified':False,'spine':['Route104','Route105','Route106','DewfordTown','Route107','Route108','Route109','SlateportCity','Route110','MauvilleCity'],'construction_gates':ledger['construction_gates'],'reserved_special_area_families':family,'extra_entrances_from_active_maps_pending':0})
 with (OUT/'coordinate_remap_ledger.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['map','kind','index','role','old_x','old_y','new_x','new_y','reason'])
  for e in ledger['events']:w.writerow([e['map'],e['kind'],e['index'],e['after'].get('script',e['after'].get('dest_map',e['after'].get('item'))),e['before']['x'],e['before']['y'],e['after']['x'],e['after']['y'],e['reason']])
 print('Extra entrance audit:',len(active),'active maps;',inventory['reserved_entrances_from_active_maps'],'reserved entrances;',len(pending),'pending in active areas.')

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--apply',action='store_true');a.add_argument('--validate',action='store_true');v=a.parse_args()
 if v.apply:apply()
 elif v.validate:validate();audit_and_report()
 else:prepare();print('Preflight passed; no canonical writes.')
