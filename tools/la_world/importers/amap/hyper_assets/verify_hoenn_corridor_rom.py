#!/usr/bin/env python3
"""Linked-ROM proof for all 54 canonical Hyper maps and 26 reservations."""
import importlib.util,struct,subprocess
from pathlib import Path
D=Path(__file__).parent
s=importlib.util.spec_from_file_location('third',D/'hoenn_canary4.py');third=importlib.util.module_from_spec(s);s.loader.exec_module(third)
s=importlib.util.spec_from_file_location('rom',D/'verify_hoenn_canary1_rom.py');rom=importlib.util.module_from_spec(s);s.loader.exec_module(rom)
rom.C.TARGETS={**third.P.C.TARGETS,**third.P.C.RETAINED,**third.P.TARGETS,**third.TARGETS};rom.C.TARGETS.update(Route105='0.20',Route107='0.22',Route108='0.23');OUT=third.ROOT/'.la_work/amap/hyper_hoenn_corridor_correction';rom.C.OUT=OUT

def verify():
 result=rom.verify();root=third.ROOT;raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(root/'pokeemerald.elf')],text=True);symbols={s[2]:int(s[0],16) for line in raw.splitlines() if len(s:=line.split())==3};data=(root/'pokeemerald.gba').read_bytes();groups=third.load(root/'data/maps/map_groups.json');ids={}
 for gi,g in enumerate(groups['group_order']):
  for mi,n in enumerate(groups[g]):
   m=third.load(root/f'data/maps/{n}/map.json');ids[m['id']]=(gi,mi)
 def u32(a):return struct.unpack_from('<I',data,a-0x08000000)[0]
 obj_count=warp_count=gate_count=0
 gates=third.load(third.P.OUT/'coordinate_remap_ledger.json')['construction_gates']+third.load(third.OUT/'coordinate_remap_ledger.json')['construction_gates']+third.load(OUT/'coordinate_remap_ledger.json')['construction_gates'];gate_labels={g['scientist']['script'] for g in gates}
 for r in result['maps']:
  n=r['canonical_name'];m=third.load(root/f'data/maps/{n}/map.json');ep=u32(symbols[n]+4);op=u32(ep+4);wp=u32(ep+8)
  for i,e in enumerate(m.get('object_events',[])):
   at=op+i*24-0x08000000;x,y=struct.unpack_from('<hh',data,at+4);assert (x,y)==(e['x'],e['y']);assert data[at+8]==e['elevation'];ptr=struct.unpack_from('<I',data,at+16)[0];script=e['script'];expected=int(script,16) if script.startswith('0x') else symbols[script];assert ptr==expected,(n,i,script);obj_count+=1
   if script in gate_labels:gate_count+=1;assert struct.unpack_from('<HH',data,at+12)==(0,0);assert struct.unpack_from('<H',data,at+20)[0]==0;assert data[at+10]==0
  for i,e in enumerate(m.get('warp_events',[])):
   at=wp+i*8-0x08000000;x,y=struct.unpack_from('<hh',data,at);assert (x,y)==(e['x'],e['y']);assert data[at+4]==e['elevation'];assert data[at+5]==int(e['dest_warp_id']);assert (data[at+7],data[at+6])==ids[e['dest_map']];warp_count+=1
  r['exact_donor_blockdata']=n not in {'Route101','RustboroCity','RusturfTunnel','Route105','Route107','Route108',*[x['map'] for x in third.load(third.OUT/'coordinate_remap_ledger.json')['geometry_compatibility_patches']]};r['native_object_script_pointers_and_warp_semantics_verified']=True
 assert gate_count==26
 cat=third.load(root/'.la_work/amap/hyper_asset_integration/asset_catalog.json');ts={x['symbol']:x for x in cat['tilesets']};ts['gTileset_Hyper_Primary_Route105']=ts['gTileset_Hyper_Primary_083DF704'];layouts=third.load(root/'data/layouts/layouts.json')['layouts'];palette_pairs=0
 for r in result['maps']:
  m=third.load(root/f'data/maps/{r["canonical_name"]}/map.json');l=next(x for x in layouts if x['id']==m['layout']);lp=symbols[l['name']]
  for offset,role in [(16,'primary_tileset'),(20,'secondary_tileset')]:
   ptr=u32(lp+offset);pal=u32(ptr+8);p=root/ts[l[role]]['path']/'palettes';expected=b''.join((p/f'{i:02}.gbapal').read_bytes() for i in range(13));assert data[pal-0x08000000:pal-0x08000000+len(expected)]==expected;(palette_pairs:=palette_pairs+1)
  r['palette_bytes_verified']=True
 assert len(result['maps'])==54
 result['tileset_palette_pairs_verified']=palette_pairs
 result.update(linked_object_events_verified=obj_count,linked_warps_verified=warp_count,construction_scientists_verified=gate_count,reviewed_geometry_compatibility_patch_count=len(third.load(third.OUT/'coordinate_remap_ledger.json')['geometry_compatibility_patches'])+len(third.load(OUT/'coordinate_remap_ledger.json')['geometry_patches'])+4);third.dump(OUT/'rom_validation.json',result);print('Verified',len(result['maps']),'canonical map headers,',obj_count,'objects,',warp_count,'warps and',gate_count,'construction scientists.');return result
if __name__=='__main__':verify()
