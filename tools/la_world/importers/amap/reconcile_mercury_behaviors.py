#!/usr/bin/env python3
"""Translate verified FRLG/CFRU visual terrain into native Reborn behaviors."""
import hashlib,json,re,struct
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
from replace_johto_mercury import R,S,D,load,dump
# CFRU's public header establishes the extended grass/stair identifiers.
# Other Mercury-specific extensions remain explicitly unverified.
# Donor UP_2 is not the native diagonal stair TOP edge. Retain straight travel.
OVERRIDES={0x69:'MB_NON_ANIMATED_DOOR',3:'MB_LONG_GRASS',0x11:'MB_INTERIOR_DEEP_WATER',0x1a:'MB_POND_WATER',0x1b:'MB_POND_WATER',0xb0:'MB_SIDEWAYS_STAIRS_LEFT_SIDE',0xb1:'MB_SIDEWAYS_STAIRS_LEFT_SIDE_BOTTOM',0xb2:'MB_NORMAL',0xb3:'MB_SIDEWAYS_STAIRS_RIGHT_SIDE',0xb4:'MB_SIDEWAYS_STAIRS_RIGHT_SIDE_BOTTOM',0xb5:'MB_NORMAL'}
def main():
 plan=load(D/'replacement_plan.json');source={m['id']:m for m in load(S/'manifest.json')['maps']};folders={load(p)['id']:p.parent for p in (S/'maps').glob('*/map.json')};used={};n=enums(R/'include/constants/metatile_behaviors.h');ledger=[]
 for k in plan['selected']:
  m=source[k];keys=[m[f] for f in ['primary_tileset','secondary_tileset']]
  for blob in [(folders[k]/'blockdata.bin').read_bytes(),(folders[k]/'border.bin').read_bytes()]:
   for v, in struct.iter_unpack('<H',blob):used.setdefault(keys[(v&1023)//512],set()).add(v&511)
 headers=R/'src/data/tilesets/mercury_johto_headers.h';text=headers.read_text();definitions=R/'src/data/tilesets/mercury_johto_metatiles.h';defs=definitions.read_text()
 for key,indices in used.items():
  bank=R/'data/mercury_johto_assets/tilesets'/key;attrs=bytearray((bank/'metatile_attributes.bin').read_bytes());raw=(bank/'source_frlg_metatile_attributes.bin').read_bytes();changed=False
  for i in indices:
   b=struct.unpack_from('<I',raw,i*4)[0]&511
   if b not in OVERRIDES:continue
   label=OVERRIDES[b];value=struct.unpack_from('<H',attrs,i*2)[0];after=(value&0xf000)|n[label]
   if value!=after:struct.pack_into('<H',attrs,i*2,after);ledger.append(dict(bank=key,index=i,source_behavior=b,native=label,before=value,after=after));changed=True
  if changed:
   (bank/'metatile_attributes.bin').write_bytes(attrs);digest=hashlib.sha256(attrs).hexdigest();sym='gMercury_Attributes_'+digest[:20];out=R/'data/mercury_johto_assets/shared'/(sym+'.bin');out.write_bytes(attrs)
   if f'const u16 {sym}[]' not in defs:defs+=f'\nconst u16 {sym}[] = INCBIN_U16("{out.relative_to(R).as_posix()}");\n'
   pattern=r'(const struct Tileset gTileset_Mercury_'+re.escape(key)+r' = \{.*?\.metatileAttributes=)\w+'
   text,count=re.subn(pattern,lambda m:m[1]+sym,text);assert count==1,key
 headers.write_text(text);definitions.write_text(defs)
 # Normalize native water elevation for the additional source water variants.
 cell=[];layouts={l['id']:l for l in load(R/'data/layouts/layouts.json')['layouts']}
 for k,name in plan['names'].items():
  m=load(R/'data/maps'/name/'map.json');l=layouts[m['layout']];blob=bytearray((R/l['blockdata_filepath']).read_bytes());source_m=source[k];aa=b''.join((S/'tilesets'/source_m[f]/'source_frlg_metatile_attributes.bin').read_bytes() for f in ['primary_tileset','secondary_tileset']);original=(folders[k]/'blockdata.bin').read_bytes()
  for i,(old,) in enumerate(struct.iter_unpack('<H',original)):
   b=struct.unpack_from('<I',aa,(old&1023)*4)[0]&511;v=struct.unpack_from('<H',blob,i*2)[0]
   if b in [0x11,0x1a,0x1b] and (v>>10&3)==0 and v>>12 not in [1,15]:
    after=(v&4095)|4096;struct.pack_into('<H',blob,i*2,after);cell.append(dict(map=name,x=i%l['width'],y=i//l['width'],before=v,after=after))
  (R/l['blockdata_filepath']).write_bytes(blob)
 if (D/'extended_behavior_reconciliation.json').exists():
  previous=load(D/'extended_behavior_reconciliation.json');ledger=previous['changes']+ledger;cell=previous['water_cells']+cell
 dump(D/'extended_behavior_reconciliation.json',dict(reference='https://github.com/Skeli789/Complete-Fire-Red-Upgrade/blob/master/include/constants/metatile_behaviors.h',changes=ledger,water_cells=cell,note='Mercury-specific unrecognized extensions remain in manual review; not treated as proven native behavior.'))
 print('Reconciled',len(ledger),'used behavior definitions;',len(cell),'water cells')
if __name__=='__main__':main()
