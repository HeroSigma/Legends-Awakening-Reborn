#!/usr/bin/env python3
"""Additive Hyper Sinnoh: recovered assets and project-owned static travel only."""
import argparse,copy,re,struct
import hoenn_finalization as F
import recover_tileset_subset as B
import special_portal_assets
R=F.R;O=R/'.la_work/amap/hyper_sinnoh_asset_travel';SOURCE=R/'.la_work/amap/HypEm_v5.7_EN_QoL_amap_export'
QUARANTINE={'37.0':'Unlinked duplicate Jubilife interior.','37.36':'Obsolete Safari template points to Hoenn; linked Pastoria gate is37.117.','37.50':'Unlinked Mauville battle template.','37.51':'Unlinked Mauville battle template.'}
SEED=({f'36.{i}' for i in range(97)}|{f'37.{i}' for i in [*range(102),*range(109,118)]}|{'34.37','35.11','35.14','35.16','35.29','35.81','35.82','35.88','26.67'})-set(QUARANTINE)
HOENN_EXTRAS={'26.58','26.59','34.72'}
def name(k):return 'HyperSinnoh_'+k.replace('.','_')+'_'+re.sub(r'[^A-Za-z0-9]+','_',F.C.P.source(k)['name']).strip('_')
def prepare():
 assert not (O/'receipt.json').exists(),'Already applied.'
 F.audit();O.mkdir(parents=True,exist_ok=True);baseline={str(p.relative_to(R)):F.digest(p) for d in F.C.P.PREFIXES for p in (R/d).rglob('*') if p.is_file() and not F.C.P.C.P.C.C.derived(str(p.relative_to(R)))}
 allmaps={p.parent.name:F.load(p) for p in (R/'data/maps').glob('*/map.json') if F.load(p).get('warp_events') is not None};original=copy.deepcopy(allmaps);ls=F.load(R/'data/layouts/layouts.json');oldls=copy.deepcopy(ls);groups=F.load(R/'data/maps/map_groups.json');oldgroups=copy.deepcopy(groups);sections=F.load(R/'src/data/region_map/region_map_sections.json');oldsections=copy.deepcopy(sections);cat=F.load(R/'.la_work/amap/hyper_asset_integration/asset_catalog.json');banks={x['symbol']:x for x in cat['tilesets']};folders={F.load(p)['id']:p.parent for p in (SOURCE/'maps').glob('*/map.json')};active={}
 for i in range(1,10):
  rec=F.load(R/f'.la_work/amap/hyper_hoenn_canary{i}/receipt.json');active.update({k:n for n,k in rec['donor_ids'].items()});active.update(rec.get('registered_special_maps',{}))
 active.update({k:n for n,k in F.load(F.O/'receipt.json')['donor_ids'].items()});active.update({x['donor_id']:x['canonical_name'] for x in F.load(R/'.la_work/amap/hyper_hoenn_corridor_correction/sea_corridor_correction_manifest.json')['maps']})
 new={k:name(k) for k in SEED if k not in active or k=='26.67'};new.update({k:F.C.P.name(k) for k in HOENN_EXTRAS});active.update(new);missing=set()
 for k in new:
  d=F.C.P.source(k)
  for role in ['primary_tileset','secondary_tileset']:
   sy='gTileset_Hyper_'+d[role].replace('primary_','Primary_').replace('secondary_','Secondary_')
   if sy not in banks:missing.add(d[role])
 files,rows,anim=B.recover(R,missing,cat);cat['tilesets']+=rows;banks.update({x['symbol']:x for x in rows});header=files['src/data/tilesets/headers.h'].decode();meta=files['src/data/tilesets/metatiles.h'].decode();scripts={};maps={};grids={};refs=[];patches=[];derivatives={};warps={};requests=[];notices=[];inventory=[]
 assert 'MAPSEC_SINNOH' not in {x['id'] for x in sections['map_sections']};sections['map_sections'].append({'id':'MAPSEC_SINNOH','name':'Sinnoh','x':0,'y':0,'width':1,'height':1});assert len(sections['map_sections'])<253
 def attrs(s):
  fp=banks[s]['path']+'/metatile_attributes.bin';b=files.get(fp) or (R/fp).read_bytes();return list(struct.unpack('<'+'H'*(len(b)//2),b))
 template=F.load(R/'data/maps/PetalburgWoods/map.json')
 for k,n in sorted(new.items(),key=lambda z:tuple(map(int,z[0].split('.')))):
  d=F.C.P.source(k);sinnoh=k not in HOENN_EXTRAS;sec='MAPSEC_SINNOH' if sinnoh else ('MAPSEC_HYPER_OUTER_SPACE' if d['name']=='Outer Space' else 'MAPSEC_HYPER_CHAMPION_ISLAND');assert sec in {x['id'] for x in sections['map_sections']};m=copy.deepcopy(template);m.update(la_imported=True,id='MAP_'+n.upper(),name=n,layout='LAYOUT_'+n.upper(),region='REGION_SINNOH' if sinnoh else 'REGION_HOENN',region_map_section=sec,music='MUS_ROUTE104',weather='WEATHER_NONE',map_type=F.C.P.special_type(d),requires_flash=False,show_map_name=True,allow_cycling=True,allow_escaping=False,allow_running=True,connections=None,object_events=[],warp_events=[],coord_events=[],bg_events=[]);maps[n]=m;scripts[n]=n+'_MapScripts::\n\t.byte 0\n';base=f'data/hyper_assets/sinnoh_layouts/{n}';primary='gTileset_Hyper_'+d['primary_tileset'].replace('primary_','Primary_');secondary='gTileset_Hyper_'+d['secondary_tileset'].replace('secondary_','Secondary_');l={'id':m['layout'],'name':n+'_Layout','width':d['width'],'height':d['height'],'primary_tileset':primary,'secondary_tileset':secondary,'border_filepath':base+'/border.bin','blockdata_filepath':base+'/map.bin','layout_version':'emerald'};ls['layouts'].append(l);files[l['border_filepath']]=(folders[k]/'border.bin').read_bytes();g=F.C.P.C.Grid.__new__(F.C.P.C.Grid);g.name=n;g.w,g.h=d['width'],d['height'];g.blocks=F.words(folders[k]/'blockdata.bin');g.attrs=[attrs(primary),attrs(secondary)];grids[n]=g
  mtcounts=[]
  for symbol in [primary,secondary]:
   fp=banks[symbol]['path']+'/metatiles.bin';mtcounts.append(len(files.get(fp) or (R/fp).read_bytes())//16)
  invalid=[at for at,v in enumerate(g.blocks) if (v&511)>=min(len(g.attrs[(v&1023)//512]),mtcounts[(v&1023)//512])]
  for at in invalid:
   x,y=at%g.w,at//g.w;v=g.blocks[at];choices=[]
   for yy in range(g.h):
    for xx in range(g.w):
     old=g.blocks[yy*g.w+xx];tile=old&1023
     if (tile&511)>=min(len(g.attrs[tile//512]),mtcounts[tile//512]) or ((old>>10)&3)!=1:continue
     mb=g.attrs[tile//512][tile&511]&255
     if mb in [0,7,8,0x80]:choices.append((abs(xx-x)+abs(yy-y),yy,xx,tile))
   assert choices,(n,x,y,'No valid source construction prop');_,yy,xx,tile=min(choices);g.blocks[at]=(v&0xf000)|0x400|tile;patches.append({'map':n,'x':x,'y':y,'before':v,'after':g.blocks[at],'reason':'Invalid donor metatile lies outside its bank. Quarantine this exact cell with an inspected existing solid donor prop; preserve raw donor data and queue manual art review.','reference_cell':[xx,yy],'manual_review':True})
  if m['map_type'] in ['MAP_TYPE_TOWN','MAP_TYPE_CITY','MAP_TYPE_ROUTE','MAP_TYPE_OCEAN_ROUTE']:
   for at,v in enumerate(g.blocks):
    cell=g.cell(at%g.w,at//g.w)
    if cell['collision']==0 and cell['translated_behavior'] in range(0x10,0x16) and cell['elevation']!=1:g.blocks[at]=(v&4095)|4096;patches.append({'map':n,'x':at%g.w,'y':at//g.w,'before':v,'after':g.blocks[at],'reason':'Surfable surface water retains elevation1.'})
  group=('gMapGroup_HyperSinnoh_' if sinnoh else 'gMapGroup_HyperHoenn_')+re.sub(r'[^A-Za-z0-9]+','_',d['name']).strip('_')
  if group not in groups:groups['group_order'].append(group);groups[group]=[]
  groups[group].append(n);inventory.append({'donor_id':k,'donor_identity':'Hyper Emerald v5.7 EN+QoL','donor_name':d['name'],'map':n,'category':m['map_type'],'group':group,'mapsec':sec,'dimensions':[d['width'],d['height']],'tilesets':[primary,secondary],'metadata':d,'canonical_flag':False,'import_flag':True,'confidence':'MEDIUM' if invalid else 'HIGH','reason':'Invalid source art slots quarantined for manual review.' if invalid else 'Exact recovered donor geometry/assets; project-owned static travel only.','gameplay_owner':'project','source_blockdata_sha256':F.digest(folders[k]/'blockdata.bin')})
 def current(n):
  if n not in maps:maps[n]=copy.deepcopy(allmaps[n]);scripts[n]=(R/f'data/maps/{n}/scripts.inc').read_text();grids[n]=F.grid(next(x for x in ls['layouts'] if x['id']==maps[n]['layout']),header,meta)
  return maps[n]
 for k,n in active.items():
  if n not in allmaps:continue
  for w in F.C.P.source(k)['warps']:
   match=[i for i,e in enumerate(allmaps[n]['warp_events']) if (e['x'],e['y'])==(w['x'],w['y'])]
   if len(match)==1:warps[k+'.'+str(w['index'])]=match[0]
 def add(k,w):
  n=active[k];m=current(n);key=k+'.'+str(w['index']);g=grids[n];assert 0<=w['x']<g.w and 0<=w['y']<g.h,(k,w)
  same=next((i for i,e in enumerate(m['warp_events']) if (e['x'],e['y'])==(w['x'],w['y'])),None)
  i=same if same is not None else len(m['warp_events'])
  if same is None:m['warp_events'].append({'x':w['x'],'y':w['y'],'elevation':w['elevation'],'dest_map':'','dest_warp_id':'0'})
  warps[key]=i;return i
 candidates=set(new)|{'34.13','34.30','34.65','35.6','37.96'}
 for k in sorted(candidates,key=lambda x:tuple(map(int,x.split('.')))):
  if k not in active:continue
  n=active[k]
  for w in F.C.P.source(k)['warps']:
   if k+'.'+str(w['index']) in warps:continue
   dk=w['target_id'];dn=active.get(dk);dw=next((x for x in F.C.P.source(dk)['warps'] if x['index']==w['dest_warp_id']),None) if dn else None
   if dn and not dw and k in new and dk in new:
    parents=[z for z in F.C.P.source(dk)['warps'] if z['target_id']==k]
    if len(parents)==1:
     before=copy.deepcopy(w);w=copy.deepcopy(w);w['dest_warp_id']=parents[0]['index'];dw=parents[0];refs.append({'map':n,'donor_id':k,'record':before,'reason':'Missing donor return slot normalized to the unique inspected parent entrance; project static travel, manual correspondence review.','resolved_project_parent':dw})
   if w['x']==w['y']==0 or dk in ['0.0','127.127'] or w['dynamic_target'] or not dn or not dw or dn in allmaps and not dn.startswith('HyperHoenn_'):
    refs.append({'map':n,'donor_id':k,'record':w,'reason':'Foreign/canonical/scripted placeholder or absent arrival is held; no donor story warp logic.'});continue
   si=add(k,w);requests.append((k,si,w,dw))
 rebindings=[]
 for k,si,w,dw in requests:
  dk=w['target_id'];key=dk+'.'+str(w['dest_warp_id']);dn=active[dk]
  if key not in warps:
   di=add(dk,dw);maps[dn]['warp_events'][di].update(dest_map=maps[active[k]]['id'],dest_warp_id=str(si));rebindings.append({'map':dn,'warp':di,'source_record':dw,'project_return':active[k],'reason':'Unowned arrival slot receives a safe reciprocal project return; donor script/dynamic semantics excluded.'})
  di=warps[key];maps[active[k]]['warp_events'][si].update(dest_map=current(dn)['id'],dest_warp_id=str(di))
 # Ancient Retreat target2 is an active Oreburgh house; source dummy7 sits on roof, not a door.
 # Use an inspected road-floor arrival-only slot and project scientist return travel.
 k='37.120';n=active[k];dk='36.3';dn=active[dk];sw=next(x for x in F.C.P.source(k)['warps'] if x['index']==1);si=add(k,sw);current(dn);di=len(maps[dn]['warp_events']);maps[dn]['warp_events'].append({'x':49,'y':8,'elevation':3,'dest_map':maps[n]['id'],'dest_warp_id':str(si)});maps[n]['warp_events'][si].update(dest_map=maps[dn]['id'],dest_warp_id=str(di));arrival_only=(dn,di);bridge={'source':n,'destination':dn,'source_cell':[27,5],'destination_cell':[49,8],'arrival_only':True,'reason':'Preserve active Oreburgh house2; dummy7 is roof metadata. Inspected street49,8 is a project arrival, with scientist return travel instead of an invisible floor portal.'}
 def notice(n,x,y,label,text,travel=None):
  m=maps[n];v=grids[n].cell(x,y);assert v['collision']==0 and v['translated_behavior'] not in range(0x10,0x16),(n,x,y,v)
  e=F.C.P.C.P.new_scientist(n,len(m['object_events'])+1,x,y,label);e['local_id']='LOCALID_'+n.upper()+'_ASSET_TRAVEL_'+str(len(m['object_events'])+1);e['elevation']=v['elevation'] if v['elevation'] not in [0,15] else 0;m['object_events'].append(e);body=f'\n@ Project asset/travel notice.\n{label}::\n\tlock\n\tfaceplayer\n\tmsgbox {label}_Text, '+('MSGBOX_YESNO' if travel else 'MSGBOX_DEFAULT')+'\n'
  if travel:body+=f'\tgoto_if_eq VAR_RESULT, NO, {label}_Cancel\n\twarp {travel}\n\twaitstate\n'
  body+='\trelease\n\tend\n'
  if travel:body+=f'{label}_Cancel:\n\trelease\n\tend\n'
  scripts[n]+=body+f'{label}_Text:\n\t.string "{text}$"\n';notices.append({'map':n,'event':e,'cell':v,'travel':travel})
 for k,n in new.items():
  g=grids[n];reserved={(w['x'],w['y']) for w in maps[n]['warp_events']};cells=[(x,y) for y in range(g.h) for x in range(g.w) if (x,y) not in reserved and g.cell(x,y)['collision']==0 and g.cell(x,y)['translated_behavior'] in [0,2,6,7,8,11,0x21] and any(0<=xx<g.w and 0<=yy<g.h and g.cell(xx,yy)['collision']==0 for xx,yy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)])]
  if cells:
   x,y=cells[0];notice(n,x,y,n+'_EventScript_Construction','This area is under construction.\\pPlease check back later!')
  else:refs.append({'map':n,'donor_id':k,'reason':'No safe ordinary land notice cell; construction notice is in connected land hubs. Geometry retained.'})
  for co in F.C.P.source(k)['connections']:
   dk=co['target_id'];op={'up':'down','down':'up','left':'right','right':'left'}.get(co['direction'])
   if dk in new and op and any(z['direction']==op and z['target_id']==k and z['offset']==-co['offset'] for z in F.C.P.source(dk)['connections']):maps[n]['connections']=maps[n]['connections'] or [];maps[n]['connections'].append({'direction':co['direction'],'offset':co['offset'],'map':maps[active[dk]]['id']})
   else:refs.append({'map':n,'donor_id':k,'record':co,'reason':'Foreign/nonreciprocal source boundary held; native boundaries unchanged.'})
 for ref in list(refs):
  w=ref.get('record',{});n=ref['map']
  if 'dest_warp_id' not in w or w.get('target_id') in ['0.0','127.127'] or n not in maps:continue
  g=grids[n];x,y=w['x'],w['y']
  if not(0<=x<g.w and 0<=y<g.h) or g.cell(x,y)['collision'] or g.cell(x,y)['translated_behavior'] in range(0x10,0x16):continue
  if any((e['x'],e['y'])==(x,y) for e in maps[n]['object_events']) or any((e['x'],e['y'])==(x,y) for e in maps[n]['warp_events']):continue
  notice(n,x,y,n+'_EventScript_HeldEntrance_'+str(len(maps[n]['object_events'])),'This entrance is under construction.\\pPlease check back later!');ref['construction_gate']=[x,y]
 # Project yes/no travel bypasses construction gates for asset testing; cancel changes no state.
 home='SootopolisCity_MysteryEventsHouse_1F';m=current(home);label=home+'_EventScript_HyperAnnexConstruction';prefix=scripts[home].split('\n@ Project-owned annex;')[0];scripts[home]=prefix;old=next(e for e in m['object_events'] if e['script']==label);m['object_events'].remove(old);notice(home,old['x'],old['y'],label,'Sinnoh is under construction.\\pWould you like to visit?',maps[dn]['id']+', 49, 8');assert grids[dn].cell(49,8)['collision']==0;notice(dn,50,8,dn+'_EventScript_ReturnHoenn','Would you like to return to Hoenn?','MAP_SOOTOPOLIS_CITY_MYSTERY_EVENTS_HOUSE_1F, 10, 6')
 # Alternate scenes and the repurposed harbor receive explicit project inspection travel, not donor story entry logic.
 inspection_travel=[]
 for pk,dk in [('36.95','36.92'),('36.95','36.96'),('35.6','26.59')]:
  pn=active[pk];destination=active[dk];pm=current(pn);g=grids[pn];occupied={(e['x'],e['y']) for e in pm['object_events']}|{(w['x'],w['y']) for w in pm['warp_events']};choices=[]
  for y in range(1,g.h-1):
   for x in range(1,g.w-1):
    v=g.cell(x,y)
    if (x,y) not in occupied and v['collision']==0 and v['translated_behavior'] in [0,2,6,7,8,11,0x21]:choices.append((x,y))
  assert choices,pn;x,y=choices[0];assert maps[destination]['warp_events'];notice(pn,x,y,pn+'_EventScript_Inspect_'+dk.replace('.','_'),'This annex is under construction.\\pWould you like to inspect it?',maps[destination]['id']+', 0');inspection_travel.append({'source':pn,'destination':destination,'destination_warp':0,'source_cell':[x,y],'reason':'Project inspection travel to registered alternate scene/repurposed harbor. Source story warps and native event-island identities remain untouched.'})
 from sinnoh_coronet_inspection import enable
 enable(maps,scripts)
 # Never leave interior scientists on newly restored static return warps.
 moved=[]
 for n,m in maps.items():
  if not n.startswith('HyperHoenn_'):continue
  g=grids[n];occupied={(e['x'],e['y']) for e in m['object_events']}|{(w['x'],w['y']) for w in m['warp_events']}
  for e in m['object_events']:
   if not any((e['x'],e['y'])==(w['x'],w['y']) for w in m['warp_events']):continue
   x,y=e['x'],e['y'];choices=[]
   for yy in range(max(0,y-4),min(g.h,y+5)):
    for xx in range(max(0,x-4),min(g.w,x+5)):
     v=g.cell(xx,yy)
     if (xx,yy) not in occupied and v['collision']==0 and v['translated_behavior'] in [0,2,6,7,8,11,0x21]:choices.append((abs(xx-x)+abs(yy-y),yy,xx,v))
   assert choices,(n,x,y);_,yy,xx,v=min(choices);before=copy.deepcopy(e);e.update(x=xx,y=yy,elevation=v['elevation'] if v['elevation'] not in [0,15] else 0);moved.append({'map':n,'before':before,'after':copy.deepcopy(e),'cell':v});occupied.add((xx,yy))
 portal={n:n for n in maps if n!=home};arrival=maps[arrival_only[0]]['warp_events'].pop(arrival_only[1]);header,meta=special_portal_assets.integrate(R,maps,ls['layouts'],portal,grids,header,meta,files,derivatives,patches,stage='sinnoh');maps[arrival_only[0]]['warp_events'].insert(arrival_only[1],arrival)
 for n,g in grids.items():
  if n==home:continue
  l=next(x for x in ls['layouts'] if x['id']==maps[n]['layout']);files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(g.blocks),*g.blocks)
 files['src/data/tilesets/headers.h']=header.encode();files['src/data/tilesets/metatiles.h']=meta.encode();files['data/event_scripts.s']=((R/'data/event_scripts.s').read_text()+'\n@ Project-owned Sinnoh asset/travel maps.\n'+''.join(f'\t.include "data/maps/{n}/scripts.inc"\n' for n in new.values())).encode()
 names=[f'    {{{maps[n]["id"]}, _("{F.C.P.source(k)["name"]}")}},' for k,n in sorted(new.items()) if k not in HOENN_EXTRAS]
 display='''/* Project presentation metadata; saved met-location remains a regional u8. */
static const struct { u16 map; u8 name[32]; } sHyperSinnohMapNames[] = {
'''+ '\n'.join(names)+'''
};
static const u8 *HyperSinnoh_CurrentDisplayName(void)
{
    u16 map = gSaveBlock1Ptr->location.mapNum | (gSaveBlock1Ptr->location.mapGroup << 8);
    u32 i;
    for (i = 0; i < ARRAY_COUNT(sHyperSinnohMapNames); i++)
        if (sHyperSinnohMapNames[i].map == map)
            return sHyperSinnohMapNames[i].name;
    return NULL;
}
'''
 files['src/hyper_sinnoh_display_names.inc']=display.encode();popup=(R/'src/map_name_popup.c').read_text();popup=popup.replace('#include "constants/map_types.h"','#include "constants/map_types.h"\n#include "constants/map_groups.h"').replace('// enums','#include "hyper_sinnoh_display_names.inc"\n\n// enums',1);needle='        GetMapName(dest, mapHeader->regionMapSectionId, 0);';assert needle in popup;popup=popup.replace(needle,'        if (mapHeader->regionMapSectionId == MAPSEC_SINNOH && HyperSinnoh_CurrentDisplayName() != NULL)\n            StringCopy(dest, HyperSinnoh_CurrentDisplayName());\n        else\n    '+needle);files['src/map_name_popup.c']=popup.encode()
 ids={m['id']:m for m in [*allmaps.values(),*maps.values()]}
 for n,m in maps.items():
  assert len(m['object_events'])<256 and len(m['warp_events'])<256
  for w in m['warp_events']:assert w['dest_map'] in ids and 0<=int(w['dest_warp_id'])<len(ids[w['dest_map']]['warp_events']),(n,w)
 from sinnoh_signed_ids import regroup
 groups=regroup(groups)
 for z in inventory:z['group']=next(g for g in groups['group_order'] if z['map'] in groups[g])
 assert groups['group_order'][:len(oldgroups['group_order'])]==oldgroups['group_order'];assert len(groups['group_order'])<=127 and all(len(groups[g])<=127 for g in groups['group_order'])
 for group in oldgroups['group_order']:assert groups[group][:len(oldgroups[group])]==oldgroups[group]
 return locals()
def apply():
 q=prepare();b=q['baseline'];assert all(F.digest(R/f)==h for f,h in b.items())
 for f in ['data/layouts/layouts.json','data/maps/map_groups.json','src/data/region_map/region_map_sections.json','src/map_name_popup.c','data/event_scripts.s',*[f'data/maps/{n}/{file}' for n in q['maps'] if n in q['original'] for file in ['map.json','scripts.inc']]]:
  p=O/'original'/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((R/f).read_bytes())
 for n,m in q['maps'].items():F.dump(R/f'data/maps/{n}/map.json',m);p=R/f'data/maps/{n}/scripts.inc';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(q['scripts'][n])
 for f,data in q['files'].items():p=R/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 F.dump(R/'data/layouts/layouts.json',q['ls']);F.dump(R/'data/maps/map_groups.json',q['groups']);F.dump(R/'src/data/region_map/region_map_sections.json',q['sections']);F.dump(R/'.la_work/amap/hyper_asset_integration/asset_catalog.json',q['cat'])
 F.dump(O/'receipt.json',{'schema':'hyper-sinnoh-assets-travel-v1','new_maps':q['new'],'touched_maps':list(q['maps']),'baseline':b,'changed_baseline_files':{f:{'before':h,'after':F.digest(R/f)} for f,h in b.items() if F.digest(R/f)!=h},'new_files':{str(p.relative_to(R)):F.digest(p) for d in F.C.P.PREFIXES for p in (R/d).rglob('*') if p.is_file() and str(p.relative_to(R)) not in b and not F.C.P.C.P.C.C.derived(str(p.relative_to(R)))},'old_mapsec_ids':[x['id'] for x in q['oldsections']['map_sections']],'asset_banks':q['rows'],'attribute_derivatives':q['derivatives'],'gameplay_imported':False,'save_abi_changed':False,'runtime_verified':False})
 F.dump(O/'manifest.json',{'maps':q['inventory'],'quarantined_sources':QUARANTINE,'source_to_project_warps':q['warps'],'deferred_references':q['refs'],'travel_bridge':q['bridge'],'arrival_rebindings':q['rebindings'],'inspection_travel':q['inspection_travel'],'geometry_patches':q['patches'],'notice_moves':q['moved'],'animation_subset':q['anim'],'policy':'Assets and static project travel only; native gameplay/save ABI remain authoritative.'});print('Registered',len(q['new']),'maps and',len(q['rows']),'recovered banks.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--apply',action='store_true');a=p.parse_args()
 if a.apply:apply()
 else:q=prepare();print('Prepared',len(q['new']),'maps;',len(q['refs']),'held references.')
