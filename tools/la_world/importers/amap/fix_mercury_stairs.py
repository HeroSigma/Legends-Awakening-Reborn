#!/usr/bin/env python3
"""Repair Mercury stair-2 translation without repainting user maps."""
import hashlib,json,re,struct
from pathlib import Path
from hyper_assets.port_hyper_assets import enums
R=Path(__file__).resolve().parents[4]
def main():
 n=enums(R/'include/constants/metatile_behaviors.h'); h=R/'src/data/tilesets/mercury_johto_headers.h'; d=R/'src/data/tilesets/mercury_johto_metatiles.h'; headers=h.read_text();defs=d.read_text();ledger=[]
 for bank in (R/'data/mercury_johto_assets/tilesets').iterdir():
  raw=bank/'source_frlg_metatile_attributes.bin'; ap=bank/'metatile_attributes.bin'
  if not raw.exists():continue
  original=raw.read_bytes();attrs=bytearray(ap.read_bytes());changed=False
  for i in range(len(attrs)//2):
   src=struct.unpack_from('<I',original,i*4)[0]&511
   if src not in (0xb2,0xb5):continue
   value=struct.unpack_from('<H',attrs,i*2)[0]
   # Only undo our incorrect TOP classification, preserving manual overrides.
   wrong=n['MB_SIDEWAYS_STAIRS_LEFT_SIDE_TOP' if src==0xb2 else 'MB_SIDEWAYS_STAIRS_RIGHT_SIDE_TOP']
   if value&0xfff != wrong:continue
   after=(value&0xf000)|n['MB_NORMAL'];struct.pack_into('<H',attrs,i*2,after);changed=True
   ledger.append(dict(bank=bank.name,index=i,source_behavior=src,before=value,after=after,reason='Donor variant 2 is not native diagonal-stair top; normal movement retains cell collision/elevation.'))
  if not changed:continue
  ap.write_bytes(attrs);sym='gMercury_Attributes_'+hashlib.sha256(attrs).hexdigest()[:20];out=R/'data/mercury_johto_assets/shared'/(sym+'.bin');out.write_bytes(attrs)
  if f'const u16 {sym}[]' not in defs:defs+=f'\nconst u16 {sym}[] = INCBIN_U16("{out.relative_to(R).as_posix()}");\n'
  pattern=r'(const struct Tileset gTileset_Mercury_'+re.escape(bank.name)+r' = \{.*?\.metatileAttributes=)\w+'
  headers,count=re.subn(pattern,lambda m:m[1]+sym,headers);assert count==1,bank.name
 h.write_text(headers);d.write_text(defs)
 report=R/'docs/la_world/mercury_johto/stair_variant_fix.json'
 if ledger:report.write_text(json.dumps(dict(changes=ledger,runtime_verified=False),indent=2)+'\n')
 print('Corrected',len(ledger),'stair definitions; no map cells changed')
if __name__=='__main__':main()
