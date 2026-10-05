#!/usr/bin/env python3
"""Reconcile the native Frontier plaza/ferry/Sudowoodo owners onto Hyper geometry."""
import copy,struct
import hoenn_finalization as F
import special_portal_assets
R=F.R;O=F.O;SCOPE={'BattleFrontier_OutsideWest':'26.4','BattleFrontier_OutsideEast':'26.14'}

def prepare():
 rec=F.load(O/'receipt.json');j=F.load(O/'reconciliation.json');assert not j.get('frontier_plazas_completed'),'Already applied'
 ls=F.load(R/'data/layouts/layouts.json');oldls=copy.deepcopy(ls);header=(R/'src/data/tilesets/headers.h').read_text();meta=(R/'src/data/tilesets/metatiles.h').read_text();by={x['donor_id']:x for x in F.load(R/'.la_work/amap/hyper_asset_integration/asset_catalog.json')['layouts']};maps={n:F.load(R/f'data/maps/{n}/map.json') for n in SCOPE};original=copy.deepcopy(maps);grids={n:F.C.P.C.Grid(by[k]) for n,k in SCOPE.items()};files={};events=[];patches=[];derivatives={}
 planner=F.load(R/'.la_work/amap/hyper_hoenn_replacement/hyper_hoenn_replacement_manifest.json');canonical={z['hyper']['id']:z['canonical']['id'] for z in planner['maps'] if z.get('hyper')}
 for n,k in SCOPE.items():
  m=maps[n];g=grids[n];d=F.C.P.source(k);l=next(x for x in ls['layouts'] if x['id']==m['layout']);assert (g.w,g.h)==(l['width'],l['height'])
  for kind,dk in F.C.P.KINDS.items():
   for i,e in enumerate(m[kind]):
    before=copy.deepcopy(e);probe=next((x for x in d[dk] if x['index']==i),None);reason='Canonical gameplay identity retained.'
    if kind=='warp_events':
     assert probe and canonical.get(probe['target_id'])==e['dest_map'],(n,i,e,probe)
     e['x'],e['y']=probe['x'],probe['y'];reason='Matched source slot and canonical facility destination; native destination and slot retained.'
    elif kind=='object_events':
     assert probe,(n,i)
     e['x'],e['y']=probe['x'],probe['y'];reason='Reviewed native/source object roles align for every native slot; donor-added NPCs ignored.'
    elif kind=='bg_events':
     assert probe and probe['type']==e['type'],(n,i,e,probe)
     e['x'],e['y']=probe['x'],probe['y'];reason='Same source BG role; retain native sign/item identity and script.'
    v=g.cell(e['x'],e['y']);assert v['collision']==0 or kind in ['bg_events','warp_events'] or e['graphics_id']=='OBJ_EVENT_GFX_SS_TIDAL',(n,kind,i,v)
    if kind=='object_events' and e['graphics_id']!='OBJ_EVENT_GFX_SS_TIDAL' and v['elevation'] not in [0,15]:e['elevation']=v['elevation']
    assert all(e[f]==before[f] for f in before if f not in ['x','y','elevation'])
    events.append({'map':n,'kind':kind,'index':i,'before':before,'after':copy.deepcopy(e),'donor_reference':probe,'cell':v,'reason':reason})
  for at,v in enumerate(list(g.blocks)):
   cell=g.cell(at%g.w,at//g.w)
   if cell['collision']==0 and cell['translated_behavior'] in range(0x10,0x16) and cell['elevation']!=1:g.blocks[at]=(v&4095)|4096;patches.append({'map':n,'x':at%g.w,'y':at//g.w,'before':v,'after':g.blocks[at],'reason':'Surfable Frontier water remains elevation1.'})
  l.update(primary_tileset=by[k]['primary_tileset'],secondary_tileset=by[k]['secondary_tileset'],border_filepath=by[k]['border_path'],blockdata_filepath=f'data/hyper_assets/finalization_layouts/{n}/map.bin')
 # Native girl shudder movements do not move cells; Sudowoodo is unchanged at54,62; ferry actors/boarding coordinates are unchanged.
 assert [(e['x'],e['y']) for e in maps['BattleFrontier_OutsideWest']['object_events'][1:3]]==[(20,70),(19,68)]
 assert (maps['BattleFrontier_OutsideEast']['object_events'][13]['x'],maps['BattleFrontier_OutsideEast']['object_events'][13]['y'])==(54,62)
 header,meta=special_portal_assets.integrate(R,maps,ls['layouts'],{n:n for n in SCOPE},grids,header,meta,files,derivatives,patches,stage='finalization_frontier')
 for n,g in grids.items():
  l=next(x for x in ls['layouts'] if x['id']==maps[n]['layout']);files[l['blockdata_filepath']]=struct.pack('<'+'H'*len(g.blocks),*g.blocks)
 return locals()

def apply():
 q=prepare();rec=q['rec'];j=q['j']
 for f,h in rec['baseline'].items():assert F.digest(R/f)==rec['changed_baseline_files'].get(f,{}).get('after',h),('Protected file changed',f)
 for n,m in q['maps'].items():F.dump(O/f'original/data/maps/{n}/map.json',q['original'][n]);F.dump(R/f'data/maps/{n}/map.json',m)
 for f,data in q['files'].items():p=R/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data);rec['new_files'][f]=F.digest(p)
 F.dump(R/'data/layouts/layouts.json',q['ls']);(R/'src/data/tilesets/headers.h').write_text(q['header']);(R/'src/data/tilesets/metatiles.h').write_text(q['meta'])
 for f,h in rec['baseline'].items():
  actual=F.digest(R/f)
  if actual!=h:rec['changed_baseline_files'][f]={'before':h,'after':actual}
 rec['donor_ids'].update(SCOPE);rec['touched_maps']=sorted(set(rec['touched_maps'])|set(SCOPE));j['frontier_events']=q['events'];j['geometry_patches']+=q['patches'];j['attribute_derivatives'].update(q['derivatives']);j['frontier_plazas_completed']=True;j['kept_original']=[x for x in j['kept_original'] if x['map'] not in SCOPE]
 for n,k in SCOPE.items():j['asset_ports'].append({'map':n,'donor_id':k,'mode':'LAYOUT_REPLACEMENT','events_remapped':True,'scripts_unchanged':True})
 F.dump(O/'receipt.json',rec);F.dump(O/'reconciliation.json',j);print('Completed Frontier plazas with',len(q['events']),'native event records.')
if __name__=='__main__':
 import sys
 if '--apply' in sys.argv:apply()
 else:q=prepare();print('Prepared Frontier geometry and',len(q['events']),'native event records.')
