#!/usr/bin/env python3
"""Inspect all seven activated canonical maps in the linked opening-spine ROM."""
import importlib.util
from pathlib import Path
D=Path(__file__).parent
s=importlib.util.spec_from_file_location('second',D/'hoenn_canary2.py');second=importlib.util.module_from_spec(s);s.loader.exec_module(second)
s=importlib.util.spec_from_file_location('rom',D/'verify_hoenn_canary1_rom.py');rom=importlib.util.module_from_spec(s);s.loader.exec_module(rom)
rom.C.TARGETS={**second.TARGETS,**second.RETAINED};rom.C.OUT=second.OUT
if __name__=='__main__':
 result=rom.verify()
 for m in result['maps']:m['exact_donor_blockdata']=m['canonical_name']!='Route101'
 result['reviewed_geometry_compatibility_patches']=[second.PATCH];second.dump(second.OUT/'rom_validation.json',result)
