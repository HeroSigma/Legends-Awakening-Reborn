#!/usr/bin/env python3
"""Opening-spine ownership, asset and path regression checks."""
import importlib.util,re,unittest
from pathlib import Path
P=Path(__file__).with_name('hoenn_canary2.py');S=importlib.util.spec_from_file_location('spine',P);C=importlib.util.module_from_spec(S);S.loader.exec_module(C)
class OpeningSpineTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.ledger=C.load(C.OUT/'coordinate_remap_ledger.json');cls.cat=C.load(C.ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');cls.grids={n:C.Grid(next(x for x in cls.cat['layouts'] if x['donor_id']==k)) for n,k in {**C.TARGETS,**C.RETAINED}.items()};g=cls.grids['Route101'];g.blocks[C.PATCH['y']*g.w+C.PATCH['x']]=C.PATCH['after']
 def test_full_protected_baseline_and_native_ownership(self):C.validate()
 def test_all_events_are_in_ledger_with_only_xy_changes(self):
  self.assertEqual(94,len(self.ledger['events']))
  for n in C.TARGETS:
   m=C.load(C.ROOT/f'data/maps/{n}/map.json')
   for k in ['object_events','warp_events','coord_events','bg_events']:self.assertEqual(m[k][:len([e for e in self.ledger['events'] if e['map']==n and e['kind']==k])],[e['after'] for e in self.ledger['events'] if e['map']==n and e['kind']==k])
 def test_native_story_scenes_and_entire_spine_connections(self):
  scripts={f'data/maps/{n}/scripts.inc':(C.ROOT/f'data/maps/{n}/scripts.inc').read_text() for n in ['PetalburgCity','Route103']}
  self.assertEqual(self.ledger['native_scene_paths'],C.scene_checks(self.grids,scripts));self.assertEqual(self.ledger['connection_checks'],C.seam_checks(self.grids))
 def test_geometry_diff_is_exactly_one_reviewed_cell(self):
  actual=C.words(C.ROOT/C.PATCH_PATH);source=C.words(C.ROOT/'data/hyper_assets/layouts/0.16/map.bin');changes=[(i,a,z) for i,(a,z) in enumerate(zip(source,actual)) if a!=z]
  self.assertEqual([(18*20+7,0x140F,0x3001)],changes);self.assertEqual([C.PATCH],self.ledger['geometry_compatibility_patches'])
  ls=C.load(C.ROOT/'data/layouts/layouts.json')['layouts']
  for n,k in C.TARGETS.items():
   m=C.load(C.ROOT/f'data/maps/{n}/map.json');l=next(x for x in ls if x['id']==m['layout']);d=next(x for x in self.cat['layouts'] if x['donor_id']==k)
   self.assertEqual(d['border_path'],l['border_filepath']);self.assertEqual(d['primary_tileset'],l['primary_tileset']);self.assertEqual(d['secondary_tileset'],l['secondary_tileset'])
   self.assertEqual(C.PATCH_PATH if n=='Route101' else d['blockdata_path'],l['blockdata_filepath'])
 def test_graphics_adapters_preserve_native_abi_and_frame_bounds(self):
  s=(C.ROOT/'src/data/object_events/object_event_anims.h').read_text()
  for x in self.ledger['graphics_adapters']:
   strip=lambda t:re.sub(r'\.(paletteTag|images)\s*=\s*[^,]+,','',t)
   self.assertEqual(strip(x['native_contract']),strip(x['replacement']));table=re.search(r'\.anims\s*=\s*(\w+)',x['native_contract'])[1];body=re.search(re.escape(table)+r'\[\]\s*=\s*\{(.*?)\};',s,re.S)[1]
   for name in set(re.findall(r'=\s*(sAnim_\w+)',body)):
    commands=re.search(re.escape(name)+r'\[\]\s*=\s*\{(.*?)\};',s,re.S)[1]
    for frame in re.findall(r'ANIMCMD_FRAME\(\s*(\d+)',commands):self.assertLess(int(frame),x['source_frame_count'],(x['map'],name,frame))
 def test_project_hook_and_native_dynamic_initializers(self):
  m=C.load(C.ROOT/'data/maps/LittlerootTown/map.json');e=next(x for x in m['object_events'] if x.get('local_id')=='LOCALID_LITTLEROOT_TELEPORT_SCIENTIST');self.assertEqual('LA_TeleportScientist',e['script']);self.assertEqual((10,16),(e['x'],e['y']))
  b=C.load(C.OUT/'baseline.json')
  for f in ['data/scripts/rival_graphics.inc','data/maps/LittlerootTown/scripts.inc','data/maps/Route101/scripts.inc','data/maps/InsideOfTruck/scripts.inc','data/maps/PetalburgCity_Gym/scripts.inc','data/maps/LittlerootTown_ProfessorBirchsLab/scripts.inc']:self.assertEqual(b[f],C.digest(C.ROOT/f),f)
  self.assertTrue(C.load(C.ROOT/'.la_work/amap/hyper_hoenn_canary1/receipt.json')['runtime_verified'])
 def test_no_donor_extra_events_or_progression(self):
  for n in C.TARGETS:
   old=C.load(C.OUT/'original'/f'data/maps/{n}/map.json');now=C.load(C.ROOT/f'data/maps/{n}/map.json')
   for k in ['object_events','warp_events','coord_events','bg_events']:self.assertEqual(len(old[k])+len(C.C.third_gates(n) if k=='object_events' else []),len(now[k]))
  self.assertFalse(self.ledger['hyper_gameplay_imported'])
 def test_postgame_cave_native_metatile_contract(self):
  g=self.grids['Route103'];self.assertEqual(0,g.attrs[0][0x09F]&255);self.assertEqual(0x60,g.attrs[0][0x0A7]&255)
  script=(C.ROOT/'data/maps/Route103/scripts.inc').read_text();self.assertIn('FLAG_SYS_GAME_CLEAR',script);self.assertIn('setmetatile 45, 6, METATILE_General_CaveEntrance_Bottom, FALSE',script)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(OpeningSpineTests));C.dump(C.OUT/'test_results.json',{'passed':r.wasSuccessful(),'tests':r.testsRun,'errors':len(r.errors),'failures':len(r.failures),'runtime_verified':False});raise SystemExit(0 if r.wasSuccessful() else 1)
