import argparse, collections, csv, hashlib, json, re, struct, subprocess
from pathlib import Path
SCHEMA='hyper-hoenn-replacement-plan-v1'
TYPE_NAMES={1:'MAP_TYPE_TOWN',2:'MAP_TYPE_CITY',3:'MAP_TYPE_ROUTE',4:'MAP_TYPE_UNDERGROUND',5:'MAP_TYPE_UNDERWATER',6:'MAP_TYPE_OCEAN_ROUTE',8:'MAP_TYPE_INDOOR',9:'MAP_TYPE_SECRET_BASE'}
EVENT_KEYS={'object':'object_events','warp':'warp_events','coord':'coord_events','bg':'bg_events'}
DONOR_KEYS={'object':'npcs','warp':'warps','coord':'coord_events','bg':'bg_events'}
REPURPOSED={'26.58':'Birth Island exterior is labeled Outer Space and enlarged; unsuitable replacement.', '26.59':'Birth Island harbor is labeled Champion Island; preserve ticket/puzzle routing.', '26.67':'Navel Rock harbor is labeled Canalave City; cross-region repurpose is outside this task.'}
KEEP_TERMS=('SecretBase_', 'BattleFrontier_', 'BattlePyramid', 'ContestHall', 'TradeCenter', 'RecordCorner', 'BattleColosseum', 'UnionRoom', 'TrainerHill', 'SSTidal', 'Prototype', 'Unused')
RISK_TERMS=('Gym','EverGrande','Littleroot','Route101','Route103','Petalburg','Rustboro','Dewford','Slateport','Mauville','Verdanturf','Fallarbor','Lavaridge','Fortree','Lilycove','Mossdeep','Sootopolis','Route104','Route110','Route111','Route112','Route114','Route116','Route118','Route119','Route120','Route121','Route122','Route123','Route128','MtChimney','MtPyre','MeteorFalls','Aqua','Magma','Seafloor','CaveOfOrigin','SkyPillar','WeatherInstitute','SpaceCenter','InsideOfTruck','Underwater','SouthernIsland','FarawayIsland','BirthIsland','NavelRock','SealedChamber','DesertRuins','IslandCave','AncientTomb','MarineCave','TerraCave','SafariZone')
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha(p):return sha_bytes(p.read_bytes()) if p.exists() else None
def read(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def words(p):
 b=p.read_bytes();assert len(b)%2==0,f'Odd u16 file: {p}'
 return list(struct.unpack('<'+'H'*(len(b)//2),b))
def integer(v,defines=None):
 try:return int(str(v),0)
 except ValueError:return (defines or {}).get(v)
def snapshot(root,donor):
 result={}
 for base in [root/'data',root/'src',root/'include',donor]:
  for p in sorted(base.rglob('*')):
   if p.is_file():result[str(p.relative_to(root)) if p.is_relative_to(root) else str(p)]=sha(p)
 return result

def tileset_catalog(root):
 headers=(root/'src/data/tilesets/headers.h').read_text();defs=(root/'src/data/tilesets/metatiles.h').read_text()
 inc={s:root/p for s,p in re.findall(r'const u16\s+(\w+)\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',defs)};result={}
 for name,body in re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',headers,re.S):
  a=re.search(r'\.metatileAttributes\s*=\s*(\w+)',body);m=re.search(r'\.metatiles\s*=\s*(\w+)',body);cb=re.search(r'\.callback\s*=\s*(\w+)',body)
  if a and a[1] in inc:result[name]={'attributes':words(inc[a[1]]),'attributes_path':str(inc[a[1]].relative_to(root)), 'attributes_sha256':sha(inc[a[1]]),'metatiles_sha256':sha(inc[m[1]]) if m and m[1] in inc else None,'callback':cb[1] if cb else None}
 return result

def behavior_names(root):
 body=(root/'include/constants/metatile_behaviors.h').read_text();body=re.sub(r'/\*.*?\*/|//[^\n]*','',body,flags=re.S);result={};value=0
 for name,assignment in re.findall(r'\b(MB_\w+)\s*(?:=\s*([^,}\n]+))?\s*[,}]',body):
  if assignment:
   try:value=int(assignment.strip(),0)
   except ValueError:continue
  result[value]=name;value+=1
 return result

def source_behavior(value,tileset,index,collision,names):
 if value in (0x1f,0x2d):
  if tileset.endswith('083DF77C') and index=={0x1f:509,0x2d:508}[value] and collision==1:return 'MB_NORMAL'
  return f'UNRESOLVED_HYPER_0x{value:02X}'
 return names.get(value,f'UNRESOLVED_HYPER_0x{value:02X}')

def script_inventory(path):
 text=path.read_text() if path.exists() else '';commands=[]
 watch=('setobjectxy','setobjectxyperm','setmetatile','setmetatileattribute','applymovement','waitmovement','warp','warpsilent','warpdoor','warphole','warpteleport','setwarp','setdynamicwarp','setescapewarp','setrespawn','special','specialvar','callnative','setvar','setflag','clearflag','map_script','map_script_2')
 for i,line in enumerate(text.splitlines(),1):
  s=line.strip()
  if s.split(' ',1)[0].split('\t',1)[0] in watch:commands.append({'line':i,'command':s})
 return {'path':str(path),'sha256':sha(path),'hooks':re.findall(r'^\s*map_script\s+(\w+)\s*,\s*(\w+)',text,re.M),'labels':re.findall(r'^(\w+):{1,2}',text,re.M),'flags':sorted(set(re.findall(r'\bFLAG_\w+',text))),'variables':sorted(set(re.findall(r'\bVAR_\w+',text))),'local_ids':sorted(set(re.findall(r'\bLOCALID_\w+',text))),'coordinate_movement_routing_and_abi_commands':commands,'policy':'PRESERVE_EXPANSION; audit full paths and hook order before geometry changes; never port numeric Hyper operands.'}

def canon_warp(x,slots,defines):
 dest=x['dest_map'];w=x['dest_warp_id']
 return [x['x'],x['y'],x.get('elevation',0),'DYNAMIC' if dest=='MAP_DYNAMIC' else slots.get(dest,f'EXTERNAL:{dest}'),'DYNAMIC' if str(w)=='WARP_ID_DYNAMIC' else integer(w,defines)]
def donor_warp(x):return [x['x'],x['y'],x.get('elevation',0),'DYNAMIC' if x.get('dynamic_target') else x['target_id'],'DYNAMIC' if x.get('dynamic_target') else x['dest_warp_id']]
def canon_conn(x,slots):return [x['direction'],int(x['offset']),slots.get(x['map'],f'EXTERNAL:{x["map"]}')]
def donor_conn(x):return [x['direction'],int(x['offset']),x['target_id']]

def story_role(name,category):
 if name=='InsideOfTruck':return 'Natural Emerald new-game truck opening, return/resume hooks and moving-box choreography.'
 if 'Littleroot' in name:return 'Opening family/home/clock/Birch lab state; preserve custom regional travel scientist where present.'
 if name=='Route101':return 'Birch rescue, starter battle and actor choreography.'
 if name=='Route103':return 'First rival battle, starter/Pokedex progression and return choreography.'
 if 'Oldale' in name:return 'Opening west-entrance gate and local healing/shopping/home services.'
 if name=='Route102':return 'Early trainer/berry/item corridor between Oldale and Petalburg.'
 if category=='GYM':return 'Badge/battle ownership, leader and trainers, field-move unlocks, puzzle and scripted tile state.'
 if 'EverGrande' in name:return 'Victory Road/League/Elite Four/Champion/Hall of Fame; healing, return and ending state.'
 if any(x in name for x in ('Aqua','Magma','Seafloor','MtChimney','MtPyre','MeteorFalls')):return 'Villain/legendary progression and field-move/transport/actor gates.'
 if any(x in name for x in ('Sootopolis','CaveOfOrigin','SkyPillar','SpaceCenter','WeatherInstitute')):return 'Weather/legendary or villain crisis progression; entry and completion state.'
 if category=='UNDERWATER':return 'Dive/emerge paired destinations, underwater terrain and escape/return contracts.'
 if category=='SYSTEM_FACILITY':return 'Facility/link/dynamic objects/GFX/minigame/save/return contracts; hold originals during first cutover.'
 if category=='PROTOTYPE_UNUSED':return 'Prototype or unused baseline room; retain original pending deliberate activation decision.'
 if category=='WORLD':return 'Canonical regional travel spine with local flags, trainers, encounters, rewards and healing/Fly/blackout consumers.'
 if category=='DUNGEON':return 'Dungeon traversal, encounters/items/trainers, field moves, exits and escape/blackout contracts.'
 return 'Current expansion room interactions and local story/service state; inspect retained flags/variables/script roots.'

def csv_write(path,rows):
 fields=['canonical_name','canonical_id','canonical_group_map','hyper_id','donor_name','category','confidence','replacement_mode','canonical_flag','import_flag','story_risk','canonical_dimensions','donor_dimensions','canonical_type','donor_type','canonical_tilesets','donor_tilesets','canonical_event_counts','donor_event_counts','geometry_compatibility','event_coordinate_compatibility','warp_compatibility','connection_compatibility','canonical_blockdata_sha256','donor_blockdata_sha256','header_pointer','layout_pointer','scripts_table_pointer','dependencies','reason']
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for r in rows:
   c=r['canonical'];d=r['hyper'];a=r['compatibility'];row={k:r.get(k,'') for k in fields}
   row.update(canonical_name=c['name'],canonical_id=c['id'],canonical_group_map=c['group_map'],hyper_id=d['id'],donor_name=d['name'],canonical_flag=True,import_flag=False,canonical_dimensions=c['dimensions'],donor_dimensions=d['dimensions'],canonical_type=c['map_type'],donor_type=d['map_type'],canonical_tilesets=c['tilesets'],donor_tilesets=d['tilesets'],canonical_event_counts=c['event_counts'],donor_event_counts=d['event_counts'],geometry_compatibility=a['geometry']['status'],event_coordinate_compatibility=a['events']['status'],warp_compatibility=a['warps']['status'],connection_compatibility=a['connections']['status'],canonical_blockdata_sha256=c['blockdata_sha256'],donor_blockdata_sha256=d['blockdata_sha256'],header_pointer=d['header_pointer'],layout_pointer=d['layout_pointer'],scripts_table_pointer=d['map_scripts'].get('table_pointer'),dependencies=r['dependencies'])
   w.writerow({k:json.dumps(v,separators=(',',':')) if isinstance(v,(dict,list)) else v for k,v in row.items()})

def build(root,donor,output,evidence_root):
 root=root.resolve();donor=donor.resolve();output=output.resolve()
 if any(output.is_relative_to(root/x) for x in ('data','src','include')) or output.is_relative_to(donor):raise ValueError('Reports must not enter gameplay/donor directories.')
 protected_before=snapshot(root,donor);groups=read(root/'data/maps/map_groups.json');group_names=groups['group_order'][:34]
 expected=[57,5,5,6,7,8,9,7,7,14,8,17,10,23,13,15,15,2,2,2,3,1,1,1,108,61,89,2,1,13,1,1,3,1]
 assert [len(groups[x]) for x in group_names]==expected,'Canonical Emerald group shape changed; review scope.'
 manifest=read(donor/'manifest.json');assert manifest['format']=='A-Map Batch Bridge v1.0'
 assert manifest['rom']['sha256']=='73d6faeb29bcc15e1627a6f237e99e11ddea8429ed31ec30057560ee069a546f','Different ROM: revalidate evidence.'
 ds={};donor_paths={}
 for p in sorted((donor/'maps').glob('*/map.json')):
  d=read(p);assert d['id'] not in ds;ds[d['id']]=d;donor_paths[d['id']]=p
 assert len(ds)==922 and manifest['scanner']['group_counts'][:34]==expected
 layouts={x['id']:x for x in read(root/'data/layouts/layouts.json')['layouts']};canonical=[];id_to_slot={};canon_by_slot={}
 for gi,gn in enumerate(group_names):
  for mi,name in enumerate(groups[gn]):
   p=root/'data/maps'/name/'map.json';c=read(p);slot=f'{gi}.{mi}';assert slot in ds
   canonical.append((gi,mi,name,c,p));id_to_slot[c['id']]=slot;canon_by_slot[slot]=c
 defines={}
 for p in (root/'include/constants').glob('*.h'):
  for name,value in re.findall(r'^#define\s+(\w+)\s+(0x[\da-fA-F]+|\d+)\b',p.read_text(errors='replace'),re.M):defines[name]=int(value,0)
 dst_tiles=tileset_catalog(root);dst_behaviors=behavior_names(root)
 source_catalog=evidence_root/'amap_behavior_translation_v0_1_2/hyper_behavior_source_catalog.json';assert source_catalog.exists(),'Recovered behavior catalog required.'
 source_names={x['source_id']:x['baseline_name'] for x in read(source_catalog)['behaviors']};dt={}
 for p in (donor/'tilesets').glob('*/tileset.json'):dt[p.parent.name]={'metadata':read(p),'attributes':words(p.parent/'metatile_attributes.bin'),'attributes_sha256':sha(p.parent/'metatile_attributes.bin'),'metatiles_sha256':sha(p.parent/'metatiles.bin')}
 refs=collections.defaultdict(list)
 for base in [root/'data',root/'src',root/'include']:
  for p in sorted(base.rglob('*')):
   if p.is_file() and p.suffix in ('.c','.h','.inc','.json'):
    for line_no,line in enumerate(p.read_text(errors='replace').splitlines(),1):
     for symbol in set(re.findall(r'\bMAP_[A-Z0-9_]+',line)) & id_to_slot.keys():refs[symbol].append({'file':str(p.relative_to(root)),'line':line_no,'text':line.strip()})
 heal=read(root/'src/data/heal_locations.json')['heal_locations'];wild=read(root/'src/data/wild_encounters.json');encounters=collections.defaultdict(list)
 def find_encounter(x):
  if isinstance(x,dict):
   if x.get('map') in id_to_slot and any(k in x for k in ('land_mons','water_mons','fishing_mons','rock_smash_mons')):encounters[x['map']].append(x)
   for v in x.values():find_encounter(v)
  elif isinstance(x,list):
   for v in x:find_encounter(v)
 find_encounter(wild);family=collections.defaultdict(list)
 for sid,d in ds.items():
  if d['group']<34:family[d['name']].append(sid)
 # A relocated Hoenn room exists outside the retained 34 groups. Verify actual
 # outdoor ownership and reciprocal indexed exits before selecting it.
 relocated={'15.9':'37.118'}
 assert next(w for w in ds['0.7']['warps'] if w['index']==8)['target_id']=='37.118'
 assert all(w['target_id']=='0.7' and w['dest_warp_id']==8 for w in ds['37.118']['warps'])
 supplemental_candidates={}
 for slot,c in canon_by_slot.items():
  base=ds[slot]; candidates=[]
  for candidate_id,v in ds.items():
   if v['group']>=34 and v['name']==base['name'] and v['map_type']==base['map_type']:
    candidates.append({'id':candidate_id,'name':v['name'],'dimensions':[v['width'],v['height']],'blockdata_sha256':v['blockdata_sha256'],'tilesets':[v['primary_tileset'],v['secondary_tileset']],'warps':v['warps'],'header_pointer':v['header_pointer'],'layout_pointer':v['layout_pointer'],'same_blockdata_as_retained_slot':v['blockdata_sha256']==base['blockdata_sha256'],'selected':relocated.get(slot)==candidate_id,'status':'SELECTED_RELOCATED_HOENN_ROOM' if relocated.get(slot)==candidate_id else 'ALTERNATIVE_REFERENCE_ONLY_NOT_AUTHORIZED'})
  if candidates:supplemental_candidates[slot]=candidates
 rows=[];event_ledger=[];warnings=[]
 for gi,mi,name,c,cp in canonical:
  slot=f'{gi}.{mi}';sid=relocated.get(slot,slot);d=ds[sid];dp=donor_paths[sid];l=layouts[c['layout']];cb=root/l['blockdata_filepath'];db=dp.parent/'blockdata.bin';cw=words(cb);dw=words(db)
  assert len(cw)==l['width']*l['height'] and len(dw)==d['width']*d['height'],sid
  assert sha(db)==d['blockdata_sha256'],f'Donor hash mismatch: {sid}'
  cc={k:len(c.get(v,[]) or []) for k,v in EVENT_KEYS.items()};dc={k:len(d.get(v,[]) or []) for k,v in DONOR_KEYS.items()};declared=d.get('event_counts',{});export_complete=dc==declared;invalid_header=all(v==255 for v in declared.values())
  same_dim=(l['width'],l['height'])==(d['width'],d['height']);same_type=c['map_type']==TYPE_NAMES.get(d['map_type'],str(d['map_type']))
  cwps=[canon_warp(x,id_to_slot,defines) for x in c.get('warp_events',[])];dwps=[donor_warp(x) for x in d['warps']]
  cconn=sorted(canon_conn(x,id_to_slot) for x in c.get('connections',[]) or []);dconn=sorted(donor_conn(x) for x in d['connections']);warp_equal=cwps==dwps;conn_equal=cconn==dconn
  cpair=[l['primary_tileset'],l['secondary_tileset']];dpair=[d['primary_tileset'],d['secondary_tileset']];semantic_unknown=set();behavior_changed=collision_changed=elevation_changed=block_changed=index_contract_changed=0
  def cell(w,pair,source):
   mt=w&1023;role=0 if mt<512 else 1;idx=mt if role==0 else mt-512;tile=pair[role];entry=dt[tile] if source else dst_tiles.get(tile)
   if entry is None or idx>=len(entry['attributes']):return {'metatile':mt,'collision':(w>>10)&3,'elevation':w>>12,'behavior':'UNRESOLVED_ATTRIBUTE'}
   attr=entry['attributes'][idx];v=attr&255;behavior=source_behavior(v,tile,idx,(w>>10)&3,source_names) if source else dst_behaviors.get(v,f'UNRESOLVED_DEST_0x{v:02X}')
   return {'metatile':mt,'collision':(w>>10)&3,'elevation':w>>12,'behavior':behavior,'attribute':attr,'layer':(attr>>12)&15}
  if same_dim:
   for a,b in zip(cw,dw):
    ca,da=cell(a,cpair,False),cell(b,dpair,True);behavior_changed+=ca['behavior']!=da['behavior'];collision_changed+=ca['collision']!=da['collision'];elevation_changed+=ca['elevation']!=da['elevation'];block_changed+=a!=b
    semantic_unknown.update(v['behavior'] for v in [ca,da] if v['behavior'].startswith('UNRESOLVED'))
   for w in set(cw):
    a,b=cell(w,cpair,False),cell(w,dpair,True);index_contract_changed+=(a['behavior'],a.get('layer'))!=(b['behavior'],b.get('layer'))
  else:
   for w in dw:
    v=cell(w,dpair,True)
    if v['behavior'].startswith('UNRESOLVED'):semantic_unknown.add(v['behavior'])
  mismatches=[];out_of_bounds=[];footprint_changes=[]
  for kind,key in EVENT_KEYS.items():
   for i,event in enumerate(c.get(key,[]) or []):
    x,y=event['x'],event['y'];inside=0<=x<d['width'] and 0<=y<d['height'];canonical_inside=0<=x<l['width'] and 0<=y<l['height']
    old=cell(cw[y*l['width']+x],cpair,False) if canonical_inside else None;new=cell(dw[y*d['width']+x],dpair,True) if inside else None
    local=integer(event.get('local_id',i+1),defines) if kind=='object' else None
    counterpart=next((v for v in d['npcs'] if v['local_id']==local),None) if kind=='object' else (d[DONOR_KEYS[kind]][i] if i<len(d[DONOR_KEYS[kind]]) else None)
    coord_same=bool(counterpart and (x,y,event.get('elevation',0))==(counterpart['x'],counterpart['y'],counterpart.get('elevation',0)))
    if not coord_same:mismatches.append({'kind':kind,'index':i,'local_id':local,'canonical_xy':[x,y],'donor_xy':[counterpart['x'],counterpart['y']] if counterpart else None})
    if not inside:out_of_bounds.append({'kind':kind,'index':i,'xy':[x,y]})
    changed=bool(old and new and any(old[k]!=new[k] for k in ('collision','elevation','behavior')))
    if changed:footprint_changes.append({'kind':kind,'index':i,'xy':[x,y],'canonical_cell':old,'donor_cell':new})
    event_ledger.append({'canonical_name':name,'canonical_id':c['id'],'hyper_id':sid,'kind':kind,'index':i,'canonical_event':event,'donor_candidate':counterpart,'same_coordinates':coord_same,'inside_donor_bounds':inside,'footprint_changed':changed,'canonical_cell':old,'donor_cell':new,'action':'PRESERVE_EXPANSION_EVENT; local-ID/index pairing is a comparison probe, NOT authority to merge donor NPC logic.'})
  scripts=script_inventory(cp.parent/'scripts.inc');sensitive=[v for v in scripts['coordinate_movement_routing_and_abi_commands'] if re.match(r'(setobjectxy|setmetatile|applymovement|warp|setdynamicwarp|setescapewarp)\b',v['command'])]
  story_high=any(t in name for t in RISK_TERMS) or (bool(c.get('coord_events')) and bool(sensitive));risk='HIGH' if story_high else ('SYSTEM' if any(t in name for t in KEEP_TERMS) else 'MODERATE' if sensitive or c.get('coord_events') else 'LOW')
  keep=any(t in name for t in KEEP_TERMS) or sid in REPURPOSED or invalid_header;confidence='HIGH';why=['Exact retained Emerald group/map slot; dimensions, map type and ordered routing independently compared.']
  if sid in REPURPOSED:confidence='NONE';why=[REPURPOSED[sid]]
  elif invalid_header:confidence='LOW';why=['Retained layout slot but all declared event counts are 255 and no events survived export; keep original pending source/header archaeology.']
  elif not export_complete:confidence='MEDIUM';why.append('Declared event counts exceed exported valid records; filtered/missing records require reconciliation.')
  elif not same_dim or not same_type:confidence='MEDIUM';why.append('Retained room slot but geometry or map type differs.')
  elif not warp_equal or not conn_equal:confidence='MEDIUM';why.append('Retained geographic/facility slot but doorway or boundary routing differs.')
  if name=='InsideOfTruck':why.append('25.40 is the truck, not a Littleroot overworld duplicate: indoor role, moving boxes and dynamic exits corroborate identity.')
  if gi in (1,16,25,26) or name.startswith('Underwater'):why.append('Repeated/generic donor label resolved by canonical slot, room geometry and explicit targets; name is not a unique key.')
  if keep:mode='KEEP_EXPANSION_ORIGINAL';why.append('Hold system/prototype/facility or repurposed destinations during first cutover.')
  elif not same_dim or not same_type or out_of_bounds or semantic_unknown or not export_complete:mode='MANUAL_REVIEW';why.append('Geometry/type/attribute uncertainty blocks automatic replacement.')
  elif story_high or sensitive or not warp_equal or not conn_equal:mode='FULL_RECONCILE';why.append('Preserve expansion story/hook/path ownership; reconcile before adopting source geometry.')
  elif mismatches or footprint_changes or behavior_changed or elevation_changed:mode='LAYOUT_REPLACEMENT';why.append('Layout adoption requires coordinate/terrain reconciliation; preserve expansion event payloads.')
  elif collision_changed:mode='VISUAL_PLUS_COLLISION';why.append('Validate altered collision and interaction reachability.')
  elif not block_changed and not index_contract_changed:mode='VISUAL_ONLY';why.append('Blocks and behavior/layer index contracts match; retain canonical collision/events/scripts while planning source art.')
  else:mode='LAYOUT_REPLACEMENT';why.append('Terrain aligns at corresponding cells; block/index changes require explicit layout migration.')
  if name.startswith('Underwater'):category='UNDERWATER'
  elif any(t in name for t in KEEP_TERMS):category='PROTOTYPE_UNUSED' if 'Prototype' in name or 'Unused' in name else 'SYSTEM_FACILITY'
  elif 'Gym' in name:category='GYM'
  elif gi==16:category='POKEMON_LEAGUE'
  elif gi==24:category='DUNGEON'
  elif gi==0:category='WORLD'
  elif gi==26:category='SPECIAL_AREA'
  else:category='INTERIOR'
  dependencies=set(x[3] for x in cwps if x[3]!='DYNAMIC')|set(x[2] for x in cconn);incoming=[]
  for oslot,oc in canon_by_slot.items():
   for i,w in enumerate(oc.get('warp_events',[]) or []):
    if w['dest_map']==c['id']:incoming.append({'canonical_source':oc['id'],'source_slot':oslot,'kind':'warp','index':i,'dest_warp_id':w['dest_warp_id']})
   for x in oc.get('connections',[]) or []:
    if x['map']==c['id']:incoming.append({'canonical_source':oc['id'],'source_slot':oslot,'kind':'connection','direction':x['direction'],'offset':x['offset']})
  geom_status='DIMENSIONS_DIFFER' if not same_dim else 'SAME_DIMENSIONS_TERRAIN_DIFFERS' if behavior_changed or collision_changed or elevation_changed else 'SAME_DIMENSIONS_TERRAIN_CONTRACT_MATCHES'
  event_status='OUT_OF_BOUNDS' if out_of_bounds else 'RECONCILE_COORDINATES_OR_FOOTPRINTS' if mismatches or footprint_changes else 'COORDINATES_MATCH_PATHS_UNVERIFIED' if sensitive else 'STATIC_COORDINATES_MATCH'
  static_candidate=mode in ('VISUAL_ONLY','VISUAL_PLUS_COLLISION','LAYOUT_REPLACEMENT') and confidence=='HIGH' and not any((mismatches,footprint_changes,behavior_changed,elevation_changed,collision_changed,index_contract_changed))
  cdata={'name':name,'id':c['id'],'group':gi,'map':mi,'group_map':slot,'map_group':group_names[gi],'map_json_path':str(cp.relative_to(root)),'map_json_sha256':sha(cp),'dimensions':[l['width'],l['height']],'map_type':c['map_type'],'layout':c['layout'],'layout_definition':l,'layout_definition_sha256':sha_bytes(json.dumps(l,sort_keys=True,separators=(',',':')).encode()),'blockdata_sha256':sha(cb),'border_sha256':sha(root/l['border_filepath']),'tilesets':cpair,'tileset_contracts':[{k:v for k,v in dst_tiles.get(t,{}).items() if k!='attributes'} for t in cpair],'event_counts':cc,'warp_events':c.get('warp_events',[]),'connections':c.get('connections'),'header_gameplay_fields':{k:v for k,v in c.items() if k not in ('object_events','warp_events','coord_events','bg_events','connections')},'script_inventory':scripts,'encounters':encounters[c['id']],'heal_locations':[x for x in heal if c['id'] in (x.get('map'),x.get('respawn_map'))]}
  hdata={'donor':'HYPER_EMERALD_V5_7_EN_QOL','rom_sha256':manifest['rom']['sha256'],'id':sid,'group':d['group'],'map':d['map'],'name':d['name'],'map_json_path':str(dp.relative_to(root)),'map_json_sha256':sha(dp),'dimensions':[d['width'],d['height']],'map_type':TYPE_NAMES.get(d['map_type'],str(d['map_type'])),'map_type_numeric':d['map_type'],'tilesets':dpair,'tileset_contracts':[{k:v for k,v in dt[t].items() if k!='attributes'} for t in dpair],'header_pointer':d['header_pointer'],'layout_pointer':d['layout_pointer'],'blockdata_pointer':d['blockdata_pointer'],'blockdata_sha256':sha(db),'border_sha256':sha(dp.parent/'border.bin'),'border_metadata':d['border'],'header_metadata':{k:d.get(k) for k in ('music','weather','layout_id','show_map_name','allow_cycling','allow_running','allow_escaping','battle_type')},'source_script_catalog_path':str(dp.parent/'scripts.json'),'source_script_catalog_sha256':sha(dp.parent/'scripts.json'),'visual_map_sha256':d.get('visual_map_sha256'),'event_counts':dc,'declared_event_counts':declared,'event_export_complete':export_complete,'invalid_event_header':invalid_header,'warps':d['warps'],'connections':d['connections'],'map_scripts':d['map_scripts'],'script_summary':d.get('script_summary'),'source_script_roots':read(dp.parent/'scripts.json').get('roots',[]),'object_graphics_summary':{'graphics_ids':sorted({v['graphics_id'] for v in d['npcs']}),'sprite_status_counts':dict(collections.Counter(v.get('sprite_status','unknown') for v in d['npcs'])),'not_static_import_safe_objects':[{'local_id':v['local_id'],'graphics_id':v['graphics_id'],'sprite_status':v.get('sprite_status'),'script_pointer':v.get('script_pointer')} for v in d['npcs'] if not v.get('sprite_project_import_safe',False)],'policy':'Preserve current expansion symbolic graphics IDs and dynamic GFX initialization; source resolved art is evidence only.'},'section_id':d['region_map_section_id'],'section_name':d['region_map_section_name'],'duplicate_name_family':family[d['name']]}
  compatibility={'geometry':{'status':geom_status,'dimensions_equal':same_dim,'map_type_equal':same_type,'raw_blocks_equal':cw==dw,'changed_block_cells':block_changed if same_dim else None,'collision_changed_cells':collision_changed if same_dim else None,'elevation_changed_cells':elevation_changed if same_dim else None,'semantic_behavior_changed_cells':behavior_changed if same_dim else None,'used_index_behavior_or_layer_changes':index_contract_changed if same_dim else None,'unknown_behaviors':sorted(semantic_unknown),'prior_hyper_asset_pipeline_proven':True,'canonical_replacement_runtime_verified':False},'events':{'status':event_status,'coordinate_mismatches':mismatches,'out_of_bounds':out_of_bounds,'terrain_footprint_changes':footprint_changes,'donor_additional_objects':dc['object']-cc['object'],'local_id_semantic_identity_verified':False,'movement_paths_verified':False},'warps':{'status':'EXACT_ORDERED_ENDPOINTS_MATCH' if warp_equal else 'RECONCILE_ENDPOINTS','canonical_normalized':cwps,'donor_normalized':dwps,'indexed_warp_ids_preserved':[(i,w[3],w[4]) for i,w in enumerate(cwps)]==[(event['index'],w[3],w[4]) for event,w in zip(d['warps'],dwps)]},'connections':{'status':'EXACT_TARGETS_OFFSETS_MATCH' if conn_equal else 'RECONCILE_TARGETS_OFFSETS','canonical_normalized':cconn,'donor_normalized':dconn}}
  rows.append({'canonical':cdata,'hyper':hdata,'category':category,'canonical_flag':True,'import_flag':False,'replacement_executed':False,'confidence':confidence,'replacement_mode':mode,'story_risk':risk,'story_importance':{'role':story_role(name,category),'critical_progression':story_high,'flags':scripts['flags'],'variables':scripts['variables'],'movement_or_coordinate_commands':len(sensitive),'services':'Preserve encounters, trainers/items/rewards, healing/Fly/blackout, escape/dynamic returns, save/transport; inspect global_reference_inventory.json.'},'candidate_resolution':{'retained_slot':slot,'retained_slot_name':ds[slot]['name'],'retained_slot_header_pointer':ds[slot]['header_pointer'],'retained_slot_blockdata_sha256':ds[slot]['blockdata_sha256'],'retained_slot_event_counts':ds[slot]['event_counts'],'supplemental_candidates':supplemental_candidates.get(slot,[]),'selection_evidence':'Hyper Sootopolis outdoor warp index 8 points to 37.118; both reciprocal doors return to outdoor warp 8; compare canonical House5 endpoints and geometry.' if slot in relocated else 'Retained Emerald room slot; supplemental candidates remain reference-only.'},'reason':' '.join(why),'compatibility':compatibility,'dependencies':sorted(dependencies),'relationships':{'incoming':incoming,'dynamic_return_contract_required':any(w[3]=='DYNAMIC' for w in cwps),'global_reference_count':len(refs[c['id']]),'global_reference_key':c['id']},'migration_policy':{'canonical_destination':c['id'],'canonical_name':name,'create_additive_map':False,'expansion_events':'PRESERVE' if static_candidate else 'PRESERVE_AND_REMAP_ONLY_WITH_REVIEWED_COORDINATE_LEDGER','expansion_scripts':'PRESERVE; reconcile movement/geometry operands only where proven necessary','hyper_scripts':'REFERENCE_ONLY_NEVER_BLIND_COPY','hyper_npcs':'REFERENCE_ONLY; additional objects excluded until deliberate design review','header_fields':'PRESERVE_EXPANSION_GAMEPLAY_SETTINGS','flags_variables_save':'PRESERVE_SYMBOLIC_OWNERSHIP_AND_SAVE_ABI','graphics_behaviors_animations':'Revalidate recovered assets and expansion semantic names; no raw callback pointers','replacement_permission':False},'readiness':{'static_visual_layout_candidate':static_candidate,'automatic_replacement_allowed':False,'runtime_validated':False,'next_action':'KEEP_ORIGINAL' if keep else 'PREPARE_ISOLATED_CANARY_PATCH_LATER' if static_candidate else 'REVIEW_EVENT_AND_ROUTING_LEDGER'}})
 assert len(rows)==518
 for r in rows:
  for w in r['hyper']['warps']:
   if not w.get('dynamic_target') and w['target_id'] not in ds:warnings.append({'map':r['hyper']['id'],'kind':'missing_donor_warp_target','target':w['target_id']})
 assert not warnings,warnings;output.mkdir(parents=True,exist_ok=True);evidence=[]
 paths=[evidence_root/'SPACE_BUNNY_ALPHA_AMAP_OFFICIAL_WORLD_HANDOFF.md',evidence_root/'amap_hoenn_story_audit_20261002/report.md',evidence_root/'amap_hoenn_integration_20261002/opening_map_pairs.json',evidence_root/'amap_hoenn_integration_20261002/opening_event_ledger.json',source_catalog,evidence_root/'amap_behavior_translation_v0_1_2/README.md',evidence_root/'amap_tileset_animation_integration_v0_2/README.md',evidence_root/'amap_dynamic_gfx_verified_bridge_v0_2_merge/README.md',root.parent/'Legends-Awakening/amap_p1_final_mapped_closure_verifier_v0_6_7_review.md',root.parent/'Legends-Awakening/amap_p2_persistent_flag_bridge_postapply_verifier_v0_4_22_review.md']
 for p in paths:evidence.append({'path':str(p),'sha256':sha(p),'available':p.exists(),'authority':'Prior recovery/other checkout evidence, not proof of application or runtime validation in Reborn.'})
 counts={'confidence':dict(collections.Counter(r['confidence'] for r in rows)),'replacement_modes':dict(collections.Counter(r['replacement_mode'] for r in rows)),'story_risk':dict(collections.Counter(r['story_risk'] for r in rows)),'incomplete_event_exports':sum(not r['hyper']['event_export_complete'] for r in rows),'dimension_changes':sum(not r['compatibility']['geometry']['dimensions_equal'] for r in rows),'warp_reconciliation':sum(r['compatibility']['warps']['status']=='RECONCILE_ENDPOINTS' for r in rows),'connection_reconciliation':sum(r['compatibility']['connections']['status']=='RECONCILE_TARGETS_OFFSETS' for r in rows),'event_coordinate_or_footprint_reconciliation':sum(r['compatibility']['events']['status'] in ('OUT_OF_BOUNDS','RECONCILE_COORDINATES_OR_FOOTPRINTS') for r in rows),'static_visual_layout_candidates':sum(r['readiness']['static_visual_layout_candidate'] for r in rows)}
 plan={'schema':SCHEMA,'plan_only':True,'source_export_diagnostics':{'warnings':manifest.get('warnings'),'sprite_diagnostics':manifest.get('sprite_diagnostics'),'script_diagnostics':manifest.get('script_diagnostics')},'scope':{'canonical_maps':518,'hyper_maps':922,'canonical_groups':list(enumerate(group_names)),'supplemental_groups_scanned_for_hoenn_correspondence':[34,35,36,37],'supplemental_group_map_count':404,'selected_relocated_hoenn_rooms':relocated,'unselected_hyper_map_count':404,'other_regions_advanced':False},'baseline':{'repo':str(root),'git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'donor_manifest':str(donor/'manifest.json'),'donor_manifest_sha256':sha(donor/'manifest.json'),'rom':manifest['rom'],'canonical_groups_sha256':sha(root/'data/maps/map_groups.json'),'canonical_layouts_sha256':sha(root/'data/layouts/layouts.json'),'protected_input_inventory_file':'hyper_hoenn_protected_inputs.json'},'policies':{'confidence_levels':{'HIGH':'Clear geographic/room identity with matching dimensions/type/routing','MEDIUM':'Likely same location but geometry/routing/export reconciliation needed','LOW':'Ambiguous or invalid retained source structure','NONE':'No suitable replacement identified'},'replacement_modes':{'VISUAL_ONLY':'Adopt reviewed artwork; keep canonical blocks/collision/behavior/events/scripts','VISUAL_PLUS_COLLISION':'Adopt reviewed art and collision; preserve/remap expansion gameplay','LAYOUT_REPLACEMENT':'Adopt donor layout with reviewed expansion event coordinates/terrain','FULL_RECONCILE':'Reconcile story/choreography/tile commands/warps/connections before replacement','KEEP_EXPANSION_ORIGINAL':'Keep current canonical source in this phase','MANUAL_REVIEW':'Resolve structural/export uncertainty before choosing replacement strategy'},'in_place_canonical_identity':True,'bulk_replacement':False,'donor_script_copy':False,'preserve_expansion_story_and_project_customizations':True,'canaries_and_validated_imports_unchanged':True,'confidence_means':'Counterpart identity, not approval or gameplay compatibility.','mode_means':'Proposed strategy, not executable authorization.','visual_geometry_limit':'Dimensions/collision/semantic cells do not prove artwork walkability, movement paths, active tile commands, or services.','prior_recovery_status':'Prior recovery is proven; reusable Reborn asset infrastructure is ported and build-validated. See .la_work/amap/hyper_asset_integration. No donor gameplay is transferred.','numeric_routing_audit':'Symbolic consumers inventoried; hard-coded numeric C comparisons and saved location semantics require manual audit.'},'summary':counts,'evidence':evidence,'current_recovery_inventory':{'hyper_primary_tileset_art_directories':[str(p.relative_to(root)) for p in (root/'data/tilesets/primary').glob('hyper_*')],'amap_animation_runtime_sources':[str(p.relative_to(root)) for p in (root/'src').glob('hyper*anim*')],'status':'Prior proven Hyper asset stack is ported to Reborn; see hyper_asset_integration plan/receipt/validation. Geometry/event reconciliation still applies.'},'recommended_asset_integration_canary':{'plan':'.la_work/amap/hyper_asset_integration/reborn_hyper_asset_integration_plan.json','canonical_names':['OldaleTown','Route102','OldaleTown_Mart'],'executed':False},'static_geometry_shortlist':[{'canonical_name':r['canonical']['name'],'canonical_id':r['canonical']['id'],'hyper_id':r['hyper']['id'],'mode':r['replacement_mode'],'executed':False} for r in rows if r['canonical']['name'] in ('OldaleTown_Mart','Route109_SeashoreHouse')],'maps':rows}
 dump(output/'hyper_hoenn_replacement_manifest.json',plan);dump(output/'hyper_hoenn_event_comparison_ledger.json',event_ledger);dump(output/'hyper_hoenn_global_reference_inventory.json',dict(sorted(refs.items())));dump(output/'hyper_hoenn_protected_inputs.json',protected_before);dump(output/'hyper_hoenn_supplemental_candidates.json',supplemental_candidates)
 csv_write(output/'hyper_hoenn_correspondence_inventory.csv',rows)
 csv_write(output/'hyper_hoenn_high_confidence_mapping.csv',[r for r in rows if r['confidence']=='HIGH'])
 csv_write(output/'hyper_hoenn_manual_review.csv',[r for r in rows if r['replacement_mode']!='KEEP_EXPANSION_ORIGINAL' and not r['readiness']['static_visual_layout_candidate']])
 csv_write(output/'hyper_hoenn_keep_expansion_original.csv',[r for r in rows if r['replacement_mode']=='KEEP_EXPANSION_ORIGINAL'])
 csv_write(output/'hyper_hoenn_static_visual_layout_candidates.csv',[r for r in rows if r['readiness']['static_visual_layout_candidate']])
 dump(output/'hyper_hoenn_duplicate_name_resolution.json',{label:[{'retained_hyper_slot':sid,'selected_hyper_id':next(r['hyper']['id'] for r in rows if r['canonical']['group_map']==sid),'canonical_name':canon_by_slot[sid]['name'],'canonical_id':canon_by_slot[sid]['id'],'replacement_mode':next(r['replacement_mode'] for r in rows if r['canonical']['group_map']==sid)} for sid in ids] for label,ids in sorted(family.items()) if len(ids)>1})
 protected_after=snapshot(root,donor);assert protected_before==protected_after,'Gameplay/donor files changed while planning.'
 write_review(output,plan)
 validation={'schema':SCHEMA,'canonical_coverage':len(rows),'unique_canonical_ids':len({r['canonical']['id'] for r in rows}),'unique_hyper_slots':len({r['hyper']['id'] for r in rows}),'all_import_flags_false':all(not r['import_flag'] for r in rows),'canonical_destination_ids_preserved':all(r['migration_policy']['canonical_destination']==r['canonical']['id'] for r in rows),'protected_file_count':len(protected_before),'protected_sources_and_donor_files_unchanged':protected_before==protected_after,'event_counts_checked_against_arrays':518,'incomplete_event_exports_flagged':counts['incomplete_event_exports'],'donor_blockdata_hashes_and_lengths_checked':518,'runtime_tests_executed':False,'outputs_sha256':{p.name:sha(p) for p in sorted(output.iterdir()) if p.is_file() and p.name!='validation.json'}}
 dump(output/'validation.json',validation)
 print(json.dumps({'output':str(output),'summary':counts,'validation':{k:v for k,v in validation.items() if k!='outputs_sha256'}},indent=2))

def write_review(output,plan):
 rows=plan['maps'];s=plan['summary']
 lines=['# Hyper Emerald Hoenn canonical replacement review','','**Planning only. No maps replaced or imported.** All 518 current Emerald map identities remain canonical. Hyper groups 34–37 were inspected for relocated Hoenn rooms; other regions remain outside this phase. One Sootopolis room uses donor 37.118 instead of its retained slot. Working BWA/SWSH imports and canaries are protected.','','## Findings','',f'Correspondence confidence: {s["confidence"]}. This describes identity, never migration approval.',f'Proposed modes: {s["replacement_modes"]}.',f'Static visual/layout candidates: {s["static_visual_layout_candidates"]}; event-coordinate or terrain-footprint review: {s["event_coordinate_or_footprint_reconciliation"]}; warp review: {s["warp_reconciliation"]}; connection review: {s["connection_reconciliation"]}. Counts overlap.','','The first 34 group shapes exactly match the original Emerald 518-map table. Each pairing uses a retained slot and independently compared dimensions/type/indexed warp endpoints/connections. Repeated town labels identify separate interior rooms; generic dynamic labels resolve by room slot and facility role. Object counts use actual `npcs` arrays, with declared source counts retained separately. Nine maps have filtered/missing event records; Sootopolis Mystery Events House 1F declares 255 for every kind and exports none. These are quarantined for review or kept original, never treated as empty valid maps.','','## Geometry changes and rejected counterparts','','| Canonical destination | Hyper slot / label | Dimensions | Disposition |','|---|---|---|---|']
 for r in rows:
  if not r['compatibility']['geometry']['dimensions_equal'] or r['hyper']['id'] in REPURPOSED:lines.append(f'| {r["canonical"]["name"]} | {r["hyper"]["id"]} / {r["hyper"]["name"]} | {r["canonical"]["dimensions"]} → {r["hyper"]["dimensions"]} | {r["replacement_mode"]}; {r["confidence"]} |')
 lines+=['','Sootopolis House5 selects **37.118**, not 15.9: the actual city entrance points there and both return doors target city warp 8; 15.9 diverts one exit to Couriway. Other supplemental candidates remain metadata-only. The Mystery Events House entrance points to 37.121, but that room adds an Ancient Retreat / Sinnoh connection and changes geometry, so the canonical original remains.\n\nInsideOfTruck is **25.40**, despite its donor Littleroot label. Champion/Hall of Fame rooms are **16.4 / 16.5**. Their identities do not authorize donor script transplantation. Repurposed Birth Island and the Canalave-labeled Navel Rock harbor retain originals; no Sinnoh routing advances.','','## Review lanes','','- **Static visual/layout candidates:** the additional candidate CSV requires matching dimensions, event coordinates/footprints, indexed warps, connections, semantic behavior, collision/elevation and used-index behavior/layer contracts. Prior Hyper extraction/recovery is proven and the reusable Reborn stack is ported. Expansion-event reachability on Hyper geometry and current runtime services remain later canary checks.','- **Event-coordinate remapping:** manual-review CSV and full event ledger compare every expansion object/trigger/sign/warp. Local-ID/index coincidence is not semantic NPC identity. Keep expansion payloads; reconcile full movement paths and endpoints, not just triggers.','- **Warp / connection reconciliation:** preserve canonical constants and ordered warp IDs. Review source-only doors, incoming exits, offsets, dive/emerge pairs and dynamic returns. Both routing graphs and incoming canonical edges are retained.','- **Story / structural reconciliation:** FULL_RECONCILE and MANUAL_REVIEW need explicit choreography, hook ordering, terrain and service ledgers. Equal dimensions are insufficient.','- **Keep originals:** system/link rooms, Secret Bases/contests, generated Pyramid/Trainer Hill rooms, Frontier, ship transport, prototypes/unused rooms and unsuitable repurposed destinations. Frontier is present and inventoried, not automatically safe.','','## Story-critical checkpoints','','| Area | Required retained systems |','|---|---|','| Littleroot, houses/lab, truck, Route 101/103 | Natural truck opening; gender-specific home, clock/Mom/Running Shoes, Birch rescue/starter, rival/Pokédex; current teleport scientist. |','| Oldale, Route 102, Petalburg, Route 104/Woods, Rustboro | West gate, Wally tutorial, Devon rescue/goods, rival/badge progression, trainers/items/berries/Cut access. |','| Dewford, Slateport, Mauville, Verdanturf | Ship routing, museum/Aqua, rival/Wally, Rock Smash, cycling road, contests/tunnel. |','| Fallarbor, Lavaridge, Fortree, Lilycove | Meteor Falls/Mt. Chimney teams, cable car/Strength, Weather Institute/rival, Devon Scope, hideout/travel. |','| Mossdeep, Sootopolis, Ever Grande | Space Center, Dive, Seafloor, weather crisis, Cave of Origin/Rayquaza, Waterfall, Victory Road, League/heal/Hall of Fame/ending. |','| All eight gym families | Badge/state ownership, battle return, trainers, puzzles and scripted tile changes. |','| Underwater, caves/dungeons | Dive/emerge, surf/currents/ice/ledges/ladders, field obstacles, encounters/escape/blackout and villain/legendary gates. |','| Safari/Frontier/Secret Bases/contests | Dynamic GFX/objects, temporary state, hook ordering, saved minigame/base state and entry/return contracts. |','','Map-level risk is conservative. The manifest retains current script symbols, flags/vars and line-level movement/coordinate/routing/special/native commands. Global reference inventory covers map constants in current C/scripts/headers/JSON; encounter/heal entries are preserved. Static scans are not gameplay proof.','','## Recovery evidence and migration contract','','The full export is A-Map v1.0 with script roots. ROM identity and every donor block hash are checked. Header/layout/block pointers, script tables/roots, tileset pointers/attributes/callbacks and hashes are retained.','', 'Prior archaeology establishes a **proven Hyper asset pipeline**. Its reusable Reborn port is now documented and build-validated in .la_work/amap/hyper_asset_integration; gameplay scripts, flags and save logic were not transferred. Evidence paths are pinned by hash. Behavior recovery resolved 128 used source IDs by semantic name; custom 0x1F/0x2D are accepted only under the exact tileset/metatile/collision pattern. Compare expansion enums by name, never raw numbers. Animation recovery identified 22 animated tilesets / 74 descriptors; Battle Dome uses the expansion palette callback. Reuse the recovered graphics/palettes/layers and object/dynamic GFX stack; its Reborn compatibility validation is recorded in the asset integration report. The previously proven asset stack is now ported to Reborn; consult .la_work/amap/hyper_asset_integration. Extraction does not need to be rediscovered map by map. Prior 46-map/460-object GFX closure is reused as proven recovery evidence; persistent-flag/save work remains reference-only.','','Canonical IDs/names, gameplay headers, flags/vars/save ABI, encounters, heals/Fly/blackout, trainers/items/rewards, script/dynamic warps, transport and expansion hook ownership remain authoritative. Hyper scripts and extra NPCs are reference-only. Geometry changes need existing-save coordinate/warp validation and explicit recovery behavior. Later patches should be isolated, hash-guarded, backed up and driven by a per-event disposition ledger.','','## Earlier minimal geometry shortlist (superseded by the asset integration canary)','']
 for n in ['OldaleTown_Mart','Route109_SeashoreHouse']:
  r=next(r for r in rows if r['canonical']['name']==n);a=r['compatibility'];lines.append(f'- **{n} ← Hyper {r["hyper"]["id"]}**: {r["confidence"]}, {r["replacement_mode"]}; {a["geometry"]["status"]}; {a["events"]["status"]}; {a["warps"]["status"]}. Close ledger issues before preparing a patch.')
 lines+=['','These were the earlier two-room static-geometry candidates. The meaningful asset integration canary is now OldaleTown 0.10 + Route102 0.17 + OldaleTown_Mart 2.4, testing world geometry, animation, object and native dynamic GFX. See the asset integration plan. The earlier suggestion would use two VISUAL_ONLY rooms as a bounded art canary; retain canonical Oldale/Route 109 outdoors and all other current geometry. Preserve room IDs, expansion NPCs/scripts and indexed exits. Enter/leave through normal canonical doors. Test Mart shop purchases/cancel, Seashore trainer battles and reward/repeat handling, every interaction, collision, animation, return, save/reload and blackout on separate saves. If artwork obstructs a preserved interaction, remap deliberately or remove that room from the batch.','', 'Route 102 / Oldale outdoors belong in a later connected-world canary after terrain, trainers/berries/objects, west-gate choreography and connections pass review. Defer Littleroot/Route 101, truck and League until complete story-path ledgers exist. No replacement was executed.','','## Deliverables and validation','','The manifest is authoritative and CSVs are flattened views. High-confidence mapping includes story-heavy/KEEP rows; it is not a bulk import list. Manual review excludes explicit KEEP rows, which have their own list. Extra ledgers retain events, global references, duplicate-name resolutions and protected-file hashes. `validation.json` checks 518-map coverage, events/blocks and byte-for-byte source protection.','','Regenerate:','','```text','python3 tools/la_world/importers/amap/hoenn_replacement/build_hyper_hoenn_plan.py --repo .','```','','Recovery evidence defaults to /mnt/c/Users/aadair/Downloads/tools; use --evidence-root when relocating the bundle. A changed ROM/group shape requires explicit review.']
 (output/'hyper_hoenn_replacement_review.md').write_text('\n'.join(lines)+'\n')

if __name__=='__main__':
 parser=argparse.ArgumentParser(description='Read-only canonical Hyper Hoenn correspondence planner; never imports maps.')
 parser.add_argument('--repo',type=Path,default=Path.cwd());parser.add_argument('--donor',type=Path);parser.add_argument('--output',type=Path);parser.add_argument('--evidence-root',type=Path,default=Path('/mnt/c/Users/aadair/Downloads/tools'))
 args=parser.parse_args();build(args.repo,args.donor or args.repo/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export',args.output or args.repo/'.la_work/amap/hyper_hoenn_replacement',args.evidence_root)
