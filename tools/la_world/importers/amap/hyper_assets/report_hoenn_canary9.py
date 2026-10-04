#!/usr/bin/env python3
"""Publish final eastern Hoenn reconciliation inventory and runtime checklist."""
import csv,collections,json
import hoenn_canary9 as C
ROOT=C.ROOT;OUT=C.OUT

def writecsv(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def publish():
 receipt=C.load(OUT/'receipt.json');v=C.load(OUT/'validation.json');ledger=C.load(OUT/'coordinate_remap_ledger.json');ls={z['id']:z for z in C.load(ROOT/'data/layouts/layouts.json')['layouts']};groups=C.load(ROOT/'data/maps/map_groups.json');locations={n:(g,gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])};rows=[];details=[]
 for n,k in [*C.TARGETS.items(),*((n,k) for k,n in receipt['registered_special_maps'].items())]:
  m=C.load(ROOT/f'data/maps/{n}/map.json');l=ls[m['layout']];d=C.P.source(k);g,gi,mi=locations[n];special=k in receipt['registered_special_maps'];row={'map':n,'map_constant':m['id'],'donor':'HYPER_EMERALD_5_7_EN_QOL','donor_id':k,'donor_name':d['name'],'group':g,'group_id':gi,'map_id':mi,'mapsec':m['region_map_section'],'width':l['width'],'height':l['height'],'map_type':m['map_type'],'primary_tileset':l['primary_tileset'],'secondary_tileset':l['secondary_tileset'],'objects':len(m['object_events']),'warps':len(m['warp_events']),'coords':len(m['coord_events']),'bg':len(m['bg_events']),'connections':len(m['connections'] or []),'source_header_pointer':d['header_pointer'],'source_layout_pointer':d['layout_pointer'],'source_blockdata_pointer':d['blockdata_pointer'],'blockdata_sha256':C.digest(ROOT/l['blockdata_filepath']),'border_sha256':C.digest(ROOT/l['border_filepath']),'mode':'CONSTRUCTION_ASSET_ONLY' if special else 'CANONICAL_HYPER_ASSETS_NATIVE_GAMEPLAY','owner':'PROJECT_CONSTRUCTION_ONLY' if special else 'POKEEMERALD_EXPANSION','runtime_status':'PENDING_USER_TEST'};rows.append(row);details.append({**row,'layout':l,'events':{kind:m[kind] for kind in C.P.KINDS},'connections_detail':m['connections'],'donor_event_counts':d['event_counts'],'donor_scripts_reference_only':d.get('map_scripts')})
 writecsv('maps_inventory.csv',rows);writecsv('canonical_replacements.csv',[z for z in rows if z['mode'].startswith('CANONICAL')]);writecsv('registered_special_areas.csv',[z for z in rows if z['mode'].startswith('CONSTRUCTION')]);manual=[{'map':z['map'],'source':z['source'],'destination':z['record'].get('target_id',''),'destination_name':z['record'].get('target_name',''),'status':'DEFERRED_NO_ACTIVE_LINK','reason':z['reason']} for z in ledger['deferred_references']];writecsv('manual_review.csv',manual)
 (OUT/'review.md').write_text(f"""# Hyper Hoenn Canary #9 — eastern sea and League

Previous Canary #8 runtime success was confirmed by the user. This batch is built/static-verified; emulator runtime testing is pending.

## Scope

**116 canonical maps**: Routes124–134, Mossdeep/all interiors and Space Center, Shoal Cave both tide layouts/ice room, Sootopolis and normal services/gyms, Ever Grande/League/Hall of Fame, Victory Road, Pacifidlog/all interiors, Aqua Hideout, Seafloor Cavern, Cave of Origin, Sky Pillar, connected underwater sectors, Sealed Chamber, Marine/Terra cave state destinations and Route124 treasure hunter house.

**22 actual construction-only special maps**: Outer Space, Basement, extra Victory Road rooms, Test of Heart, Ultra Alliance, Steven’s Island family, Distortion World, Sootopolis extra rooms and Ancient Retreat. Geometry/assets, append-only groups/mapsecs, static links and {len(ledger['construction_gates'])} notices are present. Existing special destinations are reused where their reviewed arrival is known. Foreign Sinnoh exits remain closed; no foreign canonical migration is performed.

Canonical MAP_* constants, existing layout IDs, native scripts/progression/flags/vars/encounters, native dynamic graphics initializers, original warp destinations/connections and save ABI are authoritative. All earlier core source files, user cleanup, BWA/SWSH imports and the Route110/114/119 repairs are protected by the current baseline. Native story objects receive only ledger-reviewed position/elevation changes.

## Reconciliation

- {v['native_owned_events_preserved']} original event records and {v['native_maps_with_preserved_scripts']} native script owners checked. No donor gameplay scripts, quest flags, save bridge or imported-map wrappers are added.
- League entrance source event metadata points at a wall. Native slots2/3 now use the actual source doors at (9,1)/(10,1); native guards stay at y2 and own admission. League layout grows from19×12 to19×16. Existing nurse/blackout ownership is retained.
- SkyPillar1F source stair (10,1) was blocked by a donor-only quest flag. Its inspected unlocked Hyper tile0x244/native behavior is used directly; native Rayquaza state controls the clean layouts and cracking-floor callbacks.
- All eight native story-switched layouts now use their referenced Hyper asset geometry: Sootopolis legends battle, Route131 Sky Pillar entrance and six clean Sky Pillar floors/top. Canonical identities and branching commands are unchanged. Shoal tide layouts also retain native RTC switching.
- Both native Gym collision/behavior grids exactly match their canonical puzzle grids. Mossdeep moving statues/turntables and Sootopolis ice/stair callbacks stay native. Sky Pillar cracked-cell fall arrivals are statically inspected.
- The dormant donor Aqua pad at (31,4) retains identical art with map-local native teleport behavior. Native teleporter destinations and puzzle slot ownership remain intact.
- **28,740 surface-water cells** checked.46 donor elevation anomalies are corrected to sea elevation1 without changing their art/collision. Native water/land levels are never blindly copied over Hyper geometry.
- Six unsafe source Dive cells retain their art with Surf-only behavior.838 UnderwaterRoute126 cells below blocked/nonwater surface geometry retain identical art with native no-surfacing behavior. Every active explicit Dive/emerge connection pair is checked against its destination cell.
-38 directed cardinal boundaries checked. Metadata-only underwater seams that were already fully closed in expansion remain closed; they are reached by native Dive rather than invented tunnels.
- Distortion World donor quest warps formed a closed loop. Reviewed arrival (38,12) has a project-owned static return to Route129; native Route129 destinations are not rebound.
- Reused the prior proven secondary08305DE0 bank for Distortion/Ancient Retreat, with exact prior graphics/palettes and regenerated semantic behaviors. It has no animation callback; existing animated banks retain their proven callbacks.

## Explicit holds

The two existing Mystery Events House maps stay expansion-original: the source15.13 is an empty/dormant counterpart and its alternate layout is structurally unsuitable. They are not part of the main Emerald story route.

Actual extra room37.121 and Ancient Retreat37.120 are registered and Porymap-editable, with static return paths, but their Hoenn ingress is **deferred**. Their donor entrance would replace Sootopolis’s authoritative Mystery Events House door. No duplicate warp or scientist blocks that canonical door. Removing their scientists alone does not create a new Hoenn ingress. This requires a reviewed new entrance later; these are listed explicitly in manual_review.csv.

Other foreign, conflicting or unresolved donor links are construction/reference holds, not transplanted quest/story destinations. Battle Frontier, link facilities, unused R/S floors and foreign regions remain outside this main-story batch.

## Validation and artifacts

ROM build passed. Linked verification checked **{v['editor_and_linked_hyper_maps_checked']} active Hyper maps**, {v['tilesets_checked']} banks, {v['linked_objects']} objects, {v['linked_warps']} warps and {v['linked_connections']} connections. Eight alternate layouts are linked correctly. Animation host checks passed under address/undefined sanitizers. Porymap declaration/path checks passed for438 maps and127 tilesets.

MAPSEC_NONE remains218; MAPSEC_COUNT is247. Existing numeric map/group/layout/section positions are preserved. The original map-group maximum remains within the native ABI. ROM SHA256: `{v['rom_sha256']}`.

See runtime_checklist.md, maps_inventory.csv, canonical_replacements.csv, registered_special_areas.csv, manual_review.csv, keep_expansion_original.csv, eastern_hoenn_manifest.json, coordinate_remap_ledger.json and validation.json. Reload Porymap before saving. Stop after Canary #9 for runtime feedback.
""")
 (OUT/'runtime_checklist.md').write_text("""# Hoenn Canary #9 runtime checklist

Use this ROM with a normal save copy. Re-enter/reload maps to refresh cached objects. Build/static verification is complete; these are in-game checks.

- [ ] Lilycove→Route124→Mossdeep→Route125; Route126/Sootopolis; Routes127/128/EverGrande; Routes129–134/Pacifidlog/Slateport and return. Check shore edges on foot, Surf entry/travel/exit, waterfall and strong currents.
- [ ] All sea-route trainers/doubles, items/hidden items, rocks, signs, treasure hunter shard exchange and encounters. Specifically check the corrected Route127/133 water elevations.
- [ ] Dive and Surface throughout Routes124/126/127/128; travel to Sootopolis and Seafloor Cavern; no surfacing into the island/rocks and no diving into underwater walls. Weather-created Marine/Terra entrances retain native availability and return semantics.
- [ ] Mossdeep Center/Mart/houses/King's Rock/Wingull/Beldum, HM Dive reward, Space Center both floors, native Magma scene and Steven multi-battle, both genders/starter branches, flags and return visits.
- [ ] Mossdeep Gym moving statues/buttons/warps/trainers, Tate/Liza double battle, badge/TM reward, leave/re-enter/save/reload.
- [ ] Shoal Cave high/low tide changes, both entrances/interior layouts, timed salt/shell renewal, Shell Bell full-bag/cancel cases, boulders/Strength/sliding ice/Never-Melt Ice and static return paths.
- [ ] Aqua Hideout stairs and full teleporter maze, dormant pad (31,4), items/Electrode/Master Ball, submarine escape, native Matt battle and later visits; Lilycove Wailmer blockade clears normally.
- [ ] Seafloor Cavern all rooms, Surf/currents/Rock Smash/Strength boulder puzzles, Archie/Kyogre/Maxie scene, orb/weather progression and entrance/underwater return.
- [ ] Sootopolis legends confrontation/Rayquaza scene, closed/open house/Gym doors, Steven/Wallace walks, Cave of Origin and Sky Pillar directions, native Dive entry/exit, both normal and legends-battle layouts.
- [ ] Sootopolis Gym ice step counters/cracking/falling/stair unlocks, trainers/Juan, badge/TM/Waterfall ownership and re-entry. Every town service/gift/house works; Mystery Events House remains original.
- [ ] Pacifidlog logs/bridges, Center/Fly/blackout, houses/trades/Hidden Power/Mirage Island checks; Route131→Sky Pillar and western-current path to Sealed Chamber.
- [ ] Sky Pillar early clean story ascent and later Mach Bike cracked-floor puzzle, every stair/fall/landing, Wallace/Rayquaza wake scene, Rayquaza encounter state, source stair (10,1) never requires a Hyper quest flag.
- [ ] Sealed Chamber Dive path/braille/Dig and party-order puzzle, Regi unlock flags and previous three Regi cave visits.
- [ ] Ever Grande waterfall/Center/Fly arrivals, Victory Road Wally entry/exit scenes, all trainers/items/boulders/bridges/Surf/Waterfall/Flash and normal native encounters.
- [ ] League lobby door guards/badge prerequisite, stairs/nurse/shop/purchase/cancel/blackout, Elite Four room chain/locked doors/champion, Hall of Fame/credits/postgame save and later rematches.
- [ ] Marine/Terra Cave availability, legendary scenes/capture/run/defeat, dynamic exits, weather and save/reload before/after story updates.
- [ ] Inspect all116 changed canonical maps and22 registered specials in reloaded Porymap. In a test copy remove relevant entrance scientists and rebuild: verify entered construction areas have usable static returns, including Distortion→Route129. No Hyper quests are active.
- [ ] Registered Sootopolis extra37.121/Ancient Retreat37.120 have deferred Hoenn ingress; inspect their assets in Porymap. Do not assume removing notices creates the unresolved entrance or opens foreign Sinnoh links.
- [ ] Collision/elevation/shorelines, flowers/water/terrain/tileset animations, both player genders, native dynamic graphics, blackout, Fly, save/reload.
- [ ] Regression visits: Canary8/Lilycove/MtPyre/Safari, Fortree Gym/Route120 Scope, Route119 Institute/bridges, Route110 Cycling Road/water, Route114 water edges, Rustboro/Route104 manual cleanup, New Mauville/Abandoned Ship/earlier Hoenn and validated Unova/Galar imports.

Stop after Canary #9. Report map/coordinates/direction/story state for any failure. Main-story mapping is staged through the League; runtime confirmation is still required.
""")
 writecsv('keep_expansion_original.csv',[{'map':'SootopolisCity_MysteryEventsHouse_1F','reason':'Empty donor counterpart / incompatible alternate geometry; preserve native optional-event house.'},{'map':'SootopolisCity_MysteryEventsHouse_B1F','reason':'Preserve paired native optional-event room and all semantics.'}])
 C.dump(OUT/'eastern_hoenn_manifest.json',{'schema':'hyper-hoenn-canary9-v1','canonical_maps':len(C.TARGETS),'special_maps':len(receipt['registered_special_maps']),'native_gameplay_owner':'pokeemerald-expansion','hyper_gameplay_imported':False,'runtime_verified':False,'maps':details,'alternate_layouts':receipt['alternate_layouts'],'dive_reconciliations':receipt['dive_reconciliations'],'manual_review':manual,'validation':v})
 print('Published138-map inventory and final-Hoenn runtime checklist.')
if __name__=='__main__':publish()
