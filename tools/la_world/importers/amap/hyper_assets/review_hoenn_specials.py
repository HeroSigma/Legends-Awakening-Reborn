#!/usr/bin/env python3
"""Inventory registered Hyper Hoenn specials without changing maps or gameplay."""
import csv,json,re,hashlib,shutil,collections
from pathlib import Path
import hoenn_finalization as F
R=F.R

def review():
 source=R/'.la_work/amap/hoenn_interior_polish10';out=R/'docs/la_world/hyper_hoenn/interior_polish10';out.mkdir(parents=True,exist_ok=True)
 rendered=F.load(source/'inventory.json');catalog={z['donor_id']:z for z in F.load(R/'.la_work/amap/hyper_asset_integration/asset_catalog.json')['layouts']};maps={p.parent.name:F.load(p) for p in (R/'data/maps').glob('*/map.json')};ids={m['id']:n for n,m in maps.items()};groups=F.load(R/'data/maps/map_groups.json');numeric={n:(gi,mi,g) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])};rows=[];relationships=[];gates=[];issues=[]
 for z in rendered:
  n=z['map'];m=maps[n];l=z['layout'];mo=re.match(r'HyperHoenn_(\d+)_(\d+)_(.*)',n);did=f'{mo[1]}.{mo[2]}';d=catalog.get(did);gi,mi,group=numeric[n]
  row={'map':n,'map_id':m['id'],'group_id':gi,'map_number':mi,'group_name':group,'map_section':m['region_map_section'],'donor_identity':'Hyper Emerald v5.7 EN QoL','donor_id':did,'donor_name_reference':mo[3].replace('_',' '),'category':'SPECIAL_ASSETS_TRAVEL_ONLY','layout':m['layout'],'width':l['width'],'height':l['height'],'map_type':m['map_type'],'primary_tileset':l['primary_tileset'],'secondary_tileset':l['secondary_tileset'],'object_count':len(m['object_events']),'warp_count':len(m['warp_events']),'coord_count':len(m['coord_events']),'bg_count':len(m['bg_events']),'connection_count':len(m['connections'] or []),'header_pointer':d.get('donor_header_pointer') if d else None,'layout_pointer':d.get('donor_layout_pointer') if d else None,'current_blockdata_sha256':F.digest(R/l['blockdata_filepath']),'script_sha256':F.digest(R/f'data/maps/{n}/scripts.inc'),'runtime_verified':False}
  rows.append(row)
  for i,w in enumerate(m['warp_events']):
   relationships.append({'source':n,'kind':'warp','slot':i,**w,'destination_name':ids.get(w['dest_map'])})
   if w['dest_map']!='MAP_DYNAMIC':
    if w['dest_map'] not in ids or not 0<=int(w['dest_warp_id'])<len(maps[ids[w['dest_map']]]['warp_events']):issues.append({'map':n,'kind':'INVALID_DESTINATION','event':w})
  for c in m['connections'] or []:relationships.append({'source':n,'kind':'connection',**c,'destination_name':ids.get(c['map'])})
 # Scientists at canonical entrances are part of the gate inventory too.
 special_ids={maps[z['map']]['id'] for z in rendered}
 for n,m in maps.items():
  for i,e in enumerate(m.get('object_events',[])):
   if e.get('graphics_id')!='OBJ_EVENT_GFX_SCIENTIST_1':continue
   script=e.get('script','');targets=[w['dest_map'] for w in m.get('warp_events',[]) if (w['x'],w['y'])==(e['x'],e['y'])]
   if n.startswith('HyperHoenn_') or any(t in special_ids for t in targets) or 'Construction' in script:
    gates.append({'map':n,'object_index':i,'x':e['x'],'y':e['y'],'elevation':e['elevation'],'script':script,'flag':e.get('flag'),'coincident_warp_destinations':targets,'status':'PRESERVED'})
 raw=F.load(source/'access_audit.json');queue=[]
 for i,issue in enumerate(raw['issues']):
  queue.append({'review_id':i+1,'status':'OPEN','kind':issue['kind'],'map':issue['map'],'finding':issue,'action':'Inspect source geometry, arrival facing and project travel state before opening this route.' if issue['kind']=='WARP_NO_FREE_NEIGHBOR' else 'Inspect connection/script entry and reachable scientist approach. Static warp-root BFS is insufficient to clear this finding.','runtime_verified':False})
 F.dump(out/'special_area_inventory.json',rows);F.dump(out/'relationships.json',relationships);F.dump(out/'scientist_gate_inventory.json',gates);F.dump(out/'manual_review.json',queue)
 for name,data in [('special_area_inventory.csv',rows),('manual_review.csv',[{'review_id':z['review_id'],'status':z['status'],'map':z['map'],'kind':z['kind'],'action':z['action']} for z in queue])]:
  with (out/name).open('w',newline='') as f:
   writer=csv.DictWriter(f,fieldnames=list(data[0]));writer.writeheader();writer.writerows(data)
 for p in source.glob('contact_*.png'):shutil.copy2(p,out/p.name)
 for name in ['inventory.json','access_audit.json']:shutil.copy2(source/name,out/name)
 summary={'registered_maps':len(rows),'map_types':dict(collections.Counter(z['map_type'] for z in rows)),'relationships':len(relationships),'gate_scientists':len(gates),'warp_records_checked':raw['warp_arrivals'],'actor_candidates':raw['active_actors'],'open_access_findings':len(queue),'invalid_destination_records':issues,'invalid_palette_refs':sum(len(z['invalid_palette_refs']) for z in rendered),'runtime_verified':False};F.dump(out/'summary.json',summary);print(json.dumps(summary,indent=2));return summary
if __name__=='__main__':review()
