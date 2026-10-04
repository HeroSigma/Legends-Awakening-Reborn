import importlib.util,json,hashlib,csv,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
PLAN=ROOT/'.la_work/amap/hyper_hoenn_replacement'
SPEC=importlib.util.spec_from_file_location('planner',Path(__file__).with_name('build_hyper_hoenn_plan.py'))
MODULE=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MODULE)

class ReplacementPlanTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.plan=json.loads((PLAN/'hyper_hoenn_replacement_manifest.json').read_text())
  cls.rows=cls.plan['maps'];cls.by_name={r['canonical']['name']:r for r in cls.rows}
 def test_full_current_canonical_coverage_and_in_place_identity(self):
  groups=json.loads((ROOT/'data/maps/map_groups.json').read_text())
  expected={name for g in groups['group_order'][:34] for name in groups[g]}
  self.assertEqual(expected,set(self.by_name));self.assertEqual(518,len(self.rows))
  for r in self.rows:
   self.assertEqual(r['canonical']['id'],r['migration_policy']['canonical_destination'])
   self.assertFalse(r['migration_policy']['create_additive_map']);self.assertFalse(r['import_flag']);self.assertFalse(r['readiness']['automatic_replacement_allowed'])
 def test_relocated_hoenn_room_is_selected_by_actual_routing(self):
  r=self.by_name['SootopolisCity_House5'];self.assertEqual('15.9',r['canonical']['group_map']);self.assertEqual('37.118',r['hyper']['id'])
  outdoor=self.by_name['SootopolisCity']['hyper']['warps']
  self.assertEqual('37.118',next(w['target_id'] for w in outdoor if w['index']==8))
  self.assertTrue(all(w['target_id']=='0.7' and w['dest_warp_id']==8 for w in r['hyper']['warps']))
  self.assertEqual('EXACT_ORDERED_ENDPOINTS_MATCH',r['compatibility']['warps']['status'])
 def test_equal_dimensions_do_not_mask_story_or_coordinate_changes(self):
  for n in ['LittlerootTown','Route101','OldaleTown','Route102','SootopolisCity']:
   r=self.by_name[n];self.assertTrue(r['compatibility']['geometry']['dimensions_equal'])
   self.assertFalse(r['readiness']['static_visual_layout_candidate']);self.assertIn(r['replacement_mode'],['FULL_RECONCILE','MANUAL_REVIEW'])
 def test_incomplete_event_exports_are_quarantined(self):
  partial=[r for r in self.rows if not r['hyper']['event_export_complete']]
  self.assertEqual(9,len(partial))
  for r in partial:self.assertIn(r['replacement_mode'],['KEEP_EXPANSION_ORIGINAL','MANUAL_REVIEW']);self.assertFalse(r['readiness']['static_visual_layout_candidate'])
  stale=self.by_name['SootopolisCity_MysteryEventsHouse_1F'];self.assertEqual('LOW',stale['confidence']);self.assertEqual(255,stale['hyper']['declared_event_counts']['object']);self.assertEqual(0,stale['hyper']['event_counts']['object'])
 def test_repurposed_destinations_keep_expansion_identity(self):
  for n in ['BirthIsland_Exterior','BirthIsland_Harbor','NavelRock_Harbor']:
   r=self.by_name[n];self.assertEqual('NONE',r['confidence']);self.assertEqual('KEEP_EXPANSION_ORIGINAL',r['replacement_mode'])
 def test_existing_custom_scientist_is_in_preserved_event_ledger(self):
  ledger=json.loads((PLAN/'hyper_hoenn_event_comparison_ledger.json').read_text())
  e=next(x for x in ledger if x['canonical_name']=='LittlerootTown' and x['canonical_event'].get('local_id')=='LOCALID_LITTLEROOT_TELEPORT_SCIENTIST')
  self.assertIn('TeleportScientist',e['canonical_event']['script']);self.assertTrue(e['action'].startswith('PRESERVE_EXPANSION_EVENT'))
 def test_dynamic_returns_are_not_literal_cross_region_destinations(self):
  r=self.by_name['InsideOfTruck'];self.assertEqual('25.40',r['hyper']['id']);self.assertTrue(r['relationships']['dynamic_return_contract_required'])
  self.assertTrue(all(w[3]=='DYNAMIC' for w in r['compatibility']['warps']['canonical_normalized']))
 def test_recovered_custom_behavior_requires_exact_pattern(self):
  self.assertEqual('MB_NORMAL',MODULE.source_behavior(0x1f,'secondary_083DF77C',509,1,{}))
  for tile,index,collision in [('secondary_083DF77C',509,0),('secondary_083DF77C',508,1),('secondary_083DF71C',509,1)]:
   self.assertTrue(MODULE.source_behavior(0x1f,tile,index,collision,{}).startswith('UNRESOLVED'))
 def test_canary_candidates_have_all_static_contracts_and_keep_scripts(self):
  self.assertEqual(5,sum(r['readiness']['static_visual_layout_candidate'] for r in self.rows))
  for entry in self.plan['static_geometry_shortlist']:
   r=self.by_name[entry['canonical_name']];self.assertTrue(r['readiness']['static_visual_layout_candidate']);self.assertEqual('VISUAL_ONLY',r['replacement_mode'])
   self.assertEqual('PRESERVE',r['migration_policy']['expansion_events']);self.assertTrue(r['migration_policy']['expansion_scripts'].startswith('PRESERVE'))
 def test_csv_review_partition_and_report_hashes(self):
  def names(file):
   with (PLAN/file).open() as f:return {r['canonical_name'] for r in csv.DictReader(f)}
  manual=names('hyper_hoenn_manual_review.csv');keep=names('hyper_hoenn_keep_expansion_original.csv');safe=names('hyper_hoenn_static_visual_layout_candidates.csv')
  self.assertFalse(manual&keep or manual&safe or keep&safe);self.assertEqual(set(self.by_name),manual|keep|safe)
  validation=json.loads((PLAN/'validation.json').read_text())
  for name,digest in validation['outputs_sha256'].items():self.assertEqual(digest,hashlib.sha256((PLAN/name).read_bytes()).hexdigest(),name)
 def test_current_gameplay_and_donor_source_hashes_remain_unchanged(self):
  inputs=json.loads((PLAN/'hyper_hoenn_protected_inputs.json').read_text())
  self.assertGreater(len(inputs),25000)
  for name,digest in inputs.items():self.assertEqual(digest,hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),name)

if __name__=='__main__':unittest.main(verbosity=2)
