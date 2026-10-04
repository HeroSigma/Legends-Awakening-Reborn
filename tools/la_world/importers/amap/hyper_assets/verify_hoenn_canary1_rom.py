#!/usr/bin/env python3
"""Read the linked ROM, not just source declarations, for the three-map canary."""
import importlib.util,json,re,struct,subprocess
from pathlib import Path
P=Path(__file__).with_name('hoenn_canary1.py');S=importlib.util.spec_from_file_location('canary',P);C=importlib.util.module_from_spec(S);S.loader.exec_module(C)
def verify():
 raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(C.ROOT/'pokeemerald.elf')],text=True);symbols={s[2]:int(s[0],16) for line in raw.splitlines() if len(s:=line.split())==3};rom=(C.ROOT/'pokeemerald.gba').read_bytes()
 def u32(a):return struct.unpack_from('<I',rom,a-0x08000000)[0]
 def blob(a,n):assert 0x08000000<=a<a+n<=0x08000000+len(rom);return rom[a-0x08000000:a-0x08000000+n]
 groups=C.load(C.ROOT/'data/maps/map_groups.json');layouts=C.load(C.ROOT/'data/layouts/layouts.json')['layouts'];cat=C.load(C.ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');ts={x['symbol']:x for x in cat['tilesets']};results=[]
 for name,k in C.TARGETS.items():
  m=C.load(C.ROOT/f'data/maps/{name}/map.json');layout=next(x for x in layouts if x['id']==m['layout']);group=next(g for g in groups['group_order'] if name in groups[g]);gi=groups['group_order'].index(group);mi=groups[group].index(name);gp=u32(symbols['gMapGroups']+4*gi);assert gp==symbols[group];header=u32(gp+4*mi);assert header==symbols[name]
  lp=u32(header);assert lp==symbols[layout['name']];assert [u32(lp),u32(lp+4)]==[layout['width'],layout['height']]
  for offset,path in [(8,layout['border_filepath']),(12,layout['blockdata_filepath'])]:
   data=(C.ROOT/path).read_bytes();assert blob(u32(lp+offset),len(data))==data,path
  for offset,role in [(16,'primary_tileset'),(20,'secondary_tileset')]:
   ptr=u32(lp+offset);assert ptr==symbols[layout[role]];t=ts[layout[role]]
   assert u32(ptr+20)==(0 if t['callback']=='NULL' else symbols[t['callback']]|1),t['callback']
   for po,file in [(4,'tiles.4bpp.lz'),(12,'metatiles.bin'),(16,'metatile_attributes.bin')]:
    data=(C.ROOT/t['path']/file).read_bytes();assert blob(u32(ptr+po),len(data))==data,(name,file)
  assert u32(header+8)==symbols[name+'_MapScripts'];events=u32(header+4);assert list(blob(events,4))==[len(m[x]) for x in ['object_events','warp_events','coord_events','bg_events']]
  if m['connections']:
   assert u32(header+12)==symbols[name+'_MapConnections']
  else:assert u32(header+12)==0
  results.append({'canonical_name':name,'canonical_id':m['id'],'group':gi,'map':mi,'header_address':hex(header),'layout_address':hex(lp),'donor_id':k,'script_owner':name+'_MapScripts','source_geometry_border_graphics_metatiles_behaviors_verified_in_rom':True,'animation_callback_pointers_verified':True})
 result={'passed':True,'rom_path':str(C.ROOT/'pokeemerald.gba'),'rom_sha256':C.digest(C.ROOT/'pokeemerald.gba'),'rom_bytes':len(rom),'maps':results,'runtime_verified':False};C.dump(C.OUT/'rom_validation.json',result);print(json.dumps(result,indent=2));return result
if __name__=='__main__':verify()
