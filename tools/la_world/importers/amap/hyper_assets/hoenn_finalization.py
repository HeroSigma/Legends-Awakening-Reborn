#!/usr/bin/env python3
"""Hoenn closure: guarded asset-only room ports and reviewed special links."""
import argparse,copy,collections,csv,json,re,struct
import hoenn_canary9 as C
R=C.ROOT; O=R/'.la_work/amap/hyper_hoenn_finalization'
load=C.load;dump=C.dump;digest=C.digest;words=C.words

def grid(l,header,meta):
 g=C.P.C.Grid.__new__(C.P.C.Grid);g.w,g.h=l['width'],l['height'];g.blocks=words(R/l['blockdata_filepath']);g.attrs=[]
 for role in ['primary_tileset','secondary_tileset']:
  body=re.search(r'const struct Tileset\s+'+l[role]+r'\s*=\s*\{(.*?)\};',header,re.S)[1];sy=re.search(r'\.metatileAttributes\s*=\s*(\w+)',body)[1];path=re.search(re.escape(sy)+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"\)',meta)[1];g.attrs.append(words(R/path))
 return g

def prepare():
 assert not (O/'receipt.json').exists(),'Already applied; use --audit.'
 O.mkdir(parents=True,exist_ok=True)
 baseline={str(f.relative_to(R)):digest(f) for d in C.P.PREFIXES for f in (R/d).rglob('*') if f.is_file() and not C.P.C.P.C.C.derived(str(f.relative_to(R)))}
 ls=load(R/'data/layouts/layouts.json'); oldls=copy.deepcopy(ls); maps={p.parent.name:load(p) for p in (R/'data/maps').glob('*/map.json')};original=copy.deepcopy(maps);header=(R/'src/data/tilesets/headers.h').read_text();meta=(R/'src/data/tilesets/metatiles.h').read_text();files={};ledger=[];targets={};kept=[];derivatives={};patches=[];grids={};scripts={};links=[]
 cat=load(R/'.la_work/amap/hyper_asset_integration/asset_catalog.json');by={x['donor_id']:x for x in cat['layouts']};active={}
 for i in range(1,10):
  rec=load(R/f'.la_work/amap/hyper_hoenn_canary{i}/receipt.json');active.update(rec['donor_ids'])
 active.update({x['canonical_name']:x['donor_id'] for x in load(R/'.la_work/amap/hyper_hoenn_corridor_correction/sea_corridor_correction_manifest.json')['maps']})
 planner=load(R/'.la_work/amap/hyper_hoenn_replacement/hyper_hoenn_replacement_manifest.json')
 # Only exact full-grid collision, elevation, behavior contracts qualify automatically.
 for z in planner['maps']:
  n=z['canonical']['name'];h=z.get('hyper')
  if n in active or not h:continue
  k=h['id'];m=maps[n];l=next(x for x in ls['layouts'] if x['id']==m['layout']);ng=grid(l,header,meta);dg=C.P.C.Grid(by[k]);reason='Native generated/system or unused map retains expansion ownership.'
  candidates=n.startswith('BattleFrontier_') or n.split('_')[0] in ['LittlerootTown','OldaleTown','PetalburgCity','DewfordTown','SlateportCity','MauvilleCity','RustboroCity'] or n.startswith(('ArtisanCave','AlteringCave','SouthernIsland','FarawayIsland','NavelRock'))
  cell_repairs=[]
  if (ng.w,ng.h)==(dg.w,dg.h) and candidates:
   # Equal metatile and behavior proves the same cell role. Restore only the native runtime bits.
   for at,(a,b) in enumerate(zip(ng.blocks,dg.blocks)):
    if (a&1023)==(b&1023) and (ng.attrs[(a&1023)//512][a&511]&255)==(dg.attrs[(b&1023)//512][b&511]&255) and (a&0xfc00)!=(b&0xfc00):
     dg.blocks[at]=(b&1023)|(a&0xfc00);cell_repairs.append({'map':n,'x':at%ng.w,'y':at//ng.w,'before':b,'after':dg.blocks[at],'reason':'Same metatile and behavior; preserve canonical collision/elevation on recovered Hyper artwork.'})
  if k in ['26.58','26.59','26.67']:candidates=False;reason='Donor identity repurposed as a different region/special; canonical event island is preserved.'
  compatible=(ng.w,ng.h)==(dg.w,dg.h) and all((a&0xfc00)==(b&0xfc00) and (ng.attrs[(a&1023)//512][a&511]&255)==(dg.attrs[(b&1023)//512][b&511]&255) for a,b in zip(ng.blocks,dg.blocks))
  if not candidates or not compatible:
   if candidates:reason='Full-grid runtime contract differs; requires explicit coordinate/scene reconciliation.'
   kept.append({'map':n,'donor_id':k,'reason':reason});continue
  if len([x for x in maps.values() if x['layout']==l['id']])>1:
   l=copy.deepcopy(l);l['id']='LAYOUT_HYPER_FINAL_'+C.P.const(n);l['name']='HyperFinal'+n+'_Layout';ls['layouts'].append(l);m['layout']=l['id']
  l.update(primary_tileset=by[k]['primary_tileset'],secondary_tileset=by[k]['secondary_tileset'],border_filepath=by[k]['border_path'],blockdata_filepath=f'data/hyper_assets/finalization_layouts/{n}/map.bin');patches.extend(cell_repairs);files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(dg.blocks),*dg.blocks);targets[n]=k
  ledger.append({'map':n,'donor_id':k,'mode':'LAYOUT_REPLACEMENT','full_grid_contract_equal':True,'events_and_scripts_unchanged':True})
 def current(n):
  if n not in grids:grids[n]=grid(next(x for x in ls['layouts'] if x['id']==maps[n]['layout']),header,meta)
  return grids[n]
 def warp(n,x,y,dn,di):
  assert not any((e['x'],e['y'])==(x,y) for e in maps[n]['warp_events']),(n,x,y,'duplicate')
  g=current(n);v=g.cell(x,y)
  if v['collision']:
   assert n==C.P.name('35.35') and (x,y)==(25,19),('Unreviewed blocked portal',n,x,y,v)
   g.blocks[y*g.w+x]=v['block']&~0xc00;patches.append({'map':n,'x':x,'y':y,'before':v['block'],'after':g.blocks[y*g.w+x],'reason':'Known source warp25,19 is dormant behind donor gameplay; project portal clears only its collision and binds native warp behavior.'})
  i=len(maps[n]['warp_events']);maps[n]['warp_events'].append({'x':x,'y':y,'elevation':0,'dest_map':maps[dn]['id'],'dest_warp_id':str(di)});return i
 # Source-record coordinates are used only after passable-cell and existing-slot validation.
 for n,k,wi,dn,dk,dwi in [('PacifidlogTown','0.15',6,C.P.name('34.24'),'34.24',0),('Route129','0.44',0,C.P.name('35.63'),'35.63',2),(C.P.name('35.49'),'35.49',1,C.P.name('35.3'),'35.3',0),(C.P.name('35.31'),'35.31',0,C.P.name('34.41'),'34.41',2),(C.P.name('35.35'),'35.35',0,C.P.name('35.5'),'35.5',1)]:
  sw=next(x for x in C.P.source(k)['warps'] if x['index']==wi);dw=next(x for x in C.P.source(dk)['warps'] if x['index']==dwi)
  existing=next((i for i,e in enumerate(maps[n]['warp_events']) if (e['x'],e['y'])==(sw['x'],sw['y'])),None)
  di=len(maps[dn]['warp_events']);si=existing if existing is not None else warp(n,sw['x'],sw['y'],dn,di)
  if existing is not None:assert maps[n]['warp_events'][si]['dest_map']==maps[dn]['id']
  di=warp(dn,dw['x'],dw['y'],n,si);maps[n]['warp_events'][si]['dest_warp_id']=str(di)
  links.append({'source':n,'warp_index':si,'destination':dn,'destination_warp':di,'source_record':sw,'destination_record':dw,'reason':'Complete static reciprocal arrival using actual donor cells; donor gameplay excluded.'})
 # Annex on the east side of native Mystery Events room, outside every native scripted movement.
 n='SootopolisCity_MysteryEventsHouse_1F';dn=C.P.name('37.121');m=maps[n];g=current(n);assert g.cell(9,3)['collision']==0;si=len(m['warp_events']);m['warp_events'].append({'x':9,'y':2,'elevation':0,'dest_map':maps[dn]['id'],'dest_warp_id':'0'})
 for lid in [m['layout'],'LAYOUT_SOOTOPOLIS_CITY_MYSTERY_EVENTS_HOUSE_1F_STAIRS_UNBLOCKED']:
  l=next(x for x in ls['layouts'] if x['id']==lid);b=words(R/l['blockdata_filepath']);assert (l['width'],l['height'])==(11,8);before=b[2*11+9];b[2*11+9]=0x0241;files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(b),*b);patches.append({'map':n,'layout':lid,'x':9,'y':2,'before':before,'after':0x0241,'reason':'Project annex stairs reuse existing native stair artwork; west story stairs and movements preserved.'})
 for i in [0,1]:maps[dn]['warp_events'][i].update(dest_map=m['id'],dest_warp_id=str(si))
 label=n+'_EventScript_HyperAnnexConstruction';e=C.P.C.P.new_scientist(n,1,9,2,label);e['local_id']='LOCALID_SOOTOPOLIS_HYPER_ANNEX_SCIENTIST';e['elevation']=0;m['object_events'].append(e);scripts[n]=(R/f'data/maps/{n}/scripts.inc').read_text()+f'\n@ Project-owned annex; native Mystery Events ownership retained.\n{label}::\n\tlock\n\tfaceplayer\n\tmsgbox {label}_Text, MSGBOX_DEFAULT\n\trelease\n\tend\n{label}_Text:\n\t.string "The annex is under construction.\\p"\n\t.string "Please check back later!$"\n'
 links.append({'source':n,'warp_index':si,'destination':dn,'destination_warp':0,'reason':'New east annex; source outdoor doorway remains authoritative Mystery Events entrance.'})
 # Existing native source slots are untouched. Only new/restored special portals need art-only behavior adapters.
 import special_portal_assets
 portal={n:n for n in grids if n!='SootopolisCity_MysteryEventsHouse_1F'}
 header,meta=special_portal_assets.integrate(R,maps,ls['layouts'],portal,grids,header,meta,files,derivatives,patches,stage='finalization')
 files['src/data/tilesets/headers.h']=header.encode();files['src/data/tilesets/metatiles.h']=meta.encode()
 for e in maps['Route106']['object_events']:
  if 'REGISTERED_CONSTRUCTION_' in e.get('local_id','') and (e['x'],e['y']) in [(47,19),(52,19)]:
   assert current('Route106').cell(e['x'],18)['collision']==0;e['y']=18;e['elevation']=3
 changedmaps={n:m for n,m in maps.items() if m!=original[n]}
 return locals()

def apply():
 q=prepare();b=q['baseline'];assert all(digest(R/f)==h for f,h in b.items())
 for n,m in q['changedmaps'].items():dump(R/f'data/maps/{n}/map.json',m)
 for n,s in q['scripts'].items():(R/f'data/maps/{n}/scripts.inc').write_text(s)
 for f,data in q['files'].items():p=R/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 dump(R/'data/layouts/layouts.json',q['ls'])
 for f in ['data/layouts/layouts.json',*[f'data/maps/{n}/map.json' for n in set(q['changedmaps'])|set(q['targets'])],*[f'data/maps/{n}/scripts.inc' for n in q['scripts']]]:
  p=O/'original'/f;p.parent.mkdir(parents=True,exist_ok=True)
  if f=='data/layouts/layouts.json':dump(p,q['oldls'])
  elif f.endswith('map.json'):dump(p,q['original'][f.split('/')[2]])
 # Save native script snapshots from Git is unsafe with user changes; separately retain the exact original prefix.
 for n in q['scripts']:
  s=q['scripts'][n].split('\n@ Project-owned annex;')[0];(O/f'original/data/maps/{n}/scripts.inc').write_text(s)
 dump(O/'receipt.json',{'schema':'hyper-hoenn-finalization-v1','donor_ids':q['targets'],'touched_maps':list(q['changedmaps']),'baseline':b,'changed_baseline_files':{f:{'before':h,'after':digest(R/f)} for f,h in b.items() if digest(R/f)!=h},'new_files':{f:digest(R/f) for f in q['files'] if f not in b},'hyper_gameplay_imported':False,'runtime_verified':False})
 dump(O/'reconciliation.json',{'asset_ports':q['ledger'],'completed_links':q['links'],'geometry_patches':q['patches'],'kept_original':q['kept'],'attribute_derivatives':q['derivatives']});print('Applied',len(q['targets']),'contract-compatible asset ports and',len(q['links']),'special entrance repairs.')

def audit():
 rec=load(O/'receipt.json');later_path=R/'.la_work/amap/hyper_sinnoh_asset_travel/receipt.json';later=load(later_path) if later_path.exists() else None
 fixpath=R/'.la_work/amap/hyper_sinnoh_id_correction/receipt.json';fix=load(fixpath) if fixpath.exists() else None
 for f,h in rec['baseline'].items():
  expected=rec['changed_baseline_files'].get(f,{}).get('after',h)
  if later and f in later['changed_baseline_files']:
   change=later['changed_baseline_files'][f];assert change['before']==expected,('Hoenn/Sinnoh receipt chain',f);expected=change['after']
  if fix:
   for changes in [fix['user_edits'],fix['changed_files']]:
    if f in changes:
     change=changes[f];assert change['before']==expected,('Correction chain',f);expected=change['after']
  assert (digest(R/f) if (R/f).exists() else None)==expected,('Protected baseline changed',f)
 data=load(O/'reconciliation.json');maps={p.parent.name:load(p) for p in (R/'data/maps').glob('*/map.json') if 'id' in load(p)};ids={m['id']:n for n,m in maps.items()};ls={x['id']:x for x in load(R/'data/layouts/layouts.json')['layouts']};header=(R/'src/data/tilesets/headers.h').read_text();meta=(R/'src/data/tilesets/metatiles.h').read_text();gates=[];specials={n for n in maps if n.startswith('HyperHoenn_')};roots=set();edges={}
 for n,m in maps.items():
  edges[n]=[ids[e['dest_map']] for e in m.get('warp_events',[]) if e['dest_map'] in ids]+[ids[e['map']] for e in m.get('connections') or [] if e['map'] in ids]
  if n not in specials:roots.add(n)
  for e in m.get('object_events',[]):
   if e['graphics_id']=='OBJ_EVENT_GFX_SCIENTIST_1' and 'Construction' in e['script']:
    g=grid(ls[m['layout']],header,meta);v=g.cell(e['x'],e['y']);assert v['collision']==0 or v['translated_behavior'] in range(0x60,0x70),(n,e,v)
    gates.append({'map':n,'x':e['x'],'y':e['y'],'script':e['script'],'on_warp':any((w['x'],w['y'])==(e['x'],e['y']) for w in m['warp_events']),'valid_cell':True})
 for n in maps:
  text=(R/f'data/maps/{n}/scripts.inc').read_text() if (R/f'data/maps/{n}/scripts.inc').exists() else ''
  for target in re.findall(r'^\s*warp\s+(MAP_\w+)',text,re.M):
   if target in ids:edges[n].append(ids[target])
 def reach(start):
  seen=set(start);todo=list(start)
  while todo:
   for n in edges[todo.pop()]:
    if n not in seen:seen.add(n);todo.append(n)
  return seen
 accessible=reach(roots);unreachable=sorted(specials-accessible);no_return=[n for n in specials if not reach([n])&roots]
 for n in rec['donor_ids']:
  original=load(O/f'original/data/maps/{n}/map.json') if (O/f'original/data/maps/{n}/map.json').exists() else maps[n]
  for k in ['object_events','warp_events','coord_events','bg_events','connections']:
   if n.startswith('BattleFrontier_Outside') and k.endswith('_events'):
    assert len(maps[n][k])==len(original[k]);assert all({a:b for a,b in e.items() if a not in ['x','y','elevation']}=={a:b for a,b in o.items() if a not in ['x','y','elevation']} for e,o in zip(maps[n][k],original[k])),(n,k)
   else:assert maps[n][k]==original[k],(n,k)
 result={'passed':not unreachable and not no_return,'construction_gate_count':len(gates),'special_maps':len(specials),'structurally_reachable':len(specials)-len(unreachable),'unreachable':unreachable,'without_canonical_return':no_return,'gates':gates,'runtime_verified':False};dump(O/'construction_audit.json',result);print(json.dumps({k:v for k,v in result.items() if k!='gates'},indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--apply',action='store_true');p.add_argument('--audit',action='store_true');a=p.parse_args()
 if a.apply:apply()
 elif a.audit:audit()
 else:q=prepare();print('Prepared',len(q['targets']),'maps and',len(q['links']),'links.')
