#!/usr/bin/env python3
"""Publish Fortree corridor reconciliation inventory and runtime checklist."""
import csv,collections,json
import hoenn_canary8 as C
ROOT=C.ROOT;OUT=C.OUT

def writecsv(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def publish():
 receipt=C.load(OUT/'receipt.json');v=C.load(OUT/'validation.json');ledger=C.load(OUT/'coordinate_remap_ledger.json');ls={z['id']:z for z in C.load(ROOT/'data/layouts/layouts.json')['layouts']};groups=C.load(ROOT/'data/maps/map_groups.json');locations={n:(g,gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])};rows=[];details=[]
 for n,k in [*C.TARGETS.items(),*((n,k) for k,n in receipt['registered_special_maps'].items())]:
  m=C.load(ROOT/f'data/maps/{n}/map.json');l=ls[m['layout']];d=C.P.source(k);g,gi,mi=locations[n];special=k in receipt['registered_special_maps'];row={'map':n,'map_constant':m['id'],'donor':'HYPER_EMERALD_5_7_EN_QOL','donor_id':k,'donor_name':d['name'],'group':g,'group_id':gi,'map_id':mi,'mapsec':m['region_map_section'],'width':l['width'],'height':l['height'],'map_type':m['map_type'],'primary_tileset':l['primary_tileset'],'secondary_tileset':l['secondary_tileset'],'objects':len(m['object_events']),'warps':len(m['warp_events']),'coords':len(m['coord_events']),'bg':len(m['bg_events']),'connections':len(m['connections'] or []),'source_header_pointer':d['header_pointer'],'source_layout_pointer':d['layout_pointer'],'source_blockdata_pointer':d['blockdata_pointer'],'blockdata_sha256':C.digest(ROOT/l['blockdata_filepath']),'border_sha256':C.digest(ROOT/l['border_filepath']),'mode':'CONSTRUCTION_ASSET_ONLY' if special else 'CANONICAL_HYPER_ASSETS_NATIVE_GAMEPLAY','owner':'PROJECT_CONSTRUCTION_ONLY' if special else 'POKEEMERALD_EXPANSION','runtime_status':'PENDING_USER_TEST'};rows.append(row);details.append({**row,'layout':l,'events':{kind:m[kind] for kind in C.P.KINDS},'connections_detail':m['connections'],'donor_event_counts':d['event_counts'],'donor_scripts_reference_only':d.get('map_scripts')})
 writecsv('maps_inventory.csv',rows);writecsv('canonical_replacements.csv',[z for z in rows if z['mode'].startswith('CANONICAL')]);writecsv('registered_special_areas.csv',[z for z in rows if z['mode'].startswith('CONSTRUCTION')]);manual=[{'map':z['map'],'source':z['source'],'destination':z['record'].get('target_id',''),'destination_name':z['record'].get('target_name',''),'status':'DEFERRED_NO_ACTIVE_LINK','reason':z['reason']} for z in ledger['deferred_references']];writecsv('manual_review.csv',manual)
 C.dump(OUT/'lilycove_corridor_manifest.json',{'schema':'hyper-hoenn-canary8-v1','canonical_maps':44,'actual_special_maps':2,'maps':details,'deferred':manual,'runtime_verified':False,'validation':{k:z for k,z in v.items() if k!='maps'}})
 (OUT/'review.md').write_text(f"""# Hoenn Canary #8: Lilycove, Safari and Mt. Pyre corridor

Build/static/linked-assets/animation/editor checks passed. Runtime verification is pending. Prior Canary #7 Fortree Gym test remains pending; this batch does not assert its runtime success. No later sea/Mossdeep replacement batch has advanced.

## Canonical mappings

44 canonical entries now use staged Hyper assets: Routes121/122/123 and Safari entrance/Berry Master's house; Lilycove City, both motel/museum/Center floors, Contest Lobby/Hall, Fan Club, Harbor, Move Deleter/four houses, department store floors1–5/roof/elevator and its unused Mart registry entry; six Safari sectors plus Rest House; all six Mt. Pyre interior floors, Exterior and Summit. The unused Mart remains unused, with no newly invented overworld entrance.

Canonical MAP identities and numeric positions, map-script ownership, encounters, heal/Fly/blackout identities, flags/vars, trainer/item/berry/reward state, native dynamic graphics initialization, connections and save ABI remain authoritative. 566 native event records retain gameplay fields; 50 have reviewed geometry changes (coordinates/elevation), recorded with before/after and source references. No donor NPC/story/progression/save logic or old imported-map wrappers are copied.

All new map surface heights are donor-derived. One inspected donor anomaly, Lilycove's isolated surfable water cell (53,2), is corrected from land3 to water1. All 2,661 surfable water cells pass water-level checks. Older Route110, Route114 and Route119 fixes and Rustboro/Route104 user edits remain protected.

Lilycove's rival is relocated from blocked (27,7) to its matched donor location (39,15), with native Brendan/May initialization, battle/flags and Fly departure retained. Moved Aqua actors, elderly townsfolk, store/house actors and Safari items/rocks likewise retain their native gameplay identities. Wailmer's 12 existing visual command operands exactly match the donor tile IDs; its native blockade flag remains unchanged. Native SS Tidal art, boarding/ferry logic and all dynamic GFX variables are retained.

Mt. Pyre sparse donor warp IDs are resolved explicitly: donor6F arrival3 maps to canonical native slot0, donor5 maps to native slot1, and donor4 becomes a new scientist-gated Ultra Space portal. Native staircase/fall destination slots and story ownership remain intact. Arrival-only native floor warps remain arrival-only; geometry evidence distinguishes them from step-triggered warps. Summit Aqua/orb/Magma Emblem progression remains native.

## Actual special maps

Two actual new construction-only maps are registered: `HyperHoenn_35_35_Temple_of_the_End` and `HyperHoenn_34_66_Mountain_Top`. They have geometry/borders/tilesets, groups/mapsecs, static links and notices. The Museum2F entrance is (1,2). MtPyre6F (6,7) links to the already registered Ultra Space map; its prior reviewed arrival and static return route are retained. Four new scientists/notices are present. Remove the relevant scientists in a test copy and rebuild to open reviewed links; this does not implement donor legendary/quest logic.

Temple→Rainbow Castle remains deferred because the requested donor arrival slot has no reviewed existing project counterpart. The Castle's prior import remains intact. Department Store1F's pre-existing off-map floor-name sign at (0,8) is preserved for manual review; it is not a newly placed event. These two records are in manual_review.csv.

One new section family is appended; MAPSEC_NONE=218 remains unchanged, MAPSEC_COUNT=241. Older groups/maps/layouts/sections retain their numeric positions. Kanto/Johto/Sinnoh canonical migrations are not advanced.

## Validation

- All {v['editor_and_linked_hyper_maps_checked']} active Hyper maps and {v['tilesets_checked']} linked banks checked; {v['linked_objects']} objects, {v['linked_warps']} warps, {v['linked_connections']} connections.
- {v['protected_baseline_files']} protected baseline files audited; all 44 native script owners preserved, plus original event gameplay fields, previous art binding rows, ABI and gameplay tables.
- 120 native warp records inspected; native Wailmer visual operands and Lilycove Fly/heal positions verified. New special entry/return graph checks passed; all-room collision/pathfinding and progression remain runtime tests.
- Proven animation callbacks passed host sanitizer checks. Editor references pass for all 300 maps and 108 exposed Hyper tilesets. Reload Porymap before saving the externally updated registries.

ROM SHA256: `{v['rom_sha256']}`.

See runtime_checklist.md, maps_inventory.csv, coordinate_remap_ledger.json, geometry_validation.json, special_graph_validation.json, receipt.json and validation.json. Stop here for user runtime feedback.
""")
 (OUT/'runtime_checklist.md').write_text("""# Canary #8 runtime checklist

Use the supplied ROM and a normal save copy; reload/re-enter maps so cached object positions refresh. Fortree Gym testing remains pending separately.

- [ ] Route120→121→Lilycove and return; Route121 Safari entrance; Surf south through Route122, Mt. Pyre entrance and Route123/Route118 loop.
- [ ] Routes121/123 trainers, double battles, cut trees, berries, item balls, hidden items and signs; Berry Master/wife gifts, daily/phrase reward state and full-bag/cancel behavior.
- [ ] Lilycove every building/door, moved rival (39,15), both genders and starter branches, refuse/accept battle, native Fly departure and later flags/return visits.
- [ ] Lilycove shoreline blocks foot entry, Surf entry/travel/exit; Wailmer/Aqua blockade before/after native submarine escape flag; hideout entrance still reaches the unchanged canonical hideout.
- [ ] Center healing/blackout/Fly arrival (24,15), Mart/department store purchases/cancel, floors1–5/roof/elevator, floor signs and rooftop sale states. Dormant off-map sign is a manual-review record.
- [ ] Native Contest/Pokeblock/blender flow, museum painting collection, Move Deleter, Fan Club, motel, houses and all gifts/trades/daily flags.
- [ ] Harbor availability before/after story/game clear, SS Tidal appearance, boarding/disembark/Ferry destinations and saved travel state. Native boat contract is retained.
- [ ] Safari native fee/party/Pokeblock prerequisites, ball/step limits, capture/run/retire/out-of-balls/timeout return, all four original sectors and Rest House, bikes/ledges/Surf/items/rocks.
- [ ] Safari Northeast/Southeast remain gated by native postgame state; unlock/visit/capture/items/save/reload correctly.
- [ ] Mt. Pyre all stairs/fall holes and return arrivals, six floors, trainers/items, exterior/summit paths, fog/weather, Aqua cutscene, orb/Emblem rewards/flags and save/reload before/after events.
- [ ] Museum2F scientist at (1,2) and MtPyre6F scientist at (6,7) gate only extras. Normal Museum/MtPyre progression remains usable.
- [ ] Reload Porymap; inspect all 44 canonical entries and two new special maps. In a test copy, remove relevant scientists and rebuild; enter/return from Temple, Mountain Top and existing Ultra Space. Existing Ultra static return may lead through earlier special maps, not directly back to Mt. Pyre.
- [ ] Deferred Temple/Rainbow Castle exit remains closed; removing a scientist does not create the unresolved arrival.
- [ ] Source water/bridge/shoreline elevation, animations, collision, map borders, save/reload and native encounter ownership.
- [ ] Regression: pending Fortree Gym, Devon Scope/Kecleon, Route119 Institute/bridges, Route110 Cycling Road/Surf, Route114 shores, earlier Hoenn maps, Rustboro/Route104 cleanup, New Mauville/Ship/Island Cave and validated Unova/Galar imports.

Stop after Canary #8; report map, coordinates, direction, gender and story state for failures.
""")
 print('Published 46-map inventory and runtime checklist.')
if __name__=='__main__':publish()
