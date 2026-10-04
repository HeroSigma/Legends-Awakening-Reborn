#!/usr/bin/env python3
"""Dewford–Mauville native gameplay, scene and asset closure checks."""
import importlib.util,re,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('fourth',Path(__file__).with_name('hoenn_canary4.py'));C=importlib.util.module_from_spec(s);s.loader.exec_module(C)
class DewfordMauvilleTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.ledger=C.load(C.OUT/'coordinate_remap_ledger.json');cls.cat=C.load(C.ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');cls.maps={n:C.load(C.ROOT/f'data/maps/{n}/map.json') for n in C.TARGETS};cls.scripts={n:(C.ROOT/f'data/maps/{n}/scripts.inc').read_text() for n in C.TARGETS};cls.grids={n:C.Grid(next(x for x in cls.cat['layouts'] if x['donor_id']==k)) for n,k in C.TARGETS.items()}
  for p in cls.ledger['geometry_compatibility_patches']:
   g=cls.grids[p['map']];i=p['y']*g.w+p['x'];assert g.blocks[i]==p['before'];g.blocks[i]=p['after']
 def test_exact_protected_baseline_native_ownership_and_map_ids(self):C.validate()
 def test_event_ledger_keeps_native_scripts_trainers_rewards_flags_and_destinations(self):
  for n,m in self.maps.items():
   old=C.load(C.OUT/'original'/f'data/maps/{n}/map.json')
   for kind in ['object_events','warp_events','coord_events','bg_events']:
    entries=[e for e in self.ledger['events'] if e['map']==n and e['kind']==kind];self.assertEqual(old[kind],[e['before'] for e in entries]);self.assertEqual(m[kind][:len(entries)],[e['after'] for e in entries])
   self.assertEqual(old['connections'],m['connections'])
 def test_native_rival_birch_wally_steven_museum_harbor_and_boat_scene_paths(self):
  self.assertEqual(self.ledger['native_scene_paths'],C.scenes(self.grids,self.scripts));self.assertGreaterEqual(len(self.ledger['native_scene_paths']),50)
  check=C.geometry_checks(self.grids,self.maps);self.assertEqual(check,self.ledger['geometry_checks']);self.assertFalse(check['route110_rival_land_gate']['north_reachable_without_rival_trigger']);self.assertTrue(check['mauville_puzzle']['native_puzzle_grid_metatile_and_collision_exact'])
 def test_private_geometry_patches_keep_art_and_staged_donor_bank_lossless(self):
  layouts=C.load(C.ROOT/'data/layouts/layouts.json')['layouts'];patched={p['map'] for p in self.ledger['geometry_compatibility_patches']}
  for n,k in C.TARGETS.items():
   source=next(x for x in self.cat['layouts'] if x['donor_id']==k);current=next(x for x in layouts if x['id']==self.maps[n]['layout']);self.assertEqual(source['blockdata_sha256'],C.digest(C.ROOT/source['blockdata_path']));self.assertEqual(source['border_path'],current['border_filepath']);self.assertEqual(self.grids[n].blocks,C.words(C.ROOT/current['blockdata_filepath']))
   if n in patched:self.assertIn('/canary4_layouts/',current['blockdata_filepath'])
  for p in self.ledger['geometry_compatibility_patches']:self.assertEqual(p['before']&1023,p['after']&1023)
  old=C.load(C.OUT/'original/data/layouts/layouts.json')['layouts'];self.assertEqual(len(old)+10,len(layouts))
  for id in ['LAYOUT_MART','LAYOUT_POKEMON_CENTER_1F']:self.assertEqual(next(x for x in old if x['id']==id),next(x for x in layouts if x['id']==id))
 def test_construction_gates_have_no_gameplay_or_new_destination(self):
  gates=self.ledger['construction_gates'];self.assertEqual(5,len(gates));self.assertEqual({'34.49','34.36','34.58','35.83','9.9'},{g['reserved_donor_id'] for g in gates})
  for g in gates:
   e=g['scientist'];self.assertEqual('0',e['flag']);self.assertEqual('TRAINER_TYPE_NONE',e['trainer_type']);self.assertEqual('MOVEMENT_TYPE_FACE_DOWN',e['movement_type']);self.assertEqual((0,0),(e['movement_range_x'],e['movement_range_y']));self.assertFalse(any((w['x'],w['y'])==(e['x'],e['y']) for w in self.maps[g['map']]['warp_events']));body=re.search('^'+e['script']+r'::\n(.*?)(?=^\w+:)',self.scripts[g['map']],re.M|re.S)[1];self.assertNotRegex(body,r'setflag|clearflag|setvar|warp|trainerbattle|giveitem|callnative');self.assertIn('under construction.',self.scripts[g['map']])
 def test_native_dynamic_rival_and_animation_runtime_contracts(self):
  b=C.load(C.OUT/'baseline.json');self.assertEqual(b['data/scripts/rival_graphics.inc'],C.digest(C.ROOT/'data/scripts/rival_graphics.inc'));bindings=(C.ROOT/'src/hyper_asset_graphics_bindings.inc').read_text()
  for gfx in ['BRENDAN','MAY']:self.assertIn('{MAP_ROUTE110, OBJ_EVENT_GFX_RIVAL_'+gfx+'_NORMAL',bindings)
  self.assertNotRegex(bindings,r'OBJ_EVENT_GFX_VAR_');self.assertNotIn('RIVAL_BRENDAN_MACH_BIKE,',bindings);self.assertNotIn('RIVAL_MAY_MACH_BIKE,',bindings)
  for a in self.ledger['graphics_adapters']:
   strip=lambda t:re.sub(r'\.(paletteTag|images)\s*=\s*[^,]+,','',t);self.assertEqual(strip(a['native_contract']),strip(a['replacement']));obj=next(x for x in self.cat['object_graphics'] if x['source_graphics_id']==a['source_graphics_id']);self.assertTrue(all(f<obj['frame_count'] for f in a['native_animation_frames']))
 def test_native_story_brain_and_services_are_retained(self):
  for n,commands in {'SlateportCity_OceanicMuseum_2F':['FLAG_DELIVERED_DEVON_GOODS','ITEM_DEVON_PARTS','FLAG_HIDE_ROUTE_110_TEAM_AQUA','TRAINER_GRUNT_MUSEUM_1','TRAINER_GRUNT_MUSEUM_2'],'MauvilleCity_Gym':['MauvilleGymPressSwitch','MauvilleGymDeactivatePuzzle','FLAG_BADGE03_GET'],'GraniteCave_StevensRoom':['ITEM_LETTER','FLAG_DELIVERED_STEVEN_LETTER'],'MauvilleCity_BikeShop':['ITEM_MACH_BIKE','ITEM_ACRO_BIKE']}.items():
   for command in commands:self.assertIn(command,self.scripts[n])
  base=C.load(C.OUT/'baseline.json')
  for f in ['src/data/heal_locations.json','src/data/heal_locations.h','src/data/wild_encounters.json','src/field_specials.c','src/event_object_movement.c']:self.assertEqual(base[f],C.digest(C.ROOT/f),f)
if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(DewfordMauvilleTests));C.dump(C.OUT/'test_results.json',{'passed':result.wasSuccessful(),'tests':result.testsRun,'errors':len(result.errors),'failures':len(result.failures),'runtime_verified':False});raise SystemExit(0 if result.wasSuccessful() else 1)
