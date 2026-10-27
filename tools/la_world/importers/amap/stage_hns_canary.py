#!/usr/bin/env python3
"""Stage an additive Heart & Soul asset/travel canary; no donor gameplay."""
import json,re,struct,hashlib,shutil,subprocess
from pathlib import Path
from PIL import Image
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4];S=Path('/home/allan/la-scratch/pokehns-canary-source');D=R/'docs/la_world/hns_canary';A=R/'data/hns_canary_assets';B=R/'.la_work/amap/hns_canary_backup'
NAMES=['NewBarkTown_hns','Route29_hns','CherrygroveCity_hns','Route30_hns','Route31_hns','Gate_Route31_VioletCity_hns','VioletCity_hns','CherrygroveCity_Mart_hns','VioletCity_Gym_hns']
def load(p):return json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+'\n')
def backup(p):
 t=B/p.relative_to(R)
 if not t.exists():t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,t)
def save(p,s):
 if p.exists():backup(p)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
def binout(p,b):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def graphics(p):
 im=Image.open(p);assert im.mode=='P',p
 w,h=im.size;assert w%8==h%8==0;px=im.load();b=bytearray()
 for ty in range(h//8):
  for tx in range(w//8):
   for y in range(8):
    for x in range(0,8,2):
     a,z=px[tx*8+x,ty*8+y],px[tx*8+x+1,ty*8+y];assert a<16 and z<16,p;b.append(a|(z<<4))
 return bytes(b)
def png(b,p):
 im=Image.new('P',(128,((len(b)//32+15)//16)*8));pal=[i*17 for i in range(16) for _ in range(3)];im.putpalette(pal+[0]*(768-len(pal)));px=im.load()
 for i,v in enumerate(b):
  tile,off=divmod(i,32);x=(tile%16)*8+(off%4)*2;y=(tile//16)*8+off//4;px[x,y]=v&15;px[x+1,y]=v>>4
 im.save(p)
def palette(p):
 ls=p.read_text().splitlines();rgb=[list(map(int,l.split())) for l in ls[3:] if l.strip()];assert len(rgb)==16,p
 return b''.join(struct.pack('<H',(a>>3)|((b>>3)<<5)|((c>>3)<<10)) for a,b,c in rgb)
def main():
 assert not (D/'manifest.json').exists(),'Canary already staged; do not overwrite manual changes'
 D.mkdir(parents=True,exist_ok=True);B.mkdir(parents=True,exist_ok=True)
 # Protect preexisting maps/assets and capture all additive root edits separately.
 protect={}
 for root in [R/'data/maps',R/'data/layouts',R/'data/mercury_johto_assets']:
  for p in root.rglob('*'):
   if p.is_file() and not p.name.endswith('.inc'):protect[p.relative_to(R).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
 dump(B/'protected.json',protect)
 maps={n:load(S/'data/maps'/n/'map.json') for n in NAMES};layouts={l['id']:l for l in load(S/'data/layouts/layouts.json')['layouts']};native=enums(R/'include/constants/metatile_behaviors.h');donor=enums(S/'include/constants/metatile_behaviors.h');inverse={v:k for k,v in donor.items()};hl=(S/'src/data/tilesets/headers.h').read_text();gd=(S/'src/data/tilesets/graphics.h').read_text();ts={};translations=[]
 for n,m in maps.items():
  l=layouts[m['layout']]
  for f in ['primary_tileset','secondary_tileset']:
   key=l[f]
   if key in ts:continue
   body=re.search(r'const struct Tileset '+key+r'\s*=\s*\{.*?\};',hl,re.S)[0];sym=re.search(r'\.tiles\s*=\s*(\w+)',body)[1];path=re.search(re.escape(sym)+r'\[\].*?"([^"]+)"',gd,re.S)[1];folder=S/Path(path).parent
   raw=(folder/'metatile_attributes.bin').read_bytes();assert len(raw)%2==0;attrs=[]
   for i,(v,) in enumerate(struct.iter_unpack('<H',raw)):
    code=v&255;label=inverse.get(code,'UNUSED_PADDING_'+str(code));aliases={'MB_HEADBUTT_TREE':'MB_NORMAL','MB_BOOKSHELF_GREEN':'MB_BOOKSHELF','MB_SHOP_SHELF_DEPARTMENT':'MB_SHOP_SHELF','MB_SHOP_SHELF_DEPARTMENT_FORWARD':'MB_SHOP_SHELF','MB_TALL_GRASS_IMPASSABLE_NORTH':'MB_TALL_GRASS','MB_CAVE_IMPASSABLE_NORTH':'MB_CAVE','MB_WATER_NORTH_ARROW_WARP':'MB_NORTH_ARROW_WARP','MB_BRIDGE_OVER_ICE':'MB_NORMAL'};target='MB_NORMAL' if label.startswith('UNUSED_PADDING_') else aliases.get(label,label);assert target in native,(key,i,code,label,target)
    after=(v&0xf000)|native[target];attrs.append(after)
    if code!=native[target] or label!=target:translations.append(dict(bank=key,index=i,source=label,target=target,native=native[target],note='Asset/travel test alias; donor special gameplay excluded' if label!=target else 'Name-based behavior translation'))
   ts[key]=dict(folder=folder,tiles=graphics(folder/'tiles.png'),defs=(folder/'metatiles.bin').read_bytes(),attrs=attrs,callback=re.search(r'\.callback\s*=\s*(\w+)',body)[1])
 # Generate source-derived animation callbacks under unique names.
 animsrc=(S/'src/tileset_anims.c').read_text();start=animsrc.index('// Johto General primary tileset frame data');end=animsrc.index('// National Park secondary tileset frame data',start);anim=animsrc[start:end]
 start=animsrc.index('static const u16 sEcruteakTheater_Flower_Frame0');end=animsrc.index('// Azalea Town Gym secondary tileset frame data',start);anim+=animsrc[start:end]
 for begin,endmark in [('// Johto General primary tileset callbacks','// National Park secondary tileset callbacks'),('// Ecruteak Theater secondary tileset callbacks','// Azalea Town Gym secondary tileset callbacks')]:
  start=animsrc.index(begin);anim+=animsrc[start:animsrc.index(endmark,start)]
 for path in set(re.findall(r'INCBIN_U16\("([^"]+)"\)',anim)):
  out=A/'anim'/Path(path).relative_to('data/tilesets');binout(out,graphics((S/path).with_suffix('.png')));anim=anim.replace(path,out.relative_to(R).as_posix())
 symbols=set(re.findall(r'\b(?:sJohtoGeneral_\w+|sEcruteakTheater_\w+|InitTilesetAnim_JohtoGeneral|TilesetAnim_JohtoGeneral|QueueAnimTiles_JohtoGeneral_\w+|InitTilesetAnim_EcruteakTheater|TilesetAnim_EcruteakTheater|QueueAnimTiles_EcruteakTheater_\w+)\b',anim))
 for sym in sorted(symbols,key=len,reverse=True):anim=re.sub(r'\b'+sym+r'\b','HnSCanary_'+sym,anim)
 anim=anim.replace('sSecondaryTilesetBaseTile','640');protos=''.join(f'static void HnSCanary_{n}(u16);\n' for n in ['TilesetAnim_JohtoGeneral','QueueAnimTiles_JohtoGeneral_Flower','QueueAnimTiles_JohtoGeneral_SandWaterEdge','QueueAnimTiles_JohtoGeneral_Waterfall','QueueAnimTiles_JohtoGeneral_LandWaterEdge','TilesetAnim_EcruteakTheater','QueueAnimTiles_EcruteakTheater_Flower'])
 save(R/'src/hns_canary_anims.inc','// Graphical callbacks adapted from Heart & Soul; no gameplay.\n'+protos+anim)
 p=R/'src/tileset_anims.c';save(p,p.read_text()+'\n#include "hns_canary_anims.inc"\n')
 decls={'headers':'void HnSCanary_InitTilesetAnim_JohtoGeneral(void);\nvoid HnSCanary_InitTilesetAnim_EcruteakTheater(void);\n','graphics':'','metatiles':''};banks={}
 def bank(key,primary,secondary):
  if key in banks:return banks[key]
  src=ts[primary];sec=ts[secondary] if secondary else None
  if sec:
   tiles=src['tiles'][512*32:640*32].ljust(128*32,b'\0')+sec['tiles'];defs=src['defs'][512*16:640*16].ljust(128*16,b'\0')+sec['defs'];attrs=src['attrs'][512:640]+sec['attrs'];role=True;palpaths=[src['folder']/'palettes'/f'{i:02}.pal' if i<7 else sec['folder']/'palettes'/f'{i:02}.pal' for i in range(16)];callback=sec['callback']
  else:tiles=src['tiles'][:512*32];defs=src['defs'][:512*16];attrs=src['attrs'][:512];role=False;palpaths=[src['folder']/'palettes'/f'{i:02}.pal' for i in range(16)];callback=src['callback']
  assert len(tiles)<=512*32,(key,len(tiles));tiles=tiles.ljust(512*32,b'\0');attrs=(attrs+[0]*512)[:512];defs=defs.ljust(512*16,b'\0');converted=bytearray()
  for i,v in enumerate(attrs):
   lo=list(struct.unpack_from('<4H',defs,i*16));hi=list(struct.unpack_from('<4H',defs,i*16+8));layer=v>>12
   out=([0x3014]*4+lo+hi) if layer==0 else (lo+[0]*4+hi) if layer==2 else (lo+hi+[0]*4);converted.extend(struct.pack('<12H',*out))
  folder=A/'tilesets'/key;folder.mkdir(parents=True,exist_ok=True);binout(folder/'tiles.4bpp',tiles);png(tiles,folder/'tiles.png');binout(folder/'metatiles.bin',converted);binout(folder/'metatile_attributes.bin',struct.pack('<512H',*[(v&0xfff) for v in attrs]));paltext=[]
  for i,p in enumerate(palpaths):
   dest=folder/'palettes'/f'{i:02}.pal';dest.parent.mkdir(parents=True,exist_ok=True)
   if p.exists():shutil.copy2(p,dest);raw=palette(p)
   else:dest.write_text('JASC-PAL\n0100\n16\n'+'0 0 0\n'*16);raw=bytes(32)
   binout(dest.with_suffix('.gbapal'),raw);paltext.append(f'    INCBIN_U16("{dest.with_suffix(".gbapal").relative_to(R).as_posix()}"),')
  sym='gTileset_HnSCanary_'+key;prefix='gHnSCanary_'+key;rel=folder.relative_to(R).as_posix();decls['graphics']+=f'const u32 {prefix}_Tiles[] = INCBIN_U32("{rel}/tiles.4bpp");\nconst u16 {prefix}_Palettes[][16] = {{\n'+ '\n'.join(paltext)+'\n};\n';decls['metatiles']+=f'const u16 {prefix}_Metatiles[] = INCBIN_U16("{rel}/metatiles.bin");\nconst u16 {prefix}_Attributes[] = INCBIN_U16("{rel}/metatile_attributes.bin");\n'
  cb='HnSCanary_'+callback if callback!='NULL' else 'NULL';decls['headers']+=f'const struct Tileset {sym} = {{.isCompressed=FALSE, .isSecondary={"TRUE" if role else "FALSE"}, .tiles={prefix}_Tiles, .palettes={prefix}_Palettes, .metatiles={prefix}_Metatiles, .metatileAttributes={prefix}_Attributes, .callback={cb}}};\n';banks[key]=dict(symbol=sym,path=rel,primary=primary,secondary=secondary);return banks[key]
 group=load(R/'data/maps/map_groups.json');group['group_order'].append('gMapGroup_HnS_Canary');group['gMapGroup_HnS_Canary']=[];nl=load(R/'data/layouts/layouts.json');mapping={m['id']:'MAP_HNS_TEST_'+re.sub(r'_hns$','',n).upper() for n,m in maps.items()};names={n:'HnSTest_'+re.sub(r'_hns$','',n) for n in NAMES};warpidx={n:{i:j for j,(i,w) in enumerate((i,w) for i,w in enumerate(m['warp_events']) if w['dest_map'] in mapping)} for n,m in maps.items()};idtoname={m['id']:n for n,m in maps.items()};manifest=[];arrivals=[]
 for n,m in maps.items():
  name=names[n];l=layouts[m['layout']];primary=l['primary_tileset'];secondary=l['secondary_tileset'];pk=primary.replace('gTileset_','');sk=pk+'__'+secondary.replace('gTileset_','');pb=bank(pk,primary,None);sb=bank(sk,primary,secondary);folder=A/'layouts'/name;folder.mkdir(parents=True,exist_ok=True)
  for field,fname in [('blockdata_filepath','map.bin'),('border_filepath','border.bin')]:shutil.copy2(S/l[field],folder/fname)
  lid='LAYOUT_HNS_TEST_'+re.sub(r'_hns$','',n).upper();nl['layouts'].append(dict(id=lid,name=name+'_Layout',width=l['width'],height=l['height'],primary_tileset=pb['symbol'],secondary_tileset=sb['symbol'],blockdata_filepath=str((folder/'map.bin').relative_to(R)),border_filepath=str((folder/'border.bin').relative_to(R)),border_width=2,border_height=2,layout_version='emerald'))
  combined=ts[primary]['attrs'][:640]+ts[secondary]['attrs'];cells=struct.unpack('<'+'H'*(l['width']*l['height']),(folder/'map.bin').read_bytes());blocked={(w['x'],w['y']) for w in m['warp_events']};water={v for label,v in native.items() if any(t in label for t in ['WATER','WARP','DOOR','LEDGE','STAIR','LADDER'])}
  def safe(x,y):
   if not (1<=x<l['width']-1 and 1<=y<l['height']-1) or (x,y) in blocked:return False
   v=cells[y*l['width']+x];return (v>>10&3)==0 and (combined[v&1023]&255) not in water
  candidates=[(o['x'],o['y']) for o in m['object_events']]+[(x,y) for y in range(2,l['height']-2) for x in range(2,l['width']-2)]
  x,y=next((x,y) for x,y in candidates if safe(x,y) and safe(x,y+1));arrivals.append(dict(name=name,id=mapping[m['id']],x=x,y=y+1));warps=[]
  for i,w in enumerate(m['warp_events']):
   if w['dest_map'] not in mapping:continue
   dn=idtoname[w['dest_map']];di=int(w['dest_warp_id']);assert di in warpidx[dn],(n,w)
   warps.append(dict(w,dest_map=mapping[w['dest_map']],dest_warp_id=str(warpidx[dn][di])))
  obj=dict(local_id='LOCALID_HNS_TEST_SCIENTIST',graphics_id='OBJ_EVENT_GFX_SCIENTIST_1',x=x,y=y,elevation=0,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script=name+'_Inspect',flag='0')
  native_map={k:m[k] for k in ['requires_flash','weather','map_type','allow_cycling','allow_escaping','allow_running','show_map_name','battle_scene']};native_map.update(id=mapping[m['id']],name=name,layout=lid,region_map_section='MAPSEC_GS_JOHTO',music='MUS_ROUTE104',connections=[dict(c,map=mapping[c['map']]) for c in m.get('connections') or [] if c['map'] in mapping] or None,object_events=[obj],warp_events=warps,coord_events=[],bg_events=[])
  if n=='CherrygroveCity_Mart_hns':native_map['object_events'].append(dict(obj,local_id='LOCALID_HNS_TEST_MART_CLERK',graphics_id='OBJ_EVENT_GFX_MART_EMPLOYEE',x=2,y=3,movement_type='MOVEMENT_TYPE_FACE_RIGHT',script=name+'_NativeClerk'))
  p=R/'data/maps'/name;dump(p/'map.json',native_map);group['gMapGroup_HnS_Canary'].append(name);manifest.append(dict(name=name,id=native_map['id'],source_name=n,source_id=m['id'],layout=lid,width=l['width'],height=l['height'],objects=len(native_map['object_events']),warps=len(warps),connections=len(native_map['connections'] or []),script_owner='PROJECT_TEST_ONLY',donor_gameplay_imported=False))
 for i,row in enumerate(manifest):
  name=row['name'];dest=arrivals[(i+1)%len(arrivals)];save(R/'data/maps'/name/'scripts.inc',f'{name}_MapScripts::\n\t.byte 0\n\n{name}_Inspect::\n\tlock\n\tfaceplayer\n\tmsgbox {name}_Text, MSGBOX_YESNO\n\tgoto_if_eq VAR_RESULT, YES, {name}_Next\n\trelease\n\tend\n{name}_Next::\n\twarp {dest["id"]}, {dest["x"]}, {dest["y"]}\n\twaitstate\n\trelease\n\tend\n{name}_Text:\n\t.string "Heart & Soul asset test.\\p"\n\t.string "Visit the next test map?$"\n')
 p=R/'data/maps/HnSTest_CherrygroveCity_Mart/scripts.inc';save(p,p.read_text()+'\n@ Project-owned shop test, without donor state or progression.\nHnSTest_CherrygroveCity_Mart_NativeClerk::\n\tlock\n\tfaceplayer\n\tmessage gText_HowMayIServeYou\n\twaitmessage\n\tpokemart HnSTest_CherrygroveCity_Mart_Items\n\tmsgbox gText_PleaseComeAgain, MSGBOX_DEFAULT\n\trelease\n\tend\n\t.align 2\nHnSTest_CherrygroveCity_Mart_Items:\n\t.2byte ITEM_POKE_BALL\n\t.2byte ITEM_POTION\n\t.2byte ITEM_ANTIDOTE\n\tpokemartlistend\n')
 for kind,text in decls.items():
  p=R/f'src/data/tilesets/{kind}.h';save(p,p.read_text()+'\n// BEGIN HNS_CANARY\n'+text+'// END HNS_CANARY\n')
 p=R/'data/event_scripts.s';save(p,p.read_text()+''.join(f'\n\t.include "data/maps/{x["name"]}/scripts.inc"' for x in manifest)+'\n');backup(R/'data/maps/map_groups.json');dump(R/'data/maps/map_groups.json',group);backup(R/'data/layouts/layouts.json');dump(R/'data/layouts/layouts.json',nl)
 # Start only NEW GAME in the test group; ordinary saves remain untouched.
 p=R/'src/new_game.c';text=p.read_text();text=text.replace('#if MERCURY_JOHTO_EXPLORATION_START\n    SetWarpDestination',f'#if HNS_CANARY_EXPLORATION_START\n    SetWarpDestination(MAP_GROUP({arrivals[0]["id"]}), MAP_NUM({arrivals[0]["id"]}), WARP_ID_NONE, {arrivals[0]["x"]}, {arrivals[0]["y"]});\n#elif MERCURY_JOHTO_EXPLORATION_START\n    SetWarpDestination',1);save(p,text)
 p=R/'include/config/mercury_exploration.h';save(p,p.read_text().replace('#define MERCURY_JOHTO_EXPLORATION_START TRUE','#define MERCURY_JOHTO_EXPLORATION_START TRUE\n#define HNS_CANARY_EXPLORATION_START TRUE'))
 receipt=load(R/'docs/la_world/mercury_johto/exploration_start.json');receipt['new_game_sha256']=hashlib.sha256((R/'src/new_game.c').read_bytes()).hexdigest();receipt['hns_canary_new_game_override']=True;backup(R/'docs/la_world/mercury_johto/exploration_start.json');dump(R/'docs/la_world/mercury_johto/exploration_start.json',receipt)
 # Mark only additive animation include as an authorized protected-source change.
 p=R/'tools/la_world/importers/amap/verify_mercury_johto.py';save(p,p.read_text().replace("   elif not derived(rel):changes.append(rel)","   elif rel=='src/tileset_anims.c':\n    assert (R/rel).read_text().replace('\\n#include \\\"hns_canary_anims.inc\\\"\\n','')==(R/'.la_work/amap/hns_canary_backup'/rel).read_text()\n   elif not derived(rel):changes.append(rel)"))
 dump(D/'manifest.json',dict(source_repository='https://github.com/PokemonHnS-Development/pokehns-expansion',source_commit=subprocess.check_output(['git','-C',str(S),'rev-parse','HEAD'],text=True).strip(),maps=manifest,banks=banks,behavior_translations=translations,arrivals=arrivals,donor_gameplay_imported=False,runtime_verified=False))
 save(D/'CREDITS.md','# Heart & Soul canary credits\n\nSource: PokemonHnS-Development/pokehns-expansion. Credit Pokémon Heart & Soul, Lil Dill and the HnS team, Modern Emerald/resetes12, RHH pokeemerald-expansion and pret pokeemerald. Upstream CREDITS.md and contributor chain are preserved alongside this file.\n');shutil.copy2(S/'CREDITS.md',D/'UPSTREAM-CREDITS.md')
 print('STAGED',len(manifest),'maps;',len(banks),'banks; no donor gameplay')
if __name__=='__main__':main()
