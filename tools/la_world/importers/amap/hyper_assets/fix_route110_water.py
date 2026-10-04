#!/usr/bin/env python3
"""Restore Route110's inspected Hyper water level, preserving Cycling Road."""
import struct,subprocess
import hoenn_canary1 as C
ROOT=C.ROOT;OUT=ROOT/'.la_work/amap/hyper_hoenn_route110_water_fix';BP='data/hyper_assets/canary5_layouts/Route110/map.bin';WATER={0x10,0x11,0x12,0x13,0x14,0x15,0x19,0x22,0x2A}
def grid():return C.Grid(next(z for z in C.load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json')['layouts'] if z['donor_id']=='0.25'))
def apply():
 assert not (OUT/'receipt.json').exists(),'Already applied; use --verify.'
 OUT.mkdir(parents=True,exist_ok=True);g=grid();bs=C.words(ROOT/BP);before=C.digest(ROOT/BP);(OUT/'original_map.bin').write_bytes((ROOT/BP).read_bytes());changes=[]
 for i,b in enumerate(bs):
  v=g.cell(i%g.w,i//g.w)
  if v['translated_behavior'] not in WATER:continue
  assert b&4095==v['block']&4095 and v['elevation']==1
  after=(b&4095)|0x1000
  if b!=after:changes.append({'x':i%g.w,'y':i//g.w,'before':b,'after':after,'behavior':v['translated_behavior']});bs[i]=after
 assert len(changes)==160
 (ROOT/BP).write_bytes(struct.pack('<'+'H'*len(bs),*bs));C.dump(OUT/'receipt.json',{'schema':'hyper-route110-water-fix-v1','map':'Route110','donor_id':'0.25','changed_files':{BP:{'before':before,'after':C.digest(ROOT/BP)}},'cells':changes,'reason':'Old elevation reconciliation copied native land elevation3 onto 160 Hyper water cells. Restore donor water elevation1 without touching bridge levels/art/collision/events.','runtime_verified':False});print('Restored 160 Route110 water cells.')
def verify():
 g=grid();r=C.load(OUT/'receipt.json');bs=C.words(ROOT/BP);old=C.words(OUT/'original_map.bin');count=0;bridges=0;wildcards=[]
 for i,b in enumerate(bs):
  x,y=i%g.w,i//g.w;v=g.cell(x,y)
  if v['translated_behavior'] in WATER:
   assert b>>12==1 and b&4095==old[i]&4095;count+=1
   for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    if not(0<=xx<g.w and 0<=yy<g.h):continue
    a=g.cell(xx,yy);z=bs[yy*g.w+xx]
    if a['translated_behavior'] not in WATER and ((z>>10)&3)==0 and z>>12 in [0,15] and a['translated_behavior']!=0x70:wildcards.append([xx,yy])
  else:assert b==old[i]
  if v['translated_behavior']==0x70:assert b==old[i];bridges+=1
 assert not wildcards,wildcards
 for f,z in r['changed_files'].items():assert C.digest(ROOT/f)==z['after']
 raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(ROOT/'pokeemerald-canary7.elf')],text=True);ss={z[2]:int(z[0],16) for line in raw.splitlines() if len(z:=line.split())==3};rom=(ROOT/'pokeemerald-canary7.gba').read_bytes();a=struct.unpack_from('<I',rom,ss['Route110_Layout']-0x8000000+12)[0];assert rom[a-0x8000000:a-0x8000000+len(bs)*2]==(ROOT/BP).read_bytes()
 result={'passed':True,'map':'Route110','water_cells_corrected':160,'water_cells_checked':count,'bridge_cells_unchanged':bridges,'nonwater_cells_unchanged':len(bs)-count,'nonbridge_water_wildcard_bypasses':wildcards,'linked_blockdata_matches':True,'rom_sha256':C.digest(ROOT/'pokeemerald-canary7.gba'),'runtime_verified':False};C.dump(OUT/'validation.json',result);print(result)
if __name__=='__main__':
 import sys
 verify() if '--verify' in sys.argv else apply()
