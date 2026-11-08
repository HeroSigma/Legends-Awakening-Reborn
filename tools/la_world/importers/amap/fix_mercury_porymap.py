#!/usr/bin/env python3
"""Expose Mercury declarations and standard PNG paths to Porymap's parser."""
import hashlib,json,re,shutil
from pathlib import Path
R=Path(__file__).resolve().parents[4];D=R/'docs/la_world/mercury_johto';B=R/'.la_work/amap/mercury_porymap_backup'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 protected={str(p.relative_to(R)):sha(p) for root in ['data/maps','data/layouts','data/mercury_johto_assets/layouts'] for p in (R/root).rglob('*') if p.is_file()}
 hroot=R/'src/data/tilesets';graphics=hroot/'mercury_johto_graphics.h';text=graphics.read_text();paths=re.findall(r'INCBIN_U32\("([^"\n]+\.4bpp\.lz)"\)',text)
 for rel in paths:
  source=R/rel
  if source.name=='tiles.4bpp.lz':
   assert source.parent.joinpath('tiles.png').is_file();continue
  stem=source.name.removesuffix('.4bpp.lz');png=source.parent/(stem+'.png');assert source.is_file() and png.is_file();folder=source.parent/stem;folder.mkdir(exist_ok=True);shutil.copy2(source,folder/'tiles.4bpp.lz');shutil.copy2(png,folder/'tiles.png');text=text.replace(rel,(folder/'tiles.4bpp.lz').relative_to(R).as_posix())
 B.mkdir(parents=True,exist_ok=True)
 for kind in ['graphics','headers','metatiles']:
  root=hroot/(kind+'.h');helper=hroot/('mercury_johto_'+kind+'.h');before=root.read_text();needle='#include "mercury_johto_'+kind+'.h"'
  if not (B/root.name).exists():shutil.copy2(root,B/root.name)
  if not (B/helper.name).exists():shutil.copy2(helper,B/helper.name)
  if kind=='graphics':helper.write_text(text)
  start='// BEGIN MERCURY_JOHTO_'+kind.upper();end='// END MERCURY_JOHTO_'+kind.upper();block=start+'\n'+helper.read_text()+end
  if needle in before:assert before.count(needle)==1;after=before.replace(needle,block)
  else:
   after,count=re.subn(re.escape(start)+r'.*?'+re.escape(end),lambda m:block,before,flags=re.S);assert count==1,(kind,'missing managed declaration markers')
  if after!=before:root.write_text(after)
 for rel,h in protected.items():assert sha(R/rel)==h,rel
 headers=(hroot/'headers.h').read_text();graphics=(hroot/'graphics.h').read_text();metas=(hroot/'metatiles.h').read_text();decl=dict(re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',headers,re.S));plan=json.loads((D/'replacement_plan.json').read_text());layouts={l['id']:l for l in json.loads((R/'data/layouts/layouts.json').read_text())['layouts']};checked=set()
 for name in plan['names'].values():
  m=json.loads((R/'data/maps'/name/'map.json').read_text());l=layouts[m['layout']]
  for key in ['primary_tileset','secondary_tileset']:
   label=l[key];assert label in decl,label;body=decl[label]
   for field in ['tiles','metatiles','metatileAttributes']:
    symbol=re.search(r'\.'+field+r'\s*=\s*(\w+)',body)[1];source=graphics if field=='tiles' else metas;path=re.search(re.escape(symbol)+r'\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"\n]+)"\)',source)[1];assert (R/path).is_file()
    if field=='tiles':assert (R/path).parent.joinpath('tiles.png').is_file()
   symbol=re.search(r'\.palettes\s*=\s*(\w+)',body)[1];palbody=re.search(re.escape(symbol)+r'\[\]\[16\]\s*=\s*\{(.*?)\};',graphics,re.S)[1];pals=re.findall(r'INCBIN_U16\("([^"\n]+)"\)',palbody);assert len(pals)>=13
   for pal in pals:assert (R/pal).is_file() and (R/pal).with_suffix('.pal').is_file()
   checked.add(label)
 result=dict(editor_visible_tilesets=len(checked),maps=len(plan['names']),standard_headers_graphics_metatiles=True,standard_tiles_png_paths=True,map_geometry_and_events_unchanged=True,gui_reload_required=True)
 (D/'porymap_validation.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS',result)
if __name__=='__main__':main()
