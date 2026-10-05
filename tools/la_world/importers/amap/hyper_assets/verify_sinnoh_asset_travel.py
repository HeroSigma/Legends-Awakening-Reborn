#!/usr/bin/env python3
"""Verify additive Sinnoh ownership, registration, project travel and write review artifacts."""
import collections,csv,json,re,struct,subprocess
from pathlib import Path
import hoenn_finalization as F
R=F.R;O=R/'.la_work/amap/hyper_sinnoh_asset_travel';D=R/'docs/la_world/hyper_sinnoh/asset_travel'
def run():
 rec=F.load(O/'receipt.json');manifest=F.load(O/'manifest.json');D.mkdir(parents=True,exist_ok=True)
 fixpath=R/'.la_work/amap/hyper_sinnoh_id_correction/receipt.json';fix=F.load(fixpath) if fixpath.exists() else None
 for f,h in rec['baseline'].items():
  expected=rec['changed_baseline_files'].get(f,{}).get('after',h)
  if fix:
   for changes in [fix['user_edits'],fix['changed_files']]:
    if f in changes:
     assert changes[f]['before']==expected,(f,'Correction chain');expected=changes[f]['after']
  assert (F.digest(R/f) if (R/f).exists() else None)==expected,('Baseline',f)
 if fix:
  for f,h in fix.get('added_files',{}).items():assert F.digest(R/f)==h,('Added asset-support file',f)
 for f,h in rec['new_files'].items():
  if fix and f in fix['changed_files']:
   assert fix['changed_files'][f]['before']==h,(f,'New-file correction chain');h=fix['changed_files'][f]['after']
  assert F.digest(R/f)==h,('New file',f)
 maps={p.parent.name:F.load(p) for p in (R/'data/maps').glob('*/map.json')};ids={m['id']:n for n,m in maps.items()};layouts={l['id']:l for l in F.load(R/'data/layouts/layouts.json')['layouts']};groups=F.load(R/'data/maps/map_groups.json');old=F.load(O/'original/data/maps/map_groups.json')
 assert groups['group_order'][:len(old['group_order'])]==old['group_order']
 for g in old['group_order']:assert groups[g][:len(old[g])]==old[g]
 oldlayouts=F.load(O/'original/data/layouts/layouts.json')['layouts'];assert list(layouts)[:len(oldlayouts)]==[l['id'] for l in oldlayouts]
 sections=F.load(R/'src/data/region_map/region_map_sections.json')['map_sections'];assert [s['id'] for s in sections[:len(rec['old_mapsec_ids'])]]==rec['old_mapsec_ids'];assert sections[218]['id']=='MAPSEC_NONE';assert len(sections)<253
 numeric={n:(gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])};assert all(a<127 and b<127 for a,b in numeric.values()),'Signed WarpData IDs and MAP_DYNAMIC sentinel'
 header=(R/'src/data/tilesets/headers.h').read_text();meta=(R/'src/data/tilesets/metatiles.h').read_text();cache={};scientists=[];edges={n:[] for n in maps};projecttravel=[]
 bridge=manifest['travel_bridge'];new=set(rec['new_maps'].values());allowed={'lock','faceplayer','msgbox','release','end','goto_if_eq','warp','waitstate'}
 for n,m in maps.items():
  if n in new:
   assert m.get('la_imported') and not m['coord_events'] and not m['bg_events'];assert len(m['object_events'])<256 and len(m['warp_events'])<256
   text=(R/f'data/maps/{n}/scripts.inc').read_text();assert text.startswith(n+'_MapScripts::\n\t.byte 0\n')
   for line in text.splitlines():
    if line.startswith('\t') and not line.lstrip().startswith('.'):
     cmd=line.strip().split()[0];assert cmd in allowed,(n,cmd)
     if cmd=='goto_if_eq':assert 'VAR_RESULT, NO,' in line
   assert not re.search(r'\b(setflag|clearflag|setvar|trainerbattle|giveitem|special|call|callstd)\b',text)
   for e in m['object_events']:
    assert e['graphics_id']=='OBJ_EVENT_GFX_SCIENTIST_1' and e['flag']=='0' and e['trainer_type']=='TRAINER_TYPE_NONE' and e['script'].startswith(n+'_EventScript_'),(n,e)
  for i,w in enumerate(m.get('warp_events',[])):
   if w['dest_map'] not in ids:continue
   dn=ids[w['dest_map']];dest=maps[dn];assert 0<=int(w['dest_warp_id'])<len(dest['warp_events'])
   # The Oreburgh street arrival is deliberately inert; its return is an explicit scientist.
   if n==bridge['destination'] and [w['x'],w['y']]==bridge['destination_cell']:continue
   edges[n].append(dn)
  edges[n]+=[ids[c['map']] for c in m.get('connections') or [] if c['map'] in ids]
  text=(R/f'data/maps/{n}/scripts.inc').read_text() if (R/f'data/maps/{n}/scripts.inc').exists() else ''
  for target in re.findall(r'^\s*warp\s+(MAP_\w+)',text,re.M):
   if target in ids:edges[n].append(ids[target]);projecttravel.append({'source':n,'destination':ids[target]})
  if n in new or n.startswith('HyperHoenn_'):
   occupied=[]
   for e in m.get('object_events',[]):
    if e['graphics_id']!='OBJ_EVENT_GFX_SCIENTIST_1':continue
    if m['layout'] not in cache:cache[m['layout']]=F.grid(layouts[m['layout']],header,meta)
    g=cache[m['layout']];assert 0<=e['x']<g.w and 0<=e['y']<g.h;v=g.cell(e['x'],e['y']);assert v['collision']==0 or v['translated_behavior'] in range(0x60,0x70),(n,e,v)
    cell=(e['x'],e['y']);assert cell not in occupied,(n,'Duplicate scientist',cell);occupied.append(cell)
    scientists.append({'map':n,'x':e['x'],'y':e['y'],'script':e['script'],'on_warp':any((w['x'],w['y'])==cell for w in m['warp_events']),'cell':v})
 def reach(start,graph):
  seen=set(start);todo=list(start)
  while todo:
   for n in graph[todo.pop()]:
    if n not in seen:seen.add(n);todo.append(n)
  return seen
 root='SootopolisCity_MysteryEventsHouse_1F';reached=reach([root],edges);assert new<=reached,('No ingress',sorted(new-reached))
 reverse={n:[] for n in maps}
 for n,targets in edges.items():
  for t in targets:reverse[t].append(n)
 returned=reach([root],reverse);assert new<=returned,('No project return',sorted(new-returned))
 # Native story prefix and all native Mystery Events actors, old warps and coordinate events are exact.
 home=maps[root];before=F.load(O/f'original/data/maps/{root}/map.json');prefix=(F.O/f'original/data/maps/{root}/scripts.inc').read_text();assert (R/f'data/maps/{root}/scripts.inc').read_text().startswith(prefix)
 for key in ['warp_events','coord_events','bg_events','connections']:assert home[key]==before[key],key
 native=lambda m:[e for e in m['object_events'] if 'HyperAnnexConstruction' not in e['script']]
 assert native(home)==native(before)
 raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(R/'pokeemerald-sinnoh-assets.elf')],text=True);symbols={x[2]:int(x[0],16) for line in raw.splitlines() if len(x:=line.split())==3};rom=(R/'pokeemerald-sinnoh-assets.gba').read_bytes();p=symbols['sHyperSinnohMapNames']-0x08000000
 table_sizes=subprocess.check_output(['arm-none-eabi-nm','-S',str(R/'pokeemerald-sinnoh-assets.elf')],text=True);size=int(next(l.split()[1] for l in table_sizes.splitlines() if l.endswith(' sHyperSinnohMapNames')),16);count=sum(n.startswith('HyperSinnoh_') for n in rec['new_maps'].values());stride=size//count;assert stride in [34,36] and size%count==0
 popup=[]
 for k,n in sorted(rec['new_maps'].items()):
  if not n.startswith('HyperSinnoh_'):continue
  a,b=numeric[n];value=struct.unpack_from('<H',rom,p)[0];assert value==b+(a<<8),(n,'popup map identity');popup.append(n);p+=stride
 result={'passed':True,'new_maps':len(new),'new_sinnoh_maps':len(popup),'reused_sinnoh_maps':1,'new_hoenn_alias_maps':len(new)-len(popup),'structurally_reachable_new_maps':len(new & reached),'new_maps_with_project_return':len(new & returned),'arrival_only_excluded_from_return_graph':True,'scientists_checked':len(scientists),'protected_baseline_files':len(rec['baseline']),'native_map_ids_and_save_abi_preserved':True,'native_mystery_story_preserved':True,'donor_gameplay_imported':False,'map_groups':len(groups['group_order']),'map_sections':len(sections),'rom_validation':F.load(F.O/'validation.json'),'runtime_verified':False}
 F.dump(O/'validation.json',result);F.dump(O/'construction_audit.json',{'result':result,'scientists':scientists,'project_script_travel':projecttravel,'scope':'Structural registration/return graph; construction gates intentionally restrict player access. Physical pathfinding and all entrances require runtime review.'})
 def csvwrite(name,rows):
  fields=list(dict.fromkeys(k for row in rows for k in row))
  with (D/name).open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,sort_keys=True) if isinstance(v,(dict,list)) else v for k,v in row.items()} for row in rows)
 inventory=[]
 for z in manifest['maps']:
  md=z['metadata'];m=maps[z['map']];l=layouts[m['layout']];a,b=numeric[z['map']]
  row={k:v for k,v in z.items() if k!='metadata'};row['group']=groups['group_order'][a];z['group']=row['group'];row.update(project_map_id=m['id'],project_group_id=a,project_map_number=b,header_pointer=md.get('header_pointer'),layout_pointer=md.get('layout_pointer'),scripts_pointer=md.get('scripts_pointer'),source_map_scripts=md.get('map_scripts',[]),source_event_counts=md.get('event_counts',{}),source_objects=len(md.get('npcs',[])),source_warps=len(md.get('warps',[])),source_coords=len(md.get('coord_events',[])),source_bg=len(md.get('bg_events',[])),source_connections=len(md.get('connections',[])),project_objects=len(m['object_events']),project_warps=len(m['warp_events']),project_connections=len(m.get('connections') or []),relationships=sorted(set(edges[z['map']])),project_blockdata_sha256=F.digest(R/l['blockdata_filepath']),scope='HOENN_SPECIAL_ALIAS' if z['map'].startswith('HyperHoenn_') else 'SINNOH_ADDITIVE')
  inventory.append(row)
  z['relationships']=row['relationships'];z['project_map_id']=m['id'];z['project_group_id']=a;z['project_map_number']=b
 csvwrite('full_inventory.csv',inventory);csvwrite('high_confidence_mapping.csv',[z for z in inventory if z['confidence']=='HIGH']);csvwrite('regional_spine.csv',[z for z in inventory if z['donor_id'].startswith('36.') and int(z['donor_id'].split('.')[1])<=42])
 manual=[dict(p,review_kind='INVALID_SOURCE_TILE') for p in manifest['geometry_patches'] if p.get('manual_review')]+[dict(r,review_kind='SOURCE_TRAVEL_REFERENCE') for r in manifest['deferred_references']]
 csvwrite('manual_review.csv',manual);csvwrite('excluded_legacy.csv',[{'donor_id':k,'reason':v,'import_flag':False} for k,v in manifest['quarantined_sources'].items()]);csvwrite('construction_areas.csv',scientists)
 for name,obj in [('manifest.json',manifest),('validation.json',result),('construction_audit.json',F.load(O/'construction_audit.json'))]:F.dump(D/name,obj)
 F.dump(D/'all_construction_gate_audit.json',F.load(F.O/'construction_audit.json'))
 print(json.dumps(result,indent=2))
if __name__=='__main__':run()
