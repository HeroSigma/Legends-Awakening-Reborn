#!/usr/bin/env python3
"""Replace Johto's project-owned asset/travel layer with Mercury geometry.
Retain existing IDs, exclude donor gameplay, quarantine unmapped GS destinations.
"""
import argparse,collections,csv,hashlib,json,math,re,shutil,struct,subprocess
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4];S=R/'.la_work/amap/mercury_full_v11';D=R/'docs/la_world/mercury_johto';B=R/'.la_work/amap/mercury_johto_backup'
def load(p):return json.loads(p.read_text())
def dump(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub('[^a-z0-9]','',s.lower())
def sid(s):return tuple(map(int,s.split('.')))
def role(t,w,h):
 if t in [1,2,3,6] and w*h>=400:return 'outside'
 if t==4:return 'cave'
 return 'room'
def prepare():
 mf=load(S/'manifest.json');src={m['id']:m for m in mf['maps']};bad={k for k,t in mf['tilesets'].items() if 'fallback' in t['source'].get('compression_mode','')}
 seeds=[f'3.{i}' for i in range(66,108)]+['56.25','56.26','56.27']
 selected=set(seeds);queue=list(seeds)
 while queue:
  k=queue.pop()
  for z in src[k]['connections']+src[k]['warps']:
   t=z['target_id']
   if t not in src or t in selected:continue
   m=src[t];g,n=sid(t)
   if g==3 and n<66 and n not in [45,46,47,48,49]:continue
   if m['region_map_section_id']<143 and m['region_map_section_id'] not in [99,127,132,134,135,140] and g<42:continue
   if m['width']<8 or m['height']<8 or m['primary_tileset'] in bad or m['secondary_tileset'] in bad:continue
   selected.add(t);queue.append(t)
 groups=load(R/'data/maps/map_groups.json');layouts=load(R/'data/layouts/layouts.json');ls={l['id']:l for l in layouts['layouts']}
 previous={x['source']['id']:x for x in load(R/'docs/la_world/gs_johto/manifest.json')};old={};oldsource={}
 for g in groups['group_order']:
  if 'Johto' not in g:continue
  for name in groups[g]:
   m=load(R/'data/maps'/name/'map.json');match=re.match(r'MAP_GSJOHTO_(\d+)_(\d+)_',m['id']);assert match,name
   old[name]=m;oldsource[name]=previous['.'.join(match.groups())]['source']
 pairs=[]
 for name,o in oldsource.items():
  family=norm(o['name']);family={'lighthouse':'glitterlighthouse'}.get(family,family)
  orole=role(o['map_type'],o['width'],o['height'])
  for k in selected:
   m=src[k]
   if norm(m['name'])!=family or role(m['map_type'],m['width'],m['height'])!=orole:continue
   # All current Johto gameplay is project construction inspection. Match same
   # location/role by geometry only; no donor gameplay identity is inferred.
   distance=abs(math.log(m['width']/o['width']))+abs(math.log(m['height']/o['height']))
   distance+=abs(len(m['warps'])-len(o['warps']))*.025
   pairs.append((distance,name,k))
 matched={};used=set()
 # Anchor the main world destinations; older same-name donor placeholders are excluded.
 anchors={'3.0':'3.66','3.1':'3.67','3.2':'3.68','3.3':'3.69','3.4':'3.74','3.5':'3.75','3.6':'3.70','3.7':'3.72','3.8':'3.73','3.10':'3.71','3.11':'3.100','1.0':'1.121','1.88':'1.47','1.12':'1.124'}
 for name,o in oldsource.items():
  if o['id'] in anchors:
   k=anchors[o['id']];assert k in selected,(name,k);matched[name]=k;used.add(k)
 for score,name,k in sorted(pairs):
  if name not in matched and k not in used:matched[name]=k;used.add(k)
 names={k:name for name,k in matched.items()};ids={k:old[name]['id'] for k,name in names.items()};new=[]
 for k in sorted(selected-used,key=sid):
  m=src[k];name='Johto_Mercury_'+k.replace('.','_')+'_'+re.sub('[^A-Za-z0-9]+','_',m['name']).strip('_');names[k]=name;ids[k]='MAP_'+name.upper();new.append(name)
 plan=dict(donor='Mercury English beta 2',source_sha256=mf['rom']['sha256'],selected=sorted(selected,key=sid),matched_existing=matched,new_maps=new,unmatched_registered=[n for n in old if n not in matched],policy='Unmatched registered maps retain their assets; active entrances and inspection tours exclude them. No donor gameplay.',names=names,ids=ids)
 D.mkdir(parents=True,exist_ok=True);dump(D/'replacement_plan.json',plan)
 return mf,src,selected,groups,layouts,old,oldsource,plan

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
 if (D/'receipt.json').exists():
  if a.apply:raise SystemExit('Already applied; refusing to overwrite the preserved baseline')
  print('EXISTING REPLACEMENT',load(D/'receipt.json'));return
 mf,src,selected,groups,layouts,old,oldsource,plan=prepare()
 print('PLAN',len(selected),'Mercury maps;',len(plan['matched_existing']),'retained IDs;',len(plan['new_maps']),'additional geometry destinations;',len(plan['unmatched_registered']),'held old maps',flush=True)
 if not a.apply:return
 assert not (D/'receipt.json').exists(),'Already applied'
 assert hashlib.sha256(Path(mf['rom']['path']).read_bytes()).hexdigest()==mf['rom']['sha256']
 shared={'data/layouts/layouts.json','data/maps/map_groups.json','data/event_scripts.s','data/scripts/la_teleport_scientist.inc','src/data/tilesets/headers.h','src/data/tilesets/graphics.h','src/data/tilesets/metatiles.h'}
 editable=shared|{f'data/maps/{n}/{f}' for n in old for f in ['map.json','scripts.inc']}
 protected={str(p.relative_to(R)):sha(p) for root in ['data','src','include','graphics'] for p in (R/root).rglob('*') if p.is_file() and str(p.relative_to(R)) not in editable}
 beforegroups=json.loads(json.dumps(groups));oldnames=set(old);backups={}
 for rel in sorted(editable):
  p=R/rel
  if p.exists():
   q=B/rel;q.parent.mkdir(parents=True,exist_ok=True);assert not q.exists(),('Backup already exists',q);shutil.copy2(p,q);backups[rel]=sha(p)
 dump(B/'before.json',dict(backups=backups,protected=protected,groups=beforegroups))
 native=enums(R/'include/constants/metatile_behaviors.h');fr={int(v,16):n for n,v in re.findall(r'#define (MB_\w+) (0x[0-9A-Fa-f]+)',(R/'.la_work/amap/firered_behaviors_reference.h').read_text())}
 alias={'MB_ROCK_STAIRS':'MB_NORMAL','MB_SAND_CAVE':'MB_CAVE','MB_RUNNING_DISALLOWED':'MB_NO_RUNNING','MB_WARP_DOOR':'MB_NON_ANIMATED_DOOR','MB_CAVE_DOOR':'MB_NON_ANIMATED_DOOR','MB_REGULAR_WARP':'MB_NON_ANIMATED_DOOR'}
 folders={load(p)['id']:p.parent for p in (S/'maps').glob('*/map.json')};keys=sorted({src[k][f] for k in selected for f in ['primary_tileset','secondary_tileset']});banks={};translations=[];used={k:set() for k in keys}
 for key in keys:
  folder=S/'tilesets'/key;target=R/'data/mercury_johto_assets/tilesets'/key;shutil.copytree(folder,target);raw=(folder/'source_frlg_metatile_attributes.bin').read_bytes();attrs=bytearray((folder/'metatile_attributes.bin').read_bytes());tiles=bytearray((folder/'metatiles.bin').read_bytes())
  for i in range(512):
   v=struct.unpack_from('<I',raw,i*4)[0]&511;label=alias.get(fr.get(v),fr.get(v));known=label in native
   if not known:label='MB_NORMAL'
   oldattr=struct.unpack_from('<H',attrs,i*2)[0];struct.pack_into('<H',attrs,i*2,(oldattr&0xf000)|native[label]);translations.append(dict(bank=key,index=i,donor=v,native=label,known=known))
  banks[key]=dict(target=target,raw=raw,attrs=attrs,tiles=tiles)
 names=plan['names'];ids=plan['ids'];ls={l['id']:l for l in layouts['layouts']};rows={};cellsledger=[];warpfix=[];holds=[]
 for k in sorted(selected,key=sid):
  source=src[k];name=names[k];m=json.loads(json.dumps(old[name])) if name in old else dict(id=ids[k],name=name,layout='LAYOUT_'+name.upper(),region_map_section='MAPSEC_GS_JOHTO',music='MUS_ROUTE104',weather='WEATHER_NONE',requires_flash=False,allow_cycling=True,allow_running=True,allow_escaping=False,show_map_name=True,battle_scene='MAP_BATTLE_SCENE_NORMAL',object_events=[],coord_events=[],bg_events=[])
  l=ls[m['layout']] if name in old else dict(id=m['layout'],name=name+'_Layout')
  if name not in old:
   layouts['layouts'].append(l);gs=[g for g in groups['group_order'] if 'Johto' in g and len(groups[g])<127];assert gs,'No Johto group capacity';group=min(gs,key=lambda g:len(groups[g]));groups[group].append(name)
  base=f'data/mercury_johto_assets/layouts/{name}';l.update(width=source['width'],height=source['height'],primary_tileset='gTileset_Mercury_'+source['primary_tileset'],secondary_tileset='gTileset_Mercury_'+source['secondary_tileset'],blockdata_filepath=base+'/map.bin',border_filepath=base+'/border.bin',border_width=source['border']['width'],border_height=source['border']['height'],layout_version='emerald')
  (R/base).mkdir(parents=True);shutil.copy2(folders[k]/'border.bin',R/base/'border.bin');blob=(folders[k]/'blockdata.bin').read_bytes();cells=list(struct.unpack('<'+'H'*(len(blob)//2),blob));kk=[source['primary_tileset'],source['secondary_tileset']]
  for value, in struct.iter_unpack('<H',blob+(folders[k]/'border.bin').read_bytes()):used[kk[(value&1023)//512]].add(value&511)
  rows[k]=dict(m=m,l=l,cells=cells,keys=kk)
 def rawbeh(row,mid):return struct.unpack_from('<I',banks[row['keys'][mid//512]]['raw'],(mid%512)*4)[0]&511
 def beh(row,mid):return struct.unpack_from('<H',banks[row['keys'][mid//512]]['attrs'],(mid%512)*2)[0]&255
 clones={}
 def clone(row,mid,want):
  key=row['keys'][mid//512];bank=banks[key];pair=(key,mid%512,want)
  if pair not in clones:
   available=[i for i in range(511,-1,-1) if i not in used[key]];assert available,('No spare metatile',key);slot=available[0];used[key].add(slot);clones[pair]=slot;bank['tiles'][slot*16:slot*16+16]=bank['tiles'][(mid%512)*16:(mid%512)*16+16];v=struct.unpack_from('<H',bank['attrs'],mid%512*2)[0];struct.pack_into('<H',bank['attrs'],slot*2,(v&0xf000)|want)
  return mid//512*512+clones[pair]
 # Inbound edges resolve rooms whose stale donor exits still name a Kanto parent.
 inbound=collections.defaultdict(list)
 for k in selected:
  for z in src[k]['warps']:
   if z['target_id'] in selected:inbound[(z['target_id'],z['dest_warp_id'])].append((k,z['index']))
 enabled={k:{} for k in selected}
 for k,row in rows.items():
  m=row['m'];source=src[k];m['warp_events']=[];w,h=row['l']['width'],row['l']['height']
  for z in source['warps']:
   target=z['target_id'];wid=z['dest_warp_id'];reason=None
   if z['dynamic_target'] or target not in selected:
    parent=inbound.get((k,z['index']),[])
    if len(parent)==1:
     target,wid=parent[0];warpfix.append(dict(source=k,warp=z['index'],old=z['target_id'],new=target,dest_warp=wid,reason='Unique reciprocal project parent'))
    else:reason='Dynamic/stale/out-of-region destination has no unique reciprocal parent'
   tz=next((q for q in src.get(target,{}).get('warps',[]) if q['index']==wid),None)
   if not reason and (target not in selected or tz is None):reason='Missing physical destination slot'
   if not reason:
    dl=rows[target]['l']
    if not (0<=tz['x']<dl['width'] and 0<=tz['y']<dl['height']):reason='Invalid destination coordinate'
   if reason:
    holds.append(dict(source=k,warp=z['index'],target=z['target_id'],reason=reason));continue
   enabled[k][z['index']]=(z,target,wid)
 # Drop chains ending at disabled slots, then rebuild compact destination indices.
 while True:
  remove=[(k,i) for k,v in enabled.items() for i,(z,t,j) in v.items() if j not in enabled[t]]
  if not remove:break
  for k,i in remove:holds.append(dict(source=k,warp=i,target=enabled[k][i][1],reason='Destination event disabled'));del enabled[k][i]
 lookup={(k,i):n for k,v in enabled.items() for n,i in enumerate(v)}
 warpsymbol={0x60:'MB_NON_ANIMATED_DOOR',0x61:'MB_LADDER',0x62:'MB_EAST_ARROW_WARP',0x63:'MB_WEST_ARROW_WARP',0x64:'MB_NORTH_ARROW_WARP',0x65:'MB_SOUTH_ARROW_WARP',0x66:'MB_LADDER',0x67:'MB_NON_ANIMATED_DOOR',0x68:'MB_LADDER',0x69:'MB_NON_ANIMATED_DOOR',0x6a:'MB_UP_ESCALATOR',0x6b:'MB_DOWN_ESCALATOR',0x6c:'MB_UP_RIGHT_STAIR_WARP',0x6d:'MB_UP_LEFT_STAIR_WARP',0x6e:'MB_DOWN_RIGHT_STAIR_WARP',0x6f:'MB_DOWN_LEFT_STAIR_WARP',0x71:'MB_LADDER'}
 spawns={};eventledger=[]
 for k,row in rows.items():
  m,l,cells=row['m'],row['l'],row['cells'];w,h=l['width'],l['height'];source=src[k]
  for i,v in enumerate(cells):
   if rawbeh(row,v&1023) in [0x10,0x11,0x12,0x13,0x15] and (v>>10&3)==0 and v>>12 not in [1,15]:
    cells[i]=(v&4095)|0x1000;cellsledger.append(dict(map=names[k],x=i%w,y=i//w,before=v,after=cells[i],reason='Native Surf water elevation'))
  warpcoords=set()
  for i,(z,t,j) in enabled[k].items():
   pos=z['y']*w+z['x'];assert 0<=pos<len(cells);before=cells[pos];mid=before&1023;wanted=native[warpsymbol.get(rawbeh(row,mid),'MB_NON_ANIMATED_DOOR')]
   if beh(row,mid)!=wanted:mid=clone(row,mid,wanted)
   cells[pos]=mid|0x3000;warpcoords.add((z['x'],z['y']));m['warp_events'].append(dict(x=z['x'],y=z['y'],elevation=3,dest_map=ids[t],dest_warp_id=str(lookup[(t,j)])))
   if before!=cells[pos]:cellsledger.append(dict(map=names[k],x=z['x'],y=z['y'],before=before,after=cells[pos],reason='Native static warp cell'))
  # Disabled donor entrances retain artwork but lose their travel behavior at that cell.
  for z in source['warps']:
   if z['index'] in enabled[k]:continue
   pos=z['y']*w+z['x'];v=cells[pos];mid=v&1023
   if beh(row,mid)!=native['MB_NORMAL']:mid=clone(row,mid,native['MB_NORMAL'])
   cells[pos]=(v&0xfc00)|mid
  m['connections']=[dict(direction=z['direction'],offset=z['offset'],map=ids[z['target_id']]) for z in source['connections'] if z['target_id'] in selected and z['direction'] in ['up','down','left','right']] or None
  floor={i for i,v in enumerate(cells) if (v>>10&3)==0 and v>>12 in [0,3] and beh(row,v&1023) in {native[n] for n in ['MB_NORMAL','MB_CAVE','MB_INDOOR_ENCOUNTER','MB_SHORT_GRASS','MB_SAND','MB_FOOTPRINTS']} and (i%w,i//w) not in warpcoords}
  valid=[i for i in floor if 0<i%w<w-1 and i-w in floor and i+w in floor and i-1 in floor and i+1 in floor]
  if not valid:
   valid=[i for i in floor if i-w in floor]
  if not valid:
   m['object_events']=[];m['coord_events']=[];m['bg_events']=[];m['map_type']={1:'MAP_TYPE_TOWN',2:'MAP_TYPE_CITY',3:'MAP_TYPE_ROUTE',4:'MAP_TYPE_UNDERGROUND',8:'MAP_TYPE_INDOOR'}.get(source['map_type'],'MAP_TYPE_INDOOR');holds.append(dict(source=k,reason='No safe land-based inspection actor/arrival'));(R/l['blockdata_filepath']).write_bytes(struct.pack('<'+'H'*len(cells),*cells));dump(R/'data/maps'/names[k]/'map.json',m);continue
  anchors=[(z['x'],z['y']+1) for z in source['warps']]
  pos=min(valid,key=lambda i:(min([abs(i%w-x)+abs(i//w-y) for x,y in anchors] or [abs(i%w-w//2)+abs(i//w-h//2)]),i));x,y=pos%w,pos//w;spawns[k]=[x,y]
  oldevents=m['object_events'];script=oldevents[0]['script'] if oldevents else names[k]+'_Inspect';local=oldevents[0]['local_id'] if oldevents else 'LOCALID_'+names[k].upper()+'_SCIENTIST'
  m['object_events']=[dict(local_id=local,graphics_id='OBJ_EVENT_GFX_SCIENTIST_1',x=x,y=y-1,elevation=cells[(y-1)*w+x]>>12,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script=script,flag='0')];m['coord_events']=[];m['bg_events']=[]
  m['map_type']={1:'MAP_TYPE_TOWN',2:'MAP_TYPE_CITY',3:'MAP_TYPE_ROUTE',4:'MAP_TYPE_UNDERGROUND',8:'MAP_TYPE_INDOOR'}.get(source['map_type'],'MAP_TYPE_INDOOR');m['show_map_name']=True;m['allow_running']=True
  eventledger.append(dict(map=names[k],source=k,old_events=oldevents,new_events=m['object_events'],arrival=spawns[k],reason='Construction inspector on source-geometry free five-cell cluster; no story actor or donor event logic'))
  (R/l['blockdata_filepath']).write_bytes(struct.pack('<'+'H'*len(cells),*cells));dump(R/'data/maps'/names[k]/'map.json',m)
 # Native engine stores all metatiles as twelve explicit tiles (three layers).
 payloads={};declarations={k:[] for k in ['graphics','metatiles','headers']}
 def binary_symbol(kind,data,alignment):
  digest=hashlib.sha256(data).hexdigest();key=(kind,digest)
  if key in payloads:return payloads[key]
  sym='gMercury_'+kind+'_'+digest[:20];suffix='.4bpp.lz' if kind=='Tiles' else '.gbapal' if kind=='Palettes' else '.bin';path=R/'data/mercury_johto_assets/shared'/(sym+suffix);path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data);rel=path.relative_to(R).as_posix();
  if kind=='Palettes':
   folder=path.with_suffix('');folder.mkdir(exist_ok=True);lines=[]
   for i in range(16):
    pp=folder/f'{i:02}.gbapal';pp.write_bytes(data[i*32:i*32+32]);colors=struct.unpack('<16H',pp.read_bytes());pp.with_suffix('.pal').write_text('JASC-PAL\n0100\n16\n'+''.join(f'{(v&31)*255//31} {((v>>5)&31)*255//31} {((v>>10)&31)*255//31}\n' for v in colors));lines.append(f' INCBIN_U16("{pp.relative_to(R).as_posix()}"),')
   declarations['graphics'].append(f'const u16 {sym}[][16] = {{\n'+'\n'.join(lines)+'\n};')
  else:declarations['graphics' if kind=='Tiles' else 'metatiles'].append(f'const {alignment} {sym}[] = INCBIN_{alignment.upper()}("{rel}");')
  payloads[key]=sym;return sym
 for key,bank in banks.items():
  target=bank['target'];rawtiles=target/'tiles.4bpp';compressed=target/'tiles.4bpp.lz';subprocess.run([str(R/'tools/gbagfx/gbagfx'),str(rawtiles),str(compressed)],check=True,stdout=subprocess.DEVNULL)
  palette=bytearray()
  for slot in range(16):
   p=target/f'palettes/{slot:02}.pal'
   if not p.exists():p.write_text('JASC-PAL\n0100\n16\n'+'0 0 0\n'*16)
   colors=[tuple(map(int,line.split())) for line in p.read_text().splitlines()[3:19]];palette.extend(b''.join(struct.pack('<H',(a>>3)|((b>>3)<<5)|((c>>3)<<10)) for a,b,c in colors))
  triple=[]
  for i in range(512):
   low=list(struct.unpack_from('<4H',bank['tiles'],i*16));high=list(struct.unpack_from('<4H',bank['tiles'],i*16+8));layer=struct.unpack_from('<H',bank['attrs'],i*2)[0]>>12
   triple+=([0x3014]*4+low+high) if layer==0 else (low+[0]*4+high) if layer==2 else (low+high+[0]*4)
  meta=struct.pack('<6144H',*triple);(target/'metatiles.bin').write_bytes(meta);(target/'metatile_attributes.bin').write_bytes(bank['attrs']);(target/'palettes.gbapal').write_bytes(palette)
  ts=binary_symbol('Tiles',compressed.read_bytes(),'u32');shutil.copy2(target/'tiles.png',R/'data/mercury_johto_assets/shared'/(ts+'.png'));ps=binary_symbol('Palettes',bytes(palette),'u16');ms=binary_symbol('Metatiles',meta,'u16');aa=binary_symbol('Attributes',bytes(bank['attrs']),'u16');secondary=mf['tilesets'][key]['role']=='secondary'
  declarations['headers'].append(f'const struct Tileset gTileset_Mercury_{key} = {{ .isCompressed=TRUE, .isSecondary={"TRUE" if secondary else "FALSE"}, .tiles={ts}, .palettes={ps}, .metatiles={ms}, .metatileAttributes={aa}, .callback=NULL }};')
 for kind,lines in declarations.items():
  p=R/f'src/data/tilesets/mercury_johto_{kind}.h';p.write_text('\n\n'.join(lines)+'\n');main=R/f'src/data/tilesets/{kind}.h';main.write_text(main.read_text().rstrip()+f'\n\n#include "mercury_johto_{kind}.h"\n')
 order=['3.66']+[k for k in sorted(spawns,key=sid) if k!='3.66'];includes=[]
 def inspector_text(name,script,nxt,message):
  x,y=spawns[nxt]
  return f'{name}_MapScripts::\n\t.byte 0\n\n{script}::\n\tlock\n\tfaceplayer\n\tmsgbox {script}_Text, MSGBOX_YESNO\n\tgoto_if_eq VAR_RESULT, YES, {script}_Next\n\tclosemessage\n\twarp MAP_LITTLEROOT_TOWN, 10, 17\n\twaitstate\n\trelease\n\tend\n{script}_Next::\n\tclosemessage\n\twarp {ids[nxt]}, {x}, {y}\n\twaitstate\n\trelease\n\tend\n{script}_Text:\n\t.string "{message}\\p"\n\t.string "YES: next. NO: Littleroot.$"\n'
 for i,k in enumerate(order):
  m=rows[k]['m'];name=names[k];text=inspector_text(name,m['object_events'][0]['script'],order[(i+1)%len(order)],'Mercury Johto '+k+'. Under construction.');(R/'data/maps'/name/'scripts.inc').write_text(text)
  if name not in old:includes.append(f'.include "data/maps/{name}/scripts.inc"')
 for k in selected-set(spawns):
  name=names[k];(R/'data/maps'/name/'scripts.inc').write_text(name+'_MapScripts::\n\t.byte 0\n')
  if name not in old:includes.append(f'.include "data/maps/{name}/scripts.inc"')
 for name in plan['unmatched_registered']:
  m=old[name]
  # Preserve the archived layout/events; the inspector offers only the new hub.
  if m['object_events']:
   (R/'data/maps'/name/'scripts.inc').write_text(inspector_text(name,m['object_events'][0]['script'],'3.66','Area held. No Mercury counterpart.'))
 # Remove every direct entrance from held maps into the old world, and vice versa.
 heldids={old[n]['id'] for n in plan['unmatched_registered']}
 for name in plan['unmatched_registered']:
  m=json.loads(json.dumps(old[name]));m['warp_events']=[];m['connections']=None;dump(R/'data/maps'/name/'map.json',m)
 x,y=spawns['3.66'];p=R/'data/scripts/la_teleport_scientist.inc';text=p.read_text();hub=ids['3.66'];text,count=re.subn(r'(warp '+re.escape(hub)+r'),\s*\d+,\s*\d+',rf'\1, {x}, {y}',text);assert count==1; p.write_text(text)
 ep=R/'data/event_scripts.s';ep.write_text(ep.read_text().rstrip()+'\n'+'\n'.join(includes)+'\n');dump(R/'data/layouts/layouts.json',layouts);dump(R/'data/maps/map_groups.json',groups)
 for g in beforegroups['group_order']:assert groups[g][:len(beforegroups[g])]==beforegroups[g]
 for rel,hsh in protected.items():assert sha(R/rel)==hsh,('Unexpected protected change',rel)
 dump(D/'behavior_translation.json',translations);dump(D/'coordinate_ledger.json',eventledger);dump(D/'cell_reconciliation.json',cellsledger);dump(D/'travel_remaps.json',warpfix);dump(D/'disabled_travel.json',holds);dump(D/'inspection_arrivals.json',[dict(source=k,map=names[k],id=ids[k],spawn=spawns[k]) for k in order])
 dump(D/'asset_recovery.json',load(S/'asset_recovery.json'))
 dump(D/'receipt.json',dict(applied=True,donor_gameplay_imported=False,source_sha256=mf['rom']['sha256'],replaced=len(plan['matched_existing']),added=len(plan['new_maps']),held=len(plan['unmatched_registered']),maps=len(selected),tilesets=len(keys),unique_asset_payloads=len(payloads),payload_bytes=sum((R/'data/mercury_johto_assets/shared'/(s+('.4bpp.lz' if kind=='Tiles' else '.gbapal' if kind=='Palettes' else '.bin'))).stat().st_size for (kind,digest),s in payloads.items()),warps=sum(len(row['m']['warp_events']) for row in rows.values()),connections=sum(len(row['m']['connections'] or []) for row in rows.values()),protected_files=len(protected),map_ids_preserved=True,numeric_ids_preserved=True,animations='SOURCE_REFERENCE_ONLY_CALLBACK_PORT_PENDING',runtime_verified=False))
 print('APPLIED',load(D/'receipt.json'),flush=True)
if __name__=='__main__':main()
