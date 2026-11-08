from pathlib import Path
import json,struct,shutil,hashlib,collections
P=Path(__file__).resolve().parents[2];B=P/'.la_work/triple_layer/original';D=P/'docs/la_world/triple_layer';D.mkdir(parents=True,exist_ok=True)
inv=json.loads((P/'.la_work/triple-layer-inventory.json').read_text());entries=[];types=collections.Counter()
# Back up all engine/config files before changes.
for rel in ['include/fieldmap.h','src/field_camera.c','src/shop.c','src/decoration.c','porymap.project.cfg']:
 dst=B/rel;dst.parent.mkdir(parents=True,exist_ok=True)
 if not dst.exists():shutil.copy2(P/rel,dst)
protected={}
for root in ['data/maps','data/layouts','data/tilesets','data/bwa_assets','data/gs_johto_assets','data/kanto_ar_assets','data/hyper_assets']:
 for f in (P/root).rglob('*'):
  if f.is_file() and (f.name in ['map.bin','border.bin','map.json','layouts.json','metatile_attributes.bin'] or f.suffix in ['.pal','.gbapal','.4bpp'] or 'attributes.bin' in f.name):protected[f.relative_to(P).as_posix()]=hashlib.sha256(f.read_bytes()).hexdigest()
(D/'protected_files.json').write_text(json.dumps(protected,indent=2)+'\n')
for rel,attrrel in inv['pairs'].items():
 f=P/rel;old=f.read_bytes();n=len(old)//16;attribute=(P/attrrel).read_bytes();width=len(attribute)//n;assert width in (2,4) and len(attribute)==n*width
 backup=B/rel;backup.parent.mkdir(parents=True,exist_ok=True)
 if backup.exists():
  original=backup.read_bytes();assert old==original,'Already converted; refusing a second conversion.'
 else:backup.write_bytes(old)
 rows=struct.unpack('<'+str(n*8)+'H',old);attrs=struct.unpack('<'+str(n)+('H' if width==2 else 'I'),attribute);output=[]
 for i,a in enumerate(attrs):
  kind=((a>>12)&15) if width==2 else ((a>>29)&3);types[kind]+=1;lo=list(rows[i*8:i*8+4]);hi=list(rows[i*8+4:i*8+8])
  if kind==0:layers=[0x3014]*4+lo+hi
  elif kind==1:layers=lo+hi+[0]*4
  elif kind==2:layers=lo+[0]*4+hi
  else:layers=lo+hi+[0]*4 # Undefined donor attributes retain all original tile references.
  output+=layers
 new=struct.pack('<'+str(n*12)+'H',*output);f.write_bytes(new);entries.append({'metatiles':rel,'attributes':attrrel,'attribute_bytes':width,'count':n,'original_sha256':hashlib.sha256(old).hexdigest(),'triple_sha256':hashlib.sha256(new).hexdigest()})
manifest={'tilesets':len(entries),'metatiles':sum(v['count'] for v in entries),'layer_types':dict(types),'entries':entries,'attribute_data_preserved':True,'artwork_and_palettes_preserved':True};(D/'conversion.json').write_text(json.dumps(manifest,indent=2)+'\n');print('Converted',len(entries),'tileset files;',manifest['metatiles'],'metatiles. Original graphics, palettes, attributes and maps unchanged.')
