#!/usr/bin/env python3
"""Validate compiled HnS canary, retired region slots and preserved source data."""
from pathlib import Path
import json,struct,re,hashlib,subprocess,tarfile
R=Path(__file__).resolve().parents[4];D=R/'docs/la_world/hns_canary'
def load(p):return json.loads(p.read_text())
def main():
 mf=load(D/'manifest.json');ret=load(D/'retirement.json');g=load(R/'data/maps/map_groups.json');ls=load(R/'data/layouts/layouts.json')['layouts'];layouts={l['id']:l for l in ls};rom=(R/'pokeemerald.gba').read_bytes();symbols={z[2]:int(z[0],16) for line in subprocess.check_output(['arm-none-eabi-nm','--defined-only',str(R/'pokeemerald.elf')],text=True).splitlines() if len(z:=line.split())==3}
 def data(ptr,n):
  assert 0x8000000<=ptr and ptr+n<=0x8000000+len(rom),(hex(ptr),n)
  return rom[ptr-0x8000000:ptr-0x8000000+n]
 def u(ptr):return struct.unpack('<I',data(ptr,4))[0]
 before_layouts=load(R/'.la_work/amap/hns_canary_backup/data/layouts/layouts.json')['layouts']
 for before in before_layouts:
  expected=dict(before)
  if before['id'] in ret['retired_layout_ids']:expected['layout_version']='retired_hns_reference'
  assert layouts[before['id']]==expected,before['id']
 old=load(R/'.la_work/amap/hns_canary_backup/data/maps/map_groups.json');assert all(g[n]==old[n] for n in old['group_order']);assert g['group_order'][:len(old['group_order'])]==old['group_order']
 for group in ret['retired_groups']:assert u(symbols['gMapGroups']+g['group_order'].index(group)*4)==0,group
 for lid in ret['retired_layout_ids']:
  i=next(i for i,l in enumerate(ls) if l['id']==lid);assert u(symbols['gMapLayouts']+i*4)==0,lid
 # All pre-canary map and artwork files remain exact, allowing only retirement metadata.
 protected=load(R/'.la_work/amap/hns_canary_backup/protected.json');archived_hashes=load(Path(ret['archive']).parent/'sha256.json');names=set(ret['retired_maps']);protected_count=0
 for rel,h in protected.items():
  if rel in ['data/layouts/layouts.json','data/maps/map_groups.json']:continue
  p=R/rel
  if rel.startswith('data/maps/') and p.name=='map.json' and p.parent.name in names:
   m=load(p);m.pop('la_retired_for_hns');m.pop('region');m.pop('la_imported');
   # Exact pre-retirement copy lives in the archive; validated below.
  else:assert hashlib.sha256(p.read_bytes()).hexdigest()==h,rel
  protected_count+=1
 # Verify the retirement archive and every retired map's sole metadata mutation.
 assert hashlib.sha256(Path(ret['archive']).read_bytes()).hexdigest()==ret['archive_sha256']
 with tarfile.open(ret['archive']) as archive:
  for member in archive:
   if not member.isfile():continue
   raw=archive.extractfile(member).read();assert hashlib.sha256(raw).hexdigest()==archived_hashes[member.name],member.name
   if member.name.startswith('data/maps/') and member.name.endswith('/map.json'):
    before=json.loads(raw);after=load(R/member.name)
    if before['name'] in names:
     expected=dict(before,region='REGION_JOHTO' if before['name'].startswith('Johto_') else 'REGION_KANTO',la_imported=False,la_retired_for_hns=True);assert after==expected,member.name
 group='gMapGroup_HnS_Canary';gi=g['group_order'].index(group);gp=u(symbols['gMapGroups']+gi*4);assert gp;warps=objects=connections=0
 for row in mf['maps']:
  name=row['name'];m=load(R/'data/maps'/name/'map.json');l=layouts[m['layout']];mi=g[group].index(name);hp=u(gp+mi*4);assert hp==symbols[name];lp=u(hp);assert lp==symbols[l['name']];assert (u(lp),u(lp+4))==(l['width'],l['height'])
  for off,key in [(8,'border_filepath'),(12,'blockdata_filepath')]:
   b=(R/l[key]).read_bytes();assert data(u(lp+off),len(b))==b,(name,key)
  for off,field in [(16,'primary_tileset'),(20,'secondary_tileset')]:
   key=l[field].replace('gTileset_HnSCanary_','');bank=mf['banks'][key];ptr=u(lp+off);assert ptr==symbols[l[field]]
   for o,path in [(4,'tiles.4bpp'),(12,'metatiles.bin'),(16,'metatile_attributes.bin')]:
    b=(R/bank['path']/path).read_bytes();assert data(u(ptr+o),len(b))==b,(key,path)
   pals=b''.join((R/bank['path']/'palettes'/f'{i:02}.gbapal').read_bytes() for i in range(16));assert data(u(ptr+8),len(pals))==pals
   cb=u(ptr+20);assert cb==0 or cb in [symbols['HnSCanary_InitTilesetAnim_JohtoGeneral']|1,symbols['HnSCanary_InitTilesetAnim_EcruteakTheater']|1],hex(cb)
  assert not m['coord_events'] and not m['bg_events']
  script=(R/'data/maps'/name/'scripts.inc').read_text();assert 'FLAG_' not in script and 'VAR_' not in script.replace('VAR_RESULT','');assert 'trainerbattle' not in script and 'callnative' not in script
  for w in m['warp_events']:assert w['dest_map'] in {x['id'] for x in mf['maps']}
  ev=u(hp+4);assert data(ev,4)==bytes([len(m['object_events']),len(m['warp_events']),0,0]);wp=u(ev+8)
  for i,w in enumerate(m['warp_events']):
   b=data(wp+i*8,8);dn=next(x['name'] for x in mf['maps'] if x['id']==w['dest_map']);assert struct.unpack_from('<hh',b)==(w['x'],w['y']);assert b[4:]==bytes([w['elevation'],int(w['dest_warp_id']),g[group].index(dn),gi])
  warps+=len(m['warp_events']);objects+=len(m['object_events']);connections+=len(m['connections'] or [])
 # Confirm no active source map points to a retired destination.
 retired_ids=set(ret['retired_ids'])
 for p in (R/'data/maps').glob('*/map.json'):
  if p.parent.name in names:continue
  m=load(p)
  for field,key in [('warp_events','dest_map'),('connections','map')]:
   assert not any(x[key] in retired_ids for x in m.get(field) or []),p
 result=dict(passed=True,rom_sha256=hashlib.sha256(rom).hexdigest(),rom_bytes=len(rom),maps=len(mf['maps']),banks=len(mf['banks']),objects=objects,warps=warps,connections=connections,retired_maps=len(names),numeric_slots_preserved=True,protected_files_checked=protected_count,archive_verified=True,donor_gameplay_imported=False)
 (D/'validation.json').write_text(json.dumps(result,indent=2)+chr(10));print('PASS',result)
if __name__=='__main__':main()
