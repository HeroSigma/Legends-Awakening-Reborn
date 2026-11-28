"""Pack only referenced Galar metatiles; preserve tile art, behaviors and geometry."""
from pathlib import Path
from collections import defaultdict
import json,struct,hashlib
R=Path(__file__).resolve().parents[4]
D=R/'docs/la_world/galar_recovery'
def main():
 assert not (D/'metatile-packing.json').exists(), 'Packing already recorded; do not renumber twice'
 layouts={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']}
 ledger=json.loads((D/'import_ledger.json').read_text());used=defaultdict(set);blobs=[]
 for z in ledger:
  l=layouts[z['layout']];keys=[l[k].replace('gTileset_Galar_','') for k in ['primary_tileset','secondary_tileset']]
  for field in ['blockdata_filepath','border_filepath']:
   p=R/l[field];old=p.read_bytes();blobs.append((p,keys,old))
   for v, in struct.iter_unpack('<H',old):used[keys[(v&1023)//512]].add(v&511)
 tables={};maps={};saved=0;bank_receipts=[]
 for folder in (R/'data/galar_assets/tilesets').iterdir():
  tile=folder/'metatiles.bin';attribute=folder/'metatile_attributes.bin';old=tile.read_bytes();attrs=attribute.read_bytes()
  assert len(old)==512*24 and len(attrs)==512*2,folder
  indices=sorted(used[folder.name]|{0});mapping={v:i for i,v in enumerate(indices)};maps[folder.name]=mapping
  new=b''.join(old[v*24:v*24+24] for v in indices);newattrs=b''.join(attrs[v*2:v*2+2] for v in indices)
  backup=R/'archives/galar-reviewed-source/tilesets'/folder.name;backup.mkdir(parents=True,exist_ok=True)
  (backup/'metatiles.bin').write_bytes(old);(backup/'metatile_attributes.bin').write_bytes(attrs)
  tables[folder.name]=(old,attrs,new,newattrs);tile.write_bytes(new);attribute.write_bytes(newattrs)
  saved+=len(old)+len(attrs)-len(new)-len(newattrs)
  bank_receipts.append(dict(bank=folder.name,old_indices=indices,count=len(indices)))
 receipts=[]
 for p,keys,old in blobs:
  values=[]
  for v, in struct.iter_unpack('<H',old):
   bank=(v&1023)//512;index=v&511;key=keys[bank];mapped=maps[key][index]
   a,b,c,d=tables[key]
   assert a[index*24:index*24+24]==c[mapped*24:mapped*24+24]
   assert b[index*2:index*2+2]==d[mapped*2:mapped*2+2]
   nv=(v&~1023)|(bank*512+mapped);assert nv&~1023==v&~1023;values.append(nv)
  new=struct.pack('<'+'H'*len(values),*values);p.write_bytes(new)
  receipts.append(dict(file=str(p.relative_to(R)),before_sha256=hashlib.sha256(old).hexdigest(),after_sha256=hashlib.sha256(new).hexdigest()))
 (D/'metatile-packing.json').write_text(json.dumps(dict(bytes_saved=saved,visual_and_behavior_equivalence_verified=True,collision_and_elevation_preserved=True,banks=bank_receipts,files=receipts),indent=2)+'\n')
 print('Packed Galar metatiles; saved',saved,'bytes; visuals/behaviors verified for every map and border cell.')
if __name__=='__main__':main()
