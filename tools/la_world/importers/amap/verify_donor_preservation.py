#!/usr/bin/env python3
"""Audit staged assets without linking or activating donor maps."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
def main():
 for donor,total in [('bwa',444),('swsh',701)]:
  out=ROOT/'.la_work/amap/donor_preservation'/donor
  m=json.loads((out/'preservation_manifest.json').read_text())
  for file,h in m['files'].items():
   p=out/file
   assert p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==h,file
  editor=out/'editor';maps=list((editor/'data/maps').glob('*/map.json'));assert len(maps)==total
  layouts=json.loads((editor/'data/layouts/layouts.json').read_text())['layouts'];assert len(layouts)==total
  by_id={l['id']:l for l in layouts};assert len(by_id)==total
  for p in maps:
   item=json.loads(p.read_text());assert item['connections'] is None
   for field in ['object_events','warp_events','coord_events','bg_events']:assert item[field]==[]
   layout=by_id[item['layout']]
   assert (editor/layout['blockdata_filepath']).stat().st_size==layout['width']*layout['height']*2
   assert (editor/layout['border_filepath']).stat().st_size==layout['border_width']*layout['border_height']*2
  headers=(editor/'src/data/tilesets/headers.h').read_text()
  assert headers.count('.callback = NULL')==m['tilesets']
  for layout in layouts:
   for key in ['primary_tileset','secondary_tileset']:assert 'const struct Tileset '+layout[key]+' =' in headers
  assert not (editor/'Makefile').exists()
  assert m['new_live_maps']==0 and not m['gameplay_imported']
  print(f'PASS {donor}: {total} layouts, all file hashes, tileset declarations, borders and empty gameplay ownership')
 print('Porymap GUI rendering and runtime animation/behavior/art closure are NOT verified by this audit.')
if __name__=='__main__':main()
