#!/usr/bin/env python3
"""Linked-ROM proof for Rustboro batch plus the validated opening spine."""
import importlib.util,struct,subprocess
from pathlib import Path
D=Path(__file__).parent
s=importlib.util.spec_from_file_location('third',D/'hoenn_canary3.py');third=importlib.util.module_from_spec(s);s.loader.exec_module(third)
s=importlib.util.spec_from_file_location('rom',D/'verify_hoenn_canary1_rom.py');rom=importlib.util.module_from_spec(s);s.loader.exec_module(rom)
rom.C.TARGETS={**third.C.TARGETS,**third.C.RETAINED,**third.TARGETS};rom.C.OUT=third.OUT

def verify():
 result=rom.verify();root=third.ROOT;raw=subprocess.check_output(['arm-none-eabi-nm','-n','--defined-only',str(root/'pokeemerald.elf')],text=True);symbols={s[2]:int(s[0],16) for line in raw.splitlines() if len(s:=line.split())==3};data=(root/'pokeemerald.gba').read_bytes();groups=third.load(root/'data/maps/map_groups.json');ids={}
 for gi,g in enumerate(groups['group_order']):
  for mi,n in enumerate(groups[g]):
   m=third.load(root/f'data/maps/{n}/map.json');ids[m['id']]=(gi,mi)
 def u32(a):return struct.unpack_from('<I',data,a-0x08000000)[0]
 obj_count=warp_count=gate_count=0
 gates=third.load(third.OUT/'coordinate_remap_ledger.json')['construction_gates'];gate_labels={g['scientist']['script'] for g in gates}
 for r in result['maps']:
  n=r['canonical_name'];m=third.load(root/f'data/maps/{n}/map.json');ep=u32(symbols[n]+4);op=u32(ep+4);wp=u32(ep+8)
  for i,e in enumerate(m.get('object_events',[])):
   at=op+i*24-0x08000000;x,y=struct.unpack_from('<hh',data,at+4);assert (x,y)==(e['x'],e['y']);assert data[at+8]==e['elevation'];ptr=struct.unpack_from('<I',data,at+16)[0];script=e['script'];expected=int(script,16) if script.startswith('0x') else symbols[script];assert ptr==expected,(n,i,script);obj_count+=1
   if script in gate_labels:gate_count+=1;assert struct.unpack_from('<HH',data,at+12)==(0,0);assert struct.unpack_from('<H',data,at+20)[0]==0;assert data[at+10]==0
  for i,e in enumerate(m.get('warp_events',[])):
   at=wp+i*8-0x08000000;x,y=struct.unpack_from('<hh',data,at);assert (x,y)==(e['x'],e['y']);assert data[at+4]==e['elevation'];assert data[at+5]==int(e['dest_warp_id']);assert (data[at+7],data[at+6])==ids[e['dest_map']];warp_count+=1
  r['exact_donor_blockdata']=n not in ['Route101','RustboroCity','RusturfTunnel'];r['native_object_script_pointers_and_warp_semantics_verified']=True
 assert gate_count==15
 result.update(linked_object_events_verified=obj_count,linked_warps_verified=warp_count,construction_scientists_verified=gate_count,reviewed_geometry_compatibility_patches=[third.C.PATCH,third.PATCH,*third.TUNNEL_PATCHES]);third.dump(third.OUT/'rom_validation.json',result);print('Verified',len(result['maps']),'canonical map headers,',obj_count,'objects,',warp_count,'warps and',gate_count,'construction scientists.');return result
if __name__=='__main__':verify()
