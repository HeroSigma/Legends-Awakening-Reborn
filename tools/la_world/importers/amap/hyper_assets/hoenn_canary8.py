#!/usr/bin/env python3
"""Lilycove corridor: assets only, native gameplay, real construction destinations."""
import argparse,collections,copy,re,struct
from pathlib import Path
import hoenn_canary5 as P
ROOT=P.ROOT;load=P.load;dump=P.dump;digest=P.digest;words=P.words;OUT=ROOT/'.la_work/amap/hyper_hoenn_canary8';D=Path(__file__).parent
TARGETS=load(OUT/'scope.json' if (OUT/'scope.json').exists() else D/'hoenn_canary8_scope.json');SPECIAL=load(OUT/'special_scope.json' if (OUT/'special_scope.json').exists() else D/'hoenn_canary8_special_scope.json')
def snapshot():
 if (OUT/'baseline.json').exists():return load(OUT/'baseline.json')
 OUT.mkdir(parents=True,exist_ok=True);b={str(f.relative_to(ROOT)):digest(f) for d in P.PREFIXES for f in (ROOT/d).rglob('*') if f.is_file() and not P.C.P.C.C.derived(str(f.relative_to(ROOT)))}
 for f in ['data/layouts/layouts.json','data/maps/map_groups.json','src/data/region_map/region_map_sections.json','src/data/tilesets/headers.h','src/data/tilesets/metatiles.h','src/hyper_asset_graphics_bindings.inc','src/data/object_events/hyper_assets.inc','data/event_scripts.s',*[f'data/maps/{n}/{s}' for n in TARGETS for s in ['map.json','scripts.inc']]]:
  p=OUT/'original'/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/f).read_bytes())
 dump(OUT/'baseline.json',b);return b

def prepare():
 baseline=snapshot();cat=load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');by={x['donor_id']:x for x in cat['layouts']};banks={x['symbol']:x for x in cat['tilesets']};ls=load(ROOT/'data/layouts/layouts.json');oldls=copy.deepcopy(ls);groups=load(ROOT/'data/maps/map_groups.json');sections=load(ROOT/'src/data/region_map/region_map_sections.json');oldsections=copy.deepcopy(sections);maps={n:load(ROOT/f'data/maps/{n}/map.json') for n in TARGETS};original=copy.deepcopy(maps);scripts={n:(ROOT/f'data/maps/{n}/scripts.inc').read_text() for n in TARGETS};grids={n:P.C.Grid(by[k]) for n,k in TARGETS.items()};files={};events=[];patches=[];gates=[];references=[];derivatives={};extras={k:P.name(k) for k in SPECIAL};warps={};pending=[]
 header=(ROOT/'src/data/tilesets/headers.h').read_text();metatiles=(ROOT/'src/data/tilesets/metatiles.h').read_text()
 def patch(n,x,y,v,reason):
  g=grids[n];at=y*g.w+x;old=g.blocks[at]
  if old!=v:g.blocks[at]=v;patches.append({'map':n,'x':x,'y':y,'before':old,'after':v,'reason':reason})
 for n,k in TARGETS.items():
  m=maps[n];g=grids[n];l=next(z for z in ls['layouts'] if z['id']==m['layout']);native_width,native_height=l['width'],l['height'];assert (native_width,native_height)==(g.w,g.h) ,n;native=words(ROOT/l['blockdata_filepath']);d=P.source(k);default_elevation=collections.Counter(v>>12 for v in native if ((v>>10)&3)==0).most_common(1)[0][0]
  users=[p.parent.name for p in (ROOT/'data/maps').glob('*/map.json') if load(p)['layout']==l['id']]
  if len(users)>1:l=copy.deepcopy(l);l['id']='LAYOUT_HYPER_CANARY8_'+P.const(n);l['name']='HyperCanary8'+n+'_Layout';m['layout']=l['id'];ls['layouts'].append(l)
  for y in range(g.h):
   for x in range(g.w):
    v=g.cell(x,y);el=(native[y*native_width+x]>>12) if x<native_width and y<native_height else (default_elevation if v['collision']==0 else v['elevation'])
    # Donor geometry owns elevations; an isolated Lilycove water cell is corrected to its surrounding pond/sea level.
    if v['translated_behavior'] in {0x10,0x11,0x12,0x13,0x14,0x15,0x19,0x22,0x2A} and v['elevation']!=1:patch(n,x,y,(v['block']&4095)|0x1000,'Surfable water retains water elevation1; inspected lone Lilycove (53,2) donor anomaly otherwise uses land3.')

  for kind,dk in P.KINDS.items():
   for i,e in enumerate(m[kind]):
    before=copy.deepcopy(e);probe=next((z for z in d[dk] if z['index']==i),None);reason='Native placement inspected against source geometry; all gameplay fields retained.'
    if kind=='object_events' and probe:
     current=g.cell(e['x'],e['y']);blocked=current['collision']!=0 and e['graphics_id'] not in ['OBJ_EVENT_GFX_BERRY_TREE','OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE','OBJ_EVENT_GFX_SS_TIDAL']
     if blocked or current['translated_behavior'] in {0x10,0x15}:
      e['x'],e['y']=probe['x'],probe['y'];reason='Matched donor object role/index; relocated onto inspected actual donor cell, native gameplay fields retained.'
    if kind=='bg_events' and probe and e['type']==probe['type']:e['x'],e['y']=probe['x'],probe['y'];reason='Matched native sign/item/base role and donor location; preserve text/reward/flag/base identity.'
    if kind=='warp_events':
     planner=load(ROOT/'.la_work/amap/hyper_hoenn_replacement/hyper_hoenn_replacement_manifest.json');canonical={z['hyper']['id']:z['canonical']['name'] for z in planner['maps'] if z.get('hyper')};candidates=[z for z in d[dk] if canonical.get(z['target_id']) and load(ROOT/f"data/maps/{canonical[z['target_id']]}/map.json")['id']==e['dest_map']]
     exact=[z for z in candidates if (z['x'],z['y'])==(e['x'],e['y'])];probe=exact[0] if exact else (probe if probe in candidates else None)
     if probe:e['x'],e['y']=probe['x'],probe['y'];warps[k+'.'+str(probe['index'])]=i;reason='Destination/coordinate-matched source doorway, including sparse donor IDs; native slot/destination retained.'
    if not (0<=e['x']<g.w and 0<=e['y']<g.h):
     assert n=='LilycoveCity_DepartmentStore_1F' and kind=='bg_events' and i==0 and e==before
     events.append({'map':n,'kind':kind,'index':i,'before':before,'after':copy.deepcopy(e),'donor_reference':probe,'cell':None,'reason':'Pre-existing dormant off-map floor-name sign preserved; manual review, no guessed position.','owner':'expansion'});references.append({'map':n,'source':k,'record':e,'reason':'Existing off-map BG sign at (0,8) outside 18x8 layout; retained for manual review.'});continue
    v=g.cell(e['x'],e['y'])
    if kind=='object_events' and e['graphics_id']!='OBJ_EVENT_GFX_SS_TIDAL' and v['elevation'] not in [0,15] and e['elevation'] not in [0,v['elevation']]:e['elevation']=v['elevation'];reason+=' Object elevation follows inspected donor surface, preserving gameplay fields.'
    assert 0<=e['x']<g.w and 0<=e['y']<g.h
    if kind=='object_events' and e['graphics_id'] not in ['OBJ_EVENT_GFX_BERRY_TREE','OBJ_EVENT_GFX_NURSE','OBJ_EVENT_GFX_MART_EMPLOYEE','OBJ_EVENT_GFX_SS_TIDAL']:assert v['collision']==0
    if kind=='coord_events' and e.get('type')!='weather':assert v['collision']==0,(n,kind,i,v)
    events.append({'map':n,'kind':kind,'index':i,'before':before,'after':copy.deepcopy(e),'donor_reference':probe,'cell':v,'reason':reason,'owner':'expansion'})
  l.update(width=g.w,height=g.h,primary_tileset=by[k]['primary_tileset'],secondary_tileset=by[k]['secondary_tileset'],border_filepath=by[k]['border_path'],blockdata_filepath=f'data/hyper_assets/canary8_layouts/{n}/map.bin')
  for i,w in enumerate(m['warp_events']):warps.setdefault(k+'.'+str(i),i)
 visual_tile_rebindings={}
 # Register all actual new special maps; no donor objects, scripts, flags, encounters or progression.
 template=load(ROOT/'data/maps/PetalburgWoods/map.json');sections_by={z['id']:z for z in sections['map_sections']};oldreceipt=load(P.OUT/'receipt.json');active=dict(TARGETS);active.update({n:k for k,n in oldreceipt['registered_special_maps'].items()})
 for num in [1,2,3,4]:active.update(load(ROOT/f'.la_work/amap/hyper_hoenn_canary{num}/receipt.json')['donor_ids'])
 last=load(ROOT/'.la_work/amap/hyper_hoenn_canary6/receipt.json');newlast=load(ROOT/'.la_work/amap/hyper_hoenn_canary7/receipt.json');active.update(newlast['donor_ids']);active.update({n:k for k,n in newlast['registered_special_maps'].items()});active.update(last['donor_ids']);active.update({n:k for k,n in last['registered_special_maps'].items()});active.update(oldreceipt['donor_ids']);active.update({x['canonical_name']:x['donor_id'] for x in load(P.P.OUT/'sea_corridor_correction_manifest.json')['maps']});active.update({n:k for k,n in extras.items()});reverse={k:n for n,k in active.items()};oldwarp={**load(ROOT/'.la_work/amap/hyper_hoenn_canary7/coordinate_remap_ledger.json')['warp_correspondence'],**load(P.OUT/'coordinate_remap_ledger.json')['warp_correspondence'],**load(ROOT/'.la_work/amap/hyper_hoenn_canary6/coordinate_remap_ledger.json')['warp_correspondence']}
 def mapdata(n):return maps.get(n) or load(ROOT/f'data/maps/{n}/map.json')
 for k,n in extras.items():
  d=P.source(k);folder=ROOT/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export/maps';folder=next(p for p in folder.iterdir() if (p/'map.json').exists() and load(p/'map.json')['id']==k);sec='MAPSEC_ABANDONED_SHIP' if d['name']=='Abandoned Ship' else 'MAPSEC_HYPER_'+re.sub(r'[^A-Za-z0-9]+','_',d['name']).strip('_').upper()
  if sec not in sections_by:sections_by[sec]={'id':sec,'name':d['name'],'x':0,'y':0,'width':1,'height':1};sections['map_sections'].append(sections_by[sec])
  m=copy.deepcopy(template);m.update(id='MAP_'+n.upper(),name=n,layout='LAYOUT_'+n.upper(),region_map_section=sec,music='MUS_ROUTE104',weather='WEATHER_NONE',map_type=P.special_type(d),requires_flash=False,show_map_name=True,allow_cycling=True,allow_escaping=False,allow_running=True,connections=None,object_events=[],warp_events=[],coord_events=[],bg_events=[]);maps[n]=m;scripts[n]=n+'_MapScripts::\n\t.byte 0\n'
  primary='gTileset_Hyper_'+d['primary_tileset'].replace('primary_','Primary_');secondary='gTileset_Hyper_'+d['secondary_tileset'].replace('secondary_','Secondary_');assert primary in banks and secondary in banks
  l={'id':m['layout'],'name':n+'_Layout','width':d['width'],'height':d['height'],'primary_tileset':primary,'secondary_tileset':secondary,'border_filepath':f'data/hyper_assets/canary8_layouts/{n}/border.bin','blockdata_filepath':f'data/hyper_assets/canary8_layouts/{n}/map.bin','layout_version':'emerald'};ls['layouts'].append(l);files[l['border_filepath']]=(folder/'border.bin').read_bytes();grids[n]=P.C.Grid({'dimensions':[d['width'],d['height']],'primary_tileset':primary,'secondary_tileset':secondary,'blockdata_path':str((folder/'blockdata.bin').relative_to(ROOT))});g='gMapGroup_Dungeons' if d['name']=='Abandoned Ship' else 'gMapGroup_HyperHoenn_'+re.sub(r'[^A-Za-z0-9]+','_',d['name']).strip('_')
  if g not in groups:groups['group_order'].append(g);groups[g]=[]
  groups[g].append(n)
 counts=collections.Counter()
 def gate(n,x,y,reason,dest=''):
  if any(e['graphics_id']=='OBJ_EVENT_GFX_SCIENTIST_1' and (e['x'],e['y'])==(x,y) for e in maps[n]['object_events']):return
  counts[n]+=1;i=counts[n];label=n+'_EventScript_HyperConstruction_Canary8_'+str(i);e=P.C.P.new_scientist(n,i,x,y,label);e['local_id']=e['local_id'].replace('_CONSTRUCTION_','_CANARY8_CONSTRUCTION_');maps[n]['object_events'].append(e);scripts[n]+=f'\n@ Project construction notice; no donor gameplay.\n{label}::\n\tlock\n\tfaceplayer\n\tmsgbox {label}_Text, MSGBOX_DEFAULT\n\trelease\n\tend\n{label}_Text:\n\t.string "This area is under construction.\\p"\n\t.string "Please check back later!$"\n';gates.append({'map':n,'scientist':e,'destination':dest,'reason':reason})
 def add(n,k,w):
  i=len(maps[n]['warp_events']);maps[n]['warp_events'].append({'x':w['x'],'y':w['y'],'elevation':w['elevation'],'dest_map':'','dest_warp_id':'0'});warps[k+'.'+str(w['index'])]=i;pending.append((n,k,i,w));return i
 for n,k in list(TARGETS.items())+[(n,k) for k,n in extras.items()]:
  d=P.source(k);native=len(original[n]['warp_events']) if n in original else 0
  for w in d['warps']:
   if n in original and (k+'.'+str(w['index'])) in warps:continue
   if w['x']==w['y']==0 or w['target_id']=='0.0':references.append({'map':n,'source':k,'record':w,'reason':'Script-positioned placeholder; excluded.'});continue
   dn=reverse.get(w['target_id']);dw=next((z for z in P.source(w['target_id'])['warps'] if z['index']==w['dest_warp_id']),None)
   if not dn or not dw:
    references.append({'map':n,'source':k,'record':w,'reason':'Foreign/unstaged destination or absent arrival slot; no donor gameplay imported.'});g=grids[n];v=g.cell(w['x'],w['y'])
    if v['collision']==0:gate(n,w['x'],w['y'],'Unstaged/foreign exit remains closed.',w['target_id'])
    continue
   if w['target_id'] not in extras and w['target_id'] not in TARGETS.values():
    key=w['target_id']+'.'+str(w['dest_warp_id']);di=oldwarp.get(key,w['dest_warp_id'] if w['target_group']<34 else None)
    if di is None or di>=len(mapdata(dn)['warp_events']):references.append({'map':n,'source':k,'record':w,'reason':'Existing map has no reviewed project arrival slot; held closed.'});gate(n,w['x'],w['y'],'Unresolved existing arrival remains closed.',w['target_id']);continue
   add(n,k,w)
   if n in original:gate(n,w['x'],w['y'],'New structural portal/shortcut; native gameplay unchanged.',w['target_id'])
 for n,k,i,w in pending:
  dk=w['target_id'];dn=reverse[dk];key=dk+'.'+str(w['dest_warp_id']);di=warps.get(key)
  if di is None and dk in extras:
   # Actual donor arrival coordinate is known, but its foreign story return is replaced with a safe static parent return.
   dw=next(z for z in P.source(dk)['warps'] if z['index']==w['dest_warp_id']);di=len(maps[dn]['warp_events']);warps[key]=di;maps[dn]['warp_events'].append({'x':dw['x'],'y':dw['y'],'elevation':dw['elevation'],'dest_map':maps[n]['id'],'dest_warp_id':str(i)})
  if di is None:di=oldwarp.get(key,w['dest_warp_id']);assert di<len(mapdata(dn)['warp_events'])
  maps[n]['warp_events'][i]['dest_map']=mapdata(dn)['id'];maps[n]['warp_events'][i]['dest_warp_id']=str(di)
 for k,n in extras.items():
  if not maps[n]['object_events']:
   g=grids[n];cells=[(x,y) for y in range(g.h) for x in range(g.w) if P.C.Grid.walk(g,x,y) and g.neighbors(x,y)]
   if not cells:cells=[(x,y) for y in range(g.h) for x in range(g.w) if g.cell(x,y)['collision']==0]
   assert cells,n;x,y=cells[0];gate(n,x,y,'Notice inside actual registered asset-only room.')
  for co in P.source(k)['connections']:
   dk=co['target_id'];op={'up':'down','down':'up','left':'right','right':'left'}.get(co['direction'])
   if dk in extras and op and any(z['target_id']==k and z['direction']==op and z['offset']==-co['offset'] for z in P.source(dk)['connections']):
    maps[n]['connections']=maps[n]['connections'] or [];maps[n]['connections'].append({'direction':co['direction'],'offset':co['offset'],'map':maps[extras[dk]]['id']})
   else:references.append({'map':n,'source':k,'record':co,'reason':'Foreign/nonreciprocal donor connection held as reference; no canonical boundary changed.'})
 # Preserve every native scripted tile behavior at its authoritative numeric slot, privately.
 labels={m[1]:int(m[2],16) for m in re.finditer(r'#define\s+(METATILE_\w+)\s+(0x[0-9A-Fa-f]+)',(ROOT/'include/constants/metatile_labels.h').read_text())};behavior_edits=[]
 for n in TARGETS:
  l=next(z for z in ls['layouts'] if z['id']==maps[n]['layout']);ol=next(z for z in oldls['layouts'] if z['id']==original[n]['layout']);tokens=set(re.findall(r'\bMETATILE_\w+',scripts[n]))
  if n=='AncientTomb':tokens.update(re.findall(r'\bMETATILE_\w+',(ROOT/'src/braille_puzzles.c').read_text()))
  for role,bank in [('primary_tileset',0),('secondary_tileset',1)]:
   oldbody=re.search(r'const struct Tileset\s+'+ol[role]+r'\s*=\s*\{(.*?)\};',header,re.S)[1];symbol=re.search(r'\.metatileAttributes\s*=\s*(\w+)',oldbody)[1];path=re.search(re.escape(symbol)+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',metatiles)[1];na=words(ROOT/path);a=list(grids[n].attrs[bank]);changed=[]
   for token in tokens:
    idx=labels.get(token,-1)-(512 if bank else 0)
    if 0<=idx<len(a) and idx<len(na) and (a[idx]&255)!=(na[idx]&255):before=a[idx];a[idx]=(a[idx]&0xFF00)|(na[idx]&255);changed.append({'map':n,'role':role,'token':token,'index':idx,'before':before,'after':a[idx]})
   if changed:
    base=l[role];derived='gTileset_Hyper_Canary8_'+n+('_Primary' if bank==0 else '_Secondary');sym='gMetatileAttributes_Hyper_Canary8_'+n+('_Primary' if bank==0 else '_Secondary');body=re.search(r'const struct Tileset\s+'+base+r'\s*=\s*\{(.*?)\};',header,re.S)[1];body=re.sub(r'(\.metatileAttributes\s*=\s*)\w+',lambda m:m[1]+sym,body);header+='\nconst struct Tileset '+derived+' = {'+body+'};\n';fp=f'data/hyper_assets/canary8_layouts/{n}/attributes.bin';metatiles+='\nconst u16 '+sym+'[] = INCBIN_U16("'+fp+'");\n';files[fp]=struct.pack('<'+'H'*len(a),*a);l[role]=derived;derivatives[derived]={'base':base,'attributes_path':fp};grids[n].attrs[bank]=a;behavior_edits+=changed
 import special_portal_assets
 # Private geometry folders remain canary8; the portal helper's duplicate-bank folder is harmless map-local asset infrastructure.
 header,metatiles=special_portal_assets.integrate(ROOT,maps,ls['layouts'],extras,grids,header,metatiles,files,derivatives,patches,stage="canary8")
 for n,g in grids.items():
  l=next(z for z in ls['layouts'] if z['id']==maps[n]['layout']);files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(g.blocks),*g.blocks)
 # Mark the extra canonical mouths with working project warp behaviors while retaining original native warps.
 for n in TARGETS:
  g=grids[n]
  for e in maps[n]['warp_events'][len(original[n]['warp_events']):]:
   v=g.cell(e['x'],e['y'])
   if v['translated_behavior'] not in range(0x60,0x70):
    tile=next(bank*512+i for bank,a in enumerate(g.attrs) for i,b in enumerate(a) if b&255==0x60);patch(n,e['x'],e['y'],tile|(v['elevation']<<12),'Inspected Hyper warp tile for newly registered construction-gated structural mouth.')
  l=next(z for z in ls['layouts'] if z['id']==maps[n]['layout']);files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(g.blocks),*g.blocks)
 # Reuse proven art-only adapters with native frames/animation/dimensions. No donor NPCs are added.
 safe=copy.deepcopy(events)
 for e in safe:
  if e['kind']=='object_events' and e['after']['graphics_id']=='OBJ_EVENT_GFX_REGISTEEL':pass
 old=P.C.P.TARGETS;P.C.P.TARGETS={**TARGETS,**{n:k for k,n in extras.items()}}
 try:art,bindings,audit,retained=P.C.P.graphics(cat,maps,safe)
 finally:P.C.P.TARGETS=old
 art=art.replace('Canary #3','Canary #8').replace('gHyperCanary3Graphics','gHyperCanary8Graphics');bindings=bindings.replace('gHyperCanary3Graphics','gHyperCanary8Graphics');files['src/data/object_events/hyper_canary8_graphics.inc']=art.encode();files['src/hyper_asset_graphics_bindings.inc']=((ROOT/'src/hyper_asset_graphics_bindings.inc').read_text()+'\n/* Lilycove corridor; expansion gameplay, Hyper art. */\n'+bindings).encode();files['src/data/object_events/hyper_assets.inc']=(ROOT/'src/data/object_events/hyper_assets.inc').read_text().replace('struct HyperAssetGraphicsBinding\n','#include "hyper_canary8_graphics.inc"\n\nstruct HyperAssetGraphicsBinding\n').encode();files['src/data/tilesets/headers.h']=header.encode();files['src/data/tilesets/metatiles.h']=metatiles.encode();files['data/event_scripts.s']=((ROOT/'data/event_scripts.s').read_text()+'\n@ Canary8 construction-only special maps.\n'+''.join('\t.include "data/maps/'+n+'/scripts.inc"\n' for n in extras.values())).encode()
 assert len(sections['map_sections'])<253
 return locals()

def apply():
 q=prepare();b=q['baseline'];assert all(digest(ROOT/f)==h for f,h in b.items()),'Current workspace differs from reviewed baseline.'
 for n,m in q['maps'].items():dump(ROOT/f'data/maps/{n}/map.json',m);p=ROOT/f'data/maps/{n}/scripts.inc';p.write_text(q['scripts'][n])
 for f,data in q['files'].items():p=ROOT/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 dump(ROOT/'data/layouts/layouts.json',q['ls']);dump(ROOT/'data/maps/map_groups.json',q['groups']);dump(ROOT/'src/data/region_map/region_map_sections.json',q['sections'])
 changed={f:{'before':h,'after':digest(ROOT/f)} for f,h in b.items() if digest(ROOT/f)!=h};new={str(f.relative_to(ROOT)):digest(f) for d in P.PREFIXES for f in (ROOT/d).rglob('*') if f.is_file() and str(f.relative_to(ROOT)) not in b and not P.C.P.C.C.derived(str(f.relative_to(ROOT)))}
 dump(OUT/'receipt.json',{'schema':'hyper-hoenn-canary8-v1','canonical_maps_replaced':list(TARGETS),'donor_ids':TARGETS,'registered_special_maps':q['extras'],'changed_baseline_files':changed,'new_files':new,'attribute_derivatives':q['derivatives'],'graphics_binding_maps':sorted({a['map'] for a in q['audit']}),'touched_maps':list(q['maps']),'old_mapsec_ids':[z['id'] for z in q['oldsections']['map_sections']],'visual_tile_rebindings':q['visual_tile_rebindings'],'hyper_gameplay_imported':False,'runtime_verified':False});dump(OUT/'coordinate_remap_ledger.json',{'events':q['events'],'geometry_patches':q['patches'],'construction_gates':q['gates'],'behavior_derivatives':q['behavior_edits'],'graphics_adapters':q['audit'],'native_graphics_retained':q['retained'],'warp_correspondence':q['warps'],'deferred_references':q['references']});print('Applied',len(TARGETS),'canonical maps and',len(q['extras']),'actual special maps.')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--apply',action='store_true');v=a.parse_args()
 if v.apply:apply()
 else:q=prepare();print('Reviewed',len(TARGETS),'canonical maps,',len(q['extras']),'specials and',len(q['events']),'native events.')
