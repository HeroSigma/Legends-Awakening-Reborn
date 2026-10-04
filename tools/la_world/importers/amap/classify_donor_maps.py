#!/usr/bin/env python3
"""Read-only A-Map v1.1 inventory and conservative donor classification.

Confidence describes metadata evidence, not gameplay or import readiness.
Declared event counts are retained separately from parsed array lengths.
"""
import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

EVENTS = {'object': 'npcs', 'warp': 'warps', 'coord': 'coord_events', 'bg': 'bg_events'}
CATEGORIES = ('WORLD', 'INTERIOR', 'CAVE_DUNGEON', 'TRANSITION', 'UTILITY', 'DEBUG_TEST', 'STALE_UNKNOWN')
WORLD_TYPES = {1, 2, 3, 6}

def compact(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)

def pointers(value, prefix=''):
    result = {}
    if isinstance(value, dict):
        for key, item in value.items():
            path = f'{prefix}.{key}' if prefix else key
            if 'pointer' in key:
                result[path] = item
            elif isinstance(item, (dict, list)):
                result.update(pointers(item, path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            result.update(pointers(item, f'{prefix}[{index}]'))
    return result

def classify(d, family):
    scores = Counter({c: 0 for c in CATEGORIES})
    evidence = []
    def add(category, score, reason):
        scores[category] += score
        evidence.append(f'{category}+{score}:{reason}')
    typ, name = d['map_type'], d['name'].lower()
    area = d['width'] * d['height']
    if typ in WORLD_TYPES:
        add('WORLD', 7, f'map_type={typ}')
        if d['group'] == 3:
            add('WORLD', 2, 'overworld_group_3')
        if d['connections']:
            add('WORLD', 2, 'connections')
    elif typ in {4, 5}:
        add('CAVE_DUNGEON', 8, f'map_type={typ}')
    elif typ in {8, 9}:
        add('INTERIOR', 8, f'map_type={typ}')
    else:
        add('STALE_UNKNOWN', 3, f'unspecified_map_type={typ}')
    if re.search(r'\b(debug|test|unused|dummy)\b', name):
        add('DEBUG_TEST', 12, 'explicit_name_marker')
    if re.search(r'\b(link|union|trade|colosseum|record corner|battle tower)\b', name):
        add('UTILITY', 10, 'facility_name')
    if re.search(r'\b(gate|passage|entrance|exit|connector)\b', name):
        add('TRANSITION', 10, 'transition_name')
    elif typ == 8 and area <= 300 and len(d['warps']) >= 2 and len(d['npcs']) <= 1 and not d['bg_events']:
        add('TRANSITION', 9, 'small_sparse_multiwarp_room')
    if typ == 0 and d['connections'] and area >= 600:
        add('WORLD', 5, 'large_connected_unspecified_map')
    if typ == 0 and family:
        add(family, 2, 'donor_secondary_tileset_majority')
    if typ == 0 and not any(d[a] for a in EVENTS.values()) and not d['connections']:
        add('STALE_UNKNOWN', 4, 'no_exported_events_or_connections')
    ranking = sorted(CATEGORIES, key=lambda c: (-scores[c], CATEGORIES.index(c)))
    category = ranking[0]
    margin = scores[category] - scores[ranking[1]]
    confidence = 'HIGH' if scores[category] >= 7 and margin >= 3 else 'MEDIUM' if margin >= 2 else 'LOW'
    if category == 'STALE_UNKNOWN':
        confidence = 'LOW'
    return category, confidence, scores, evidence

def inventory(donor, root):
    manifest = json.loads((root / 'manifest.json').read_text())
    if manifest.get('format') != 'A-Map Batch Bridge v1.1':
        raise ValueError(f'{root}: not a validated v1.1 export')
    maps = []
    for path in (root / 'maps').glob('*/map.json'):
        d = json.loads(path.read_text())
        for key in ('id', 'group', 'map', 'name', 'width', 'height', 'map_type', 'event_counts', 'connections', 'primary_tileset', 'secondary_tileset', *EVENTS.values()):
            if key not in d:
                raise ValueError(f'{path}: missing {key}')
        if d['id'] != f"{d['group']}.{d['map']}" or any(not isinstance(d[a], list) for a in (*EVENTS.values(), 'connections')):
            raise ValueError(f'{path}: inconsistent identity or event schema')
        maps.append((path, d))
    maps.sort(key=lambda pair: (pair[1]['group'], pair[1]['map']))
    if len({d['id'] for _, d in maps}) != len(maps):
        raise ValueError(f'{donor}: duplicate map IDs')
    families = defaultdict(Counter)
    layouts = defaultdict(list)
    for _, d in maps:
        base = 'WORLD' if d['map_type'] in WORLD_TYPES else 'INTERIOR' if d['map_type'] == 8 else 'CAVE_DUNGEON' if d['map_type'] == 4 else None
        if base:
            families[d['secondary_tileset']][base] += 1
        if d.get('layout_pointer'):
            layouts[d['layout_pointer']].append(d['id'])
    rows = []
    for path, d in maps:
        counts = families[d['secondary_tileset']]
        family = counts.most_common(1)[0][0] if counts and counts.most_common(1)[0][1] / sum(counts.values()) >= .8 else None
        category, confidence, scores, evidence = classify(d, family)
        issues = []
        row = {'donor': donor, 'profile': manifest['profile'], 'rom_sha256': manifest['rom']['sha256'], 'id': d['id'], 'group': d['group'], 'map': d['map'], 'name': d['name'], 'category': category, 'confidence': confidence}
        for key in ('width', 'height', 'map_type', 'region_map_section_id', 'region_map_section_name', 'layout_id', 'primary_tileset', 'secondary_tileset', 'header_pointer', 'layout_pointer', 'blockdata_pointer', 'visual_map_sha256', 'blockdata_sha256'):
            row[key] = d.get(key, '')
        for event, array in EVENTS.items():
            declared = d['event_counts'].get(event)
            parsed = len(d[array])
            row[event + '_count'] = declared
            row[event + '_exported_count'] = parsed
            if declared != parsed:
                issues.append(f'{event}_count_mismatch:{declared}/{parsed}')
        row['connection_count'] = len(d['connections'])
        row['connection_targets'] = compact([c.get('target_id') for c in d['connections']])
        row['warp_targets'] = compact([w.get('target_id') for w in d['warps']])
        peers = [i for i in layouts.get(d.get('layout_pointer'), []) if i != d['id']]
        row['shared_layout_ids'] = compact(peers)
        if peers:
            issues.append('shared_layout_not_proof_of_staleness')
        if confidence != 'HIGH':
            issues.append('ambiguous_metadata')
        if d['map_type'] == 0:
            issues.append('unspecified_map_type')
        row['validated_canary'] = d['id'] == '3.0'
        row['review_required'] = bool(issues)
        row['review_reasons'] = ';'.join(issues)
        row['scores'] = compact(dict(scores))
        row['evidence'] = ';'.join(evidence)
        row['source_json'] = str(path.resolve())
        row['source_json_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        row['pointers'] = compact(pointers(d))
        tileset_pointers = {}
        for role in ('primary', 'secondary'):
            ts_path = root / 'tilesets' / d[role + '_tileset'] / 'tileset.json'
            if ts_path.exists():
                tileset_pointers[role] = pointers(json.loads(ts_path.read_text()))
                # Struct addresses are also provenance pointers.
                tileset_pointers[role]['source'] = json.loads(ts_path.read_text()).get('source', {})
        row['tileset_source'] = compact(tileset_pointers)
        rows.append(row)
    return rows

def write_reports(donor, rows, out):
    target = out / donor.lower()
    target.mkdir(parents=True, exist_ok=True)
    subsets = {
        'inventory': rows,
        'world_candidates': [r for r in rows if r['category'] == 'WORLD' and r['confidence'] == 'HIGH' and not r['review_required']],
        'interior_dungeon_candidates': [r for r in rows if r['category'] in {'INTERIOR', 'CAVE_DUNGEON'}],
        'review_unknown': [r for r in rows if r['review_required'] or r['category'] in {'STALE_UNKNOWN', 'DEBUG_TEST'}],
    }
    for name, subset in subsets.items():
        with (target / (name + '.csv')).open('w', newline='', encoding='utf-8') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(subset)
    counts = Counter(r['category'] for r in rows)
    text = [f'# {donor} donor-map classification', '', f'Total: {len(rows)} usable exported maps. Metadata candidates only; no import performed.', '', '| Category | Count |', '|---|---:|']
    text += [f'| {c} | {counts[c]} |' for c in CATEGORIES]
    text += ['', f'High-confidence world shortlist: {len(subsets["world_candidates"])}. Interior/dungeon candidates: {len(subsets["interior_dungeon_candidates"])}. Review queue: {len(subsets["review_unknown"])}.', '', 'Object events: event_counts.object; parsed objects: npcs. All four declared counts and exported lengths are preserved; mismatches and shared layouts enter review. Shared layouts and empty events do not prove stale content. Type 0 remains review-only. Names are supporting evidence; region labels may describe interiors. Tileset majority is donor-local and weak evidence only. Transition/utility/debug suggestions require review before selection.', '', 'Scores and reasons are in CSV. HIGH requires score >=7 and margin >=3; MEDIUM requires margin >=2; otherwise LOW. Confidence is classification evidence, not gameplay validation. Review CSV overlaps candidate CSVs by design.', '']
    canary = next(r for r in rows if r['id'] == '3.0')
    text += [f'Validated canary: 3.0 {canary["name"]}, {canary["width"]} x {canary["height"]}, {canary["category"]}/{canary["confidence"]}. Review flags: {canary["review_reasons"] or "none"}. Working import untouched.', '', '## World shortlist', '', '| ID | Name | Dimensions | Connections |', '|---|---|---|---:|']
    text += [f'| {r["id"]} | {r["name"].replace("|", "/")} | {r["width"]} x {r["height"]} | {r["connection_count"]} |' for r in subsets['world_candidates']]
    text += ['', '## Review preview (first 25; full queue in review_unknown.csv)', '', '| ID | Name | Category | Reasons |', '|---|---|---|---|']
    text += [f'| {r["id"]} | {r["name"].replace("|", "/")} | {r["category"]} | {r["review_reasons"]} |' for r in subsets['review_unknown'][:25]]
    (target / 'report.md').write_text('\n'.join(text) + '\n', encoding='utf-8')
    print(f'{donor}: {len(rows)} maps; categories={dict(counts)}; world={len(subsets["world_candidates"])}; review={len(subsets["review_unknown"])}')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    repo = Path(__file__).resolve().parents[4]
    parser.add_argument('--bwa-root', type=Path, default=repo / '.la_work/amap/bwa_full_v11')
    parser.add_argument('--swsh-root', type=Path, default=repo / '.la_work/amap/swsh_full_v11')
    parser.add_argument('--out', type=Path, default=repo / '.la_work/amap/classification_v11')
    parser.add_argument('--allow-count-change', action='store_true', help='Permit inventories other than validated 444/701 counts')
    args = parser.parse_args()
    for root in (args.bwa_root, args.swsh_root):
        if args.out.resolve() == root.resolve() or root.resolve() in args.out.resolve().parents or args.out.resolve() in root.resolve().parents:
            parser.error('Report output must be separate from source exports')
    inventories = [(donor, inventory(donor, root)) for donor, root in [('BWA', args.bwa_root), ('SWSH', args.swsh_root)]]
    for donor, rows in inventories:
        if not rows or (not args.allow_count_change and len(rows) != {'BWA': 444, 'SWSH': 701}[donor]):
            parser.error(f'{donor}: unexpected usable map count {len(rows)}')
        if not any(r['id'] == '3.0' and r['category'] == 'WORLD' for r in rows):
            parser.error(f'{donor}: validated canary missing or misclassified')
    for donor, rows in inventories:
        write_reports(donor, rows, args.out)

if __name__ == '__main__':
    main()
