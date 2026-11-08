"""Validate HnS preservation, stable numeric identities and placeholder ownership."""
import hashlib,json,struct
from pathlib import Path
R=Path(__file__).resolve().parents[4];D=R/'docs/la_world/hns_regions'
def read(p):return json.loads(p.read_text())
def main():
 mf=read(D/'manifest.json');groups=read(R/'data/maps/map_groups.json');layouts=read(R/'data/layouts/layouts.json');bylayout={x['id']:x for x in layouts['layouts']};rows={x['id']:x for x in mf['maps']};fail=[]
 generated={'data/maps/groups.inc','data/maps/headers.inc','data/maps/events.inc','data/maps/connections.inc','data/layouts/layouts_table.inc','data/layouts/layouts.inc'}
 protected=read(R/'.la_work/amap/hns_regions_backup/protected.json')
 for f,h in protected.items():
  if f in generated:continue
  p=R/f
  if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:fail.append(dict(type='preexisting_file_changed',path=f))
 counts=dict(maps=len(rows),preserved_preexisting_files=len(protected)-len(generated),runtime_objects=0,hidden_objects=0,warps=0,connections=0,coord_markers=0,bg_markers=0)
 for row in rows.values():
  name=row['name'];m=read(R/'data/maps'/name/'map.json');l=bylayout[row['layout']]
  assert groups[groups['group_order'][row['group']]][row['map']]==name
  for field,hashfield in [('blockdata_filepath','blockdata_sha256'),('border_filepath','border_sha256')]:
   assert hashlib.sha256((R/l[field]).read_bytes()).hexdigest()==row[hashfield],name
  assert len(m['object_events'])<=64
  for e in m['object_events']:
   assert e['trainer_type']=='TRAINER_TYPE_NONE' and e['trainer_sight_or_berry_tree_id']=='0'
   assert e['flag'] in ['0','FLAG_HIDE_HNS_PLACEHOLDER_VARIANTS']
   assert e['script'] in ['HnsRegion_Placeholder',name+'_Inspect']
   counts['runtime_objects']+=1;counts['hidden_objects']+=e['flag']=='FLAG_HIDE_HNS_PLACEHOLDER_VARIANTS'
  for e in m['warp_events']:
   dest=rows[e['dest_map']];dm=read(R/'data/maps'/dest['name']/'map.json')
   assert 0<=int(e['dest_warp_id'])<len(dm['warp_events']),(name,e)
   assert row['reference_only'] or not dest['reference_only']
   counts['warps']+=1
  for e in m['connections']:
   assert e['map'] in rows and not rows[e['map']]['reference_only'];counts['connections']+=1
  for e in m['coord_events']:
   assert e['script']=='HnsRegion_NoOp' and e['var']=='VAR_TEMP_1' and e['var_value']=='65535';counts['coord_markers']+=1
  for e in m['bg_events']:
   assert e['type']=='sign' and e['script']=='HnsRegion_Sign';counts['bg_markers']+=1
  text=(R/'data/maps'/name/'scripts.inc').read_text()
  for forbidden in ['trainerbattle','giveitem','setvar','clearflag','setwildbattle','callnative']:
   assert forbidden not in text,(name,forbidden)
 # All old map/group and layout numeric positions were retained.
 import tarfile
 with tarfile.open(R/'.la_work/amap/hns_regions_backup/before.tar.gz') as z:
  og=json.load(z.extractfile('data/maps/map_groups.json'));ol=json.load(z.extractfile('data/layouts/layouts.json'))
 for i,g in enumerate(og['group_order']):
  assert groups['group_order'][i]==g and groups[g][:len(og[g])]==og[g]
 for i,l in enumerate(ol['layouts']):assert layouts['layouts'][i]['id']==l['id']
 counts.update(failures=fail,source_object_records=len(read(D/'object_event_ledger.json')),source_art_selectors=len(read(D/'object_assets.json')['assets']))
 (D/'validation.json').write_text(json.dumps(counts,indent=2)+'\n')
 assert not fail,fail
 print(json.dumps(counts))
if __name__=='__main__':main()
