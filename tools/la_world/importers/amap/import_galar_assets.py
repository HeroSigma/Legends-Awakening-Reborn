#!/usr/bin/env python3
"""Import the reviewed non-excluded Galar candidate set as blank travel maps."""
import json,re,struct,hashlib,shutil,subprocess
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4]
S=R/'.la_work/amap/swsh_full_v11'
D=R/'docs/la_world/galar_import'
def dump(path,value):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,indent=2)+'\n')
def main():
 assert not (D/'import_ledger.json').exists(), 'Already imported'
 review=json.loads((R/'.la_work/amap/swsh_galar_review/swsh_galar_import_manifest.json').read_text())
 manifest=json.loads((S/'manifest.json').read_text());source={m['id']:m for m in manifest['maps']}
 selected={m['id'] for m in review['maps'] if m['disposition'] not in ['EXCLUDED_LEGACY','EXCLUDED_SUPERSEDED']}
 existing={m['donor_id']:m for m in review['observed_destination_imports']}
 folders={json.loads((f/'map.json').read_text())['id']:f for f in (S/'maps').iterdir() if (f/'map.json').exists()}
 protected={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest() for root in ['data/gs_johto_assets','data/bwa_assets','data/kanto_ar_assets'] for f in (R/root).rglob('*') if f.is_file()}
 shared=['data/maps/map_groups.json','data/layouts/layouts.json','data/event_scripts.s','src/data/tilesets/headers.h','src/data/tilesets/graphics.h','src/data/tilesets/metatiles.h','src/data/region_map/region_map_sections.json','data/scripts/la_teleport_scientist.inc']
 backup=R/'.la_work/amap/galar_import_backup';backup.mkdir(parents=True,exist_ok=True)
 for rel in shared:
  target=backup/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/rel,target)
 for e in existing.values():
  for f in (R/'data/maps'/e['destination_map']).glob('*'):
   if f.is_file():q=backup/f.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,q)
 native=enums(R/'include/constants/metatile_behaviors.h')
 donor={int(v,16):n for n,v in re.findall(r'#define (MB_\w+) (0x[0-9A-Fa-f]+)',(R/'.la_work/amap/firered_behaviors_reference.h').read_text())}
 needed={source[i][k] for i in selected for k in ['primary_tileset','secondary_tileset']}
 labels={k:'gTileset_Galar_'+k for k in needed};banks={};decl={k:[] for k in ['headers','graphics','metatiles']};translations=[]
 for key in sorted(needed):
  folder=S/'tilesets'/key;meta=manifest['tilesets'][key];target=R/'data/galar_assets/tilesets'/key;target.mkdir(parents=True)
  for file in ['tiles.4bpp','metatiles.bin','metatile_attributes.bin','source_frlg_metatile_attributes.bin']:shutil.copy2(folder/file,target/file)
  subprocess.run([str(R/'tools/gbagfx/gbagfx'),str(target/'tiles.4bpp'),str(target/'tiles.4bpp.lz')],check=True)
  raw=(target/'source_frlg_metatile_attributes.bin').read_bytes();attrs=bytearray((target/'metatile_attributes.bin').read_bytes());tiles=bytearray((target/'metatiles.bin').read_bytes())
  for slot in range(512):
   b=struct.unpack_from('<I',raw,4*slot)[0]&511;name=donor.get(b);name={'MB_ROCK_STAIRS':'MB_NORMAL','MB_SAND_CAVE':'MB_CAVE','MB_RUNNING_DISALLOWED':'MB_NO_RUNNING'}.get(name,name)
   if name and any(w in name for w in ['WARP','DOOR','LADDER']):name='MB_NORMAL'
   if name not in native:translations.append({'bank':key,'metatile':slot,'source_behavior':b});name='MB_NORMAL'
   old=struct.unpack_from('<H',attrs,2*slot)[0];struct.pack_into('<H',attrs,2*slot,(old&0xf000)|native[name])
  banks[key]=(target,attrs,tiles,raw)
  palette=bytearray()
  for slot in range(13):
   f=folder/'palettes'/f'{slot:02}.pal';colors=[tuple(map(int,l.split())) for l in f.read_text().splitlines()[3:19]] if f.exists() else [(0,0,0)]*16
   assert len(colors)==16
   palette.extend(b''.join(struct.pack('<H',(a>>3)|((b>>3)<<5)|((c>>3)<<10)) for a,b,c in colors))
  (target/'palettes.gbapal').write_bytes(palette)
  for slot in range(13):(target/f'palette_{slot:02}.gbapal').write_bytes(palette[slot*32:slot*32+32])
  base=target.relative_to(R).as_posix();label=labels[key]
  decl['graphics'].append(f'const u32 {label}_Tiles[] = INCBIN_U32("{base}/tiles.4bpp.lz");\nconst u16 {label}_Palettes[][16] = {{\n'+''.join(f' INCBIN_U16("{base}/palette_{i:02}.gbapal"),\n' for i in range(13))+'};')
  decl['metatiles'].append(f'const u16 {label}_Metatiles[] = INCBIN_U16("{base}/metatiles.bin");\nconst u16 {label}_Attributes[] = INCBIN_U16("{base}/metatile_attributes.bin");')
  decl['headers'].append(f'const struct Tileset {label} = {{ .isCompressed=TRUE, .isSecondary={"TRUE" if meta["role"]=="secondary" else "FALSE"}, .tiles={label}_Tiles, .palettes={label}_Palettes, .metatiles={label}_Metatiles, .metatileAttributes={label}_Attributes, .callback=NULL }};')
 for kind,lines in decl.items():
  f=R/f'src/data/tilesets/{kind}.h';f.write_text(f.read_text().rstrip()+'\n\n'+'\n\n'.join(lines)+'\n')
 lp=R/'data/layouts/layouts.json';layouts=json.loads(lp.read_text());ls={l['id']:l for l in layouts['layouts']};gp=R/'data/maps/map_groups.json';groups=json.loads(gp.read_text());oldgroups=json.loads(gp.read_text());names={};rows={};ledger=[];includes=[];used={k:set() for k in needed}
 for did in sorted(selected,key=lambda i:tuple(map(int,i.split('.')))):
  s=source[did];name=existing[did]['destination_map'] if did in existing else f'Galar_{s["group"]}_{s["map"]}_'+re.sub('[^A-Za-z0-9]+','_',s['name']).strip('_');names[did]=name
  if did in existing:
   m=json.loads((R/existing[did]['destination_path']).read_text());l=ls[m['layout']]
   block=(R/l['blockdata_filepath']).read_bytes();border=(R/l['border_filepath']).read_bytes()
   assert (l['width'],l['height'])==(s['width'],s['height'])
  else:
   l={'id':'LAYOUT_'+name.upper(),'name':name+'_Layout','width':s['width'],'height':s['height'],'border_width':s['border']['width'],'border_height':s['border']['height']};layouts['layouts'].append(l)
   block=(folders[did]/'blockdata.bin').read_bytes();border=(folders[did]/'border.bin').read_bytes()
   candidates=[k for k in groups['group_order'] if groups['group_order'].index(k)<127 and len(groups[k])<127]
   group=min(candidates,key=lambda k:(0 if groups['group_order'].index(k)>=82 else 1,len(groups[k]),groups['group_order'].index(k)));groups[group].append(name)
   m={'id':'MAP_'+name.upper(),'name':name,'layout':l['id'],'requires_flash':False,'weather':'WEATHER_NONE','allow_escaping':False,'allow_running':True,'battle_scene':'MAP_BATTLE_SCENE_NORMAL','object_events':[],'coord_events':[],'bg_events':[]}
   includes.append(f'.include "data/maps/{name}/scripts.inc"')
  target=R/'data/galar_assets/layouts'/name;target.mkdir(parents=True);(target/'map.bin').write_bytes(block);(target/'border.bin').write_bytes(border);base=target.relative_to(R).as_posix()
  keys=[s[k] for k in ['primary_tileset','secondary_tileset']];l.update(primary_tileset=labels[keys[0]],secondary_tileset=labels[keys[1]],blockdata_filepath=base+'/map.bin',border_filepath=base+'/border.bin')
  m.update(region_map_section='MAPSEC_GALAR_ASSETS',music='MUS_ROUTE104',show_map_name=True,allow_cycling=bool(s['allow_cycling']),map_type={1:'MAP_TYPE_TOWN',2:'MAP_TYPE_CITY',3:'MAP_TYPE_ROUTE',4:'MAP_TYPE_UNDERWATER',5:'MAP_TYPE_OCEAN_ROUTE',6:'MAP_TYPE_INDOOR',7:'MAP_TYPE_SECRET_BASE',8:'MAP_TYPE_UNDERGROUND'}.get(s['map_type'],'MAP_TYPE_INDOOR'))
  cells=list(struct.unpack('<'+'H'*(l['width']*l['height']),block));rows[did]=(m,l,keys,cells)
  for blob in [block,border]:
   for v, in struct.iter_unpack('<H',blob):used[keys[(v&1023)//512]].add(v&511)
  ledger.append({'donor_id':did,'project_name':name,'layout':l['id'],'existing_import':did in existing,'original_blockdata_sha256':hashlib.sha256(block).hexdigest()})
 revisions={'3.1':'5.6','3.2':'6.10','3.3':'7.11','3.4':'8.7','3.5':'9.10','3.6':'10.21','3.7':'11.10','3.8':'12.10','3.10':'14.10','4.6':'3.0'}
 disabled=[];remaps=[];changes=[];clones={};tour=[];warpnames={0x60:'MB_NON_ANIMATED_DOOR',0x61:'MB_LADDER',0x62:'MB_EAST_ARROW_WARP',0x63:'MB_WEST_ARROW_WARP',0x64:'MB_NORTH_ARROW_WARP',0x65:'MB_SOUTH_ARROW_WARP',0x66:'MB_LADDER',0x67:'MB_AQUA_HIDEOUT_WARP',0x68:'MB_LADDER',0x69:'MB_NON_ANIMATED_DOOR',0x6a:'MB_UP_ESCALATOR',0x6b:'MB_DOWN_ESCALATOR',0x6c:'MB_UP_RIGHT_STAIR_WARP',0x6d:'MB_UP_LEFT_STAIR_WARP',0x6e:'MB_DOWN_RIGHT_STAIR_WARP',0x6f:'MB_DOWN_LEFT_STAIR_WARP',0x71:'MB_LADDER'}
 def clone(keys,mid,behavior):
  key=keys[mid//512];target,a,t,raw=banks[key];pair=(key,mid%512,behavior)
  if pair not in clones:
   free=[i for i in range(511,-1,-1) if i not in used[key]];assert free,(key,'no unused scoped metatiles');slot=free[0];used[key].add(slot);clones[pair]=slot;t[slot*16:slot*16+16]=t[(mid%512)*16:(mid%512)*16+16];old=struct.unpack_from('<H',a,2*(mid%512))[0];struct.pack_into('<H',a,2*slot,(old&0xf000)|behavior)
  return mid//512*512+clones[pair]
 def rawbehavior(keys,mid):return struct.unpack_from('<I',banks[keys[mid//512]][3],4*(mid%512))[0]&511
 # Preserve event indices even where an unsafe donor event is disabled.
 enabled={}
 for did,(m,l,keys,cells) in rows.items():
  enabled[did]={};m['warp_events']=[]
  for index,z in enumerate(source[did]['warps']):
   target=z['target_id'];wid=z['dest_warp_id'];reason=None
   if z['dynamic_target']:reason='dynamic donor return has no trusted project origin'
   elif target not in selected:
    revised=revisions.get(target);matches=[(i,w) for i,w in enumerate(source[revised]['warps']) if w['target_id']==did and w['dest_warp_id']==index] if revised else []
    if len(matches)==1:remaps.append({'map':did,'warp':index,'old_target':target,'new_target':revised,'new_warp':matches[0][0]});target=revised;wid=matches[0][0]
    else:reason='target excluded or ambiguous city revision'
   if not reason and not (0<=wid<len(source[target]['warps'])):reason='destination warp index invalid'
   if not (0<=z['x']<l['width'] and 0<=z['y']<l['height']):reason='source coordinates outside layout'
   if not reason:
    dest=source[target]['warps'][wid];dl=rows[target][1]
    if not (0<=dest['x']<dl['width'] and 0<=dest['y']<dl['height']):reason='destination coordinates outside layout'
   if reason:
    disabled.append({'kind':'warp','map':did,'index':index,'target':z['target_id'],'reason':reason});m['warp_events'].append({'x':-1,'y':-1,'elevation':0,'dest_map':'MAP_LITTLEROOT_TOWN','dest_warp_id':'0'})
   else:
    enabled[did][index]=(target,wid);m['warp_events'].append({'x':z['x'],'y':z['y'],'elevation':3,'dest_map':'MAP_'+names[target].upper(),'dest_warp_id':str(wid)})
 # An otherwise valid source must not land on a disabled destination event.
 while True:
  before=sum(len(v) for v in enabled.values())
  for did in rows:
   for index,(target,wid) in list(enabled[did].items()):
    if wid not in enabled[target]:
     rows[did][0]['warp_events'][index]={'x':-1,'y':-1,'elevation':0,'dest_map':'MAP_LITTLEROOT_TOWN','dest_warp_id':'0'};disabled.append({'kind':'warp','map':did,'index':index,'target':target,'reason':'destination event disabled'});del enabled[did][index]
  if sum(len(v) for v in enabled.values())==before:break
 for did,(m,l,keys,cells) in rows.items():
  connections=[]
  for z in source[did]['connections']:
   target=revisions.get(z['target_id'],z['target_id'])
   if target in selected and z['direction'] in ['up','down','left','right','dive','emerge']:
    connections.append({'map':'MAP_'+names[target].upper(),'offset':z['offset'],'direction':z['direction']})
   else:disabled.append({'kind':'connection','map':did,'target':z['target_id'],'reason':'excluded destination or invalid direction'})
  m['connections']=connections or None
  for index in enabled[did]:
   z=m['warp_events'][index];pos=z['y']*l['width']+z['x'];v=cells[pos];mid=clone(keys,v&1023,native[warpnames.get(rawbehavior(keys,v&1023),'MB_LADDER')]);new=0x3000|mid;cells[pos]=new;changes.append({'map':m['name'],'x':z['x'],'y':z['y'],'before':v,'after':new,'reason':'scoped native warp trigger'})
  warppos={(z['x'],z['y']) for z in m['warp_events']};floor=set()
  for i,v in enumerate(cells):
   key=keys[(v&1023)//512];behavior=struct.unpack_from('<H',banks[key][1],2*(v&511))[0]&255
   if (v>>10&3)==0 and v>>12 in [0,3] and behavior==native['MB_NORMAL'] and (i%l['width'],i//l['width']) not in warppos:floor.add(i)
  occupied={(o['x'],o['y']) for o in m['object_events']}
  candidates=[i for i in floor if (i%l['width'],i//l['width']) not in occupied and (i%l['width'],i//l['width']-1) not in occupied and i%l['width']>0 and i%l['width']<l['width']-1 and i-l['width'] in floor and i+l['width'] in floor and i-1 in floor and i+1 in floor]
  if candidates:
   pos=min(candidates,key=lambda i:abs(i%l['width']-l['width']//2)+abs(i//l['width']-l['height']//2));x,y=pos%l['width'],pos//l['width'];tour.append({'donor_id':did,'map':m['name'],'map_id':m['id'],'spawn':[x,y]})
   m['object_events'].append({'local_id':'LOCALID_'+m['name'].upper()+'_GALAR_INSPECTOR','graphics_id':'OBJ_EVENT_GFX_SCIENTIST_1','x':x,'y':y-1,'elevation':3,'movement_type':'MOVEMENT_TYPE_FACE_DOWN','movement_range_x':0,'movement_range_y':0,'trainer_type':'TRAINER_TYPE_NONE','trainer_sight_or_berry_tree_id':'0','script':m['name']+'_GalarInspect','flag':'0'})
  (R/l['blockdata_filepath']).write_bytes(struct.pack('<'+'H'*len(cells),*cells));dump(R/'data/maps'/m['name']/'map.json',m)
 for target,a,t,raw in banks.values():(target/'metatile_attributes.bin').write_bytes(a);(target/'metatiles.bin').write_bytes(t)
 tour.sort(key=lambda z:(0 if z['donor_id']=='3.0' else 1,tuple(map(int,z['donor_id'].split('.')))))
 for index,z in enumerate(tour):
  nxt=tour[(index+1)%len(tour)];f=R/'data/maps'/z['map']/'scripts.inc';old=f.read_text() if z['donor_id'] in existing else z['map']+'_MapScripts::\n\t.byte 0\n';f.write_text(old+f'\n{z["map"]}_GalarInspect::\n\tcall Galar_InspectionPrompt\n\twarp {nxt["map_id"]}, {nxt["spawn"][0]}, {nxt["spawn"][1]}\n\tgoto Galar_InspectionFinish\n')
 for did in selected-existing.keys():
  f=R/'data/maps'/names[did]/'scripts.inc'
  if not f.exists():f.write_text(names[did]+'_MapScripts::\n\t.byte 0\n')
 common=R/'data/scripts/galar_inspection.inc';common.write_text('Galar_InspectionPrompt::\n\tlock\n\tfaceplayer\n\tmsgbox Galar_InspectionText, MSGBOX_YESNO\n\tgoto_if_eq VAR_RESULT, NO, Galar_InspectionHome\n\tclosemessage\n\treturn\nGalar_InspectionHome::\n\tclosemessage\n\twarp MAP_LITTLEROOT_TOWN, 10, 17\nGalar_InspectionFinish::\n\twaitstate\n\trelease\n\tend\nGalar_InspectionText:\n\t.string "Visit the next Galar candidate map?\\p"\n\t.string "YES: next. NO: Littleroot.$"\n')
 includes.append('.include "data/scripts/galar_inspection.inc"');f=R/'data/event_scripts.s';f.write_text(f.read_text().rstrip()+'\n'+'\n'.join(includes)+'\n');dump(lp,layouts);dump(gp,groups)
 sectionsfile=R/'src/data/region_map/region_map_sections.json';sections=json.loads(sectionsfile.read_text());sections['map_sections'].append({'id':'MAPSEC_GALAR_ASSETS','name':'Galar','x':0,'y':0,'width':1,'height':1});dump(sectionsfile,sections)
 first=tour[0];assert first['donor_id']=='3.0';f=R/'data/scripts/la_teleport_scientist.inc';s=f.read_text();s=s.replace('warp MAP_AMAP_3_0_POSTWICK, 15, 24',f'warp {first["map_id"]}, {first["spawn"][0]}, {first["spawn"][1]}');f.write_text(s)
 for k,v in oldgroups.items():assert groups[k][:len(v)]==v
 for rel,h in protected.items():assert hashlib.sha256((R/rel).read_bytes()).hexdigest()==h,rel
 dump(D/'import_ledger.json',ledger);dump(D/'inspection_arrivals.json',tour);dump(D/'travel_cell_changes.json',changes);dump(D/'disabled_links.json',disabled);dump(D/'remapped_links.json',remaps);dump(D/'unknown_behaviors.json',translations)
 dump(D/'summary.json',{'maps':len(rows),'new_maps':len(rows)-len(existing),'tilesets':len(banks),'inspection_maps':len(tour),'enabled_warps':sum(len(v) for v in enabled.values()),'connections':sum(len(m['connections'] or []) for m,l,k,c in rows.values()),'disabled_links':len(disabled),'city_revision_remaps':len(remaps),'scoped_warp_metatiles':len(clones),'protected_files':len(protected),'runtime_verified':False,'story_scripts_imported':False})
 print((D/'summary.json').read_text())
if __name__=='__main__':main()
