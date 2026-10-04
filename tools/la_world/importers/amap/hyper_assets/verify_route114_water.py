#!/usr/bin/env python3
"""Check Route114 water geometry, native ownership, and linked ROM correction."""
import struct,subprocess
import fix_route114_water as F
C=F.C;ROOT=F.ROOT;OUT=F.OUT
def verify():
 receipt=C.load(OUT/'receipt.json');m=C.load(ROOT/'data/maps/Route114/map.json');old=C.load(OUT/'original/data/maps/Route114/map.json');l=next(z for z in C.load(ROOT/'data/layouts/layouts.json')['layouts'] if z['id']==m['layout']);blocks=C.words(ROOT/l['blockdata_filepath']);previous=C.words(OUT/'original'/l['blockdata_filepath']);shore_path=ROOT/'.la_work/amap/hyper_hoenn_route114_shore_fix/receipt.json';shore=C.load(shore_path) if shore_path.exists() else None;shore_cells={(z['x'],z['y']):z for z in shore['cells']} if shore else {};cat=C.load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');g=C.Grid(next(z for z in cat['layouts'] if z['donor_id']=='0.29'));water=0
 for i,b in enumerate(blocks):
  v=g.cell(i%g.w,i//g.w)
  if v['translated_behavior'] in F.WATER:
   assert b>>12==v['elevation']==1 and b&4095==previous[i]&4095;water+=1
  elif (i%g.w,i//g.w) in shore_cells:assert b==shore_cells[i%g.w,i//g.w]['after'] and b&4095==previous[i]&4095
  else:assert b==previous[i]
 expected=C.load(OUT/'original/data/maps/Route114/map.json')
 for e in receipt['events']:
  assert expected[e['kind']][e['index']]==e['before'];expected[e['kind']][e['index']]=e['after']
 assert m==expected
 for f,v in receipt['changed_files'].items():
  expected=v['after']
  if shore and f in shore['changed_files']:assert shore['changed_files'][f]['before']==expected;expected=shore['changed_files'][f]['after']
  assert C.digest(ROOT/f)==expected and C.digest(OUT/'original'/f)==v['before']
 edges=0
 if shore:
  for i,b in enumerate(blocks):
   x,y=i%g.w,i//g.w
   if g.cell(x,y)['translated_behavior'] not in F.WATER:continue
   for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    if not(0<=xx<g.w and 0<=yy<g.h):continue
    land=blocks[yy*g.w+xx]
    if g.cell(xx,yy)['translated_behavior'] not in F.WATER and ((land>>10)&3)==0:assert land>>12 not in [0,1,15];edges+=1
 raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(ROOT/'pokeemerald-canary6.elf')],text=True);symbols={s[2]:int(s[0],16) for line in raw.splitlines() if len(s:=line.split())==3};rom=(ROOT/'pokeemerald-canary6.gba').read_bytes()
 def u32(a):return struct.unpack_from('<I',rom,a-0x08000000)[0]
 layout=symbols[l['name']];address=u32(layout+12);assert rom[address-0x08000000:address-0x08000000+len(blocks)*2]==(ROOT/l['blockdata_filepath']).read_bytes()
 result={'passed':True,'map':'Route114','water_cells_checked':water,'water_cells_corrected':119,'source_water_elevation':1,'shore_land_cells_corrected':len(shore_cells),'land_water_boundaries_checked':edges,'nonwater_cells_unchanged':len(blocks)-water-len(shore_cells),'native_gameplay_fields_preserved':True,'event_coordinate_changes':receipt['events'],'linked_blockdata_matches':True,'rom_sha256':C.digest(ROOT/'pokeemerald-canary6.gba'),'runtime_verified':False}
 C.dump(OUT/'validation.json',result);print('Route114 passed: '+str(water)+' water cells at source elevation1; linked blockdata and native ownership verified.')
if __name__=='__main__':verify()
