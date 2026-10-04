#!/usr/bin/env python3
"""Canary geometry and ownership contracts; runtime checklist is a separate gate."""
import importlib.util,json,re,unittest
from pathlib import Path
P=Path(__file__).with_name('hoenn_canary1.py');S=importlib.util.spec_from_file_location('canary',P);C=importlib.util.module_from_spec(S);S.loader.exec_module(C)
class CanaryTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.ledger=C.load(C.OUT/'coordinate_remap_ledger.json');cls.receipt=C.load(C.OUT/'receipt.json')
 def test_canonical_identity_ownership_and_protected_files(self):C.validate()
 def test_ledger_exactly_covers_all_expansion_events(self):
  self.assertEqual(33,len(self.ledger['events']))
  for name in C.TARGETS:
   m=C.load(C.ROOT/f'data/maps/{name}/map.json')
   for k in ['object_events','warp_events','coord_events','bg_events']:
    entries=[e for e in self.ledger['events'] if e['map']==name and e['kind']==k]
    self.assertEqual(list(range(len(entries))),[e['index'] for e in entries]);self.assertEqual(m[k][:len(entries)],[e['after'] for e in entries])
    for e in entries:self.assertEqual({a:b for a,b in e['before'].items() if a not in ['x','y']},{a:b for a,b in e['after'].items() if a not in ['x','y']})
 def test_lossless_source_geometry_and_shared_mart_isolation(self):
  cat=C.load(C.ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');layouts=C.load(C.ROOT/'data/layouts/layouts.json')['layouts']
  for name,k in C.TARGETS.items():
   m=C.load(C.ROOT/f'data/maps/{name}/map.json');l=next(x for x in layouts if x['id']==m['layout']);d=next(x for x in cat['layouts'] if x['donor_id']==k)
   self.assertEqual(d['blockdata_path'],l['blockdata_filepath']);self.assertEqual(d['blockdata_sha256'],C.digest(C.ROOT/l['blockdata_filepath']));self.assertEqual(d['border_path'],l['border_filepath']);self.assertEqual(d['dimensions'],[l['width'],l['height']]);self.assertEqual(d['primary_tileset'],l['primary_tileset']);self.assertEqual(d['secondary_tileset'],l['secondary_tileset'])
  old=C.load(C.OUT/'original/data/layouts/layouts.json')['layouts'];self.assertEqual(next(l for l in old if l['id']=='LAYOUT_MART'),next(l for l in layouts if l['id']=='LAYOUT_MART'))
 def test_recompute_scripted_paths_trainers_patrols_and_seams(self):
  cat=C.load(C.ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');g={n:C.Grid(next(x for x in cat['layouts'] if x['donor_id']==k)) for n,k in C.TARGETS.items()};o={n:C.load(C.OUT/'original'/f'data/maps/{n}/map.json') for n in C.TARGETS}
  self.assertEqual(self.ledger['geometry_checks'],C.geometry_checks(g,o))
 def test_route102_early_game_reachability(self):
  # No Surf, no jumps, and static NPC cells are excluded: each retained event
  # must have an approach reachable from the canonical Oldale boundary.
  import collections
  cat=C.load(C.ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');g=C.Grid(next(x for x in cat['layouts'] if x['donor_id']=='0.17'));m=C.load(C.ROOT/'data/maps/Route102/map.json');blocked={(e['x'],e['y']) for e in m['object_events']};seen={(49,10)};q=collections.deque(seen)
  while q:
   x,y=q.popleft()
   for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
    if 0<=nx<g.w and 0<=ny<g.h and (nx,ny) not in seen and (nx,ny) not in blocked and g.walk(nx,ny):seen.add((nx,ny));q.append((nx,ny))
  self.assertIn((0,6),seen)
  for e in m['object_events'][:9]+m['bg_events']:self.assertTrue(any(xy in seen for xy in [(e['x']+1,e['y']),(e['x']-1,e['y']),(e['x'],e['y']+1),(e['x'],e['y']-1)]),e['script'])
 def test_native_graphics_contracts_and_actual_animation_frame_bounds(self):
  source=(C.ROOT/'src/data/object_events/object_event_anims.h').read_text()
  for x in self.ledger['graphics_adapters']:
   before=x['native_contract'];after=x['replacement']
   normalize=lambda s:re.sub(r'\.(paletteTag|images)\s*=\s*[^,]+,','',s)
   self.assertEqual(normalize(before),normalize(after));table=re.search(r'\.anims\s*=\s*(\w+)',before)[1]
   t=re.search(re.escape(table)+r'\[\]\s*=\s*\{(.*?)\};',source,re.S);self.assertIsNotNone(t,table)
   refs=set(re.findall(r'=\s*(sAnim_\w+)',t[1]));self.assertTrue(refs)
   for symbol in refs:
    animation=re.search(re.escape(symbol)+r'\[\]\s*=\s*\{(.*?)\};',source,re.S);self.assertIsNotNone(animation,symbol)
    for frame in re.findall(r'ANIMCMD_FRAME\(\s*(\d+)',animation[1]):self.assertLess(int(frame),x['source_frame_count'],(symbol,frame,x))
 def test_dynamic_init_and_native_berry_item_contracts(self):
  for n in C.TARGETS:self.assertEqual(C.hashlib.sha256(C.native_script_text(n).encode()).hexdigest(),C.load(C.OUT/'baseline.json')[f'data/maps/{n}/scripts.inc'])
  bindings=(C.ROOT/'src/hyper_asset_graphics_bindings.inc').read_text();self.assertNotIn('OBJ_EVENT_GFX_VAR_',bindings);self.assertNotIn('OBJ_EVENT_GFX_BERRY_TREE',bindings);self.assertNotIn('OBJ_EVENT_GFX_ITEM_BALL',bindings)
  self.assertIn('OBJ_EVENT_GFX_RIVAL_BRENDAN_NORMAL',bindings);self.assertIn('OBJ_EVENT_GFX_RIVAL_MAY_NORMAL',bindings)
  for x in self.ledger['graphics_adapters']:self.assertNotRegex(x['replacement'],r'FLAG_|VAR_|EventScript_')
 def test_extra_hyper_gameplay_events_quarantined(self):
  m=C.load(C.ROOT/'data/maps/Route102/map.json');self.assertEqual(9+len(C.third_gates('Route102')),len(m['object_events']));self.assertEqual(C.third_gates('Route102'),m['object_events'][9:]);self.assertEqual([],m['warp_events']);self.assertEqual([],m['coord_events']);self.assertFalse(self.receipt['hyper_gameplay_imported'])
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(CanaryTests));C.dump(C.OUT/'test_results.json',{'passed':r.wasSuccessful(),'tests':r.testsRun,'failures':len(r.failures),'errors':len(r.errors),'runtime_verified':False});raise SystemExit(0 if r.wasSuccessful() else 1)
