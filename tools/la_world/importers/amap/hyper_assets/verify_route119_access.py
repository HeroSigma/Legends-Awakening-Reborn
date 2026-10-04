#!/usr/bin/env python3
"""Validate restored Route119 donor levels and expansion ownership."""
import copy,struct,subprocess
import hoenn_canary1 as C
ROOT=C.ROOT;OUT=ROOT/'.la_work/amap/hyper_hoenn_route119_access_fix'
def verify():
 receipt=C.load(OUT/'receipt.json');mp='data/maps/Route119/map.json';bp='data/hyper_assets/canary7_layouts/Route119/map.bin';m=C.load(ROOT/mp);expected=C.load(OUT/'original'/mp)
 for e in receipt['events']:
  assert expected[e['kind']][e['index']]==e['before'];before=copy.deepcopy(e['before']);before['elevation']=e['after']['elevation'];assert before==e['after'];expected[e['kind']][e['index']]=e['after']
 assert m==expected
 cat=C.load(ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');g=C.Grid(next(z for z in cat['layouts'] if z['donor_id']=='0.34'));bs=C.words(ROOT/bp);old=C.words(OUT/'original'/bp)
 for i,b in enumerate(bs):assert b>>12==g.blocks[i]>>12 and b&4095==old[i]&4095
 for f,z in receipt['changed_files'].items():assert C.digest(ROOT/f)==z['after'] and C.digest(OUT/'original'/f)==z['before']
 geometry=C.load(OUT/'geometry_validation.json');assert geometry['passed'];assert (m['warp_events'][0]['x'],m['warp_events'][0]['y'],m['warp_events'][0]['dest_map'],m['warp_events'][0]['dest_warp_id'])==(7,32,'MAP_ROUTE119_WEATHER_INSTITUTE_1F','0')
 raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(ROOT/'pokeemerald-canary7.elf')],text=True);ss={z[2]:int(z[0],16) for line in raw.splitlines() if len(z:=line.split())==3};rom=(ROOT/'pokeemerald-canary7.gba').read_bytes();a=struct.unpack_from('<I',rom,ss['Route119_Layout']-0x8000000+12)[0];assert rom[a-0x8000000:a-0x8000000+len(bs)*2]==(ROOT/bp).read_bytes()
 result={'passed':True,'restored_layout_elevations':len(receipt['cells']),'object_elevation_remaps':len(receipt['events']),'all_5600_cells_match_donor_elevation':True,'art_collision_behaviors_unchanged':True,'native_gameplay_fields_and_scripts_preserved':True,'linked_blockdata_matches':True,'institute_approach_path_cells':len(geometry['land_approach_path']),'rom_sha256':C.digest(ROOT/'pokeemerald-canary7.gba'),'runtime_verified':False};C.dump(OUT/'validation.json',result);print(result)
if __name__=='__main__':verify()
