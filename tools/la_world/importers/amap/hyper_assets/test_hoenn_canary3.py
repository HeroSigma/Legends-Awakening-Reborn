#!/usr/bin/env python3
"""Rustboro progression ownership, reachability, construction and asset checks."""
import collections,importlib.util,re,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('third',Path(__file__).with_name('hoenn_canary3.py'));C=importlib.util.module_from_spec(s);s.loader.exec_module(C)
class RustboroBatchTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.ledger=C.load(C.OUT/'coordinate_remap_ledger.json');cls.cat=C.load(C.ROOT/'.la_work/amap/hyper_asset_integration/asset_catalog.json');cls.grids={n:C.Grid(next(x for x in cls.cat['layouts'] if x['donor_id']==k)) for n,k in {**C.TARGETS,**C.GATE_ONLY}.items()};g=cls.grids['RustboroCity'];g.blocks[C.PATCH['y']*g.w+C.PATCH['x']]=C.PATCH['after'];
  for patch in C.TUNNEL_PATCHES:
   g=cls.grids[patch['map']];g.blocks[patch['y']*g.w+patch['x']]=patch['after']
  cls.maps={n:C.load(C.ROOT/f'data/maps/{n}/map.json') for n in {**C.TARGETS,**C.GATE_ONLY}};cls.scripts={n:(C.ROOT/f'data/maps/{n}/scripts.inc').read_text() for n in C.SCRIPT_MAPS}
 def flood(self,n,start,blocked):
  g=self.grids[n];seen={start};q=collections.deque([start])
  while q:
   x,y=q.popleft()
   for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    if 0<=a<g.w and 0<=b<g.h and (a,b) not in seen and (a,b) not in blocked and g.walk(a,b):seen.add((a,b));q.append((a,b))
  return seen
 def test_full_protected_baseline_and_native_ownership(self):C.validate()
 def test_native_event_ledger_exact_and_construction_is_only_append(self):
  for n in C.TARGETS:
   old=C.load(C.OUT/'original'/f'data/maps/{n}/map.json');now=self.maps[n]
   for k in ['object_events','warp_events','coord_events','bg_events']:
    entries=[x for x in self.ledger['events'] if x['map']==n and x['kind']==k];self.assertEqual(len(old[k]),len(entries));self.assertEqual(now[k][:len(entries)],[x['after'] for x in entries])
 def test_geometry_scene_paths_and_connection_elevations(self):
  self.assertEqual(self.ledger['native_scene_paths'],C.scenes(self.grids,self.scripts));self.assertEqual(self.ledger['connection_checks'],C.seam_checks(self.grids,self.maps));self.assertEqual(45,len(self.ledger['native_scene_paths']))
  links=self.ledger['connection_checks'];self.assertEqual(2,sum(x['crossable'] for l in links if l['from']=='Route104' and l['to']=='PetalburgCity' for x in l['cells']));self.assertEqual(8,sum(x['crossable'] for l in links if l['from']=='Route104' and l['to']=='RustboroCity' for x in l['cells']));self.assertEqual(5,sum(x['crossable'] for l in links if l['from']=='RustboroCity' and l['to']=='Route116' for x in l['cells']))
 def test_woods_devon_scene_cannot_be_bypassed_before_cut(self):
  n='PetalburgWoods';m=self.maps[n];blocked={(e['x'],e['y']) for e in m['object_events'] if e['graphics_id'] in ['OBJ_EVENT_GFX_CUTTABLE_TREE','OBJ_EVENT_GFX_SCIENTIST_1']};triggers={(e['x'],e['y']) for e in m['coord_events']}
  for start in [(26,43),(27,43),(36,43),(37,43)]:
   reachable=self.flood(n,start,blocked);without=self.flood(n,start,blocked|triggers);self.assertIn((8,4),reachable);self.assertNotIn((8,4),without);self.assertTrue(triggers<=reachable)
 def test_rusturf_rocks_preserve_west_east_progression_gate(self):
  m=self.maps['RusturfTunnel'];blocked={(e['x'],e['y']) for e in m['object_events'] if e['graphics_id'] in ['OBJ_EVENT_GFX_BREAKABLE_ROCK','OBJ_EVENT_GFX_SCIENTIST_1']};before=self.flood('RusturfTunnel',(4,10),blocked);after=self.flood('RusturfTunnel',(4,10),{xy for xy in blocked if xy not in [(24,4),(24,5)]});self.assertNotIn((29,16),before);self.assertIn((29,16),after)
 def test_fifteen_gates_are_fixed_project_owned_and_destinations_unregistered(self):
  gates=self.ledger['construction_gates'];self.assertEqual(15,len(gates));self.assertEqual(4,sum(g['map']=='Route102' and g['reserved_donor_id']=='34.67' for g in gates))
  groups=C.load(C.ROOT/'data/maps/map_groups.json');baseline=C.load(C.OUT/'baseline.json');self.assertEqual(baseline['data/maps/map_groups.json'],C.digest(C.ROOT/'data/maps/map_groups.json'))
  for gate in gates:
   e=gate['scientist'];self.assertEqual('0',e['flag']);self.assertEqual('TRAINER_TYPE_NONE',e['trainer_type']);self.assertEqual('MOVEMENT_TYPE_FACE_DOWN',e['movement_type']);self.assertEqual((0,0),(e['movement_range_x'],e['movement_range_y']));self.assertFalse(any((w['x'],w['y'])==(e['x'],e['y']) for w in self.maps[gate['map']]['warp_events']))
   text=self.scripts[gate['map']];body=re.search('^'+e['script']+r'::\n(.*?)(?=^\w+:)',text,re.M|re.S)[1];self.assertNotRegex(body,r'setflag|clearflag|setvar|warp|giveitem|trainerbattle|callnative');self.assertIn('under construction.',text)
 def test_shared_mart_center_layouts_isolated_and_bank_lossless(self):
  old=C.load(C.OUT/'original/data/layouts/layouts.json')['layouts'];current=C.load(C.ROOT/'data/layouts/layouts.json')['layouts'];self.assertEqual(len(old)+3+C.C.C.fourth_layout_delta(),len(current))
  for key in ['LAYOUT_MART','LAYOUT_POKEMON_CENTER_1F']:self.assertEqual(next(x for x in old if x['id']==key),next(x for x in current if x['id']==key))
  for n,k in C.TARGETS.items():
   l=next(x for x in current if x['id']==self.maps[n]['layout']);d=next(x for x in self.cat['layouts'] if x['donor_id']==k);self.assertEqual(d['border_path'],l['border_filepath']);self.assertEqual(d['primary_tileset'],l['primary_tileset']);self.assertEqual(d['secondary_tileset'],l['secondary_tileset']);self.assertEqual(C.PATCH_PATH if n=='RustboroCity' else C.TUNNEL_PATCH_PATH if n=='RusturfTunnel' else d['blockdata_path'],l['blockdata_filepath'])
  actual=C.words(C.ROOT/C.TUNNEL_PATCH_PATH);source=C.words(C.ROOT/'data/hyper_assets/layouts/24.4/map.bin');self.assertEqual(sorted([(x['y']*36+x['x'],x['before'],x['after']) for x in C.TUNNEL_PATCHES]),[(i,a,b) for i,(a,b) in enumerate(zip(source,actual)) if a!=b])
  actual=C.words(C.ROOT/C.PATCH_PATH);source=C.words(C.ROOT/'data/hyper_assets/layouts/0.3/map.bin');self.assertEqual([(12*40+30,0x160F,0x32BB)],[(i,a,b) for i,(a,b) in enumerate(zip(source,actual)) if a!=b])
 def test_heal_fly_rebind_only_coordinates_and_native_respawn(self):
  old=C.load(C.OUT/'original/src/data/heal_locations.json');now=C.load(C.ROOT/'src/data/heal_locations.json');a=next(x for x in old['heal_locations'] if x['id']=='HEAL_LOCATION_RUSTBORO_CITY');b=next(x for x in now['heal_locations'] if x['id']=='HEAL_LOCATION_RUSTBORO_CITY');self.assertEqual((16,39),(a['x'],a['y']));self.assertEqual((16,47),(b['x'],b['y']));a['y']=47;self.assertEqual(old,now);self.assertTrue(self.grids['RustboroCity'].walk(16,47));self.assertEqual('MAP_RUSTBORO_CITY_POKEMON_CENTER_1F',b['respawn_map']);self.assertEqual('LOCALID_RUSTBORO_NURSE',b['respawn_npc'])
  h=(C.OUT/'original/src/data/heal_locations.h').read_text();new=(C.ROOT/'src/data/heal_locations.h').read_text();expected=re.sub(r'(\[HEAL_LOCATION_RUSTBORO_CITY - 1\] = \{.*?\.y = )39(,.*?\},)',lambda m:m[1]+'47'+m[2],h,count=1,flags=re.S);self.assertEqual(expected,new)
 def test_native_graphics_abi_and_animation_frame_closure(self):
  for x in self.ledger['graphics_adapters']:
   strip=lambda t:re.sub(r'\.(paletteTag|images)\s*=\s*[^,]+,','',t);self.assertEqual(strip(x['native_contract']),strip(x['replacement']));self.assertTrue(all(f<x['source_frame_count'] for f in x['native_animation_frames']))
  bindings=(C.ROOT/'src/hyper_asset_graphics_bindings.inc').read_text();self.assertNotRegex(bindings,r'OBJ_EVENT_GFX_(VAR_|BERRY_TREE|ITEM_BALL|MR_BRINEYS_BOAT|WINGULL)');baseline=C.load(C.OUT/'baseline.json');self.assertEqual(baseline['data/scripts/rival_graphics.inc'],C.digest(C.ROOT/'data/scripts/rival_graphics.inc'));self.assertIn('{MAP_RUSTBORO_CITY, OBJ_EVENT_GFX_RIVAL_BRENDAN_NORMAL',bindings);self.assertIn('{MAP_RUSTBORO_CITY, OBJ_EVENT_GFX_RIVAL_MAY_NORMAL',bindings)
 def test_native_weather_counter_and_elevation_runtime_contracts(self):
  g=self.grids['Route116'];self.assertEqual(0x60,g.attrs[0][0xA7]&255)
  for n,x,y in [('RustboroCity_PokemonCenter_1F',7,3),('RustboroCity_Mart',1,4)]:self.assertEqual(0x80,self.grids[n].cell(x,y)['translated_behavior'])
  source=(C.ROOT/'src/event_object_movement.c').read_text();self.assertIn('UpdateObjectEventElevationAndPriority(objEvent, sprite);',source);self.assertIn('objEvent->currentElevation = curElevation;',source)
if __name__=='__main__':
 r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(RustboroBatchTests));C.dump(C.OUT/'test_results.json',{'passed':r.wasSuccessful(),'tests':r.testsRun,'errors':len(r.errors),'failures':len(r.failures),'runtime_verified':False});raise SystemExit(0 if r.wasSuccessful() else 1)
