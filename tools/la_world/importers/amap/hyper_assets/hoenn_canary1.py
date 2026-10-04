#!/usr/bin/env python3
"""Explicit, hash-guarded canonical Hyper Hoenn canary; never imports donor logic."""
import argparse,copy,csv,hashlib,importlib.util,json,re,struct
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
OUT=ROOT/'.la_work/amap/hyper_hoenn_canary1'
TARGETS={'OldaleTown':'0.10','Route102':'0.17','OldaleTown_Mart':'2.4'}
CHANGED=['data/layouts/layouts.json',*[f'data/maps/{n}/map.json' for n in TARGETS],'src/hyper_asset_graphics_bindings.inc','src/data/object_events/hyper_assets.inc']
def load(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def words(p):b=p.read_bytes();return list(struct.unpack('<'+'H'*(len(b)//2),b))
def derived(f):return bool(re.fullmatch(r'data/maps/[^/]+/(events|header|connections)\.inc',f) or f in ['include/constants/map_event_ids.h','include/constants/layouts.h','data/layouts/layouts.inc','data/layouts/layouts_table.inc'])
def baseline():
 OUT.mkdir(parents=True,exist_ok=True);p=OUT/'baseline.json'
 if p.exists():return load(p)
 b={}
 for directory in ['data','src','include','graphics']:
  for f in (ROOT/directory).rglob('*'):
   if f.is_file() and not derived(str(f.relative_to(ROOT))):b[str(f.relative_to(ROOT))]=digest(f)
 for f in CHANGED:
  q=OUT/'original'/f;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes((ROOT/f).read_bytes())
 dump(p,b);return b
class Grid:
 def __init__(self,layout):
  self.layout=layout;self.w,self.h=layout['dimensions'];self.blocks=words(ROOT/layout['blockdata_path']);catalog=load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');ts={x['symbol']:x for x in catalog['tilesets']};self.ts=[ts[layout[k]] for k in ['primary_tileset','secondary_tileset']];self.attrs=[words(ROOT/t['path']/'metatile_attributes.bin') for t in self.ts]
 def cell(self,x,y):
  assert 0<=x<self.w and 0<=y<self.h,(x,y)
  b=self.blocks[y*self.w+x];i=b&1023;a=self.attrs[i>=512][i-512 if i>=512 else i]
  return {'x':x,'y':y,'metatile':i,'block':b,'collision':(b>>10)&3,'elevation':b>>12,'translated_behavior':a&255,'layer':a>>12}
 def walk(self,x,y):c=self.cell(x,y);return c['collision']==0 and c['elevation'] in [0,3] and c['translated_behavior'] not in [0x10,0x11,0x12,0x13,0x14,0x15]
 def path(self,xy,steps):
  result=[self.cell(*xy)];x,y=xy
  for dx,dy in steps:
   x+=dx;y+=dy;assert self.walk(x,y),(x,y,self.cell(x,y));result.append(self.cell(x,y))
  return result

def prepare():
 b=baseline();assert all(digest(ROOT/f)==b[f] for f in CHANGED),'Canary already applied or target changed; validate existing receipt instead.'
 catalog=load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');layouts={x['donor_id']:x for x in catalog['layouts']};ldata=load(ROOT/'data/layouts/layouts.json');ledger=[];maps={};grids={};omaps={}
 for name,k in TARGETS.items():
  m=load(ROOT/f'data/maps/{name}/map.json');omaps[name]=copy.deepcopy(m);g=Grid(layouts[k]);grids[name]=g
  donorpath=next((ROOT/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export/maps').glob(f'{int(k.split(".")[0]):02}.{int(k.split(".")[1]):02}_*/map.json'));d=load(donorpath)
  for key,dk in [('object_events','npcs'),('warp_events','warps'),('coord_events','coord_events'),('bg_events','bg_events')]:
   for i,e in enumerate(m[key]):
    old=copy.deepcopy(e);probe=d[dk][i];reason='Retain expansion coordinate: verified valid Hyper cell and native scripted movement/ownership.'
    if name=='Route102' or (name=='OldaleTown' and key in ['warp_events','bg_events']):
     e['x'],e['y']=probe['x'],probe['y'];reason='Matched donor event role/local ID/order and inspected actual Hyper cell; copy only geometry operands.'
    if name=='OldaleTown' and key=='object_events' and i==3:reason='Keep rival at (11,19), not donor (10,19): walkable Hyper short grass; preserves all three native approach branches and gender/state logic.'
    if name=='OldaleTown' and key=='coord_events':reason='Keep native gate/rival trigger coordinates: validated trigger cells and expansion approach paths; donor trigger 3 differs and is deliberately not transplanted.'
    c=g.cell(e['x'],e['y']);approaches=[g.cell(x,y) for x,y in [(e['x']-1,e['y']),(e['x']+1,e['y']),(e['x'],e['y']-1),(e['x'],e['y']+1)] if 0<=x<g.w and 0<=y<g.h and g.walk(x,y)]
    if key=='object_events':
     if e['graphics_id']=='OBJ_EVENT_GFX_BERRY_TREE':assert c['collision']==1;assert g.walk(e['x'],e['y']+1)
     else:assert g.walk(e['x'],e['y'])
     assert approaches
    elif key=='coord_events':assert g.walk(e['x'],e['y']) and c['elevation']==e['elevation']
    elif key=='warp_events':assert c['translated_behavior'] in [0x69,0x60,0x65],c
    elif key=='bg_events':assert c['collision']==1 and approaches
    ledger.append({'map':name,'canonical_id':m['id'],'donor_id':k,'kind':key,'index':i,'local_id':e.get('local_id',i+1) if key=='object_events' else None,'role':e.get('script'),'before':old,'after':copy.deepcopy(e),'donor_reference':probe,'donor_json':str(donorpath.relative_to(ROOT)),'cell':c,'walkable_interaction_neighbors':approaches,'reason':reason,'review':'source geometry + event comparison ledger + movement/interaction cell checks','gameplay_owner':'pokeemerald-expansion'})
  oldlayout=next(x for x in ldata['layouts'] if x['id']==m['layout'])
  if name=='OldaleTown_Mart':
   newlayout=copy.deepcopy(oldlayout);newlayout['id']='LAYOUT_HYPER_CANARY1_OLDALE_TOWN_MART';newlayout['name']='HyperCanary1OldaleTownMart_Layout';ldata['layouts'].append(newlayout);m['layout']=newlayout['id']
  else:newlayout=oldlayout
  source=layouts[k];newlayout.update(width=g.w,height=g.h,primary_tileset=source['primary_tileset'],secondary_tileset=source['secondary_tileset'],border_filepath=source['border_path'],blockdata_filepath=source['blockdata_path'])
  maps[name]=m
 return b,ldata,maps,omaps,ledger,grids,catalog
def geometry_checks(grids,omaps):
 g=grids['OldaleTown'];paths=[]
 def path(label,start,steps):paths.append({'label':label,'start':start,'cells':g.path(start,steps),'owner':'unchanged expansion script'})
 U=(0,-1);D=(0,1);L=(-1,0);R=(1,0)
 path('EmployeeEast/North',[13,14],[U]*7);path('EmployeeSouth',[13,14],[L,U,U,R]+[U]*5)
 path('PlayerEast',[12,14],[R]+[U]*6);path('PlayerSouth',[13,13],[U]*5);path('PlayerNorth',[13,15],[U]*7)
 path('Gate player stepback',[0,10],[R]);path('Gate actor backup',[1,11],[U,R]);path('Gate actor return',[2,10],[D,L])
 path('RivalApproachPlayer1',[11,19],[L,L]);path('RivalApproachPlayer2',[11,19],[L]);path('RivalApproachPlayer3',[11,19],[])
 assert not g.walk(14,14),'No west-facing guide case: east side must remain obstructed.'
 paths.append({'label':'Rival exit all states','x_values':[9,10,11],'y_values':list(range(20,32)),'reason':'Native six-step exit executes twice, then actor removal/flag/state update. Same native starting x/y and unchanged Route101 connection/geometry; preserve forced offscreen movement, not donor exit logic.','runtime_check_required':True})
 route=grids['Route102'];rmap=omaps['Route102'];donor=load(next((ROOT/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export/maps').glob('00.17_*/map.json')))
 for i,directions in [(1,[D]),(2,[U]),(3,[D,R]),(8,[D])]:
  e=donor['npcs'][i];n=int(rmap['object_events'][i]['trainer_sight_or_berry_tree_id'])
  for direction in directions:paths.append({'label':rmap['object_events'][i]['script']+' sight corridor','cells':route.path([e['x'],e['y']],[direction]*n),'range':n,'owner':'unchanged expansion trainer ID, range and facing logic'})
 for i in [4]:
  e=donor['npcs'][i];cells=[route.cell(x,y) for x in range(e['x']-1,e['x']+2) for y in range(e['y']-1,e['y']+2)]
  assert route.walk(e['x'],e['y']) and sum(route.walk(c['x'],c['y']) for c in cells)>=5;paths.append({'label':'Route102 boy native 1x1 patrol','cells':cells,'note':'Native random movement collision checks reject blocked range cells; preserve native range/type, donor center is walkable.'})
 mart=grids['OldaleTown_Mart'];assert all(mart.walk(9,y) for y in [3,4,5]);paths.append({'label':'Mart boy up/down patrol','cells':[mart.cell(9,y) for y in [3,4,5]]})
 seams=[]
 for y in range(20):
  a=g.cell(0,y);b=route.cell(49,y);assert (a['collision'],a['elevation'])==(b['collision'],b['elevation'])
  seams.append({'Oldale':a,'Route102':b,'offset':0})
 assert [y for y in range(20) if g.walk(0,y)]==[10,11]
 # All external boundaries compare walkable masks/elevations to pre-canary expansion geometry.
 ls=load(OUT/'original/data/layouts/layouts.json')['layouts'];external=[]
 for name,edge,neighbor in [('OldaleTown','up','Route103'),('OldaleTown','down','Route101'),('Route102','left','PetalburgCity')]:
  current=grids[name];native=next(x for x in ls if x['id']==omaps[name]['layout']);old=words(ROOT/native['blockdata_filepath']);coords=([(x,0) for x in range(current.w)] if edge=='up' else [(x,current.h-1) for x in range(current.w)] if edge=='down' else [(0,y) for y in range(current.h)])
  neighbor_map=load(ROOT/f'data/maps/{neighbor}/map.json');neighbor_layout=next(x for x in ls if x['id']==neighbor_map['layout']);neighbor_blocks=words(ROOT/neighbor_layout['blockdata_filepath'])
  mask=[]
  for x,y in coords:
   before=old[y*current.w+x];after=current.cell(x,y)
   nx,ny=(x,neighbor_layout['height']-1) if edge=='up' else (x,0) if edge=='down' else (neighbor_layout['width']-1,y+10)
   nb=neighbor_blocks[ny*neighbor_layout['width']+nx]
   old_cross=((before>>10)&3)==0 and ((nb>>10)&3)==0
   new_cross=after['collision']==0 and ((nb>>10)&3)==0
   assert old_cross==new_cross,(name,edge,x,y,before,after,nb)
   if new_cross:assert before>>12==after['elevation']==nb>>12
   mask.append({'x':x,'y':y,'before_block':before,'after':after,'unchanged_neighbor_block':nb,'crossable_before':old_cross,'crossable_after':new_cross})
  external.append({'map':name,'edge':edge,'neighbor':neighbor,'original_crossable_seam_mask_and_elevations_retained':True,'cells':mask})
 return {'scripted_paths':paths,'oldale_route102_seam':seams,'external_boundary_masks':external,'gate_proof':'Only west edge rows 10/11 are walkable. Row10 has unchanged state=0 trigger; row11 is occupied by footprints actor at (1,11). Backup/return and player stepback verified.'}

# Resolve semantic expansion symbols first; donor numeric keys are only asset references.
STATIC={'OldaleTown':{'GIRL_3':14,'MART_EMPLOYEE':83,'MANIAC':39},'Route102':{'LITTLE_BOY':11,'YOUNGSTER':35,'BUG_CATCHER':36,'LASS':47,'BOY_1':7},'OldaleTown_Mart':{'MART_EMPLOYEE':83,'WOMAN_5':34,'BOY_1':7}}
def graphics(catalog):
 native=(ROOT/'src/data/object_events/object_event_graphics_info.h').read_text();pointers=(ROOT/'src/data/object_events/object_event_graphics_info_pointers.h').read_text();objects={x['source_graphics_id']:x for x in catalog['object_graphics']};out=['/* Canary #1: art/palette only; animation, size, OAM, slots and runtime contracts stay native. */'];bindings=[];audit=[];done=set()
 for name in TARGETS:
  choices=dict(STATIC.get(name,{}))
  if name=='OldaleTown':choices.update(RIVAL_BRENDAN_NORMAL=100,RIVAL_MAY_NORMAL=105)
  for semantic,source in choices.items():
   gfx='OBJ_EVENT_GFX_'+semantic;m=re.search(r'\['+gfx+r'\]\s*=\s*&?(\w+)',pointers);assert m,gfx
   symbol=m[1];match=re.search(r'const struct ObjectEventGraphicsInfo '+symbol+r' = \{(.*?)\};',native,re.S);assert match,symbol
   body=match[1];obj=objects[source]
   for field in ['width','height']:assert int(re.search(r'\.'+field+r'\s*=\s*(\d+)',body)[1])==obj[field],(semantic,field)
   adapter='gHyperCanary1Graphics_'+semantic
   if semantic not in done:
    replacement=re.sub(r'(\.paletteTag\s*=\s*)[^,]+',lambda m:m[1]+f'0x{obj["palette_tag"]:04X}',body)
    replacement=re.sub(r'(\.images\s*=\s*)\w+',lambda m:m[1]+f'sPicTable_HyperAsset{source:03}',replacement)
    out.append('static const struct ObjectEventGraphicsInfo '+adapter+' = {'+replacement+'};');done.add(semantic)
    audit.append({'expansion_symbol':gfx,'native_struct':symbol,'source_graphics_id':source,'adapter':adapter,'source_frame_count':obj['frame_count'],'native_contract':body,'replacement':replacement,'changed_fields':['images','paletteTag'],'source_evidence':'donor NPC local-ID + graphics role; rival source 100/105 recovered normal graphics, native initializer still assigns expansion rival symbols'})
   canonical=load(OUT/'original'/f'data/maps/{name}/map.json')['id'];bindings.append(f'    {{{canonical}, {gfx}, &{adapter}}},')
 return '\n\n'.join(out)+'\n','/* Canonical Canary #1 only. Native variable resolution occurs before these visual bindings. */\n'+'\n'.join(bindings)+'\n',audit

def apply():
 b,ldata,maps,omaps,ledger,grids,catalog=prepare();checks=geometry_checks(grids,omaps);adapters,bindings,gaudit=graphics(catalog)
 # No writes to canonical maps until every geometry/path/graphics preflight has passed.
 for name,m in maps.items():dump(ROOT/f'data/maps/{name}/map.json',m)
 dump(ROOT/'data/layouts/layouts.json',ldata)
 adapterpath='src/data/object_events/hyper_canary1_graphics.inc';(ROOT/adapterpath).write_text(adapters)
 (ROOT/'src/hyper_asset_graphics_bindings.inc').write_text(bindings)
 p=ROOT/'src/data/object_events/hyper_assets.inc';s=p.read_text();assert '#include "hyper_canary1_graphics.inc"' not in s;s=s.replace('struct HyperAssetGraphicsBinding\n','#include "hyper_canary1_graphics.inc"\n\nstruct HyperAssetGraphicsBinding\n');p.write_text(s)
 dump(OUT/'coordinate_remap_ledger.json',{'schema':'hyper-hoenn-canary1-events-v1','status':'source/cell/path reviewed; in-game verification pending','events':ledger,'geometry_checks':checks,'graphics_adapters':gaudit,'omitted_donor_only_events':{'Route102':{'objects':6,'warps':4,'coord_events':2}},'berry_graphics_policy':'Preserve native BerryTree renderer/growth animation and berry state. Hyper source 60 is a one-frame placeholder, not a growth atlas; do not replace native growth struct.','item_graphics_policy':'Preserve native item/PokeBall visual struct: expansion uses 16x32 six-frame follower Pokeball animation contract; Hyper 59 is one 16x16 frame. Native item state and follower animation remain authoritative; no guessed padding or one-frame substitution.','gameplay_scripts_changed':[]})
 with (OUT/'coordinate_remap_ledger.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['map','kind','index','role','old_x','old_y','new_x','new_y','collision','elevation','behavior','reason'])
  for e in ledger:w.writerow([e['map'],e['kind'],e['index'],e['role'],e['before']['x'],e['before']['y'],e['after']['x'],e['after']['y'],e['cell']['collision'],e['cell']['elevation'],e['cell']['translated_behavior'],e['reason']])
 receipt={'schema':'hyper-hoenn-canary1-receipt-v1','canonical_maps_replaced':list(TARGETS),'donor_ids':TARGETS,'runtime_verified':False,'hyper_gameplay_imported':False,'changed_baseline_files':{f:{'before':b[f],'after':digest(ROOT/f)} for f in CHANGED},'new_files':{adapterpath:digest(ROOT/adapterpath)},'map_ids_header_sha256':digest(ROOT/'include/constants/map_groups.h'),'map_groups_json_sha256':digest(ROOT/'data/maps/map_groups.json'),'original_layout_count':len(load(OUT/'original/data/layouts/layouts.json')['layouts']),'event_counts':{n:{k:len(m[k]) for k in ['object_events','warp_events','coord_events','bg_events']} for n,m in maps.items()}}
 dump(OUT/'receipt.json',receipt);print('Applied three canonical maps only. Run validate and the ROM build; runtime success is pending.')

def later_canary_hash(f,expected):
 p=ROOT/'.la_work/amap/hyper_hoenn_canary2/receipt.json'
 if p.exists():
  receipt=load(p);assert receipt['canonical_maps_replaced']==['LittlerootTown','Route101','Route103','PetalburgCity']
  permitted={'data/layouts/layouts.json','data/maps/LittlerootTown/map.json','data/maps/Route101/map.json','data/maps/Route103/map.json','data/maps/PetalburgCity/map.json','data/maps/Route103/scripts.inc','data/maps/PetalburgCity/scripts.inc','src/hyper_asset_graphics_bindings.inc','src/data/object_events/hyper_assets.inc'}
  assert set(receipt['changed_baseline_files'])==permitted
  if f in receipt['changed_baseline_files']:
   change=receipt['changed_baseline_files'][f];assert change['before']==expected,(f,'canary receipt chain mismatch');return change['after']
 return expected

def validate():
 b=load(OUT/'baseline.json');receipt=load(OUT/'receipt.json');allowed=receipt['changed_baseline_files'];assert set(allowed)==set(CHANGED)
 for f,h in b.items():assert digest(ROOT/f)==later_canary_hash(f,allowed[f]['after'] if f in allowed else h),f
 for f,h in receipt['new_files'].items():assert digest(ROOT/f)==h,f
 assert digest(ROOT/'include/constants/map_groups.h')==receipt['map_ids_header_sha256'];assert digest(ROOT/'data/maps/map_groups.json')==receipt['map_groups_json_sha256']
 ls=load(ROOT/'data/layouts/layouts.json')['layouts'];orig=load(OUT/'original/data/layouts/layouts.json')['layouts'];assert len(ls)==len(orig)+1
 for i,l in enumerate(orig):
  if l['id'] not in ['LAYOUT_OLDALE_TOWN','LAYOUT_ROUTE102']+(['LAYOUT_LITTLEROOT_TOWN','LAYOUT_ROUTE101','LAYOUT_ROUTE103','LAYOUT_PETALBURG_CITY'] if (ROOT/'.la_work/amap/hyper_hoenn_canary2/receipt.json').exists() else []):assert ls[i]==l,l['id']
  else:assert ls[i]['id']==l['id'] and ls[i]['name']==l['name']
 for name in TARGETS:
  old=load(OUT/'original'/f'data/maps/{name}/map.json');new=load(ROOT/f'data/maps/{name}/map.json');assert old.keys()==new.keys()
  for key in old:
   if key=='layout':continue
   if key.endswith('_events'):
    assert len(old[key])==len(new[key])
    for a,z in zip(old[key],new[key]):assert {k:v for k,v in a.items() if k not in ['x','y']}=={k:v for k,v in z.items() if k not in ['x','y']},(name,key)
   else:assert old[key]==new[key],(name,key)
  assert digest(ROOT/f'data/maps/{name}/scripts.inc')==b[f'data/maps/{name}/scripts.inc']
 validation={'passed':True,'protected_files_checked':len(b),'only_three_canonical_maps_replaced':True,'map_ids_unchanged':True,'all_gameplay_event_fields_unchanged_except_coordinates':True,'all_expansion_scripts_unchanged':True,'all_other_layouts_maps_bwa_swsh_save_flags_vars_unchanged_except_explicit_later_canary_receipt':True,'runtime_verified':False}
 dump(OUT/'validation.json',validation);print(json.dumps(validation,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--apply',action='store_true');p.add_argument('--validate',action='store_true');a=p.parse_args()
 if a.apply:apply()
 elif a.validate:validate()
 else:prepare();print('Preflight ready; use --apply for this explicitly scoped batch.')
