#!/usr/bin/env python3
"""Publish Canary #6's canonical dungeon and construction-area registry."""
import csv,collections
import hoenn_canary6 as C
ROOT=C.ROOT;OUT=C.OUT

def csvout(name,rows):
 if not rows:return
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def publish():
 r=C.load(OUT/'receipt.json');v=C.load(OUT/'validation.json');led=C.load(OUT/'coordinate_remap_ledger.json');groups=C.load(ROOT/'data/maps/map_groups.json');ls={z['id']:z for z in C.load(ROOT/'data/layouts/layouts.json')['layouts']};oldls={z['id']:z for z in C.load(OUT/'original/data/layouts/layouts.json')['layouts']};loc={n:(g,gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])};rows=[];detail=[]
 for n,k in [*C.TARGETS.items(),*((n,k) for k,n in r['registered_special_maps'].items())]:
  m=C.load(ROOT/f'data/maps/{n}/map.json');l=ls[m['layout']];d=C.P.source(k);special=k in r['registered_special_maps'];g,gi,mi=loc[n];original=C.load(OUT/f'original/data/maps/{n}/map.json') if not special else None;old=oldls[original['layout']] if original else None
  row={'map':n,'map_constant':m['id'],'donor':'HYPER_EMERALD_5_7_EN_QOL','donor_id':k,'donor_name':d['name'],'group':g,'group_id':gi,'map_id':mi,'mapsec':m['region_map_section'],'map_type':m['map_type'],'width':l['width'],'height':l['height'],'original_width':old['width'] if old else '', 'original_height':old['height'] if old else '', 'primary_tileset':l['primary_tileset'],'secondary_tileset':l['secondary_tileset'],'object_events':len(m['object_events']),'warps':len(m['warp_events']),'coord_events':len(m['coord_events']),'bg_events':len(m['bg_events']),'connections':len(m['connections'] or []),'source_object_events':len(d['npcs']),'source_warps':len(d['warps']),'source_header_pointer':d['header_pointer'],'source_layout_pointer':d['layout_pointer'],'source_blockdata_pointer':d['blockdata_pointer'],'blockdata_sha256':C.digest(ROOT/l['blockdata_filepath']),'border_sha256':C.digest(ROOT/l['border_filepath']),'mode':'CONSTRUCTION_ASSET_ONLY' if special else 'CANONICAL_HYPER_ASSETS_NATIVE_GAMEPLAY','script_owner':'PROJECT_CONSTRUCTION_ONLY' if special else 'POKEEMERALD_EXPANSION','runtime_status':'PENDING_USER_TEST'};rows.append(row);detail.append({**row,'layout':l,'events':{kind:m[kind] for kind in C.P.KINDS},'connections_detail':m['connections'],'source_event_counts':d['event_counts'],'source_script_pointers_reference_only':d.get('map_scripts'),'ownership_policy':'No donor story/NPC/progression/flag/var/save semantics or old imported-map wrappers.'})
 csvout('maps_inventory.csv',rows);csvout('canonical_replacements.csv',[z for z in rows if z['mode'].startswith('CANONICAL')]);csvout('registered_special_areas.csv',[z for z in rows if z['mode'].startswith('CONSTRUCTION')]);manual=[{'map':z['map'],'source':z['source'],'source_record':z['record'].get('index',z['record'].get('direction','')),'destination':z['record'].get('target_id',''),'destination_name':z['record'].get('target_name',''),'status':'DEFERRED_NO_ACTIVE_LINK','reason':z['reason']} for z in led['deferred_references']];csvout('manual_review.csv',manual)
 C.dump(OUT/'earlier_hoenn_dungeon_manifest.json',{'schema':'hyper-hoenn-canary6-v1','canonical_maps_replaced':16,'actual_special_maps_registered':25,'runtime_verified':False,'maps':detail,'manual_review':manual,'validation':{k:z for k,z in v.items() if k!='maps'}})
 counts=collections.Counter(z['donor_name'] for z in rows if z['mode'].startswith('CONSTRUCTION'));family='\n'.join(f'| {n} | {i} |' for n,i in sorted(counts.items()))
 (OUT/'review.md').write_text(f'''# Hoenn Canary #6: New Mauville, Abandoned Ship and Island Cave

Status: implementation, build, linked-ROM/assets/animation and editor declaration checks passed. In-game verification remains pending. Canary #5 runtime status was not changed by this batch.

## Canonical replacements

16 canonical maps now use staged Hyper geometry/assets: NewMauville_Entrance and NewMauville_Inside; all 13 AbandonedShip rooms/deck/corridors/underwater/hidden rooms; IslandCave.

Canonical MAP identities and numeric positions remain unchanged. Expansion owns the Basemen​​t Key/Wattson quest, generator/switch state, Voltorb encounters and rewards; the ship's trainers, storage/room keys, Dive mapping, Scanner/Stern reward chain; and Regice's braille/walking puzzle, species battle and encounter flag. No Hyper gameplay scripts, donor flags/vars, encounters, quests or save semantics were imported.

The Scanner alone moves from (16,10), an impassable Hyper shelf, to the inspected donor Room 2 item-ball floor cell (21,10), retaining ITEM_SCANNER, its native script and original flag. All other native event coordinates and all native warp indices/destination semantics remain intact.

AbandonedShip_Underwater1 expands from 8×8 to 25×8. Existing dive/warp coordinates are retained; original cell elevations are preserved and passable extension cells use the inspected native underwater floor elevation. The native Dive table, move requirements and surface mapping are unchanged.

Native scripted metatile behavior slots already match the recovered Hyper bank for doors, switches and Regice's wall; no native progression scripts or shared behavior banks were changed. Locked ship doors remain controlled by native room-key flags. Regice's full 36-cell native perimeter is walkable on the Hyper geometry.

42 compatible object-art adapters retain native dimensions/frame/animation contracts. Native item-ball/Voltorb reward rendering remains intact. Regice retains its native object graphic because donor GFX185 cannot satisfy the native dimensions/animation contract; its Hyper cave assets are active and its native battle/puzzle ownership is preserved.

## Actual special-area registration

25 actual associated special maps are registered, not merely entrance markers. They have geometry/borders/tilesets, append-only map/group/layout/mapsec IDs, static project-owned links and scientists. Source NPCs, EV training rewards, island/legendary quests and donor gameplay are absent.

| New family | Maps |
|---|---:|
{family}

All 25 have static entry and return paths from canonical maps, ignoring scientists. Remote Island's reciprocal internal sector connections are registered. Existing canonical connections remain unchanged. Your Rustboro geometry and Route104/Rustboro event edits are preserved byte-for-byte; the registry merge restored the required batch entries and portal aliases. See `editor_merge_review.json`. New Mauville's other Ultra Space portal reuses the already registered special destination and its existing static return; it does not transplant donor dynamic-return logic.

Reload Porymap. Exact names/groups/mapsecs are in `registered_special_areas.csv`. New names begin `HyperHoenn_`; ship extras reuse the dungeon group and native Abandoned Ship map section; existing Ultra Space sections/groups are reused, and new families have their own appended groups/sections. Scientists at the new native mouths prevent early portal entry. In a test copy, remove the relevant scientists and rebuild to open reviewed static links. Removing them does not implement donor quests.

Nine donor exits/connections remain deferred, including Cerulean Cave, Whirl Islands, future Pacifidlog/Route129 links, a missing reviewed Rainbow Castle arrival and a nonreciprocal Slateport connection. Their geometries/destinations outside this batch were not migrated. See `manual_review.csv`.

## Validation

The isolated `pokeemerald-canary6.gba` build passed: 32 MiB padded ROM, 29,083,672 bytes linked usage (86.68%). EWRAM/IWRAM usage is unchanged from Canary #5.

- All 225 active Hyper maps verified in linked ROM: layouts/borders, graphics/palettes/metatiles/behaviors, animation callbacks, native script owners, {v['linked_objects']} objects, {v['linked_warps']} warps and {v['linked_connections']} connections.
- {v['protected_baseline_files']} baseline source/asset files audited; 139 native event records preserve all non-coordinate gameplay fields. Existing group/map/layout/mapsec numeric positions and MAPSEC_NONE=218 remain unchanged. MAPSEC_COUNT grows to 237, within the existing byte storage range.
- Save/flags/vars, encounter tables, heal/Fly/blackout tables, Dive and braille runtime code, earlier canonical files except your recorded Rustboro/Route104 editor changes, and validated BWA/SWSH assets remain protected. New art binding rows are appended; previous binding rows remain intact.
- 20 animation callbacks and 18 pairs passed 256 ticks each under AddressSanitizer/UndefinedBehaviorSanitizer: 4,168 frame transfers. Porymap declarations/paths pass for all 225 active Hyper maps and 105 exposed Hyper tilesets.

ROM SHA-256: `{v['rom_sha256']}`.

See `runtime_checklist.md`, `coordinate_remap_ledger.json`, `maps_inventory.csv`, `earlier_hoenn_dungeon_manifest.json` and `validation.json`. Stop here for runtime confirmation. Route119/Fortree and other later Hoenn replacements have not been advanced.
'''.replace('Basemen​​t','Basement'))
 (OUT/'runtime_checklist.md').write_text('''# Canary #6 runtime checklist

Use the supplied Canary #6 ROM and a save copy. This batch is not runtime verified yet.

- [ ] New Mauville: Route110 entrance reachable with Surf; before the Basement Key the native door stays locked; after Wattson's prerequisite the key opens it.
- [ ] Blue/green button switches correctly alternate all barriers. Item balls on buttons and Voltorb encounters preserve their original rewards/flags and button behavior after battle.
- [ ] Generator red switch, power animation/state, Thunder Stone/items, leave/re-enter/save/reload, and Wattson's completion reward work once with native quest state.
- [ ] Abandoned Ship: enter/exit both deck cells from Route108, every corridor/room ladder and doorway, trainers/rewards, Captain Stern's aide, Storage Key and storage-room door before/after key.
- [ ] Dive: correct surface pool → Underwater1 → Underwater2 → hidden floor and return. Test movement through the widened first underwater room; no elevation barrier, incorrect emergence or unintended scientist interference with the normal Dive route.
- [ ] Hidden rooms: sparkle/search cues, keys for Rooms1/2/4/6, locked/unlocked doors, Scanner at (21,10), native Water Stone/Luxury Ball/TM and no repeated item collection after reload.
- [ ] Scanner delivery to Stern and native Deep Sea Tooth/Scale choice/reward state, including cancellation/full-bag handling where applicable.
- [ ] Island Cave: Route105's native Regi entrance before/after Sealed Chamber prerequisite; braille wall, complete native perimeter walk, puzzle success/door animation, Regice graphic/battle/capture/defeat flags, leave/re-enter/save/reload.
- [ ] Collision/elevation, water/Dive floor, animated assets and all dungeon border/warp landings.
- [ ] Both player genders, Escape Rope where native maps allow it, healing/blackout, Fly back to canonical towns and save/reload inside each dungeon family.
- [ ] Porymap: reload project; open all 16 canonical maps and every new special entry in registered_special_areas.csv. Inspect geometry, border, layers, collision/events and make visual cleanup manually if desired.
- [ ] Construction notices at New Mauville extra portals, expanded underwater shortcuts and ship hidden-floor special-room mouth are present; native normal paths remain usable.
- [ ] In a separate test copy, remove construction scientists at selected portals, rebuild, visit/return through the actual registered ship extra, Ultra Space/training/Deep Sea/Remote Island rooms. Verify Remote Island internal sector connections; donor trainer/quest/EV-reward gameplay is intentionally absent.
- [ ] Deferred exits remain closed: Cerulean Cave/Whirl Islands, future Hoenn maps, unresolved Rainbow Castle arrival and copied Slateport boundary. Removing a notice does not create a deferred link.
- [ ] Regression: your Rustboro/Route104 manual cleanup, all through-Mauville locations, northwest Canary #5 maps/scientists, Oldale/Mart, Routes105/107/108, Nuvema/Unova and Postwick/Galar validated imports.

Stop after Canary #6. Report failures with map, coordinates/warp, player gender and progression state. Do not replace further Hoenn maps before runtime confirmation.
''')
 print('Published 41 map rows, 25 actual special maps, and',len(manual),'deferred records.')
if __name__=='__main__':publish()
