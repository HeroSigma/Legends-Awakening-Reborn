#!/usr/bin/env python3
"""GS Chronicles asset geometry and explicit project static-travel port; no donor gameplay."""
import json,re,struct,hashlib,shutil
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4];S=R/'.la_work/amap/gs_chronicles_full';O=R/'docs/la_world/gs_johto'
def load(p):return json.loads(p.read_text())
def dump(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2)+'\n')
def append(p,line):
 s=p.read_text()
 if line not in s:p.write_text(s.rstrip()+'\n'+line+'\n')
# Outdoor GS stairs reuse FR arrow-warp behavior bytes; classify by proven bank/metatile,
# never globally translate arrow warps (real interior exits retain their semantics).
GS_OUTDOOR_STAIRS = {
 0x15F: 'MB_SIDEWAYS_STAIRS_RIGHT_SIDE_TOP',
 0x15B: 'MB_SIDEWAYS_STAIRS_RIGHT_SIDE_BOTTOM',
 0x162: 'MB_SIDEWAYS_STAIRS_LEFT_SIDE_TOP',
 0x15C: 'MB_SIDEWAYS_STAIRS_LEFT_SIDE_BOTTOM',
}
def gs_behavior_override(key, index):
 if key == 'primary_f2e_GS_CHRONICLES_276_082D4A94':
  return GS_OUTDOOR_STAIRS.get(index)
 return None
def main():
 assert not (O/'receipt.json').exists(),'Already applied'
 audit=load(S/'audit.json');rows=[z for z in audit['maps'] if 88<=z['map_section']<=145 and z['map_section']!=97]
 folders={load(p)['id']:p.parent for p in (S/'maps').glob('*/map.json')};donors={z['id']:load(folders[z['id']]/'map.json') for z in rows};names={k:'GSJohto_'+k.replace('.','_')+'_'+re.sub('[^A-Za-z0-9]+','_',d['name']).strip('_') for k,d in donors.items()}
 protected={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'data/maps').rglob('*') if p.is_file() and p.name=='map.json'}
 # Existing map JSON and scripts are protected; only hub script shared outside map folders changes.
 protected.update({str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'data/maps').glob('*/scripts.inc')})
 ls=load(R/'data/layouts/layouts.json');groups=load(R/'data/maps/map_groups.json');before=json.loads(json.dumps(groups));sections=load(R/'src/data/region_map/region_map_sections.json');assert len(sections['map_sections'])<252
 sections['map_sections'].append(dict(id='MAPSEC_GS_JOHTO',name='Johto',x=0,y=0,width=1,height=1))
 native=enums(R/'include/constants/metatile_behaviors.h');donor_mb={int(v,16):n for n,v in re.findall(r'#define (MB_\w+) (0x[0-9A-Fa-f]+)',(R/'.la_work/amap/firered_behaviors_reference.h').read_text())};alias={'MB_ROCK_STAIRS':'MB_NORMAL','MB_SAND_CAVE':'MB_CAVE','MB_RUNNING_DISALLOWED':'MB_NO_RUNNING','MB_WARP_DOOR':'MB_ANIMATED_DOOR','MB_CAVE_DOOR':'MB_NON_ANIMATED_DOOR','MB_REGULAR_WARP':'MB_NON_ANIMATED_DOOR'}
 keys=sorted({d[k] for d in donors.values() for k in ['primary_tileset','secondary_tileset']});graphics=[];metas=[];headers=[];attrs={};translation=[]
 for key in keys:
  src=S/'tilesets'/key;dest=R/'data/gs_johto_assets/tilesets'/key;shutil.copytree(src,dest,dirs_exist_ok=True);sy='gTileset_GSJohto_'+key;meta=load(src/'tileset.json');raw=(src/'source_frlg_metatile_attributes.bin').read_bytes();compat=(src/'metatile_attributes.bin').read_bytes();values=[]
  for i in range(512):
   v=struct.unpack_from('<I',raw,i*4)[0]&511;n=(gs_behavior_override(key,i) or alias.get(donor_mb.get(v),donor_mb.get(v)));nv=native.get(n,native['MB_NORMAL']);values.append((struct.unpack_from('<H',compat,i*2)[0]&0xf000)|nv);translation.append(dict(bank=key,index=i,donor=v,native=nv,known=n in native))
  attrs[key]=values;(dest/'metatile_attributes.bin').write_bytes(struct.pack('<512H',*values));base=dest.relative_to(R).as_posix()
  for i in range(16):
   pp=dest/f'palettes/{i:02}.pal'
   if not pp.exists():pp.write_text('JASC-PAL\n0100\n16\n'+'0 0 0\n'*16)
  graphics.append(f'const u32 {sy}_Tiles[] = INCBIN_U32("{base}/tiles.4bpp.lz");\nconst u16 {sy}_Palettes[][16] = {{\n'+''.join(f' INCBIN_U16("{base}/palettes/{i:02}.gbapal"),\n' for i in range(16))+'};')
  metas.append(f'const u16 {sy}_Metatiles[] = INCBIN_U16("{base}/metatiles.bin");\nconst u16 {sy}_Attributes[] = INCBIN_U16("{base}/metatile_attributes.bin");')
  headers.append(f'const struct Tileset {sy} = {{.isCompressed=TRUE,.isSecondary={"TRUE" if meta["role"]=="secondary" else "FALSE"},.tiles={sy}_Tiles,.palettes={sy}_Palettes,.metatiles={sy}_Metatiles,.metatileAttributes={sy}_Attributes,.callback=NULL}};')
 for kind,lines in [('graphics',graphics),('metatiles',metas),('headers',headers)]:
  (R/f'src/data/tilesets/gs_johto_{kind}.h').write_text('\n'.join(lines)+'\n');append(R/f'src/data/tilesets/{kind}.h','\n'.join(lines))
 maps={};spawns={};grids={};ledger=[];holds=[];warp_lookup={};types={1:'MAP_TYPE_TOWN',2:'MAP_TYPE_CITY',3:'MAP_TYPE_ROUTE',4:'MAP_TYPE_UNDERGROUND',5:'MAP_TYPE_UNDERWATER',6:'MAP_TYPE_OCEAN_ROUTE',8:'MAP_TYPE_INDOOR',9:'MAP_TYPE_SECRET_BASE'}
 for row in rows:
  k=row['id'];d=donors[k];n=names[k];w,h=d['width'],d['height'];b=(folders[k]/'blockdata.bin').read_bytes();cells=list(struct.unpack('<'+'H'*(len(b)//2),b));aa=attrs[d['primary_tileset']]+attrs[d['secondary_tileset']];patch=[]
  for i,v in enumerate(cells):
   if (v>>10&3)==0 and (aa[v&1023]&255) in range(0x10,0x16) and v>>12!=1:cells[i]=(v&4095)|4096;patch.append(i)
  floor={i for i,v in enumerate(cells) if v>>10&3==0 and v>>12 in [0,3] and aa[v&1023]&255==0};candidates=[i for i in floor if i-w in floor and i+w in floor and i%w>0 and i%w<w-1 and i-1 in floor and i+1 in floor]
  # Prefer an actual door apron, not the unreviewed map center.
  anchors=[(z['x'],z['y']+1) for z in d['warps'] if 0<z['x']<w-1 and 0<z['y']<h-2]
  if candidates:
   i=min(candidates,key=lambda i:min([abs(i%w-x)+abs(i//w-y) for x,y in anchors] or [abs(i%w-w//2)+abs(i//w-h//2)]));spawns[k]=[i%w,i//w]
  base=f'data/gs_johto_assets/layouts/{n}';(R/base).mkdir(parents=True,exist_ok=True);(R/base/'map.bin').write_bytes(struct.pack('<'+'H'*len(cells),*cells));shutil.copy2(folders[k]/'border.bin',R/base/'border.bin')
  l=dict(id='LAYOUT_'+n.upper(),name=n+'_Layout',width=w,height=h,primary_tileset='gTileset_GSJohto_'+d['primary_tileset'],secondary_tileset='gTileset_GSJohto_'+d['secondary_tileset'],blockdata_filepath=base+'/map.bin',border_filepath=base+'/border.bin',border_width=d['border']['width'],border_height=d['border']['height'],layout_version='emerald');ls['layouts'].append(l)
  m=dict(id='MAP_'+n.upper(),name=n,layout=l['id'],region_map_section='MAPSEC_GS_JOHTO',music='MUS_ROUTE104',weather='WEATHER_NONE',map_type=types.get(d['map_type'],'MAP_TYPE_INDOOR'),requires_flash=False,allow_cycling=True,allow_running=True,allow_escaping=False,show_map_name=True,battle_scene='MAP_BATTLE_SCENE_NORMAL',connections=None,object_events=[],warp_events=[],coord_events=[],bg_events=[]);maps[k]=m;grids[k]=(w,h,cells,aa)
  banks=[g for g in groups['group_order'] if g.startswith('gMapGroup_AMap_Bank') and len(groups[g])<120];assert banks,'No safe existing map bank capacity';group=banks[0];groups[group].append(n)
  from PIL import Image
  pic=Image.open(folders[k]/'preview.png');blank=len(set(pic.getdata()))<20
  ledger.append(dict(donor_id=k,map=n,name=d['name'],mapsec='MAPSEC_GS_JOHTO',map_group=group,dimensions=[w,h],source=d,water_elevation_cells=patch,blank_or_low_detail=blank,spawn=spawns.get(k),gameplay_owner='project',animation='STATIC_PENDING_CALLBACK_PORT'))
  if blank or k not in spawns:holds.append(dict(id=k,name=d['name'],reason='Blank/low-detail preview' if blank else 'No safe scientist/arrival cluster'))
 # Only retain static, in-range destinations within the selected Johto inventory.
 for k,d in donors.items():
  w,h,_,_=grids[k]
  for z in d['warps']:
   dk=z['target_id'];di=z['dest_warp_id'];target=donors.get(dk);dz=next((a for a in target['warps'] if a['index']==di),None) if target else None
   if z['dynamic_target'] or not dz or not (0<=z['x']<w and 0<=z['y']<h) or not (0<=dz['x']<target['width'] and 0<=dz['y']<target['height']):continue
   warp_lookup[(k,z['index'])]=len(maps[k]['warp_events']);maps[k]['warp_events'].append(dict(x=z['x'],y=z['y'],elevation=z['elevation'],dest_map=maps[dk]['id'],dest_warp_id=str(di),_source=z['index']))
 for k,m in maps.items():
  keep=[]
  for z in m['warp_events']:
   source=next(a for a in donors[k]['warps'] if a['index']==z['_source']);dest=(source['target_id'],source['dest_warp_id'])
   if dest in warp_lookup:keep.append(z)
  m['warp_events']=keep
 # Iteratively remove edges whose destination source slot is not present.
 while True:
  lookup={(k,z['_source']):i for k,m in maps.items() for i,z in enumerate(m['warp_events'])};removed=0
  for k,m in maps.items():
   out=[]
   for z in m['warp_events']:
    source=next(a for a in donors[k]['warps'] if a['index']==z['_source']);dk=source['target_id'];di=lookup.get((dk,source['dest_warp_id']))
    if di is None:removed+=1
    else:z['dest_warp_id']=str(di);out.append(z)
   m['warp_events']=out
  if not removed:break
 for k,m in maps.items():
  for z in m['warp_events']:z.pop('_source')
  con=[]
  for c in donors[k]['connections']:
   if c['target_id'] in maps and c['direction'] in ['up','down','left','right']:con.append(dict(direction=c['direction'],offset=c['offset'],map=maps[c['target_id']]['id']))
  m['connections']=con or None
 order=sorted(spawns,key=lambda k:tuple(map(int,k.split('.'))));scripts=[]
 for k,m in maps.items():
  n=m['name'];body=n+'_MapScripts::\n\t.byte 0\n'
  if k in spawns:
   x,y=spawns[k];v=grids[k][2][(y-1)*grids[k][0]+x];m['object_events'].append(dict(local_id='LOCALID_'+n.upper()+'_SCIENTIST',graphics_id='OBJ_EVENT_GFX_SCIENTIST_1',x=x,y=y-1,elevation=v>>12,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script=n+'_Inspect',flag='0'))
   nk=order[(order.index(k)+1)%len(order)];nx,ny=spawns[nk]
   body+=f'\n{n}_Inspect::\n\tlock\n\tfaceplayer\n\tmsgbox {n}_Text, MSGBOX_YESNO\n\tgoto_if_eq VAR_RESULT, YES, {n}_Next\n\tclosemessage\n\twarp MAP_LITTLEROOT_TOWN, 10, 17\n\twaitstate\n\trelease\n\tend\n{n}_Next::\n\tclosemessage\n\twarp {maps[nk]["id"]}, {nx}, {ny}\n\twaitstate\n\trelease\n\tend\n{n}_Text:\n\t.string "Johto {k}: under construction.\\n"\n\t.string "YES: next map. NO: Littleroot.$"\n'
  for e in m['object_events']:
   occupied={(z['x'],z['y']) for z in m['warp_events']}
   if (e['x'],e['y']) in occupied:
    x,y=e['x'],e['y'];w,h,cells,aa=grids[k]
    options=[(x+1,y+1),(x-1,y+1),(x+1,y),(x-1,y)]
    options=[(xx,yy) for xx,yy in options if 0<=xx<w and 0<=yy<h and (xx,yy) not in occupied and (cells[yy*w+xx]>>10&3)==0]
    if options:e['x'],e['y']=options[0];e['elevation']=cells[e['y']*w+e['x']]>>12
  dump(R/'data/maps'/n/'map.json',m);(R/'data/maps'/n/'scripts.inc').write_text(body);append(R/'data/event_scripts.s',f'.include "data/maps/{n}/scripts.inc"')
 p=R/'src/data/script_menu.h';text=p.read_text().replace('{COMPOUND_STRING("BWA MAP TEST")},','{COMPOUND_STRING("BWA MAP TEST")},\n    {COMPOUND_STRING("JOHTO")},');p.write_text(text)
 k='3.0';assert k in spawns;x,y=spawns[k];p=R/'data/scripts/la_teleport_scientist.inc';text=p.read_text().replace('\t@ 5 = CANCEL','\tgoto_if_eq VAR_RESULT, 5, LA_TeleportScientist_WarpJohto\n\t@ 6 = CANCEL');text+=f'\nLA_TeleportScientist_WarpJohto::\n\tclosemessage\n\twarp {maps[k]["id"]}, {x}, {y}\n\twaitstate\n\trelease\n\tend\n';p.write_text(text)
 dump(R/'data/layouts/layouts.json',ls);dump(R/'data/maps/map_groups.json',groups);dump(R/'src/data/region_map/region_map_sections.json',sections)
 for g,old in before.items():assert groups[g][:len(old)]==old
 for f,digest in protected.items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==digest,f
 dump(O/'manifest.json',ledger);dump(O/'manual_review.json',holds);dump(O/'behavior_translation.json',translation);dump(O/'receipt.json',dict(maps=len(maps),tilesets=len(keys),protected=protected,previous_numeric_ids_preserved=True,donor_gameplay_imported=False,animation_callbacks_pending=True,inspection_order=order,rom_runtime_verified=False));print('PORTED',len(maps),'maps',len(keys),'banks',len(holds),'review maps')
if __name__=='__main__':main()
