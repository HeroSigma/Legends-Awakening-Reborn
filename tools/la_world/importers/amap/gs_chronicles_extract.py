import sys,json,inspect,textwrap
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import frlg_bridge as F,legacy_emerald_bridge as L
O=Path('/home/allan/projects/Legends-Awakening-Reborn/.la_work/amap/gs_chronicles_goldenrod')
profile=json.loads((O/'audit.json').read_text())['profile']
s=F.FireRedScanner.__new__(F.FireRedScanner);L.RomScanner.__init__(s,Path('/mnt/c/Users/aadair/Downloads/gschronicles v2.7.6.gba'));s.layout_border_sizes={};s.profile_key='gs_chronicles_276';s.profile=profile
assert s.sha256==json.loads((O/'audit.json').read_text())['sha256']
class GSExtractor(F.FireRedNormalizedExtractor):
 SRC_PRIMARY_TILES=512
 SRC_SECONDARY_TILES=512
 SRC_PRIMARY_METATILES=512
 SRC_SECONDARY_METATILES=512
source=textwrap.dedent(inspect.getsource(F.FireRedNormalizedExtractor.extract_tileset_pair))
source=source.replace('p_tiles[512*32:640*32] + q_tiles[:384*32]','q_tiles[:512*32]').replace('p_defs[512*16:640*16] + q_defs[:384*16]','q_defs[:512*16]').replace('p_attrs_raw[512*4:640*4] + q_attrs_raw[:384*4]','q_attrs_raw[:512*4]')
namespace=dict(F.__dict__);exec(source,namespace);GSExtractor.extract_tileset_pair=namespace['extract_tileset_pair']

import hashlib,struct
starts=[L.gba_to_offset(L.u32(s.data,0x3526a8+4*i),s.size) for i in range(43)]
counts=[]
for i,off in enumerate(starts):
 if i+1<len(starts) and 0<starts[i+1]-off<=1200:count=(starts[i+1]-off)//4
 else:
  count=0
  for j in range(1024):
   at=off+j*4
   if j and at in starts:break
   h=L.gba_to_offset(L.u32(s.data,at),s.size)
   if h is None or not s.parse_header(h):break
   count+=1
 counts.append(count)
s.profile['group_counts']=counts
def all_names(max_section_id):
 names={}
 for i in range(168):
  off=L.gba_to_offset(L.u32(s.data,0x3f1cac+i*4),s.size)
  text=s.decode_gen3_text(off,64) if off is not None else None
  if text:names[88+i]=text
 s.region_map_names=names
 return names
s.discover_region_map_names=all_names
maps=s.discover()
O=O.parent/'gs_chronicles_full';O.mkdir(exist_ok=True)
manifest=GSExtractor(s,O).extract(maps)
for pp in (O/'maps').glob('*/map.json'):
 dd=json.loads(pp.read_text());dd['normalization']='gs_chronicles_native_512_512';pp.write_text(json.dumps(dd,indent=2))
ref=json.loads((Path(__file__).resolve().parent/'firered_map_reference.json').read_text())['maps']
rows=[]
for m in maps:
 l=s.parse_layout(m.layout_offset);digest=hashlib.sha256(s.data[l.blockdata_offset:l.blockdata_offset+m.width*m.height*2]).hexdigest();old=ref.get(m.id,{})
 rows.append({'id':m.id,'name':m.name,'width':m.width,'height':m.height,'map_type':m.map_type,'blockdata_sha256':digest,'stock_slot':old.get('name'),'stock_geometry_unchanged':digest==old.get('blockdata_sha256'),'map_section':m.region_map_section_id})
(O/'audit.json').write_text(json.dumps({'sha256':s.sha256,'profile':s.profile,'maps':rows,'invalid_slots':sum(counts)-len(maps)},indent=2))
print('EXTRACTED',len(maps),'invalid',sum(counts)-len(maps))
for row in rows:
 if row['map_type'] in [1,2,3,6]:print(row)
