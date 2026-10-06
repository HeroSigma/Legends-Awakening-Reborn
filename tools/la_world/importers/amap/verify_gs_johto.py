import json,struct,subprocess,hashlib,re
from pathlib import Path
R=Path(__file__).resolve().parents[4]
O=R/'docs/la_world/gs_johto'
symbols={z[2]:int(z[0],16) for line in subprocess.check_output(['arm-none-eabi-nm','--defined-only',str(R/'pokeemerald-sinnoh-assets.elf')],text=True).splitlines() if len(z:=line.split())==3}
rom=(R/'pokeemerald-sinnoh-assets.gba').read_bytes()
def blob(a,n):
 assert 0x8000000<=a<=a+n<=0x8000000+len(rom)
 return rom[a-0x8000000:a-0x8000000+n]
def u(a):return struct.unpack('<I',blob(a,4))[0]
ls={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']}
g=json.loads((R/'data/maps/map_groups.json').read_text());headers=(R/'src/data/tilesets/gs_johto_headers.h').read_text();checked=[];allmaps={p.parent.name:json.loads(p.read_text()) for p in (R/'data/maps').glob('GSJohto_*/map.json')};numeric={m['id']:(g['group_order'].index(k),g[k].index(n)) for n,m in allmaps.items() for k in g['group_order'] if n in g[k]}
for item in json.loads((O/'manifest.json').read_text()):
 n=item['map'];m=json.loads((R/f'data/maps/{n}/map.json').read_text());l=ls[m['layout']]
 gi,mi=next((i,g[k].index(n)) for i,k in enumerate(g['group_order']) if n in g[k]);hp=u(u(symbols['gMapGroups']+4*gi)+4*mi);assert hp==symbols[n];lp=u(hp);assert lp==symbols[l['name']];assert (u(lp),u(lp+4))==(l['width'],l['height'])
 for off,key in [(8,'border_filepath'),(12,'blockdata_filepath')]:
  b=(R/l[key]).read_bytes();assert blob(u(lp+off),len(b))==b
 for off,key in [(16,'primary_tileset'),(20,'secondary_tileset')]:
  ts=u(lp+off);assert ts==symbols[l[key]];assert u(ts+20)==0
  body=re.search(re.escape(l[key])+r'\s*=\s*\{(.*?)\};',headers,re.S)[1]
  for po,field in [(4,'tiles'),(8,'palettes'),(12,'metatiles'),(16,'metatileAttributes')]:assert u(ts+po)==symbols[re.search(r'\.'+field+r'\s*=\s*(\w+)',body)[1]]
 assert u(hp+8)==symbols[n+'_MapScripts'];assert blob(u(hp+8),1)==b'\0';assert blob(u(hp+4),4)==bytes([len(m['object_events']),len(m['warp_events']),0,0])
 for j,e in enumerate(m['object_events']):
  ob=blob(u(u(hp+4)+4)+j*24,24);assert struct.unpack_from('<hh',ob,4)==(e['x'],e['y']);assert struct.unpack_from('<I',ob,16)[0]==symbols[e['script']]
 for j,e in enumerate(m['warp_events']):
  ob=blob(u(u(hp+4)+8)+j*8,8);assert struct.unpack_from('<hh',ob)==(e['x'],e['y']);assert ob[5]==int(e['dest_warp_id']);assert (ob[7],ob[6])==numeric[e['dest_map']];dest=next(z for z in allmaps.values() if z['id']==e['dest_map']);assert int(e['dest_warp_id'])<len(dest['warp_events'])
 assert not any(m[k] for k in ['coord_events','bg_events']);checked.append({'map':n,'group':gi,'number':mi})
v={};v.update(build_passed=True,linked_maps=checked,rom_sha256=hashlib.sha256(rom).hexdigest(),runtime_verified=False,donor_gameplay_imported=False,animation_callbacks_pending=True)
(O/'validation.json').write_text(json.dumps(v,indent=2)+'\n');print('PASS:',len(checked),'linked Johto maps, geometry, tileset pointers, project scripts and events')
