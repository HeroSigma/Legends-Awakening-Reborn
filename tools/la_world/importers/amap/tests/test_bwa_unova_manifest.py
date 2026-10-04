"""Safety and identity regressions against the validated BWA export fixture."""
import csv
from copy import deepcopy
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from build_bwa_unova_manifest import build, validate_manifest, audit_destination_imports, REPO

class BwaUnovaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = REPO / '.la_work/amap/bwa_full_v11'
        cls.metadata_csv = REPO / '.la_work/amap/donor_map_metadata_report.csv'
        cls.metadata_md = REPO / '.la_work/amap/donor_map_metadata_report.md'
        cls.rules = HERE / 'bwa_unova_rules.json'
        cls.reference = HERE / 'firered_map_reference.json'
        cls.manifest, cls.corrected = build(cls.root, cls.metadata_csv, cls.metadata_md, cls.rules, cls.reference)
        cls.maps = {r['id']: r for r in cls.manifest['maps']}

    def test_complete_partition_and_disabled_runtime(self):
        validate_manifest(self.manifest)
        self.assertEqual(len(self.maps), 444)
        self.assertEqual(self.manifest['summary']['exact_firered_blockdata_matches'], 316)
        self.assertEqual(len(self.manifest['lists']['high_confidence_import']), 25)
        self.assertTrue(all(not r['runtime_import_flag'] and not r['relationship_import_flag'] for r in self.maps.values()))

    def test_canary_and_event_counts(self):
        self.assertEqual(self.maps['3.0']['disposition'], 'PRESERVE_CANARY')
        self.assertFalse(self.maps['3.0']['import_flag'])
        self.assertEqual(self.maps['3.0']['object_count'], 5)
        self.assertEqual(self.maps['3.0']['event_count_mismatches']['bg'], {'declared': 6, 'exported': 5})
        self.assertTrue(all(str(r['objects']).isdigit() for r in self.corrected))
        self.assertEqual(self.manifest['summary']['event_count_mismatch_maps'], 6)

    def test_names_do_not_override_exact_legacy_geometry(self):
        for identifier in ('1.1', '1.5', '1.39', '1.47', '3.25', '3.42'):
            self.assertEqual(self.maps[identifier]['disposition'], 'EXCLUDED_LEGACY')
            self.assertTrue(self.maps[identifier]['exact_firered_blockdata'])
            self.assertFalse(self.maps[identifier]['import_flag'])
        self.assertEqual(self.maps['1.1']['base_firered_slot']['name'], 'MtMoon_1F')
        self.assertEqual(self.maps['1.5']['base_firered_slot']['name'], 'SSAnne_1F_Corridor')

    def test_duplicate_families_preserve_distinct_roles(self):
        for identifier in ('3.21', '3.22', '1.30', '3.4', '3.45', '3.46'):
            self.assertTrue(self.maps[identifier]['canonical_flag'])
        self.assertEqual(self.maps['1.30']['visual_map_sha256'], self.maps['1.32']['visual_map_sha256'])
        self.assertFalse(self.maps['1.32']['canonical_flag'])
        self.assertEqual(self.maps['5.6']['visual_map_sha256'], self.maps['42.3']['visual_map_sha256'])
        self.assertNotEqual(self.maps['5.6']['coord_count'], self.maps['42.3']['coord_count'])
        self.assertFalse(self.maps['3.1']['import_flag'])
        self.assertFalse(self.maps['3.5']['import_flag'])
        self.assertTrue(self.maps['39.0']['canonical_flag'])
        self.assertFalse(self.maps['44.3']['canonical_flag'])

    def test_legacy_dependencies_are_not_recursive_imports(self):
        dependencies = self.maps['3.22']['dependencies']
        target = next(d for d in dependencies if d['target'] == '1.1')
        self.assertEqual(target['target_disposition'], 'EXCLUDED_LEGACY')
        self.assertFalse(target['import_automatically'])
        self.assertIn(target, self.maps['3.22']['wiring_blockers'])
        self.assertTrue(any(e['source'] == '3.3' for e in self.maps['42.3']['relationships']['incoming']))

    def test_observed_existing_imports_are_never_reimported(self):
        for observation in self.manifest.get('observed_destination_imports', []):
            record = self.maps[observation['donor_id']]
            self.assertTrue(record['already_imported'])
            self.assertEqual(record['import_action'], 'SKIP_EXISTING_IMPORT')
            self.assertFalse(record['reimport_flag'])
            self.assertFalse(observation['gameplay_validated_by_this_audit'])
            self.assertNotIn(record['id'], self.manifest['remaining_asset_candidates'])

    def test_stale_curated_decision_is_quarantined(self):
        with tempfile.TemporaryDirectory() as tmp:
            rules = json.loads(self.rules.read_text())
            rules['rules']['3.2']['preview_sha256'] = '0' * 64
            path = Path(tmp) / 'rules.json'
            path.write_text(json.dumps(rules))
            result, _ = build(self.root, self.metadata_csv, self.metadata_md, path, self.reference)
            changed = next(r for r in result['maps'] if r['id'] == '3.2')
            self.assertEqual(changed['disposition'], 'MANUAL_REVIEW')
            self.assertFalse(changed['import_flag'])
            self.assertFalse(changed['canonical_flag'])
            self.assertTrue(changed['stale_curated_rule'])

    def test_user_game_verification_is_bound_to_current_files(self):
        rules = json.loads(self.rules.read_text())
        verifications = rules.get('destination_verifications', {})
        if '3.2' not in verifications:
            self.skipTest('No user game-test record in this fixture')
        current = next(item for item in self.manifest['observed_destination_imports'] if item['donor_id'] == '3.2')
        self.assertEqual(current['status'], 'GAME_TESTED_VERIFIED_BY_USER')
        self.assertFalse(current['gameplay_validated_by_this_audit'])
        stale = deepcopy(verifications)
        stale['3.2']['destination_json_sha256'] = '0' * 64
        observations = audit_destination_imports(deepcopy(self.manifest['maps']), stale)
        changed = next(item for item in observations if item['donor_id'] == '3.2')
        self.assertEqual(changed['status'], 'USER_VERIFICATION_STALE_RECHECK_REQUIRED')
        self.assertFalse(changed['user_gameplay_verification']['matches_current_import'])
        self.assertFalse(changed['reimport_flag'])

    def test_missing_metadata_row_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.metadata_csv.open(newline='') as stream:
                reader = csv.DictReader(stream)
                fields, rows = reader.fieldnames, list(reader)
            removed = False
            reduced = []
            for row in rows:
                if row['donor'] == 'BWA' and not removed:
                    removed = True
                    continue
                reduced.append(row)
            path = Path(tmp) / 'incomplete.csv'
            with path.open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                writer.writerows(reduced)
            with self.assertRaisesRegex(ValueError, '444'):
                build(self.root, path, self.metadata_md, self.rules, self.reference)

if __name__ == '__main__':
    unittest.main()
