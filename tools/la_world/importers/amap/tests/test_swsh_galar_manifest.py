"""Galar identity, provenance, dependency and canary safety regressions."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from build_swsh_galar_manifest import build, validate_manifest, REPO

class SwshGalarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = REPO/'.la_work/amap/swsh_full_v11'
        cls.csv = REPO/'.la_work/amap/donor_map_metadata_report.csv'
        cls.md = REPO/'.la_work/amap/donor_map_metadata_report.md'
        cls.rules = HERE/'swsh_galar_rules.json'
        cls.reference = HERE/'firered_map_reference.json'
        cls.manifest, cls.corrected = build(cls.root, cls.csv, cls.md, cls.rules, cls.reference)
        cls.maps = {record['id']: record for record in cls.manifest['maps']}

    def test_complete_inventory_and_disjoint_decisions(self):
        validate_manifest(self.manifest)
        self.assertEqual(len(self.maps), 701)
        self.assertEqual(self.manifest['summary']['exact_firered_blockdata_matches'], 225)
        self.assertEqual(self.manifest['summary']['postwick_labelled_maps'], 172)
        self.assertEqual(len(self.manifest['lists']['high_confidence_import']), 55)

    def test_postwick_canary_is_never_replaced(self):
        self.assertEqual(self.maps['3.0']['disposition'], 'PRESERVE_CANARY')
        self.assertTrue(self.maps['3.0']['canonical_flag'])
        self.assertFalse(self.maps['3.0']['import_flag'])
        self.assertEqual(self.maps['4.6']['canonical_replacement'], '3.0')
        self.assertEqual(self.maps['4.6']['disposition'], 'EXCLUDED_SUPERSEDED')
        edge = next(dep for dep in self.maps['3.19']['dependencies'] if dep['target'] == '4.6')
        self.assertEqual(edge['canonical_target_hint'], '3.0')
        self.assertFalse(edge['import_automatically'])

    def test_postwick_aliases_have_specific_town_replacements(self):
        pairs = [('3.1','5.6'), ('3.2','6.10'), ('3.3','7.11'), ('3.4','8.7'), ('3.6','10.21'), ('3.7','11.10'), ('3.8','12.10'), ('3.10','14.10')]
        for old, new in pairs:
            self.assertEqual(self.maps[old]['canonical_replacement'], new)
            self.assertFalse(self.maps[old]['import_flag'])
            self.assertTrue(self.maps[new]['canonical_flag'])
        self.assertEqual(self.maps['3.5']['canonical_replacement'], '9.10')

    def test_fire_red_slots_do_not_override_edited_galar_routes(self):
        for legacy in ('3.11', '3.22', '3.24', '3.25', '3.26', '3.27', '1.5'):
            self.assertEqual(self.maps[legacy]['disposition'], 'EXCLUDED_LEGACY')
            self.assertTrue(self.maps[legacy]['exact_firered_blockdata'])
        self.assertTrue(self.maps['7.17']['canonical_flag'])
        self.assertTrue(self.maps['10.20']['canonical_flag'])
        self.assertEqual(self.maps['1.5']['base_firered_slot']['name'], 'SSAnne_1F_Corridor')

    def test_map_types_and_names_are_not_the_only_evidence(self):
        self.assertEqual(self.maps['14.10']['map_type'], 4)
        self.assertEqual(self.maps['14.10']['category'], 'WORLD')
        self.assertEqual(self.maps['42.12']['map_type'], 3)
        self.assertEqual(self.maps['42.12']['category'], 'CAVE_DUNGEON')
        self.assertEqual(self.maps['3.23']['category'], 'INTERIOR')
        self.assertEqual(self.maps['42.8']['category'], 'DEBUG_TEST')
        self.assertEqual(self.maps['42.8']['disposition'], 'MANUAL_REVIEW')

    def test_all_object_counts_are_corrected_and_mismatches_deferred(self):
        self.assertEqual(len(self.corrected), 701)
        self.assertTrue(all(str(row['objects']).isdigit() for row in self.corrected))
        mismatches = [record for record in self.maps.values() if record['event_count_mismatches']]
        self.assertEqual(len(mismatches), 31)
        self.assertTrue(all(not record['import_flag'] for record in mismatches))
        self.assertEqual(self.maps['5.6']['event_count_mismatches']['coord'], {'declared':9, 'exported':7})

    def test_duplicate_sectors_keep_individual_roles_and_relationships(self):
        self.assertTrue(self.maps['6.30']['canonical_flag'])
        self.assertTrue(self.maps['6.31']['canonical_flag'])
        self.assertNotEqual(self.maps['6.30']['role'], self.maps['6.31']['role'])
        self.assertEqual(self.maps['8.8']['visual_map_sha256'], self.maps['8.26']['visual_map_sha256'])
        self.assertEqual(self.maps['8.8']['canonical_replacement'], '8.26')
        self.assertFalse(self.maps['8.8']['canonical_flag'])
        for i in ('6.28','8.20','1.3'):
            self.assertTrue(self.maps[i]['canonical_flag'])
            self.assertEqual(self.maps[i]['category'], 'CAVE_DUNGEON')

    def test_runtime_imports_and_recursive_dependencies_disabled(self):
        self.assertFalse(self.manifest['execution_allowed'])
        self.assertFalse(self.manifest['bulk_import_allowed'])
        for record in self.maps.values():
            self.assertTrue(all(not record[key] for key in ('runtime_import_flag','event_import_flag','script_import_flag','relationship_import_flag')))
            self.assertTrue(all(not dep['import_automatically'] for dep in record['dependencies']))
            self.assertTrue(record['pointers'])
            self.assertTrue(record['tileset_source'])

    def test_changed_preview_decision_falls_back_to_manual_review(self):
        rules = json.loads(self.rules.read_text())
        rules['rules']['6.10']['preview_sha256'] = '0' * 64
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'rules.json'
            path.write_text(json.dumps(rules))
            manifest, _ = build(self.root, self.csv, self.md, path, self.reference)
        changed = next(record for record in manifest['maps'] if record['id']=='6.10')
        self.assertEqual(changed['disposition'], 'MANUAL_REVIEW')
        self.assertFalse(changed['canonical_flag'])
        self.assertFalse(changed['import_flag'])

    def test_changed_canary_decision_fails_without_replacing_it(self):
        rules = json.loads(self.rules.read_text())
        rules['rules']['3.0']['source_json_sha256'] = '0' * 64
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'rules.json'
            path.write_text(json.dumps(rules))
            with self.assertRaisesRegex(ValueError, 'Postwick canary'):
                build(self.root, self.csv, self.md, path, self.reference)

if __name__ == '__main__':
    unittest.main()
