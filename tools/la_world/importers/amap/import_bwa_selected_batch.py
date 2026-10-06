#!/usr/bin/env python3
"""Import the approved BWA visual batch with project-owned inspection travel."""
import json,re,shutil,struct,hashlib
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4]
def dump(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2)+'\n')
def include(p,line):
 s=p.read_text()
 if line not in s:p.write_text(s.rstrip()+'\n'+line+'\n')
def main():
 manifest=json.loads((R/'.la_work/amap/bwa_selected_assets/selected_asset_manifest.json').read_text());rows=manifest['maps'];assert len(rows)==19
 protected={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for root in ['data/maps','data/layouts','data/tilesets'] for p in (R/root).rglob('*') if p.is_file() and ('AMap' in str(p) or 'amap_' in str(p))}
 native=enums(R/'include/constants/metatile_behaviors.h');ref=R/'.la_work/amap/firered_behaviors_reference.h';donor={int(v,16):n for n,v in re.findall(r'#define (MB_\w+) (0x[0-9A-Fa-f]+)',ref.read_text())}
 aliases={'MB_ROCK_STAIRS':'MB_NORMAL','MB_SAND_CAVE':'MB_CAVE','MB_RUNNING_DISALLOWED':'MB_NO_RUNNING','MB_POWER_PLANT_MACHINE':'MB_NORMAL','MB_BLINKING_LIGHTS':'MB_NORMAL'}
 # Visual mechanics without donor script ownership. Unwired warp behaviors are ordinary terrain during inspection.
 def translate(b):
  n=donor.get(b);n=aliases.get(n,n)
  if n and any(t in n for t in ['WARP','DOOR','LADDER']):n='MB_NORMAL'
  return native.get(n,native['MB_NORMAL']),n or 'UNUSED_QUARANTINED'
 root=R/'.la_work/amap/bwa_full_v11';bank=R/'data/bwa_assets';bank.mkdir(exist_ok=True);meta_by={};graphics=[];headers=[];metas=[];behavior_ledger=[]
 keys=set()
 for row in rows:
  m=json.loads((R/row['source_json']).read_text());keys.update([m['primary_tileset'],m['secondary_tileset']])
 for key in sorted(keys):
  src=root/'tilesets'/key;meta=json.loads((src/'tileset.json').read_text());dest=bank/'tilesets'/key;shutil.copytree(src,dest,dirs_exist_ok=True);label='gTileset_BWABatch_'+key;meta_by[key]=(label,meta)
  pals=dest/'palettes';pals.mkdir(exist_ok=True)
  for i in range(16):
   f=pals/f'{i:02}.pal'
   if not f.exists():f.write_text('JASC-PAL\n0100\n16\n'+'0 0 0\n'*16)
  raw=(src/'source_frlg_metatile_attributes.bin').read_bytes();compat=(src/'metatile_attributes.bin').read_bytes();attrs=[]
  for i in range(512):
   a=struct.unpack_from('<I',raw,i*4)[0];b=a&511;v,n=translate(b);layer=struct.unpack_from('<H',compat,i*2)[0]&0xf000;attrs.append(layer|v);behavior_ledger.append(dict(tileset=key,metatile=i,donor_behavior=b,target_behavior=v,target_name=n))
  (dest/'metatile_attributes.bin').write_bytes(struct.pack('<512H',*attrs));base=dest.relative_to(R).as_posix()
  graphics.append(f'const u32 {label}_Tiles[] = INCBIN_U32("{base}/tiles.4bpp.lz");\nconst u16 {label}_Palettes[][16] = {{\n'+''.join(f' INCBIN_U16("{base}/palettes/{i:02}.gbapal"),\n' for i in range(16))+'};')
  metas.append(f'const u16 {label}_Metatiles[] = INCBIN_U16("{base}/metatiles.bin");\nconst u16 {label}_Attributes[] = INCBIN_U16("{base}/metatile_attributes.bin");')
  headers.append(f'const struct Tileset {label} = {{\n .isCompressed = TRUE,\n .isSecondary = {"TRUE" if meta["role"]=="secondary" else "FALSE"},\n .tiles = {label}_Tiles,\n .palettes = {label}_Palettes,\n .metatiles = {label}_Metatiles,\n .metatileAttributes = {label}_Attributes,\n .callback = NULL,\n}};')
 for name,lines in [('graphics',graphics),('metatiles',metas),('headers',headers)]:
  p=R/f'src/data/tilesets/bwa_batch_{name}.h';p.write_text('\n\n'.join(lines)+'\n');include(R/f'src/data/tilesets/{name}.h',f'#include "bwa_batch_{name}.h"')
 layouts_path=R/'data/layouts/layouts.json';layouts=json.loads(layouts_path.read_text());gp=R/'data/maps/map_groups.json';groups=json.loads(gp.read_text());original_groups={k:list(v) for k,v in groups.items()};assert len(groups['group_order'])==127
 ledger=[]
 for idx,row in enumerate(rows):
  source=R/row['source_json'];assert hashlib.sha256(source.read_bytes()).hexdigest()==row['source_json_sha256'];m=json.loads(source.read_text());name=f'BWA_{m["group"]}_{m["map"]}';lid='LAYOUT_'+name.upper();folder=bank/'layouts'/m['id'];folder.mkdir(parents=True,exist_ok=True);raw=(source.parent/'blockdata.bin').read_bytes();cells=list(struct.unpack('<'+'H'*(len(raw)//2),raw));attrs=[]
  for key in [m['primary_tileset'],m['secondary_tileset']]:attrs+=list(struct.unpack('<512I',(root/'tilesets'/key/'source_frlg_metatile_attributes.bin').read_bytes()))
  changed=[]
  for i,v in enumerate(cells):
   b=attrs[v&1023]&511
   if b in [16,17,18,19,21] and (v>>10&3)==0 and v>>12 not in [1,15]:
    cells[i]=(v&0xfff)|0x1000;changed.append(i)
  floor={i for i,v in enumerate(cells) if (v>>10&3)==0 and v>>12 in [0,3] and attrs[v&1023]&511==0}
  candidates=[i for i in floor if i+m['width'] in floor and i+1 in floor and i-1 in floor and i-m['width'] in floor]
  assert candidates,(m['id'],'no valid spawn cluster')
  # Derived from actual passable cells, not donor NPC coordinates.
  spawn=min(candidates,key=lambda i:abs(i%m['width']-m['width']//2)+abs(i//m['width']-m['height']//2));x,y=spawn%m['width'],spawn//m['width']
  (folder/'map.bin').write_bytes(struct.pack('<'+'H'*len(cells),*cells));shutil.copy2(source.parent/'border.bin',folder/'border.bin');base=folder.relative_to(R).as_posix()
  layout=dict(id=lid,name=name+'_Layout',width=m['width'],height=m['height'],primary_tileset=meta_by[m['primary_tileset']][0],secondary_tileset=meta_by[m['secondary_tileset']][0],blockdata_filepath=base+'/map.bin',border_filepath=base+'/border.bin',border_width=m['border']['width'],border_height=m['border']['height'],layout_version='emerald')
  assert not any(l['id']==lid for l in layouts['layouts']);layouts['layouts'].append(layout)
  if m['id']=='3.20': x,y=20,30
  events=[dict(local_id='LOCALID_'+name.upper()+'_SCIENTIST',graphics_id='OBJ_EVENT_GFX_SCIENTIST_1',x=x,y=y-1,elevation=3,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script=name+'_Inspect',flag='0')]
  obj=dict(id='MAP_'+name.upper(),name=name,layout=lid,music='MUS_DUMMY',region_map_section='MAPSEC_NONE',requires_flash=False,weather='WEATHER_NONE',map_type='MAP_TYPE_INDOOR' if row['category']=='INTERIOR' else 'MAP_TYPE_TOWN',allow_cycling=False,allow_escaping=False,allow_running=True,show_map_name=False,battle_scene='MAP_BATTLE_SCENE_NORMAL',connections=None,object_events=events,warp_events=[],coord_events=[],bg_events=[])
  dump(R/'data/maps'/name/'map.json',obj);groups['gMapGroup_AMap_Bank3'].append(name)
  ledger.append(dict(donor_id=row['id'],name=m['name'],destination=name,map_id=obj['id'],spawn=[x,y],scientist=[x,y-1],water_elevation_remaps=changed,donor_gameplay_imported=False,animations='STATIC_PENDING_RECOVERY'))
 for i,item in enumerate(ledger):
  nxt=ledger[(i+1)%len(ledger)];name=item['destination'];script=f'{name}_MapScripts::\n\t.byte 0\n\n{name}_Inspect::\n\tlock\n\tfaceplayer\n\tmsgbox {name}_Text, MSGBOX_YESNO\n\tgoto_if_eq VAR_RESULT, YES, {name}_Next\n\tclosemessage\n\twarp MAP_LITTLEROOT_TOWN, 10, 17\n\twaitstate\n\trelease\n\tend\n{name}_Next::\n\tclosemessage\n\twarp {nxt["map_id"]}, {nxt["spawn"][0]}, {nxt["spawn"][1]}\n\twaitstate\n\trelease\n\tend\n{name}_Text:\n\t.string "BWA inspection {i+1} of 19.\\n"\n\t.string "Visit the next map?\\p"\n\t.string "YES: next. NO: Littleroot.$"\n';p=R/'data/maps'/name/'scripts.inc';p.write_text(script);include(R/'data/event_scripts.s',f'.include "data/maps/{name}/scripts.inc"')
 first=ledger[0];p=R/'data/scripts/la_teleport_scientist.inc';s=p.read_text();s=s.replace('\t@ 4 = CANCEL','\tgoto_if_eq VAR_RESULT, 4, LA_TeleportScientist_WarpBWABatch\n\t@ 5 = CANCEL');s+=f'\nLA_TeleportScientist_WarpBWABatch::\n\tclosemessage\n\twarp {first["map_id"]}, {first["spawn"][0]}, {first["spawn"][1]}\n\twaitstate\n\trelease\n\tend\n';p.write_text(s)
 p=R/'src/data/script_menu.h';s=p.read_text();needle='{COMPOUND_STRING("MOTOSTOKE")},';assert s.count(needle)==1;s=s.replace(needle,needle+'\n    {COMPOUND_STRING("BWA MAP TEST")},');p.write_text(s)
 dump(layouts_path,layouts);dump(gp,groups)
 for k,v in original_groups.items():assert groups[k][:len(v)]==v
 for p,h in protected.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h,p
 doc=R/'docs/la_world/donor_preservation/bwa/runtime_batch';dump(doc/'import_ledger.json',ledger);dump(doc/'behavior_translation.json',behavior_ledger);dump(doc/'validation.json',dict(maps=19,tilesets=len(keys),existing_numeric_ids_unchanged=True,protected_files=len(protected),donor_scripts=False,donor_flags=False,donor_npcs=False,donor_warps=False,natural_connections=False,animation_recovery_pending=True))
 (doc/'runtime_checklist.md').write_text('# BWA 19-map asset inspection\n\nUse Littleroot teleport scientist > BWA MAP TEST. Each inspection scientist offers YES for next map and NO for Littleroot; all 19 form a loop. Natural entrances and donor connections are intentionally unwired. No donor story/NPC/flag/script ownership is installed.\n\nCheck every map with both genders: graphics, walking boundaries, ledges/stairs, Surf-only water, scientist next/cancel/return; then save/reload. Visit existing BWA and SWSH canaries for regression. Centers are visual rooms, without healing/shop gameplay yet. Blackout/Fly locations remain native; this batch defines none. Animations remain static until the separate FRLG animation recovery pass.\n')
 print('Imported',len(ledger),'maps',len(keys),'tilesets; existing map IDs and protected assets unchanged')
if __name__=='__main__':main()
