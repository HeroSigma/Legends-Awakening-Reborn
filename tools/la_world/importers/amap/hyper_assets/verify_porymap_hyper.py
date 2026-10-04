#!/usr/bin/env python3
"""Check editor-visible Hyper declarations and source paths without editing maps."""
import hashlib,json,re
import hoenn_canary1 as chain
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
def verify():
 out=ROOT/'.la_work/amap/porymap_hyper_compat';receipt=json.loads((out/'receipt.json').read_text());catalog=json.loads((ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json').read_text());headers=(ROOT/'src/data/tilesets/headers.h').read_text();graphics=(ROOT/'src/data/tilesets/graphics.h').read_text();metatiles=(ROOT/'src/data/tilesets/metatiles.h').read_text()
 northwest_path=ROOT/'.la_work/amap/hyper_hoenn_canary5/receipt.json';northwest=json.loads(northwest_path.read_text()) if northwest_path.exists() else None
 closure_path=ROOT/'.la_work/amap/hyper_hoenn_canary6/receipt.json';closure=json.loads(closure_path.read_text()) if closure_path.exists() else None
 fortree_path=ROOT/'.la_work/amap/hyper_hoenn_canary7/receipt.json';fortree=json.loads(fortree_path.read_text()) if fortree_path.exists() else None
 lily_path=ROOT/'.la_work/amap/hyper_hoenn_canary8/receipt.json';lily=json.loads(lily_path.read_text()) if lily_path.exists() else None
 finale_path=ROOT/'.la_work/amap/hyper_hoenn_canary9/receipt.json';finale=json.loads(finale_path.read_text()) if finale_path.exists() else None
 for f,h in receipt['changes'].items():
  expected=chain.corridor_hash(f,h['after'])
  if northwest and f in northwest['changed_baseline_files']:
   change=northwest['changed_baseline_files'][f];assert change['before']==expected,(f,'receipt chain');expected=change['after']
  if closure and f in closure['changed_baseline_files']:
   change=closure['changed_baseline_files'][f];assert change['before']==expected,(f,'closure receipt chain');expected=change['after']
  if fortree and f in fortree['changed_baseline_files']:
   change=fortree['changed_baseline_files'][f];assert change['before']==expected,(f,'fortree receipt chain');expected=change['after']
  if lily and f in lily['changed_baseline_files']:
   change=lily['changed_baseline_files'][f];assert change['before']==expected,(f,'Lilycove receipt chain');expected=change['after']
  if finale and f in finale['changed_baseline_files']:
   change=finale['changed_baseline_files'][f];assert change['before']==expected,(f,'finale receipt chain');expected=change['after']
  assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==expected,f
 declarations=dict(re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',headers,re.S));checked=[]
 tiles=list(catalog['tilesets'])
 if chain.corridor_receipt():tiles.append({'symbol':'gTileset_Hyper_Primary_Route105'})
 if northwest:tiles.extend({'symbol':s} for s in northwest['attribute_derivatives'])
 if closure:tiles.extend({'symbol':s} for s in closure['attribute_derivatives'])
 if fortree:tiles.extend({'symbol':s} for s in fortree['attribute_derivatives'])
 if lily:tiles.extend({'symbol':s} for s in lily['attribute_derivatives'])
 if finale:tiles.extend({'symbol':s} for s in finale['attribute_derivatives'])
 for tile in tiles:
  symbol=tile['symbol'];assert symbol in declarations,symbol;body=declarations[symbol]
  for field in ['tiles','palettes','metatiles','metatileAttributes']:assert re.search(r'\.'+field+r'\s*=\s*\w+',body),(symbol,field)
  for name,field in [('tiles','tiles'),('metatiles','metatiles'),('attributes','metatileAttributes')]:
   asset=re.search(r'\.'+field+r'\s*=\s*(\w+)',body)[1];text=graphics if field=='tiles' else metatiles;match=re.search(re.escape(asset)+r'\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"]+)"\)',text);assert match,(symbol,asset);path=ROOT/match[1];assert path.is_file(),path
   if field=='tiles':assert (path.parent/'tiles.png').is_file()
  asset=re.search(r'\.palettes\s*=\s*(\w+)',body)[1];palettebody=re.search(re.escape(asset)+r'\[\]\[16\]\s*=\s*\{(.*?)\};',graphics,re.S)[1];paths=re.findall(r'INCBIN_U16\("([^"]+)"\)',palettebody);assert len(paths)==13
  for path in paths:assert (ROOT/path).is_file() and (ROOT/path).with_suffix('.pal').is_file()
  checked.append(symbol)
 layouts={l['id']:l for l in json.loads((ROOT/'data/layouts/layouts.json').read_text())['layouts']};maps=[]
 for p in (ROOT/'data/maps').glob('*/map.json'):
  m=json.loads(p.read_text());l=layouts[m['layout']]
  if not l['primary_tileset'].startswith('gTileset_Hyper_'):continue
  assert l['primary_tileset'] in declarations and l['secondary_tileset'] in declarations
  assert (ROOT/l['blockdata_filepath']).stat().st_size==l['width']*l['height']*2
  assert (ROOT/l['border_filepath']).is_file();maps.append(p.parent.name)
 assert len(maps)==51+(3 if chain.corridor_receipt() else 0)+(len(northwest['canonical_maps_replaced'])+len(northwest['registered_special_maps']) if northwest else 0)+(len(closure['canonical_maps_replaced'])+len(closure['registered_special_maps']) if closure else 0)+(len(fortree['canonical_maps_replaced'])+len(fortree['registered_special_maps']) if fortree else 0)+(len(lily['canonical_maps_replaced'])+len(lily['registered_special_maps']) if lily else 0)+(len(finale['canonical_maps_replaced'])+len(finale['registered_special_maps']) if finale else 0),len(maps)
 result={'passed':True,'editor_visible_hyper_tilesets':len(checked),'canonical_hyper_maps_with_valid_editor_references':len(maps),'maps':sorted(maps),'scope':'Declaration/path validation against installed Porymap source reading standard headers/graphics/metatiles files; editor reload still required.','map_geometry_events_asset_bytes_modified':False};(out/'editor_validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='maps'},indent=2));return result
if __name__=='__main__':verify()
