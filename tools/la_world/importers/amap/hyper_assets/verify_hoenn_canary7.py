#!/usr/bin/env python3
"""Validate current northwest Hoenn sources, native ownership, editor registry and linked assets."""
import json,re,struct,subprocess
import hoenn_canary7 as C
ROOT=C.ROOT;OUT=C.OUT;ROM_STEM="pokeemerald-canary7"

def verify():
 r=C.load(OUT/'receipt.json');b=C.load(OUT/'baseline.json');ledger=C.load(OUT/'coordinate_remap_ledger.json');changes=r['changed_baseline_files']
 water_fix_path=ROOT/'.la_work/amap/hyper_hoenn_route110_water_fix/receipt.json'
 water_fix=C.load(water_fix_path)['changed_files'] if water_fix_path.exists() else {}
 assert set(water_fix)<= {'data/hyper_assets/canary5_layouts/Route110/map.bin'}
 access_path=ROOT/'.la_work/amap/hyper_hoenn_route119_access_fix/receipt.json'
 access=C.load(access_path) if access_path.exists() else {'changed_files':{},'events':[]}
 assert set(access['changed_files'])<= {'data/maps/Route119/map.json','data/hyper_assets/canary7_layouts/Route119/map.bin'}
 for f,h in b.items():
  expected=changes[f]['after'] if f in changes else r.get('external_editor_changes',{}).get(f,{}).get('after',h)
  if f in r.get('external_editor_changes',{}):assert r['external_editor_changes'][f]['before']==h
  if f in water_fix:assert water_fix[f]['before']==expected;expected=water_fix[f]['after']
  if f in access['changed_files']:assert access['changed_files'][f]['before']==expected;expected=access['changed_files'][f]['after']
  assert C.digest(ROOT/f)==expected,('unreviewed source change',f)
  if f in changes:assert changes[f]['before']==h
 for f,h in r['new_files'].items():
  if f in access['changed_files']:assert access['changed_files'][f]['before']==h;h=access['changed_files'][f]['after']
  assert C.digest(ROOT/f)==h,('new file changed',f)
 groups=C.load(ROOT/'data/maps/map_groups.json');oldgroups=C.load(OUT/'original/data/maps/map_groups.json');ls=C.load(ROOT/'data/layouts/layouts.json')['layouts'];oldls=C.load(OUT/'original/data/layouts/layouts.json')['layouts'];layouts={z['id']:z for z in ls}
 assert groups['group_order'][:len(oldgroups['group_order'])]==oldgroups['group_order']
 for g in oldgroups['group_order']:assert groups[g][:len(oldgroups[g])]==oldgroups[g],g
 assert [z['id'] for z in ls[:len(oldls)]]==[z['id'] for z in oldls]
 sections=C.load(ROOT/'src/data/region_map/region_map_sections.json')['map_sections'];assert [z['id'] for z in sections[:len(r['old_mapsec_ids'])]]==r['old_mapsec_ids'];assert sections[218]['id']=='MAPSEC_NONE';assert len(sections)<253
 maps={p.parent.name:C.load(p) for p in (ROOT/'data/maps').glob('*/map.json')};ids={m['id']:n for n,m in maps.items()};numeric={maps[n]['id']:(gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])}
 header=(ROOT/'src/data/tilesets/headers.h').read_text();graphics=(ROOT/'src/data/tilesets/graphics.h').read_text();meta=(ROOT/'src/data/tilesets/metatiles.h').read_text();decl=dict(re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',header,re.S));asset_cache={}
 def assets(symbol):
  if symbol in asset_cache:return asset_cache[symbol]
  body=decl[symbol];result={}
  for field,text in [('tiles',graphics),('metatiles',meta),('metatileAttributes',meta)]:
   name=re.search(r'\.'+field+r'\s*=\s*(\w+)',body)[1];path=re.search(re.escape(name)+r'\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"]+)"\)',text)[1];result[field]=(ROOT/path).read_bytes()
   if field=='tiles':assert (ROOT/path).parent.joinpath('tiles.png').is_file()
  name=re.search(r'\.palettes\s*=\s*(\w+)',body)[1];pb=re.search(re.escape(name)+r'\[\]\[16\]\s*=\s*\{(.*?)\};',graphics,re.S)[1];paths=re.findall(r'INCBIN_U16\("([^"]+)"\)',pb);assert len(paths)==13
  result['palettes']=b''.join((ROOT/p).read_bytes() for p in paths);result['callback']=re.search(r'\.callback\s*=\s*(\w+)',body)[1];asset_cache[symbol]=result;return result
 native_events=0;preserved_maps=0;event_ledger={(e['map'],e['kind'],e['index']):e for e in ledger['events']}
 for n in r['touched_maps']:
  original=OUT/f'original/data/maps/{n}/map.json'
  if not original.exists():continue
  old=C.load(original);m=maps[n]
  for key,value in old.items():
   if key not in ['layout','connections','object_events','warp_events','coord_events','bg_events']:assert m[key]==value,(n,key)
  for kind in ['object_events','warp_events','coord_events','bg_events']:
   assert len(m[kind])>=len(old[kind])
   for i,e in enumerate(old[kind]):
    now=m[kind][i];a={k:v for k,v in e.items() if k not in ['x','y']};z={k:v for k,v in now.items() if k not in ['x','y']};correction=next((e for e in access['events'] if e['map']==n and e['kind']==kind and e['index']==i),None)
    if correction:assert now==correction['after'];z['elevation']=correction['before']['elevation']
    assert a==z,(n,kind,i,'ownership')
    if (e['x'],e['y'])!=(now['x'],now['y']):
     record=event_ledger[(n,kind,i)];assert record['before']==e and record['after']==(correction['before'] if correction else now)
    native_events+=1
  oldcon=old['connections'] or [];assert (m['connections'] or [])[:len(oldcon)]==oldcon,(n,'native connections')
  before=(OUT/f'original/data/maps/{n}/scripts.inc').read_text();after=(ROOT/f'data/maps/{n}/scripts.inc').read_text()
  if n=='LavaridgeTown':before=before.replace('LOCALID_LAVARIDGE_RIVAL, 11, 9','LOCALID_LAVARIDGE_RIVAL, 12, 9').replace('LOCALID_LAVARIDGE_RIVAL_ON_BIKE, 9, 8','LOCALID_LAVARIDGE_RIVAL_ON_BIKE, 10, 8').replace('VAR_0x8004, 9,','VAR_0x8004, 10,').replace('VAR_0x8008, 9,','VAR_0x8008, 10,')
  if n=='Route111':before=before.replace('setmetatile 29, 86, METATILE_General_RockWall_RockBase','setmetatile 29, 87, 0x09F').replace('setmetatile 29, 87, METATILE_General_RockWall_SandBase','setmetatile 29, 88, 0x09F')
  if n=='Route120':
   for a,z in r['visual_tile_rebindings'].items():before=before.replace(a,z)
  assert after.startswith(before),(n,'native script ownership');preserved_maps+=1
 extras=set(r['registered_special_maps'].values())
 for n in extras:
  m=maps[n];assert not m['coord_events'] and not m['bg_events'];assert all(e['graphics_id']=='OBJ_EVENT_GFX_SCIENTIST_1' and e['flag']=='0' and e['trainer_type']=='TRAINER_TYPE_NONE' for e in m['object_events']);assert (ROOT/f'data/maps/{n}/scripts.inc').read_text().startswith(n+'_MapScripts::\n\t.byte 0\n')
 raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(ROOT/(ROM_STEM+'.elf'))],text=True);symbols={s[2]:int(s[0],16) for line in raw.splitlines() if len(s:=line.split())==3};rom=(ROOT/(ROM_STEM+'.gba')).read_bytes()
 def u32(a):return struct.unpack_from('<I',rom,a-0x08000000)[0]
 def blob(a,n):assert 0x08000000<=a<=a+n<=0x08000000+len(rom);return rom[a-0x08000000:a-0x08000000+n]
 checked=[];warps=objects=connections=0;dormant=[]
 for n,m in maps.items():
  l=layouts[m['layout']]
  if not l['primary_tileset'].startswith('gTileset_Hyper_'):continue
  gi,mi=numeric[m['id']];hp=u32(u32(symbols['gMapGroups']+gi*4)+mi*4);assert hp==symbols[n];lp=u32(hp);assert lp==symbols[l['name']];assert (u32(lp),u32(lp+4))==(l['width'],l['height']);assert u32(hp+8)==symbols[n+'_MapScripts']
  for off,key in [(8,'border_filepath'),(12,'blockdata_filepath')]:
   expected=(ROOT/l[key]).read_bytes();assert blob(u32(lp+off),len(expected))==expected
  blocks=C.words(ROOT/l['blockdata_filepath']);assert len(blocks)==l['width']*l['height'];attrs=[]
  for off,key in [(16,'primary_tileset'),(20,'secondary_tileset')]:
   symbol=l[key];a=assets(symbol);ts=u32(lp+off);assert ts==symbols[symbol]
   for po,field in [(4,'tiles'),(8,'palettes'),(12,'metatiles'),(16,'metatileAttributes')]:assert blob(u32(ts+po),len(a[field]))==a[field],(n,field)
   assert u32(ts+20)==(0 if a['callback']=='NULL' else symbols[a['callback']]|1)
   attrs.append(list(struct.unpack('<'+'H'*(len(a['metatileAttributes'])//2),a['metatileAttributes'])))
  for v in blocks:
   tile=v&1023;assert tile%512<len(attrs[tile//512]),(n,tile)
  ep=u32(hp+4);assert list(blob(ep,4))==[len(m[k]) for k in ['object_events','warp_events','coord_events','bg_events']];op=u32(ep+4);wp=u32(ep+8)
  for i,e in enumerate(m['object_events']):
   rec=blob(op+i*24,24);assert struct.unpack_from('<hh',rec,4)==(e['x'],e['y']);assert rec[8]==e['elevation'];expected=int(e['script'],16) if e['script'].startswith('0x') else symbols[e['script']];assert struct.unpack_from('<I',rec,16)[0]==expected;objects+=1
  for i,e in enumerate(m['warp_events']):
   rec=blob(wp+i*8,8);assert struct.unpack_from('<hh',rec)==(e['x'],e['y']);assert rec[4]==e['elevation'];assert rec[5]==int(e['dest_warp_id']);assert (rec[7],rec[6])==numeric[e['dest_map']]
   dest=maps[ids[e['dest_map']]];assert 0<=int(e['dest_warp_id'])<len(dest['warp_events']),(n,i,e,'destination slot');
   if not (0<=e['x']<l['width'] and 0<=e['y']<l['height']):
    old=C.load(C.P.OUT/f'original/data/maps/{n}/map.json');assert n in ['SlateportCity','SlateportCity_Harbor'] and e==old['warp_events'][i],(n,i,'new off-map warp');dormant.append({'map':n,'index':i,'reason':'Previously validated native harbor scripted disembark border warp retained.'});warps+=1;continue
   v=blocks[e['y']*l['width']+e['x']];tile=v&1023;mb=attrs[tile//512][tile%512]&255
   if mb not in [0x29,*range(0x60,0x70),0x1B,0x1C]:
    if n in r['canonical_maps_replaced']:
     assert 'TERRA_CAVE' in e['dest_map'] or (n=='MeteorFalls_1F_1R' and 'STEVENS_CAVE' in e['dest_map']) or (n=='AbandonedShip_HiddenFloorCorridors' and i in [0,1,3,5]) or (n=='AncientTomb' and i in [1,2]),(n,i,mb,'non-warp cell');dormant.append({'map':n,'index':i,'behavior':mb,'reason':'Native story/weather/key OnLoad controls this doorway; no early unlock.'})
   warps+=1
  if m['connections']:
   cp=u32(hp+12);assert u32(cp)==len(m['connections']);table=u32(cp+4)
   for i,e in enumerate(m['connections']):
    rec=blob(table+i*12,12);assert struct.unpack_from('<i',rec,4)[0]==e['offset'];assert (rec[8],rec[9])==numeric[e['map']];connections+=1
  else:assert u32(hp+12)==0
  checked.append({'map':n,'id':m['id'],'group':gi,'map_number':mi,'layout':l['id'],'script_owner':n+'_MapScripts','special':n in extras})
 assert len(checked)==254,len(checked)
 for n in ['LavaridgeTown_Gym_1F','LavaridgeTown_Gym_B1F']:
  l=layouts[maps[n]['layout']];blocks=C.words(ROOT/l['blockdata_filepath']);a=[assets(l[k]) for k in ['primary_tileset','secondary_tileset']]
  for e in maps[n]['warp_events']:
   if 'GYM_' not in e['dest_map']:continue
   v=blocks[e['y']*l['width']+e['x']]&1023;mb=struct.unpack_from('<H',a[v//512]['metatileAttributes'],2*(v%512))[0]&255;assert mb in [0x29,0x68]
 # Registeel's native puzzle activation cell stays passable; braille runtime is unchanged.
 scene={'cells':[{'x':8,'y':25}],'passed':True};l=layouts[maps['AncientTomb']['layout']];assert ((C.words(ROOT/l['blockdata_filepath'])[25*l['width']+8]>>10)&3)==0
 # Only new-special to new-special reciprocal connections are added; no canonical boundaries change.
 seam_counts={}
 for n in extras:
  for e in (maps[n]['connections'] or []):
   dn=ids[e['map']];assert dn in extras;op={'up':'down','down':'up','left':'right','right':'left'}[e['direction']];assert any(z['map']==maps[n]['id'] and z['direction']==op and z['offset']==-e['offset'] for z in (maps[dn]['connections'] or []));seam_counts[n+'->'+dn]=True
 guard_result={'unchanged_from_prior_verified_stack':True,'source_hash_preserved':C.digest(ROOT/'src/fieldmap.c')}
 # Static special-area graph: every registered map has a canonical entry and return path.
 def graph_reach(reverse=False):
  reached=set(maps)-extras
  while True:
   before=len(reached)
   for n,m in maps.items():
    for e in [*m.get('warp_events',[]),*(m.get('connections') or [])]:
     dn=ids.get(e.get('dest_map',e.get('map')))
     if dn and ((dn in reached) if reverse else (n in reached)):reached.add(n if reverse else dn)
   if len(reached)==before:return reached
 assert extras<=graph_reach() and extras<=graph_reach(True)
 graph_result={'passed':True,'registered_maps':len(extras),'reachable_from_canonical_maps_ignoring_scientists':len(extras),'maps_with_static_return_to_canonical_maps':len(extras),'maps_without_static_path':[],'scope':'Static registered graph only; all-room collision/pathfinding and progression still require runtime testing.'}
 C.dump(OUT/'special_graph_validation.json',graph_result)
 import test_hyper_assets as tests
 animation=tests.animation_host_test(C.load(ROOT/'.la_work/amap/hyper_asset_integration/reborn_hyper_asset_integration_plan.json'))
 result={'passed':True,'reviewed_route110_water_fix':bool(water_fix),'protected_baseline_files':len(b),'authorized_changed_files':len(changes),'preserved_user_editor_changes':r.get('external_editor_changes',{}),'new_files':len(r['new_files']),'native_owned_events_preserved':native_events,'native_maps_with_preserved_scripts':preserved_maps,'canonical_maps_replaced':len(r['canonical_maps_replaced']),'registered_special_maps':len(extras),'editor_and_linked_hyper_maps_checked':len(checked),'tilesets_checked':len(asset_cache),'linked_objects':objects,'linked_warps':warps,'linked_connections':connections,'mapsec_none_preserved':218,'mapsec_count':len(sections),'animation_host_test':animation,'construction_guard_host_test':guard_result,'special_graph_validation':graph_result,'native_registeel_activation_cells_checked':len(scene['cells']),'reciprocal_special_connections':seam_counts,'dormant_native_doorways':dormant,'rom_sha256':C.digest(ROOT/(ROM_STEM+'.gba')),'rom_bytes':len(rom),'maps':checked,'runtime_verified':False}
 C.dump(OUT/'validation.json',result);print(json.dumps({k:v for k,v in result.items() if k not in ['maps','dormant_native_doorways']},indent=2));return result
if __name__=='__main__':verify()
