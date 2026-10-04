#!/usr/bin/env python3
"""Inventory all 701 SWSH maps and build a non-executable Galar asset manifest.

FireRed reference hashes and manual decisions are offline, donor-scoped evidence.
Canonical roles are descriptive donor roles, not invented official sector names.
No exports, destination maps, canaries or BWA reports are written by this tool.
"""
import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict, deque
from pathlib import Path
from classify_donor_maps import inventory, compact, EVENTS
from build_bwa_unova_manifest import csv_write, sort_id, sha

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
CATEGORIES = ('WORLD', 'INTERIOR', 'CAVE_DUNGEON', 'TRANSITION', 'UTILITY', 'DEBUG_TEST', 'STALE_UNKNOWN')
TOWNS = {'postwick', 'wedgehurst', 'motostoke', 'turffield', 'hulbury', 'hammerlocke', 'stow on side', 'ballonlea', 'circhester', 'spikemuth', 'wyndon'}
REFERENCE_COMMIT = '037335f4c725d7c9aecdac87066f2002b4bd7e14'

def name_family(name):
    return ' '.join(name.lower().split())

def automatic_decision(d, base, exact, core_ids):
    typ = d['map_type']
    category = 'WORLD' if typ in {1, 2, 3, 6} else 'CAVE_DUNGEON' if typ in {4, 5} else 'INTERIOR' if typ in {8, 9} else 'STALE_UNKNOWN'
    result = {'category': category, 'canonical_flag': False, 'import_flag': False, 'confidence': 'LOW',
              'reason': 'Semantic identity unresolved; donor name/type alone is insufficient for canonical selection.',
              'role': 'unresolved', 'visual_review': 'NOT_REVIEWED', 'major_dungeon': False, 'disposition': 'MANUAL_REVIEW'}
    targets = {e.get('target_id') for e in d['warps'] + d['connections']}
    if exact:
        if d['group'] == 3 and base['name'].startswith('Prototype_'):
            result.update(category='DEBUG_TEST', role='legacy.prototype')
        elif d['group'] == 0 and d['map'] < 5:
            result.update(category='UTILITY', role='legacy.link_facility')
        elif d['group'] not in {0, 1, 2, 3} and (name_family(d['name']) in TOWNS or targets & core_ids):
            result.update(confidence='MEDIUM', reason='Exact FireRed room geometry reused in a named/core-linked donor family; possible intended reuse, not safe to select or discard solely by hash.', role='core.reused_room_candidate')
            return result
        result.update(confidence='HIGH', disposition='EXCLUDED_LEGACY',
                      reason='Exact blockdata SHA-256 match to FireRed slot ' + base['name'] + '; quarantine inherited geometry despite donor label. This does not assert identical scripts/events.')
        return result
    if d['width'] * d['height'] <= 1:
        result.update(category='STALE_UNKNOWN', confidence='HIGH', role='placeholder.degenerate', reason='Degenerate 1x1 export; no usable region geometry. Retained for review, never imported.')
    elif any(count >= 200 for count in d['event_counts'].values()):
        result.update(category='STALE_UNKNOWN', confidence='HIGH', role='invalid_event_metadata', reason='Implausible declared event counts and/or empty exported arrays; metadata requires repair before semantic selection.')
    elif typ == 0 and d['connections'] and d['width'] * d['height'] >= 600:
        result.update(category='WORLD', confidence='MEDIUM', role='outdoor.unspecified_candidate', reason='Large connected typeless layout suggests outdoor geometry; name/region/preview still unresolved.')
    elif typ == 8 and (name_family(d['name']) in TOWNS or targets & core_ids):
        result.update(confidence='MEDIUM', role='core.interior_candidate', reason='Indoor metadata with named or direct core-town relationships; preview and exact room identity not yet validated.')
    if d['warps'] and all(e.get('dynamic_target') for e in d['warps']) and d['width'] * d['height'] < 1000:
        result.update(category='UTILITY', confidence='MEDIUM', role='utility.dynamic_return', reason='Only dynamic-return warps; utility/elevator/link-room candidate, not standalone geography.')
    if base and ('Entrance' in base['name'] or 'Tunnel' in base['name']) and result['category'] == 'INTERIOR':
        result.update(category='TRANSITION', role='transition.inherited_candidate')
    return result

def region_hints(data, core_regions):
    """Weak distance hints for fallback names; never select maps from these alone."""
    neighbors = defaultdict(set)
    for i, d in data.items():
        for edge in d['warps'] + d['connections']:
            target = edge.get('target_id')
            if target in data and not edge.get('dynamic_target'):
                neighbors[i].add(target)
                neighbors[target].add(i)
    hints = defaultdict(set)
    for seed, region in core_regions.items():
        queue = deque([(seed, 0)])
        seen = {seed}
        while queue:
            node, distance = queue.popleft()
            if distance:
                hints[node].add(region)
            if distance == 2:
                continue
            for target in neighbors[node]:
                if target not in seen and (target not in core_regions or target == seed):
                    seen.add(target)
                    queue.append((target, distance + 1))
    return {i: sorted(values) for i, values in hints.items()}

def build(root, metadata_csv, metadata_md, rules_path, reference_path):
    rules_doc = json.loads(rules_path.read_text())
    reference_doc = json.loads(reference_path.read_text())
    export = json.loads((root/'manifest.json').read_text())
    if export['profile'] != rules_doc['profile'] or export['rom']['sha256'] != rules_doc['rom_sha256']:
        raise ValueError('SWSH curated decisions do not match donor profile/ROM hash')
    if reference_doc['commit'] != REFERENCE_COMMIT:
        raise ValueError('Unexpected FireRed reference revision')
    old_rows = {}
    with metadata_csv.open(encoding='utf-8-sig', newline='') as stream:
        for row in csv.DictReader(stream):
            if row['donor'] == 'SWSH':
                i = f"{int(row['group'])}.{int(row['map'])}"
                if i in old_rows:
                    raise ValueError('Duplicate SWSH metadata row: ' + i)
                old_rows[i] = row
    md = metadata_md.read_text(encoding='utf-8-sig')
    if 'SWSH' not in md or '701' not in md:
        raise ValueError('Metadata Markdown does not describe validated SWSH inventory')
    generic = inventory('SWSH', root)
    data = {row['id']: json.loads(Path(row['source_json']).read_text()) for row in generic}
    if len(data) != 701 or set(old_rows) != set(data):
        raise ValueError('Expected exactly 701 usable SWSH maps in exports and metadata report')
    if not set(rules_doc['rules']) <= set(data):
        raise ValueError('Rule references absent SWSH map')
    core_ids = {i for i, rule in rules_doc['rules'].items() if rule['canonical_flag'] and rule['category'] == 'WORLD'}
    town_seeds = {i: rule['role'].split('.')[0] for i, rule in rules_doc['rules'].items() if rule['canonical_flag'] and rule['role'].endswith('.main') and rule['role'].split('.')[0].replace('_', ' ') in TOWNS}
    hints = region_hints(data, town_seeds)
    incoming = defaultdict(list)
    edges = []
    layouts, visuals, blocks, families = (defaultdict(list) for _ in range(4))
    for i, d in data.items():
        layouts[d['layout_pointer']].append(i)
        visuals[d['visual_map_sha256']].append(i)
        blocks[d['blockdata_sha256']].append(i)
        families[name_family(d['name'])].append(i)
        for kind, values in [('WARP', d['warps']), ('CONNECTION', d['connections'])]:
            for n, edge in enumerate(values):
                relationship = {'source': i, 'kind': kind, 'index': n, 'target': edge.get('target_id'), 'dynamic_target': bool(edge.get('dynamic_target')), 'donor_record': edge}
                incoming[edge.get('target_id')].append(relationship)
                edges.append(relationship)
    records, corrected = [], []
    for row in generic:
        i = row['id']
        d = data[i]
        path = Path(row['source_json'])
        if sha(path.parent/'blockdata.bin') != d['blockdata_sha256']:
            raise ValueError(i + ': exported blockdata hash differs from map JSON')
        base = reference_doc['maps'].get(i)
        exact = bool(base and base['blockdata_sha256'] == d['blockdata_sha256'])
        decision = automatic_decision(d, base, exact, core_ids)
        rule = rules_doc['rules'].get(i)
        if rule:
            if rule['source_json_sha256'] == sha(path) and rule['preview_sha256'] == sha(path.parent/'preview.png'):
                decision.update(rule)
                decision['disposition'] = rule.get('disposition', 'SELECTED_ASSET' if decision['import_flag'] else 'MANUAL_REVIEW')
            else:
                if i == '3.0':
                    raise ValueError('Postwick canary metadata/preview changed; re-inspection required, no replacement permitted')
                decision.update(canonical_flag=False, import_flag=False, confidence='LOW', visual_review='STALE_RULE', disposition='MANUAL_REVIEW', reason='Source JSON or preview changed after manual decision; re-inspection required.')
        mismatch = {kind: {'declared': d['event_counts'][kind], 'exported': len(d[array])} for kind, array in EVENTS.items() if d['event_counts'][kind] != len(d[array])}
        if mismatch and decision['import_flag']:
            decision.update(import_flag=False, disposition='MANUAL_REVIEW')
            decision['reason'] += ' Declared/exported event mismatch blocks the high-confidence asset list.'
        record = {**decision, 'donor': 'SWSH', 'profile': export['profile'], 'rom_sha256': export['rom']['sha256'], 'id': i, 'group': d['group'], 'map': d['map'], 'name': d['name'],
                  'name_family': name_family(d['name']), 'nearby_region_hints': hints.get(i, []),
                  'canonical_selection_status': decision.get('canonical_selection_status', 'CONFIRMED' if decision['canonical_flag'] else 'NOT_CANONICAL'),
                  'import_scope': 'VISUAL_ASSETS_ONLY' if decision['import_flag'] else 'NONE', 'runtime_import_flag': False, 'event_import_flag': False, 'script_import_flag': False, 'relationship_import_flag': False,
                  'event_counts': d['event_counts'], 'exported_event_counts': {kind: len(d[array]) for kind, array in EVENTS.items()}, 'event_count_mismatches': mismatch,
                  'connection_count': len(d['connections']), 'map_scripts': d['map_scripts'],
                  'source_json': str(path.resolve()), 'source_json_sha256': sha(path), 'preview_sha256': sha(path.parent/'preview.png'),
                  'pointers': json.loads(row['pointers']), 'tileset_source': json.loads(row['tileset_source']),
                  'base_firered_slot': base, 'exact_firered_blockdata': exact,
                  'shared_layout_ids': sorted([peer for peer in layouts[d['layout_pointer']] if peer != i], key=sort_id),
                  'same_visual_ids': sorted([peer for peer in visuals[d['visual_map_sha256']] if peer != i], key=sort_id),
                  'same_blockdata_ids': sorted([peer for peer in blocks[d['blockdata_sha256']] if peer != i], key=sort_id),
                  'relationships': {'warps': d['warps'], 'connections': d['connections'], 'incoming': incoming[i]},
                  'asset_dependencies': {'primary_tileset': d['primary_tileset'], 'secondary_tileset': d['secondary_tileset'], 'map_folder': str(path.parent), 'import_automatically': False, 'excluded_from_visual_import': list(EVENTS.values()) + ['map_scripts', 'connections', 'scripts']}}
        for key in ('width', 'height', 'map_type', 'layout_id', 'primary_tileset', 'secondary_tileset', 'header_pointer', 'layout_pointer', 'blockdata_pointer', 'region_map_section_id', 'region_map_section_name', 'visual_map_sha256', 'blockdata_sha256', 'allow_escaping', 'allow_cycling', 'weather', 'music'):
            record[key] = d.get(key)
        for kind, array in EVENTS.items():
            record[kind+'_count'] = d['event_counts'][kind]
            record[kind+'_exported_count'] = len(d[array])
        original = old_rows[i]
        values = {'objects': d['event_counts']['object'], 'warps': d['event_counts']['warp'], 'coords': d['event_counts']['coord'], 'bg': d['event_counts']['bg'], 'connections': len(d['connections']), 'map_section': d['region_map_section_id'], 'width': d['width'], 'height': d['height']}
        record['metadata_report_discrepancies'] = {key: {'old_report': original[key], 'map_json': value} for key, value in values.items() if str(original[key]) != str(value)}
        correction = {**original, **values, **{kind+'_exported_count': len(d[array]) for kind, array in EVENTS.items()}, 'event_count_mismatches': mismatch}
        corrected.append(correction)
        records.append(record)
    byid = {record['id']: record for record in records}
    for record in records:
        dependencies = []
        for kind, values in [('WARP', record['relationships']['warps']), ('CONNECTION', record['relationships']['connections'])]:
            for n, edge in enumerate(values):
                target = edge.get('target_id')
                dest = byid.get(target)
                dynamic = bool(edge.get('dynamic_target'))
                status = 'DYNAMIC_RUNTIME_TARGET' if dynamic else dest['disposition'] if dest else 'MISSING_EXPORTED_TARGET'
                dependency = {'kind': kind, 'index': n, 'target': target, 'target_disposition': status, 'canonical_target_hint': dest.get('canonical_replacement') if dest else None,
                              'destination_warp_id': edge.get('dest_warp_id'), 'import_automatically': False, 'action': 'REBUILD_DYNAMIC_RETURN_LOGIC' if dynamic else 'DEFER_AND_REMAP'}
                if kind == 'WARP' and dest and not dynamic:
                    index = edge.get('dest_warp_id')
                    dependency['exported_destination_index_issue'] = not isinstance(index, int) or not 0 <= index < dest['warp_exported_count']
                dependencies.append(dependency)
        record['dependencies'] = dependencies
        record['wiring_blockers'] = [dep for dep in dependencies if dep['target_disposition'] not in {'SELECTED_ASSET', 'PRESERVE_CANARY'} or dep.get('exported_destination_index_issue')]
        record['gameplay_blockers'] = ['Destination IDs and donor connections/warps require explicit remapping.', 'FireRed NPC graphics/scripts are not validated runnable Emerald content.']
        if record['event_count_mismatches']:
            record['gameplay_blockers'].append('Declared event counts differ from exported arrays.')
        if record['canonical_selection_status'] == 'PROVISIONAL':
            record['gameplay_blockers'].append('Canonical feature identity/geometry still needs review.')
    normalized_edges = []
    spine_ids = {record['id'] for record in records if record['canonical_flag'] and record['category'] in {'WORLD', 'CAVE_DUNGEON'}}
    for edge in edges:
        if edge['source'] not in spine_ids:
            continue
        target = byid.get(edge['target'])
        normalized = target.get('canonical_replacement', edge['target']) if target else edge['target']
        normalized_edges.append({**edge, 'normalized_target_hint': normalized, 'requires_alias_remapping': normalized != edge['target'], 'normalization_executed': False})
    family_records = []
    for name, ids in sorted(families.items()):
        if len(ids) < 2:
            continue
        members = [byid[i] for i in sorted(ids, key=sort_id)]
        family_records.append({'normalized_name': name, 'member_count': len(members), 'canonical_members': [member['id'] for member in members if member['canonical_flag']],
                               'members': [{key: member.get(key) for key in ('id', 'name', 'width', 'height', 'category', 'canonical_flag', 'import_flag', 'confidence', 'role', 'disposition', 'canonical_replacement', 'nearby_region_hints', 'reason', 'layout_pointer', 'visual_map_sha256')} for member in members],
                               'resolution': 'Separate rooms/sectors remain separate. Superseded town revisions have explicit replacement hints. Region-distance hints never justify importing or name-based deduplication.'})
    sources = {label: {'path': str(path.resolve()), 'sha256': sha(path)} for label, path in [('export_manifest', root/'manifest.json'), ('metadata_csv', metadata_csv), ('metadata_markdown', metadata_md), ('curated_rules', rules_path), ('firered_reference', reference_path)]}
    lists = {'high_confidence_import': [r['id'] for r in records if r['disposition'] == 'SELECTED_ASSET'], 'excluded_legacy': [r['id'] for r in records if r['disposition'] == 'EXCLUDED_LEGACY'],
             'excluded_superseded': [r['id'] for r in records if r['disposition'] == 'EXCLUDED_SUPERSEDED'], 'manual_review': [r['id'] for r in records if r['disposition'] == 'MANUAL_REVIEW'], 'preserve_canary': ['3.0']}
    manifest = {'schema_version': '1.0', 'donor': 'SWSH', 'region': 'GALAR', 'profile': export['profile'], 'rom_sha256': export['rom']['sha256'], 'execution_allowed': False, 'bulk_import_allowed': False, 'destination_writes_performed': False,
                'import_flag_semantics': 'Future visually reviewed asset selection only. No executable gameplay plan, no recursive dependencies, no scripts/events/relationships imported.',
                'canonical_flag_semantics': 'Chosen donor-local sector or feature. Provisional features remain outside the import list; descriptive sector roles are not official names.',
                'canary_policy': 'Preserve existing validated SWSH 3.0 Postwick import. Never replace it with 4.6 or other revisions. BWA/Nuvema and the user-verified BWA stretch are outside this run.',
                'sources': sources, 'firered_reference': {'commit': REFERENCE_COMMIT, 'url': f'https://github.com/pret/pokefirered/tree/{REFERENCE_COMMIT}', 'method': 'Compare same-slot raw map.bin/blockdata SHA-256 and preserve ancestry; exact geometry does not prove identical scripts or intended repurposing.'},
                'summary': {'usable_maps': len(records), 'exact_firered_blockdata_matches': sum(r['exact_firered_blockdata'] for r in records), 'event_count_mismatch_maps': sum(bool(r['event_count_mismatches']) for r in records),
                            'postwick_labelled_maps': sum(r['name'] == 'Postwick' for r in records), 'categories': dict(Counter(r['category'] for r in records)), 'dispositions': dict(Counter(r['disposition'] for r in records)),
                            'canonical_spine_nodes': len(spine_ids), 'provisional_spine_nodes': sum(r['id'] in spine_ids and r['canonical_selection_status'] == 'PROVISIONAL' for r in records)},
                'lists': lists, 'canonical_region_spine': {'nodes': [{key: byid[i].get(key) for key in ('id', 'name', 'role', 'category', 'confidence', 'canonical_selection_status', 'import_flag')} for i in sorted(spine_ids, key=sort_id)],
                        'internal_relationships': [edge for edge in normalized_edges if edge['normalized_target_hint'] in spine_ids], 'boundary_relationships': [edge for edge in normalized_edges if edge['normalized_target_hint'] not in spine_ids],
                        'notes': ['The source is not a clean official-game progression. Missing static links are recorded, not fabricated.', 'Route 1 still points at Postwick revision 4.6; alias-remap hint points to preserved 3.0, with no write performed.', 'Core named route alternatives replace inherited FireRed slots; later route labels do not establish canonical Galar geography.', 'Unnamed groups 37/38 and mislabeled Postwick ocean/expansion sectors stay in review; no official DLC sector names are guessed.']},
                'duplicate_name_families': family_records, 'maps': records}
    validate_manifest(manifest)
    return manifest, corrected

def validate_manifest(manifest):
    records = manifest['maps']
    ids = {record['id'] for record in records}
    if len(records) != 701 or len(ids) != 701:
        raise ValueError('Incomplete or duplicate SWSH inventory')
    partition = [i for values in manifest['lists'].values() for i in values]
    if len(partition) != 701 or len(set(partition)) != 701 or set(partition) != ids:
        raise ValueError('Disposition lists must partition all 701 maps')
    for record in records:
        if record['category'] not in CATEGORIES or any(record[key] for key in ('runtime_import_flag', 'event_import_flag', 'script_import_flag', 'relationship_import_flag')):
            raise ValueError('Unsafe category/runtime flag')
        if record['import_flag'] and not (record['canonical_flag'] and record['confidence'] == 'HIGH' and record['visual_review'] == 'PASS' and not record['event_count_mismatches'] and record['disposition'] == 'SELECTED_ASSET'):
            raise ValueError('Unsafe asset selection: ' + record['id'])
        if record['disposition'].startswith('EXCLUDED') and (record['canonical_flag'] or record['import_flag']):
            raise ValueError('Excluded map cannot be canonical/imported')
        if record.get('canonical_replacement') not in ids | {None}:
            raise ValueError('Unknown replacement target')
    canary = next(record for record in records if record['id'] == '3.0')
    if not (canary['canonical_flag'] and canary['disposition'] == 'PRESERVE_CANARY' and not canary['import_flag']):
        raise ValueError('Postwick canary must remain protected')
    if manifest['execution_allowed'] or manifest['bulk_import_allowed']:
        raise ValueError('Execution must remain disabled')

def write_outputs(manifest, corrected, out):
    out.mkdir(parents=True, exist_ok=True)
    (out/'swsh_galar_import_manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    records = manifest['maps']
    fields = ['donor', 'id', 'group', 'map', 'name', 'category', 'canonical_flag', 'canonical_selection_status', 'import_flag', 'confidence', 'disposition', 'role', 'canonical_replacement', 'reason', 'width', 'height', 'object_count', 'object_exported_count', 'warp_count', 'warp_exported_count', 'coord_count', 'coord_exported_count', 'bg_count', 'bg_exported_count', 'connection_count', 'primary_tileset', 'secondary_tileset', 'header_pointer', 'layout_pointer', 'exact_firered_blockdata', 'shared_layout_ids', 'same_visual_ids', 'nearby_region_hints', 'dependencies', 'wiring_blockers', 'source_json', 'source_json_sha256']
    subsets = {'inventory': records, 'high_confidence_import': [r for r in records if r['import_flag']], 'exclusions': [r for r in records if r['disposition'].startswith('EXCLUDED')],
               'excluded_legacy': [r for r in records if r['disposition'] == 'EXCLUDED_LEGACY'], 'manual_review': [r for r in records if r['disposition'] == 'MANUAL_REVIEW'], 'postwick_duplicate_resolution': [r for r in records if r['name'] == 'Postwick']}
    for filename, rows in subsets.items():
        csv_write(out/('swsh_galar_'+filename+'.csv'), rows, fields)
    csv_write(out/'swsh_donor_map_metadata_corrected.csv', corrected, list(corrected[0]))
    summary = manifest['summary']
    text = ['# SWSH / Galar review', '', 'All 701 usable SWSH maps inventoried. No bulk import or destination write performed. Postwick 3.0 remains the validated canary; BWA/Nuvema and its user-verified imports remain untouched.', '',
            '**High-confidence import flags select future visual assets only. Gameplay, events, scripts, connections and warps remain disabled. This is not an executable migration plan.**', '',
            f"Asset candidates: {len(subsets['high_confidence_import'])}. Legacy exclusions: {len(subsets['excluded_legacy'])}. Superseded revisions: {len(manifest['lists']['excluded_superseded'])}. Manual review: {len(subsets['manual_review'])}. Protected canary: 1.", '',
            f"{summary['exact_firered_blockdata_matches']} maps match their pinned FireRed slot's raw blockdata exactly. Geometry ancestry is not proof of unchanged events or intent; linked reusable rooms may remain review rather than exclusion.", '',
            f"Reference: [pret/pokefirered {REFERENCE_COMMIT[:12]}](https://github.com/pret/pokefirered/tree/{REFERENCE_COMMIT}). Offline slot/hash data is bundled with the classifier.", '',
            '## Postwick resolution', '',
            '172 maps carry the Postwick label; that is not 172 towns. Keep validated 3.0. 4.6 is an active alternate linked by Route 1/houses, but is not authorized to replace the canary. 4.9 is orphaned; 0.17 is an adventure-linked revision; 4.5 is a malformed 1x1 record.', '',
            '| Older slot | Resolved feature | Preferred canonical map |', '|---|---|---|',
            '| 3.1 | Wedgehurst | 5.6 |', '| 3.2 | Motostoke | 6.10 |', '| 3.3 | Turffield | 7.11 |', '| 3.4 | Hulbury | 8.7 |', '| 3.5 | Hammerlocke | 9.10 |', '| 3.6 | Stow-on-Side | 10.21 |', '| 3.7 | Ballonlea | 11.10 |', '| 3.8 | Circhester | 12.10 |', '| 3.10 | Spikemuth | 14.10 |', '',
            'These are preview/graph/event-backed revision decisions, not name-only relabels. All original identities, pointers, counts and relationships remain in the manifest. Postwick-labelled interiors receive weak nearby-region hints only. Generic expansion/ocean sectors in groups 37/38 are not assigned official area names.', '',
            '## Canonical donor spine', '', '| ID | Feature / role | Selection |', '|---|---|---|']
    for node in manifest['canonical_region_spine']['nodes']:
        text.append(f"| {node['id']} | {node['name']} / {node['role']} | {'asset candidate' if node['import_flag'] else node['canonical_selection_status'] + ' / deferred'} |")
    text += ['', '## Relationships and gaps', '',
             '- Early chain: Route 1 links Postwick revision 4.6 and canonical Wedgehurst 5.6. The manifest suggests remapping 4.6 to preserved 3.0; no remapping is executed. Route 2 ends at its donor local relationships; no direct clean route into Motostoke is fabricated.',
             '- Motostoke -> Route 3 -> Galar Mine 6.28 -> Route 4 -> Turffield -> Route 5 -> Hulbury causeway/main is supported by source relationships. Motostoke outskirts 6.32 and mine 8.20 form an additional branch.',
             '- Hammerlocke -> Route 6 -> Stow-on-Side -> forest candidate 1.109 -> Ballonlea is recorded, with the forest identity provisional and Ballonlea event truncation deferred.',
             '- Route 7, both Route 8 sectors, Circhester, Route 9 and edited Spikemuth are retained; cave 1.37 and inherited route links remain blockers. Route 10/Wyndon are supported, but gaps to earlier towns are not invented.',
             '- Main Wild Area sectors connect through 6.27/6.29/6.30/6.31 and central 42.2 towards Hammerlocke 42.15, dry basin/ridges, cave 42.12 and lake 42.13. Lava and snow branches are provisional. Grass-smiley 42.8 stays novelty/test review. Unnamed official sector names are not guessed.', '',
             '## Dungeons and leftovers', '',
             '- Galar Mine floors 6.28, 8.20 and 1.3 have distinct edited geometry/entrance roles. Slumbering forest and approaches are outdoor dungeon features, not extra Postwick towns.',
             '- Dynamax Adventure hub 34.4 and chambers 1.99/1.101/2.57 are retained candidates. Named strip/return maps keep review status because their relationships reuse inherited route graphs.',
             '- Courageous Cavern 1.40/1.41, Warm-up/unnamed cave floors, Ice Dream Cave, Newmoon/Underwater branches and Route 6 cave 1.122 remain identity/geometry review. Generic forest 1.109 is a Stow–Ballonlea bridge candidate; corrupt alternate 1.110 is excluded.',
             '- FireRed route slots 3.22/3.24-3.27 and later inherited route/island geometry are quarantined even when labelled Galar. Spikemuth 3.11 is stock Saffron connection geometry; edited street 14.10 is the canonical choice despite its cave map type.',
             '- Crystal Hotel 1.4-1.29 contains SS Anne geometry mixed with edited rooms. Silph Co and other inherited dungeon/room families are preserved as exclusions or ambiguity, not recursively imported.', '',
             '## Metadata and safety', '',
             f"Corrected all 701 object counts from event_counts.object; npcs lengths are retained separately. {summary['event_count_mismatch_maps']} maps have declared/exported count mismatches, including Wedgehurst, Ballonlea, Route 9 and Wild Area branches. Those records stay outside the high-confidence asset list.", '',
             'Exact layout/visual/blockdata duplicate families preserve event and script differences. Every warp/connection retains the donor record, incoming links, target disposition and deferred remapping action. Missing/truncated destination indices, legacy dependencies and dynamic returns remain explicit blockers. No map is imported solely through a dependency.', '',
             '## Files', '',
             '- swsh_galar_import_manifest.json: complete inventory, spine, relationships, family resolutions and provenance.',
             '- swsh_galar_high_confidence_import.csv: visually reviewed future asset candidates.',
             '- swsh_galar_exclusions.csv: legacy geometry plus superseded revisions; excluded_legacy.csv isolates legacy exclusions.',
             '- swsh_galar_manual_review.csv: unresolved identities, revisions, render issues and event truncation.',
             '- swsh_galar_postwick_duplicate_resolution.csv: every one of the 172 Postwick-labelled maps.',
             '- swsh_donor_map_metadata_corrected.csv: SWSH-only corrected counts; original combined metadata reports are unchanged.', '',
             'Classification phase complete. Remaining uncertainties are recorded explicitly; no gameplay validation or import is claimed.']
    (out/'swsh_galar_review.md').write_text('\n'.join(text)+'\n', encoding='utf-8')
    print(compact(summary))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=REPO/'.la_work/amap/swsh_full_v11')
    parser.add_argument('--metadata-csv', type=Path, default=REPO/'.la_work/amap/donor_map_metadata_report.csv')
    parser.add_argument('--metadata-md', type=Path, default=REPO/'.la_work/amap/donor_map_metadata_report.md')
    parser.add_argument('--rules', type=Path, default=HERE/'swsh_galar_rules.json')
    parser.add_argument('--reference', type=Path, default=HERE/'firered_map_reference.json')
    parser.add_argument('--out', type=Path, default=REPO/'.la_work/amap/swsh_galar_review')
    args = parser.parse_args()
    for protected in [args.root.resolve(), (REPO/'.la_work/amap/bwa_full_v11').resolve(), (REPO/'.la_work/amap/bwa_unova_review').resolve(), HERE]:
        if args.out.resolve() == protected or protected in args.out.resolve().parents or args.out.resolve() in protected.parents:
            parser.error('Output must be separate from sources, tools, and BWA reports')
    manifest, corrected = build(args.root, args.metadata_csv, args.metadata_md, args.rules, args.reference)
    write_outputs(manifest, corrected, args.out)

if __name__ == '__main__':
    main()
