#!/usr/bin/env python3
"""Build a conservative BWA-only Unova asset-selection manifest; never import.

Curated rules are guarded by source and preview hashes. FireRed slot ancestry
and exact blockdata hashes are evidence, not proof that donor events are stock.
All gameplay, event, script, warp and connection migration stays disabled.
"""
import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from classify_donor_maps import inventory, EVENTS, compact

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
REFERENCE_COMMIT = '037335f4c725d7c9aecdac87066f2002b4bd7e14'
CATEGORY_NAMES = ('WORLD', 'INTERIOR', 'CAVE_DUNGEON', 'TRANSITION', 'UTILITY', 'DEBUG_TEST', 'STALE_UNKNOWN')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def sort_id(identifier):
    return tuple(int(x) for x in identifier.split('.'))

def normalized_name(name):
    return ' '.join(name.lower().split()).replace('driftiveil', 'driftveil').replace('pinhweel', 'pinwheel')

def default_decision(d, base, exact, root_ids):
    typ, group = d['map_type'], d['group']
    category = 'WORLD' if typ in {1, 2, 3, 6} else 'CAVE_DUNGEON' if typ in {4, 5} else 'INTERIOR' if typ in {8, 9} else 'STALE_UNKNOWN'
    result = {'category': category, 'canonical_flag': False, 'import_flag': False,
              'confidence': 'LOW', 'reason': 'Unresolved semantic identity; metadata alone does not justify an import.',
              'role': 'unresolved', 'visual_review': 'NOT_REVIEWED', 'major_dungeon': False,
              'disposition': 'MANUAL_REVIEW'}
    def exclude(reason, role='legacy.geometry', cat=None):
        result.update(confidence='HIGH', reason=reason, role=role, disposition='EXCLUDED_LEGACY')
        if cat:
            result['category'] = cat
        return result
    if group == 0 and d['map'] < 5 and exact:
        return exclude('Exact FireRed link-facility blockdata and dynamic-target warps; utility, not Unova geography.', 'legacy.link_utility', 'UTILITY')
    if group == 3 and base and base['name'].startswith('Prototype_') and exact:
        return exclude('Exact FireRed prototype blockdata with no exported events; inherited prototype/stale content.', 'legacy.prototype', 'DEBUG_TEST')
    if exact and group in {1, 2}:
        return exclude('Exact blockdata match to FireRed ' + base['name'] + '; quarantine legacy geometry despite donor label. Repurposing would require a separate explicit review.')
    if group == 3 and exact:
        return exclude('Outdoor blockdata is identical to FireRed ' + base['name'] + '; route numbers or Unova neighbors do not establish an edited Unova area.')
    if group in {11, 12, 13, 14}:
        return exclude('Explicit Kanto location family and inherited host relationships; exclude from Unova selection.', 'legacy.kanto_interior')
    if base and (group in {24, 26, 28, 29, 30} or 31 <= group <= 38 or group == 40 or (group == 41 and d['map'] == 1)):
        return exclude('FireRed/Sevii host family remains tied to excluded legacy outdoor areas; no independent Unova identity.', 'legacy.host_interior')
    if group == 27 and not d['warps'] and not d['npcs']:
        return exclude('Unused standard indoor layout, no exported events or relationships, in inherited Kanto route family.', 'legacy.empty_room', 'STALE_UNKNOWN')
    if typ == 0 and not any(d[a] for a in EVENTS.values()) and not d['connections']:
        result.update(category='STALE_UNKNOWN', reason='Unspecified map type and no exported events/connections; possible staging or stale room, not proven debug content.')
    targets = {c.get('target_id') for c in d['warps'] + d['connections']}
    if typ == 8 and targets & root_ids:
        result.update(confidence='MEDIUM', reason='Interior with a direct Unova-core relationship; possible reused standard room. Needs preview/semantic validation.', role='core.interior_candidate')
    if base and ('Entrance' in base['name'] or 'Tunnel' in base['name']):
        result.update(category='TRANSITION', confidence='MEDIUM', reason='Inherited entrance/tunnel role with donor relationships; unresolved Unova versus legacy use.', role='transition.candidate')
    if d['warps'] and all(w.get('dynamic_target') for w in d['warps']):
        result.update(category='UTILITY', confidence='MEDIUM', reason='All exported warps are dynamic return targets; utility/elevator role, not autonomous geography.', role='utility.dynamic_return')
    return result

def csv_write(path, rows, fields):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: compact(row.get(k)) if isinstance(row.get(k), (list, dict)) else row.get(k, '') for k in fields})

def build(root, report_csv, report_md, rules_path, reference_path):
    exported_manifest = json.loads((root / 'manifest.json').read_text())
    rules_doc = json.loads(rules_path.read_text())
    reference_doc = json.loads(reference_path.read_text())
    if exported_manifest['profile'] != rules_doc['profile'] or exported_manifest['rom']['sha256'] != rules_doc['rom_sha256']:
        raise ValueError('Curated BWA rules do not match this donor ROM/profile')
    if reference_doc['commit'] != REFERENCE_COMMIT:
        raise ValueError('Unexpected FireRed reference revision')
    originals = {}
    with report_csv.open(encoding='utf-8-sig', newline='') as stream:
        for row in csv.DictReader(stream):
            if row['donor'] == 'BWA':
                key = f"{int(row['group'])}.{int(row['map'])}"
                if key in originals:
                    raise ValueError('Duplicate BWA metadata-report ID: ' + key)
                originals[key] = row
    markdown = report_md.read_text(encoding='utf-8-sig')
    if 'BWA' not in markdown or '444' not in markdown:
        raise ValueError('Referenced Markdown report does not describe the validated BWA inventory')
    generic = inventory('BWA', root)
    if len(generic) != 444 or set(originals) != {row['id'] for row in generic}:
        raise ValueError('Expected exactly 444 BWA maps in both JSON exports and metadata CSV')
    data = {row['id']: json.loads(Path(row['source_json']).read_text()) for row in generic}
    if not set(rules_doc['rules']) <= set(data):
        raise ValueError('Curated rules reference absent maps')
    core_ids = {i for i, rule in rules_doc['rules'].items() if rule['canonical_flag'] and rule['category'] == 'WORLD'}
    relationships = []
    incoming = defaultdict(list)
    for identifier, d in data.items():
        for kind, values in [('WARP', d['warps']), ('CONNECTION', d['connections'])]:
            for index, edge in enumerate(values):
                rel = {'source': identifier, 'kind': kind, 'index': index, 'target': edge.get('target_id'),
                       'dynamic_target': bool(edge.get('dynamic_target', False)), 'donor_record': edge}
                relationships.append(rel)
                incoming[edge.get('target_id')].append(rel)
    visual_families = defaultdict(list)
    layouts = defaultdict(list)
    names = defaultdict(list)
    for identifier, d in data.items():
        visual_families[d.get('visual_map_sha256')].append(identifier)
        layouts[d.get('layout_pointer')].append(identifier)
        names[normalized_name(d['name'])].append(identifier)
    records, corrected = [], []
    for generic_row in generic:
        identifier = generic_row['id']
        d = data[identifier]
        path = Path(generic_row['source_json'])
        base = reference_doc['maps'].get(identifier)
        block_hash = sha(path.parent / 'blockdata.bin')
        if block_hash != d['blockdata_sha256']:
            raise ValueError(f'{identifier}: blockdata provenance hash mismatch')
        exact = bool(base and block_hash == base['blockdata_sha256'])
        decision = default_decision(d, base, exact, core_ids)
        curated = rules_doc['rules'].get(identifier)
        stale_rule = False
        if curated:
            if sha(path) == curated['source_json_sha256'] and sha(path.parent / 'preview.png') == curated['preview_sha256']:
                decision.update(curated)
                decision['disposition'] = 'PRESERVE_CANARY' if identifier == '3.0' else 'SELECTED_ASSET' if decision['import_flag'] else 'MANUAL_REVIEW'
            else:
                stale_rule = True
                decision.update(canonical_flag=False, import_flag=False, confidence='LOW', disposition='MANUAL_REVIEW', reason='Source JSON or preview changed since manual decision; re-inspection required.', visual_review='STALE_RULE')
        count_issues = {kind: {'declared': d['event_counts'].get(kind), 'exported': len(d[array])}
                        for kind, array in EVENTS.items() if d['event_counts'].get(kind) != len(d[array])}
        if count_issues and decision['import_flag']:
            decision.update(import_flag=False, disposition='MANUAL_REVIEW')
            decision['reason'] += ' Declared/exported event mismatch blocks asset shortlist selection.'
        selected = decision['import_flag']
        record = {**decision, 'donor': 'BWA', 'profile': exported_manifest['profile'], 'rom_sha256': exported_manifest['rom']['sha256'],
                  'id': identifier, 'group': d['group'], 'map': d['map'], 'name': d['name'],
                  'normalized_name_family': normalized_name(d['name']), 'canonical_selection_status': 'PROVISIONAL' if identifier in {'3.1', '3.5'} else 'CONFIRMED' if decision['canonical_flag'] else 'NOT_CANONICAL',
                  'import_scope': 'VISUAL_ASSETS_ONLY' if selected else 'NONE',
                  'runtime_import_flag': False, 'relationship_import_flag': False, 'event_import_flag': False, 'script_import_flag': False,
                  'source_json': str(path.relative_to(root.parent.parent.parent)), 'source_json_sha256': sha(path),
                  'preview_sha256': sha(path.parent / 'preview.png'), 'stale_curated_rule': stale_rule,
                  'event_counts': d['event_counts'], 'exported_event_counts': {kind: len(d[array]) for kind, array in EVENTS.items()},
                  'event_count_mismatches': count_issues, 'connection_count': len(d['connections']),
                  'base_firered_slot': base, 'exact_firered_blockdata': exact,
                  'shared_layout_ids': sorted([i for i in layouts[d['layout_pointer']] if i != identifier], key=sort_id),
                  'same_visual_ids': sorted([i for i in visual_families[d.get('visual_map_sha256')] if i != identifier], key=sort_id),
                  'relationships': {'warps': d['warps'], 'connections': d['connections'], 'incoming': incoming[identifier]},
                  'pointers': json.loads(generic_row['pointers']), 'tileset_source': json.loads(generic_row['tileset_source'])}
        for key in ('width', 'height', 'map_type', 'layout_id', 'primary_tileset', 'secondary_tileset', 'header_pointer', 'layout_pointer', 'blockdata_pointer', 'visual_map_sha256', 'blockdata_sha256', 'region_map_section_id', 'region_map_section_name', 'allow_escaping', 'allow_cycling', 'weather', 'music'):
            record[key] = d.get(key)
        record['asset_dependencies'] = {
            'primary_tileset': {'id': d['primary_tileset'], 'path': str((root/'tilesets'/d['primary_tileset']).resolve()), 'import_automatically': False},
            'secondary_tileset': {'id': d['secondary_tileset'], 'path': str((root/'tilesets'/d['secondary_tileset']).resolve()), 'import_automatically': False},
            'geometry_files': [str((path.parent/filename).resolve()) for filename in ('blockdata.bin', 'border.bin', 'preview.png')],
            'excluded_from_visual_import': ['npcs.json', 'warps.json', 'coord_events.json', 'bg_events.json', 'connections.json', 'map_scripts.json', 'scripts.json']
        }
        record['map_scripts'] = d['map_scripts']
        for kind, array in EVENTS.items():
            record[kind + '_count'] = d['event_counts'].get(kind)
            record[kind + '_exported_count'] = len(d[array])
        discrepancies = {}
        original = originals[identifier]
        mapping = {'objects': d['event_counts']['object'], 'warps': d['event_counts']['warp'], 'coords': d['event_counts']['coord'], 'bg': d['event_counts']['bg'], 'map_section': d['region_map_section_id'], 'width': d['width'], 'height': d['height'], 'connections': len(d['connections'])}
        for field, actual in mapping.items():
            if str(original[field]) != str(actual):
                discrepancies[field] = {'old_report': original[field], 'map_json': actual}
        record['metadata_report_discrepancies'] = discrepancies
        correction = dict(original)
        correction.update(mapping)
        correction.update({kind + '_exported_count': len(d[array]) for kind, array in EVENTS.items()})
        correction['event_count_mismatches'] = count_issues
        corrected.append(correction)
        records.append(record)
    byid = {record['id']: record for record in records}
    for record in records:
        dependencies = []
        blockers = []
        for kind, edges in [('WARP', record['relationships']['warps']), ('CONNECTION', record['relationships']['connections'])]:
            for index, edge in enumerate(edges):
                target = edge.get('target_id')
                dest = byid.get(target)
                dynamic = bool(edge.get('dynamic_target'))
                status = 'DYNAMIC_RUNTIME_TARGET' if dynamic else dest['disposition'] if dest else 'MISSING_EXPORTED_TARGET'
                dep = {'kind': kind, 'index': index, 'target': target, 'target_disposition': status, 'target_category': dest['category'] if dest else None,
                       'destination_warp_id': edge.get('dest_warp_id'), 'action': 'DEFER_AND_REMAP', 'import_automatically': False}
                if dynamic:
                    dep['action'] = 'REBUILD_DYNAMIC_RETURN_LOGIC'
                if kind == 'WARP' and dest and not dynamic:
                    warp_id = edge.get('dest_warp_id')
                    if not isinstance(warp_id, int) or not 0 <= warp_id < dest['warp_exported_count']:
                        dep['exported_destination_index_issue'] = True
                dependencies.append(dep)
                if status not in {'SELECTED_ASSET', 'PRESERVE_CANARY'} or dep.get('exported_destination_index_issue'):
                    blockers.append(dep)
        record['dependencies'] = dependencies
        record['wiring_blockers'] = blockers
        record['gameplay_blockers'] = ['Donor IDs require destination remapping; no donor relationships may be copied automatically.',
                                       'FireRed event scripts and NPC graphics are pointer metadata, not validated runnable Emerald content.']
        if blockers:
            record['gameplay_blockers'].append('One or more relationships point to excluded, ambiguous, dynamic, missing or truncated destination records.')
        if record['event_count_mismatches']:
            record['gameplay_blockers'].append('Declared/exported event counts differ.')
    families = []
    for name, identifiers in sorted(names.items()):
        if len(identifiers) < 2:
            continue
        members = [byid[i] for i in sorted(identifiers, key=sort_id)]
        families.append({'normalized_name': name, 'members': [{'id': m['id'], 'name': m['name'], 'width': m['width'], 'height': m['height'],
                        'category': m['category'], 'canonical_flag': m['canonical_flag'], 'import_flag': m['import_flag'], 'role': m['role'],
                        'disposition': m['disposition'], 'reason': m['reason'], 'layout_pointer': m['layout_pointer'], 'visual_map_sha256': m['visual_map_sha256']} for m in members],
                        'canonical_members': [m['id'] for m in members if m['canonical_flag']],
                        'resolution': 'Multiple canonical members represent separate sectors/rooms, never name-based deduplication. Alternatives and legacy members remain individually quarantined.'})
    selected = [r['id'] for r in records if r['import_flag']]
    excluded = [r['id'] for r in records if r['disposition'] == 'EXCLUDED_LEGACY']
    review = [r['id'] for r in records if r['disposition'] == 'MANUAL_REVIEW']
    canary = [r['id'] for r in records if r['disposition'] == 'PRESERVE_CANARY']
    spine_ids = [r['id'] for r in records if r['canonical_flag'] and r['category'] == 'WORLD']
    source_info = {label: {'path': str(path), 'sha256': sha(path)} for label, path in [('export_manifest', root/'manifest.json'), ('metadata_csv', report_csv), ('metadata_markdown', report_md), ('curated_rules', rules_path), ('firered_reference', reference_path)]}
    manifest = {'schema_version': '1.0', 'donor': 'BWA', 'region': 'UNOVA', 'profile': exported_manifest['profile'], 'rom_sha256': exported_manifest['rom']['sha256'],
                'execution_allowed': False, 'bulk_import_allowed': False, 'destination_writes_performed': False,
                'import_flag_semantics': 'Select high-confidence, visually inspected asset candidates for a future VISUAL_ASSETS_ONLY import. This is not a runnable import plan or authorization to execute. All events/scripts/relationships remain disabled.',
                'canonical_flag_semantics': 'Chosen donor-local regional sector/interior. Distinct sectors may share a name. Accumula and Nimbasa are provisional and not selected for import.',
                'canary_policy': {'BWA': 'Preserve validated 3.0 Nuvema working import; never overwrite.', 'SWSH': 'Postwick untouched; SWSH is outside this run.'},
                'sources': source_info, 'firered_reference': {'url': f'https://github.com/pret/pokefirered/blob/{REFERENCE_COMMIT}/data/maps/map_groups.json', 'commit': REFERENCE_COMMIT,
                'method': 'Slot ancestry plus SHA-256 of raw little-endian map blockdata compared with the pinned reference layout map.bin. Exact geometry is not proof that donor labels/scripts/events are unchanged.'},
                'summary': {'usable_maps': len(records), 'exact_firered_blockdata_matches': sum(r['exact_firered_blockdata'] for r in records), 'categories': dict(Counter(r['category'] for r in records)), 'dispositions': dict(Counter(r['disposition'] for r in records)),
                            'event_count_mismatch_maps': sum(bool(r['event_count_mismatches']) for r in records)},
                'lists': {'high_confidence_import': selected, 'excluded_legacy': excluded, 'manual_review': review, 'preserve_canary': canary},
                'canonical_region_spine': {'nodes': [{'id': i, 'name': byid[i]['name'], 'role': byid[i]['role'], 'confidence': byid[i]['confidence'], 'selection_status': byid[i]['canonical_selection_status'], 'import_flag': byid[i]['import_flag']} for i in spine_ids],
                    'internal_relationships': [rel for rel in relationships if rel['source'] in spine_ids and rel['target'] in spine_ids],
                    'boundary_relationships': [rel for rel in relationships if rel['source'] in spine_ids and rel['target'] not in spine_ids],
                    'notes': ['Source topology is preserved, not assumed to match official Unova geography.', 'No canonical Route 6 or later-route Unova assignment is invented.', 'No Cold Storage or Victory Road floors are selected: their floor geometry matches FireRed Mt Moon / Victory Road.', 'Dreamyard and Pinwheel Forest are supported outdoor dungeon features; unnamed cave 1.122 remains manual review.']},
                'duplicate_name_families': families, 'maps': records}
    manifest['observed_destination_imports'] = audit_destination_imports(records, rules_doc.get('destination_verifications', {}))
    manifest['remaining_asset_candidates'] = [r['id'] for r in records if r['import_flag'] and not r.get('already_imported')]
    validate_manifest(manifest)
    return manifest, corrected

def validate_manifest(manifest):
    maps = manifest['maps']
    ids = {r['id'] for r in maps}
    assert len(maps) == len(ids) == 444
    partition = [i for values in manifest['lists'].values() for i in values]
    assert len(partition) == len(set(partition)) == 444 and set(partition) == ids
    assert not manifest['execution_allowed'] and not manifest['bulk_import_allowed']
    for record in maps:
        assert record['category'] in CATEGORY_NAMES
        assert not any(record[k] for k in ('runtime_import_flag', 'event_import_flag', 'script_import_flag', 'relationship_import_flag'))
        if record['import_flag']:
            assert record['canonical_flag'] and record['confidence'] == 'HIGH' and record['visual_review'] == 'PASS'
            assert not record['event_count_mismatches'] and record['disposition'] == 'SELECTED_ASSET'
        if record['disposition'] == 'EXCLUDED_LEGACY':
            assert not record['import_flag'] and not record['canonical_flag']
    canary = next(r for r in maps if r['id'] == '3.0')
    assert canary['canonical_flag'] and not canary['import_flag'] and canary['disposition'] == 'PRESERVE_CANARY'

def audit_destination_imports(records, user_verifications=None):
    """Observe existing imports without changing maps or claiming gameplay validation."""
    user_verifications = user_verifications or {}
    layouts_path = REPO / 'data/layouts/layouts.json'
    groups_path = REPO / 'data/maps/map_groups.json'
    if not layouts_path.exists() or not groups_path.exists():
        return []
    layouts = {item.get('id'): item for item in json.loads(layouts_path.read_text())['layouts']}
    groups = json.loads(groups_path.read_text())
    registered = {name for values in groups.values() if isinstance(values, list) for name in values}
    byid = {record['id']: record for record in records}
    observations = []
    for path in sorted((REPO / 'data/maps').glob('AMap_*/map.json')):
        destination = json.loads(path.read_text())
        provenance = destination.get('amap_batch_bridge', {})
        record = byid.get(provenance.get('map_id'))
        if not record or provenance.get('rom_sha256') != record['rom_sha256']:
            continue
        layout = layouts.get(destination.get('layout'), {})
        blob = REPO / layout.get('blockdata_filepath', '__missing__')
        objects = destination.get('object_events', [])
        local_ids = Counter(str(obj.get('local_id')) for obj in objects)
        duplicates = sorted(identifier for identifier, count in local_ids.items() if count > 1)
        geometry_match = blob.is_file() and sha(blob) == record['blockdata_sha256']
        dimension_match = (layout.get('width'), layout.get('height')) == (record['width'], record['height'])
        issues = []
        if destination.get('map_type') == 'MAP_TYPE_NONE':
            issues.append('Destination map type remains MAP_TYPE_NONE.')
        if duplicates:
            issues.append('Duplicate object local IDs: ' + ', '.join(duplicates))
        if not geometry_match or not dimension_match:
            issues.append('Destination geometry differs from classified source.')
        if destination.get('name') not in registered:
            issues.append('Destination map is not registered in map_groups.json.')
        observation = {
            'donor_id': record['id'], 'destination_map': destination.get('name'),
            'destination_map_id': destination.get('id'), 'destination_path': str(path.relative_to(REPO)),
            'destination_json_sha256': sha(path), 'layout_id': destination.get('layout'),
            'registered': destination.get('name') in registered,
            'dimensions_match': dimension_match, 'blockdata_matches': geometry_match,
            'map_type': destination.get('map_type'), 'object_count': len(objects),
            'duplicate_object_local_ids': duplicates,
            'active_connection_count': len(destination.get('connections') or []),
            'active_warp_count': len(destination.get('warp_events', [])),
            'pending_connection_count': len(destination.get('amap_pending_connections', [])),
            'pending_warp_count': len(destination.get('amap_pending_warps', [])),
            'active_connections': destination.get('connections') or [],
            'active_warps': destination.get('warp_events', []),
            'gameplay_validated_by_this_audit': False, 'issues': issues,
            'status': 'PRESERVE_VALIDATED_CANARY' if record.get('disposition') == 'PRESERVE_CANARY' else 'IMPORTED_PENDING_GAMEPLAY_VALIDATION',
            'import_action': 'SKIP_EXISTING_IMPORT', 'reimport_flag': False,
        }
        reported = user_verifications.get(record['id'])
        if reported:
            current_layout_hash = hashlib.sha256(compact(layout).encode()).hexdigest()
            matches = (reported.get('destination_json_sha256') == observation['destination_json_sha256']
                       and blob.is_file() and reported.get('blockdata_sha256') == sha(blob)
                       and reported.get('layout_definition_sha256') == current_layout_hash)
            observation['user_gameplay_verification'] = {**reported, 'matches_current_import': matches}
            observation['status'] = 'GAME_TESTED_VERIFIED_BY_USER' if matches else 'USER_VERIFICATION_STALE_RECHECK_REQUIRED'
        record.update(already_imported=True, import_action='SKIP_EXISTING_IMPORT', reimport_flag=False, destination_import=observation)
        observations.append(observation)
    for record in records:
        record.setdefault('already_imported', False)
        record.setdefault('import_action', 'CANDIDATE_ONLY_NO_EXECUTION' if record['import_flag'] else 'DO_NOT_IMPORT')
        record.setdefault('reimport_flag', False)
    return observations

def write_outputs(manifest, corrected, out):
    out.mkdir(parents=True, exist_ok=True)
    (out/'bwa_unova_import_manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    fields = ['already_imported', 'import_action', 'reimport_flag', 'donor', 'id', 'group', 'map', 'name', 'category', 'canonical_flag', 'import_flag', 'confidence', 'disposition', 'role', 'reason', 'width', 'height', 'object_count', 'object_exported_count', 'warp_count', 'warp_exported_count', 'coord_count', 'coord_exported_count', 'bg_count', 'bg_exported_count', 'connection_count', 'primary_tileset', 'secondary_tileset', 'header_pointer', 'layout_pointer', 'exact_firered_blockdata', 'shared_layout_ids', 'same_visual_ids', 'dependencies', 'wiring_blockers', 'source_json', 'source_json_sha256']
    for key, filename in [('high_confidence_import','bwa_unova_high_confidence_import.csv'), ('excluded_legacy','bwa_unova_excluded_legacy.csv'), ('manual_review','bwa_unova_manual_review.csv')]:
        wanted = set(manifest['lists'][key])
        csv_write(out/filename, [r for r in manifest['maps'] if r['id'] in wanted], fields)
    csv_write(out/'bwa_unova_inventory.csv', manifest['maps'], fields)
    csv_write(out/'bwa_donor_map_metadata_corrected.csv', corrected, list(corrected[0]))
    summary = manifest['summary']
    text = ['# BWA / Unova review', '', 'Scope: all 444 BWA maps. No imports, destination writes, or SWSH classification. Nuvema and Postwick working imports remain untouched.', '',
            '**The import list selects visual assets only. It must not execute donor scripts, copy NPCs, or wire donor warps/connections. All gameplay import flags are false.**', '',
            f"{len(manifest['lists']['high_confidence_import'])} high-confidence visual asset candidates; {len(manifest['lists']['excluded_legacy'])} legacy exclusions; {len(manifest['lists']['manual_review'])} manual-review maps; 1 protected canary.", '',
            f"{summary['exact_firered_blockdata_matches']} map blockdata hashes match their pinned FireRed reference slots exactly. This establishes inherited geometry, not unchanged donor events or intended gameplay. Exclusions quarantine legacy geometry; nothing is deleted.", '',
            f"Reference: [pret/pokefirered, {REFERENCE_COMMIT[:12]}](https://github.com/pret/pokefirered/tree/{REFERENCE_COMMIT}). Offline reference hashes/slot ancestry are bundled with the classifier.", '', '## Canonical donor region spine', '', '| ID | Feature / role | Decision |', '|---|---|---|']
    byid = {r['id']: r for r in manifest['maps']}
    for node in manifest['canonical_region_spine']['nodes']:
        r = byid[node['id']]
        text.append(f"| {r['id']} | {r['name']} / {r['role']} | {r['disposition']} ({r['confidence']}) |")
    text += ['', 'Core connected run: Nuvema -> Route 1 -> Accumula -> Route 2 -> Striaton -> Route 3 west/east -> Nacrene -> Pinwheel approach/inner forest -> Castelia. Actual donor edges, including direction and warp records, are retained in JSON; this is not an asserted official-game progression.', '',
             'Castelia main/docks/waterfront/north street are distinct sectors. Route 4 desert and Route 5 exterior are edited candidates. Nimbasa and Driftveil remain separate donor features with inherited links; do not invent a clean connected Unova progression where the source lacks one.', '',
             '## Family decisions and exclusions', '',
             '- **Nuvema:** 3.0 is the protected validated canary. 4.4 is an alternate outdoor revision. Active canary house/lab relationships are preserved; no replacement.',
             '- **Accumula:** 3.1 remains a provisional graph default, not an import candidate: its preview repeats town geometry. 5.6/42.1/42.2/42.3 are distinct revisions. 5.6 and 42.3 share visual/blockdata hashes but differ in script/coord records; 42.3 is unexpectedly reached from Nacrene.',
             '- **Route 3:** 3.21 and 3.22 are separate connected sectors, not competing duplicates. Route-number labels alone are insufficient: 3.22 occupies the old Route 4 slot.',
             '- **Castelia:** 1.30, 3.4, 3.45 and 3.46 are retained sectors. 1.32/1.33/1.35 reuse the exact 1.30 visuals but retain inherited tunnel/gate relationships; quarantine them. The renamed 1.47-1.58 family retains Silph Co floor geometry.',
             '- **Dreamyard:** 39.0 is the active Striaton-linked ruins exterior. 44.3 is an orphan alternate; mislabeled 46.0 also shows ruins. 1.4-1.29 retain the SS Anne layouts and are excluded legacy geometry.',
             '- **Pinwheel:** 1.95 and 1.114 are distinct supported forest segments. 44.1/44.2 are duplicate blank previews with event-count mismatches, not usable additional forest sectors.',
             '- **Cold Storage / Victory Road:** 1.1-1.3 are exact Mt Moon floors; 1.39-1.41 are exact FireRed Victory Road floors. No genuine Unova replacement is established.',
             '- **Later routes and islands:** stock blockdata identifies inherited Kanto/Sevii routes, towns, dungeons and their host interiors. Do not promote them simply because core maps reference them.',
             '- **Desert 17.1 / gate 18.0:** identical layout pointer and visual/blockdata hash, different types and event/warp roles. Manual selection required.',
             '- **Nimbasa 3.5:** canonical donor slot is provisional; blank green preview blocks import. Unnamed edited cave 1.122 is dungeon review, not a named Unova dungeon assignment.',
             '- **Utilities/tests:** 0.0-0.4 are inherited link facilities; 43.0 is a portrait/cutscene panel. 3.50-3.53 are inherited prototypes; 7.5 is only a possible test/staging map. Empty rooms alone are not declared debug maps.', '',
             '## Counts and dependency safety', '',
             'Corrected BWA metadata is in bwa_donor_map_metadata_corrected.csv. All 444 object counts come from event_counts.object; npcs lengths are preserved separately. The original combined reports are retained as provenance, and SWSH rows are untouched.', '',
             f"{summary['event_count_mismatch_maps']} maps have declared/exported count mismatches. Nuvema BG=6/5, Route 1 coord=3/2, desert gate 1.0 BG=8/3, alternate Nuvema 4.4 BG=1/0, and 44.1/44.2 warp=6/3 and BG=8/3.", '',
             'Every outgoing warp/connection has a target disposition and a deferred remapping action. Incoming links, dynamic returns, missing/truncated destination indices, layout sharing and visual duplicates are retained. Visual asset selection does not recursively select legacy dependencies. Runnable world migration remains blocked pending destination mapping and script/event implementation.', '',
             '## Files', '',
             '- bwa_unova_import_manifest.json: complete inventory, provenance, family resolutions, spine and relationship records.',
             '- bwa_unova_high_confidence_import.csv: selected visual assets; all gameplay migration disabled.',
             '- bwa_unova_excluded_legacy.csv: quarantined inherited geometry/host families.',
             '- bwa_unova_manual_review.csv: unresolved revisions, identities, render problems and event issues.',
             '- bwa_unova_inventory.csv: all 444 decisions.', '',
             'BWA review is complete for this phase. Remaining uncertainties are recorded explicitly; SWSH/Galar has not been advanced.']
    imported = [item for item in manifest.get('observed_destination_imports', []) if item['donor_id'] != '3.0']
    text += ['', '## Observed destination imports', '',
             'Existing imports are skipped on future passes. Matching exported blockdata is not gameplay validation. The protected Nuvema canary keeps its prior validation status.', '',
             '| Donor ID | Destination | Geometry | Status | Metadata notes |', '|---|---|---|---|---|']
    verified = [item['donor_id'] for item in imported if item['status'] == 'GAME_TESTED_VERIFIED_BY_USER']
    if verified:
        text += ['User-reported game testing is recorded for: ' + ', '.join(verified) + '. Verification is tied to destination JSON, blockdata and layout-definition hashes; changes require rechecking. Metadata notes and pending external links do not negate the reported testing of the imported stretch.', '']
    for item in imported:
        text.append(f"| {item['donor_id']} | {item['destination_map']} | {'matches' if item['blockdata_matches'] and item['dimensions_match'] else 'REVIEW'} | {item['status']} | {'; '.join(item['issues']) or 'none'} |")
    csv_write(out/'bwa_unova_import_status.csv', manifest.get('observed_destination_imports', []),
              ['donor_id', 'destination_map', 'status', 'import_action', 'reimport_flag', 'registered', 'dimensions_match', 'blockdata_matches', 'map_type', 'object_count', 'duplicate_object_local_ids', 'active_connection_count', 'active_warp_count', 'pending_connection_count', 'pending_warp_count', 'user_gameplay_verification', 'issues'])
    (out/'bwa_unova_review.md').write_text('\n'.join(text)+'\n', encoding='utf-8')
    (out/'bwa_donor_map_metadata_corrected.md').write_text('# Corrected BWA metadata\n\n444 maps. Object counts use event_counts.object; exported objects use len(npcs).\n\nAll declared and exported event counts, section IDs and original source identities are in bwa_donor_map_metadata_corrected.csv. Six maps have array/count mismatches. Original combined donor reports and SWSH rows remain unchanged.\n', encoding='utf-8')
    print(compact(summary))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=REPO/'.la_work/amap/bwa_full_v11')
    parser.add_argument('--metadata-csv', type=Path, default=REPO/'.la_work/amap/donor_map_metadata_report.csv')
    parser.add_argument('--metadata-md', type=Path, default=REPO/'.la_work/amap/donor_map_metadata_report.md')
    parser.add_argument('--rules', type=Path, default=HERE/'bwa_unova_rules.json')
    parser.add_argument('--reference', type=Path, default=HERE/'firered_map_reference.json')
    parser.add_argument('--out', type=Path, default=REPO/'.la_work/amap/bwa_unova_review')
    args = parser.parse_args()
    protected = [args.root.resolve(), (REPO/'.la_work/amap/swsh_full_v11').resolve()]
    for path in protected:
        if args.out.resolve() == path or path in args.out.resolve().parents or args.out.resolve() in path.parents:
            parser.error('Output must be separate from donor exports')
    if args.out.resolve() == HERE or HERE in args.out.resolve().parents:
        parser.error('Output must be separate from classifier source')
    manifest, corrected = build(args.root, args.metadata_csv, args.metadata_md, args.rules, args.reference)
    write_outputs(manifest, corrected, args.out)

if __name__ == '__main__':
    main()
