#!/usr/bin/env python3
"""Extract exact-build Mercury assets; no destination gameplay activation."""
import argparse,hashlib,json,types,struct
from pathlib import Path
from zipfile import ZipFile
import frlg_bridge as F
R=Path(__file__).resolve().parents[4]
ROM=Path('/home/allan/mercury-map-inspection/mercury_beta2.gba')
def scanner():
 reference=Path('/home/allan/mercury-map-inspection');profile=json.loads((reference/'mercury_profile.json').read_text());F.PROFILES['mercury']=profile;s=F.FireRedScanner(ROM,'mercury')
 names=json.loads((reference/'location_names.json').read_text())
 def discover_names(self,maxid):
  self.region_map_names={int(k):v for k,v in names.items()};return self.region_map_names
 s.discover_region_map_names=types.MethodType(discover_names,s);s.discover();return s
def main():
 s=scanner();out=R/'.la_work/amap/mercury_full_v11';out.mkdir(parents=True,exist_ok=True);e=F.FireRedNormalizedExtractor(s,out)
 # The English patch damages five bytes inside this Goldenrod graphics LZ stream.
 # Recover graphical bytes from the other user-provided Mercury build only when
 # its tileset headers, metatile definitions, attributes and palette bytes match.
 zipfile=Path('/mnt/c/Users/aadair/Downloads/PokemonMercuryBeta22.zip')
 with ZipFile(zipfile) as z:alt=z.read('PokemonMercuryBeta22.gba')
 off=0x2d501c;assert s.data[off:off+24]==alt[off:off+24]
 for pointer,length in [(0x2983bc,13*32),(0x98423c,640*16),(0x986a3c,640*4)]:assert s.data[pointer:pointer+length]==alt[pointer:pointer+length]
 original=e.lz77_decompress;fix=[]
 def decompress(offset,require_type_byte=False):
  try:return original(offset,require_type_byte)
  except ValueError:
   if offset!=0xb2f9c0:raise
   old=s.data
   try:
    s.data=alt;data=original(offset,require_type_byte)
   finally:s.data=old
   fix.append(dict(pointer='0x08B2F9C0',reason='Invalid LZ back-reference in English patch',asset_source=str(zipfile),asset_rom_sha256=hashlib.sha256(alt).hexdigest(),decoded_sha256=hashlib.sha256(data).hexdigest(),matched='tileset header, palettes, metatile definitions and raw attributes'))
   return data
 e.lz77_decompress=decompress
 manifest=e.extract(s.maps)
 (out/'asset_recovery.json').write_text(json.dumps(fix,indent=2)+'\n')
 print('EXTRACTED',len(manifest['maps']),'maps',len(manifest['tilesets']),'tilesets; repairs',len(fix),'warnings',e.warnings,flush=True)
if __name__=='__main__':main()
