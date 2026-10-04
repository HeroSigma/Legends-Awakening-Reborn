#!/usr/bin/env python3
"""Publish Fortree corridor reconciliation inventory and runtime checklist."""
import csv,collections,json
import hoenn_canary7 as C
ROOT=C.ROOT;OUT=C.OUT

def writecsv(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def publish():
 receipt=C.load(OUT/'receipt.json');v=C.load(OUT/'validation.json');ledger=C.load(OUT/'coordinate_remap_ledger.json');ls={z['id']:z for z in C.load(ROOT/'data/layouts/layouts.json')['layouts']};groups=C.load(ROOT/'data/maps/map_groups.json');locations={n:(g,gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])};rows=[];details=[]
 for n,k in [*C.TARGETS.items(),*((n,k) for k,n in receipt['registered_special_maps'].items())]:
  m=C.load(ROOT/f'data/maps/{n}/map.json');l=ls[m['layout']];d=C.P.source(k);g,gi,mi=locations[n];special=k in receipt['registered_special_maps'];row={'map':n,'map_constant':m['id'],'donor':'HYPER_EMERALD_5_7_EN_QOL','donor_id':k,'donor_name':d['name'],'group':g,'group_id':gi,'map_id':mi,'mapsec':m['region_map_section'],'width':l['width'],'height':l['height'],'map_type':m['map_type'],'primary_tileset':l['primary_tileset'],'secondary_tileset':l['secondary_tileset'],'objects':len(m['object_events']),'warps':len(m['warp_events']),'coords':len(m['coord_events']),'bg':len(m['bg_events']),'connections':len(m['connections'] or []),'source_header_pointer':d['header_pointer'],'source_layout_pointer':d['layout_pointer'],'source_blockdata_pointer':d['blockdata_pointer'],'blockdata_sha256':C.digest(ROOT/l['blockdata_filepath']),'border_sha256':C.digest(ROOT/l['border_filepath']),'mode':'CONSTRUCTION_ASSET_ONLY' if special else 'CANONICAL_HYPER_ASSETS_NATIVE_GAMEPLAY','owner':'PROJECT_CONSTRUCTION_ONLY' if special else 'POKEEMERALD_EXPANSION','runtime_status':'PENDING_USER_TEST'};rows.append(row);details.append({**row,'layout':l,'events':{kind:m[kind] for kind in C.P.KINDS},'connections_detail':m['connections'],'donor_event_counts':d['event_counts'],'donor_scripts_reference_only':d.get('map_scripts')})
 writecsv('maps_inventory.csv',rows);writecsv('canonical_replacements.csv',[z for z in rows if z['mode'].startswith('CANONICAL')]);writecsv('registered_special_areas.csv',[z for z in rows if z['mode'].startswith('CONSTRUCTION')]);manual=[{'map':z['map'],'source':z['source'],'destination':z['record'].get('target_id',''),'destination_name':z['record'].get('target_name',''),'status':'DEFERRED_NO_ACTIVE_LINK','reason':z['reason']} for z in ledger['deferred_references']];writecsv('manual_review.csv',manual)
 C.dump(OUT/'fortree_corridor_manifest.json',{'schema':'hyper-hoenn-canary7-v1','canonical_maps':18,'actual_special_maps':11,'maps':details,'deferred':manual,'runtime_verified':False,'validation':{k:z for k,z in v.items() if k!='maps'}})
 (OUT/'review.md').write_text(f"""# Hoenn Canary #7: Route119, Fortree and Route120

Build/static/linked-asset/animation/editor checks passed. Runtime verification is pending. No later replacement batch has advanced.

## Canonical world

18 canonical maps use staged Hyper assets: Route119, both Weather Institute floors and the Route119 house; Fortree City, Gym, Mart, both Center floors, five houses and Decoration Shop; Route120, Ancient Tomb and Scorched Slab. Canonical MAP identities, numeric IDs, encounters, heal/Fly/blackout destinations, connections, flags/vars, native dynamic-GFX initialization and save ABI remain authoritative and unchanged.

289 native event records retain their gameplay fields. Twenty coordinate remaps place doors, signs, hidden items, secret bases, one Fortree actor and the Scorched Slab TM on matched donor cells; the full coordinate ledger records before/after and source evidence. Native trainers/rewards/berry identities stay intact. Fortree Gym has identical native metatile geometry, preserving its rotating-gate puzzle.

Route119 retains both rival trigger branches, Brendan/May and bike states, battle/Fly reward, Scott positions and movements. Eight movement traces pass the inspected geometry checks. Weather Institute retains Aqua, healing/bed, Castform, full-party handling and progression scripts.

Route120 retains Steven, Devon Scope, bridge Kecleon, other Kecleon and weather/progression ownership. Only five visual metatile operands in its existing script are rebound to the inspected Hyper bridge, water and rock-wall assets. Story branching, flags, coordinates and map-script ownership remain expansion's. No donor NPC/gameplay/story logic is copied.

Ancient Tomb retains native Sealed Chamber/Registeel puzzle, activation at (8,25), battle/flags and wall-opening runtime. Registeel stays on its native object graphic because donor art cannot satisfy its native animation/dimension contract. Native Wingull, berries, items, dynamic rival graphics and incompatible specialty art likewise retain their native contracts.

## Actual associated special maps

Eleven actual maps, with geometry/assets/groups/mapsecs and static project-owned links, are registered: seven Couriway-labelled rooms/sectors, two Cave of Despair maps, Mountain Top, and the Scorched Slab Ultra Space room. They are construction-only visual destinations, without donor story, trainers, legendary quests or rewards. Fourteen new scientists/notices are present. The canonical extra entrances are Route119 (20,5) and Scorched Slab (7,2). Remove their scientists in a test copy to open the reviewed links; this does not enable donor quest logic.

Exact Porymap names/group IDs are in registered_special_areas.csv. The three new section families are appended; older sections remain in position, MAPSEC_NONE=218 and MAPSEC_COUNT=240. Fifteen donor references remain deferred: dummy Petalburg story returns, Shoal Cave, Bellchime/Johto, future Sootopolis, an unresolved Allearth Forest arrival and nonreciprocal connections. Kanto/Johto/Sinnoh canonical migrations are not advanced.

## Verification

- All {v['editor_and_linked_hyper_maps_checked']} active Hyper maps and {v['tilesets_checked']} linked asset banks checked; {v['linked_objects']} objects, {v['linked_warps']} warps, {v['linked_connections']} connections.
- {v['protected_baseline_files']} protected baseline files checked. Earlier imports, both Route114 repairs and user Rustboro/Route104 cleanup remain intact.
- 1,038 surface water cells in the new routes retain source water elevation; no water-adjacent wildcard0 land bypasses. Source bridge elevation15/behavior0x70 remains deliberate.
- Connection boundaries have 3 compatible pairs from Route118→119, 4 from Route119→Fortree and 3 from Fortree→Route120.
- Eleven new special maps have static entry/return paths; this is a graph check, not all-room pathfinding or runtime proof.
- Prior animation callbacks pass the host sanitizer checks. Editor declaration/path checks pass for all 254 maps and 107 exposed Hyper tilesets. Reload Porymap before saving updated registries.

ROM SHA256: `{v['rom_sha256']}`.

Use runtime_checklist.md, geometry_validation.json, connection_boundary_validation.json, coordinate_remap_ledger.json and validation.json. Stop for runtime confirmation.
""")
 (OUT/'runtime_checklist.md').write_text("""# Canary #7 runtime checklist

Load the supplied ROM and a save copy. Runtime verification is pending.

- [ ] Route118→119→Fortree→120 crossings and return trips; native Route120→121 boundary remains usable with Route121 unchanged.
- [ ] Route119 water edges block walking; Surf entry/travel/exit, waterfall behavior and bike bridges above/under water work. Rain, tall grass, terrain animations and elevation transitions remain correct.
- [ ] Weather Institute before/after Aqua: blockers, both floors/stairs, trainers/Admin, bed healing, Castform with free/full party, reward/progression and return visit after saving.
- [ ] Route119 rival scene for both player genders and both trigger columns (25,31)/(26,31): bike approach, on-foot battle, Fly reward, departure, Scott scene, later state and save/reload.
- [ ] Route119/120 trainers, berries, item balls, relocated hidden items, signs and Secret Power/base entrances retain rewards/flags. Scorched Slab TM is at (7,3).
- [ ] Fortree every Center/Mart/house/Decoration Shop entrance and exit; purchase/cancel, healing, trades/gifts, Wingull delivery and rooftop walkways/ladders/underpasses.
- [ ] Fortree Gym stays blocked by native Kecleon until Devon Scope; reveal/flee animation and return/save state. Gym rotating gates, all trainers, Winona, badge/TM/full-bag and rematches.
- [ ] Route120 Steven/Devon Scope scene from both sides; bridge Kecleon appearance/battle and flags, bridge/water tile restoration before/after scene; other Kecleon interactions.
- [ ] Route120 weather bands, water/shorelines, ledges, bridge layers, Scorched Slab and Ancient Tomb entrances.
- [ ] Ancient Tomb before/after Sealed Chamber; braille/puzzle at (8,25), native wall opening, Registeel appearance/battle/capture/defeat flags and save/reload. Native Registeel graphic is retained.
- [ ] Construction scientists at Route119 (20,5) and Scorched Slab (7,2) block only extras. Native routes, Institute, TM and Registeel access remain usable.
- [ ] Reload Porymap; open all 18 canonical and 11 special maps from the inventory. Verify real geometry, collision, event overlays, groups/mapsecs and manual editing.
- [ ] In a test copy, remove the relevant scientists, rebuild, visit/return through actual Couriway rooms/sectors, Cave of Despair, Mountain Top and Ultra Space. Internal static warps work; donor puzzles/quests/rewards remain absent.
- [ ] Deferred story/foreign exits remain closed; scientists do not imply a missing active link exists.
- [ ] Both player genders, native dynamic rival graphics, blackout/heal/Fly, save/reload and native encounter ownership.
- [ ] Regression: Route114 shore repairs, prior northwest maps, New Mauville/Abandoned Ship/Island Cave, through-Mauville world, Rustboro/Route104 cleanup and validated Unova/Galar imports.

Stop after Canary #7 and report failures with map, coordinates, direction and progression state.
""")
 print('Published 29-map inventory and runtime checklist.')
if __name__=='__main__':publish()
