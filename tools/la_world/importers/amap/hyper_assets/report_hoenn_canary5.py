#!/usr/bin/env python3
"""Publish the actual northwest Hoenn registry, donor references, review queue and runtime checklist."""
import csv,json,collections
import hoenn_canary5 as C
ROOT=C.ROOT;OUT=C.OUT

def csvout(path,rows):
 if not rows:return
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def publish():
 r=C.load(OUT/'receipt.json');led=C.load(OUT/'coordinate_remap_ledger.json');validation=C.load(OUT/'validation.json');groups=C.load(ROOT/'data/maps/map_groups.json');layouts={z['id']:z for z in C.load(ROOT/'data/layouts/layouts.json')['layouts']};loc={n:(g,gi,mi) for gi,g in enumerate(groups['group_order']) for mi,n in enumerate(groups[g])};rows=[];details=[]
 for n,k in [*C.ALL_TARGETS.items(),*((n,k) for k,n in r['registered_special_maps'].items())]:
  m=C.load(ROOT/f'data/maps/{n}/map.json');l=layouts[m['layout']];d=C.source(k);g,gi,mi=loc[n];special=k in r['registered_special_maps'];mode='REGISTERED_ASSET_ONLY_CONSTRUCTION' if special else 'KEEP_NATIVE_RUNTIME_LAYOUT' if n in C.KEEP else 'CANONICAL_HYPER_ASSETS_NATIVE_GAMEPLAY';row={'map':n,'canonical_id':m['id'],'donor':'Hyper Emerald 5.7 EN QoL','donor_id':k,'donor_name':d['name'],'group':g,'group_id':gi,'map_id':mi,'mapsec':m['region_map_section'],'map_type':m['map_type'],'width':l['width'],'height':l['height'],'primary_tileset':l['primary_tileset'],'secondary_tileset':l['secondary_tileset'],'object_events':len(m['object_events']),'warp_events':len(m['warp_events']),'coord_events':len(m['coord_events']),'bg_events':len(m['bg_events']),'connections':len(m['connections'] or []),'source_object_events':len(d['npcs']),'source_warps':len(d['warps']),'source_header':d['header_pointer'],'source_layout':d['layout_pointer'],'layout_sha256':C.digest(ROOT/l['blockdata_filepath']),'border_sha256':C.digest(ROOT/l['border_filepath']),'mode':mode,'runtime_status':'PENDING_USER_TEST','script_owner':'PROJECT_CONSTRUCTION_ONLY' if special else 'POKEEMERALD_EXPANSION','reason':C.KEEP.get(n,'Actual special geometry registered; static project links and construction scientists; donor gameplay excluded.' if special else 'Inspected geometry, native event ledger and private behavior/coordinate reconciliation; expansion progression retained.')};rows.append(row);details.append({**row,'events':{kind:m[kind] for kind in ['object_events','warp_events','coord_events','bg_events']},'connections_detail':m['connections'],'source_reference_counts':d['event_counts'],'source_map_script_pointers':d.get('map_scripts',[]),'layout_record':l})
 csvout(OUT/'northwest_hoenn_inventory.csv',rows);csvout(OUT/'registered_special_areas.csv',[x for x in rows if x['mode'].startswith('REGISTERED')]);csvout(OUT/'canonical_replacement_maps.csv',[x for x in rows if not x['mode'].startswith('REGISTERED')]);queue=[]
 def issue(n,k,index,dest,reason,status='QUARANTINED_REFERENCE_ONLY'):
  queue.append({'map':n,'donor_id':k,'source_record':index,'destination':dest,'status':status,'reason':reason})
 for e in led['blocked_external_links']:issue(r['registered_special_maps'].get(e['from'],''),e['from'],'foreign family',e['to'],e['name']+' is outside this Hoenn asset batch; no foreign gameplay migration.')
 active_ids=set(r['donor_ids'].values())|set(r['registered_special_maps']);active_ids.update(k for k,n in [(x['donor_id'],x['canonical_name']) for x in C.load(C.P.OUT/'sea_corridor_correction_manifest.json')['maps']])
 for number in [1,2,3,4]:active_ids.update(C.load(ROOT/f'.la_work/amap/hyper_hoenn_canary{number}/receipt.json')['donor_ids'].values())
 for k,n in r['registered_special_maps'].items():
  for w in C.source(k)['warps']:
   key=k+'.'+str(w['index']);registered=key in led['warp_correspondence']
   if w['x']==w['y']==0:issue(n,k,w['index'],w['target_id'],'Placeholder (0,0) slot needs donor script repositioning; no donor script copied.')
   elif w['target_id'] in active_ids and not any(a['index']==w['dest_warp_id'] for a in C.source(w['target_id'])['warps']):issue(n,k,w['index'],w['target_id'],'Declared destination warp slot is absent in export; entrance held behind project construction notice.')
   elif w.get('dynamic_target'):issue(n,k,w['index'],w['target_id'],'Donor dynamic gameplay return semantics excluded; only reviewed static project link, if present, is active.','STATIC_PROJECT_RETURN_REVIEW')
   elif not registered and w['target_id'] not in active_ids:issue(n,k,w['index'],w['target_id'],'Foreign-area donor exit not activated in this batch.')
 for e in led.get('withheld_connections',[]):issue(e['map'],'',e['source_connection']['direction'],e['source_connection']['map'],e['reason'])
 for n in r['registered_special_maps'].values():
  m=C.load(ROOT/f'data/maps/{n}/map.json')
  for i,w in enumerate(m['warp_events']):
   if w['dest_map']==m['id'] and int(w['dest_warp_id'])==i:issue(n,'',i,m['id'],'Source self-return placeholder is not a usable new gameplay route; construction-area portal needs manual authoring.','MANUAL_PORTAL_REVIEW')
 csvout(OUT/'manual_review.csv',queue)
 manifest={'schema':'hyper-hoenn-northwest-and-special-registration-v1','canonical_maps_replaced':len(r['canonical_maps_replaced']),'native_runtime_layouts_kept':C.KEEP,'registered_special_maps':len(r['registered_special_maps']),'runtime_verified':False,'maps':details,'manual_review':queue,'special_graph_validation':C.load(OUT/'special_graph_validation.json'),'project_warp_reconciliations':led.get('project_warp_reconciliations',[]),'ownership':'Hyper geometry/assets; expansion canonical gameplay; project-owned construction notices/static special links only.','validation':{k:v for k,v in validation.items() if k!='maps'}};C.dump(OUT/'northwest_hoenn_replacement_manifest.json',manifest)
 counts=collections.Counter(x['donor_name'] for x in rows if x['mode'].startswith('REGISTERED'));families='\n'.join(f'| {n} | {count} |' for n,count in sorted(counts.items()));new_gates=sum(not e['existing'] for e in led['construction_gates']);lines=f'''# Hoenn northwest batch and actual special-area registration

Status: source implementation and linked-ROM/asset checks passed; this batch awaits in-game confirmation. Through Mauville remains user verified.

## Completed scope

67 canonical replacements: Route 117 and Day Care, Verdanturf and interiors; Routes 111/112/113/114/115/118; Lavaridge and Fallarbor and progression interiors; cable stations, Mt. Chimney, Jagged Pass, Fiery Path, Meteor Falls and Steven's cave; Desert Ruins, Mirage Tower, Desert Underpass, Fossil Maniac/Lanette/Winstrate/rest/Glass Workshop; Magma Hideout rooms and Trainer Hill entrance/elevator.

Five Trainer Hill course/roof layouts stay native because expansion generates playable courses at runtime. Their canonical destinations and gameplay remain intact.

63 real special maps are registered with geometry, borders, tilesets, map IDs, groups, map sections, editor-visible declarations, project construction scientists and static project links. Earlier entrance-only reservations now have real destinations. Existing Native Hoenn boundaries are preserved; the reciprocal western Dewford/Route 106 extension is appended. No Hyper story/NPC/quest/save scripts were transplanted.

| Registered donor family | Maps |
|---|---:|
{families}

## Editor use and opening areas

Reload the project in Porymap. Existing canonical names stay in their normal groups. Special names start `HyperHoenn_`; find exact group and map section in `registered_special_areas.csv`. Rooms reuse appropriate native groups/mapsecs where applicable; other families have appended `gMapGroup_HyperHoenn_*` and `MAPSEC_HYPER_*` entries. New map sections are labels without new Fly/heal destinations.

Scientists are project-owned construction notices. All 63 registered special maps have a static graph path from canonical maps and a return path, ignoring construction blockers. This verifies registry relationships, not in-game walkability of every room. Existing reserved entrance markers were retained and {new_gates} additional notices/blockers were registered across the new graph. For the western Dewford coast, deleting its construction scientists in Porymap also releases the project border guard after rebuilding; no collision wall needs to be erased. Keep boundaries/warps when removing blockers. Registered special areas have no donor trainers, gifts, legendary/quest scripts or donor encounters.

Opening an area enables its reviewed static geometry links, not its original Hyper quest. Shared donor portal returns use project-authored static Hoenn destinations. The manual queue lists foreign exits, script-positioned placeholder slots, missing export destinations and unresolved portals; removing a scientist does not implement those missing gameplay systems.

## Reviewed reconciliations

- Explicit native-role remaps on Routes 111/112/115, Lavaridge and a Verdanturf interior; full per-event before/after ledger retained.
- Route 117's third native berry plot uses adjacent inspected Hyper soil, preserving its berry identity/state.
- Native two-fossil Mirage Tower chamber and disappearing-tower Route 111 alternate layout preserved.
- Lavaridge rival/PC exit coordinate operands remapped; native Brendan/May graphics initializers, bike states, flags and script commands remain expansion owned.
- Lavaridge Gym steam-hole cells use functioning Hyper hole art/behaviors with native warp indices/destinations.
- Native-script metatile behaviors use map-local derivatives; shared asset banks remain unchanged.
- 32 script-dependent special portal cells retain identical Hyper artwork through private metatile duplicates with native static warp behavior.
- Meteor Falls/Steven postgame doorway and Terra Cave weather entrances remain native OnLoad-controlled, rather than being opened early.
- Rainbow Castle’s unique same-room portal pair has a project-owned reciprocal return instead of the donor self-return placeholder.
- Four copied one-way special connections conflict with authoritative native reciprocal boundaries and remain reference-only. Their maps are registered with warp access.

## Validation

Build: passed, 32 MiB padded ROM. {validation['editor_and_linked_hyper_maps_checked']} active Hyper maps checked in linked ROM, including geometry/borders, graphics, palettes, metatiles, behaviors, animation pointers, native script owners, {validation['linked_objects']} objects, {validation['linked_warps']} warps and {validation['linked_connections']} connections.

{validation['protected_baseline_files']} baseline source/asset files audited; {validation['native_owned_events_preserved']} native events retain all non-coordinate gameplay fields. Existing map group/map/layout numeric positions and old map-section IDs remain stable, including MAPSEC_NONE=218. Save/flags/vars, encounters, heal/Fly/blackout tables and validated BWA/SWSH sources remain protected.

20 animation callbacks / 18 pairs / 256 ticks per case passed AddressSanitizer and UndefinedBehaviorSanitizer checks (4,168 frame transfers). Scientist-driven connection guard passed 10 host cases. 22 native story movement paths checked, including Meteor Falls, Mt. Chimney, Route 118 Steven and Lavaridge rivals. Porymap declarations/paths checked for all 184 active Hyper maps; editor reload and visual cleanup remain user steps.

ROM SHA-256: `{validation['rom_sha256']}`.

See `runtime_checklist.md`, `coordinate_remap_ledger.json`, `registered_special_areas.csv`, `manual_review.csv`, and `northwest_hoenn_replacement_manifest.json`. Stop here for runtime confirmation; no further Hoenn batch has been advanced.
''';(OUT/'review.md').write_text(lines)
 (OUT/'runtime_checklist.md').write_text('''# Northwest Hoenn runtime checklist

This batch is not runtime verified yet. Use a save copy and the supplied Canary #5 ROM.

- [ ] Both player genders: rivals render correctly in Lavaridge (walking/bike), PC and herb-shop scenes; receive Go-Goggles with the native prerequisite/state.
- [ ] Mauville ↔ Route117 ↔ Verdanturf: transitions, trainers, items, all three native berry plots/growth, Day Care deposit/withdraw/fees/Egg handling.
- [ ] Wanda/Rusturf story, Verdanturf tent/interiors, healing, Mart buy/cancel, entrances/exits and Fly/blackout destinations.
- [ ] Route111: Winstrate sequence, Rock Smash gate before/after unlock, rest stop, Trainer Hill entrance/elevator and native generated courses; desert blocked before goggles and usable after.
- [ ] Route112/Fiery Path/Route113/Fallarbor: trainers, items, encounters, cable station progression, ash/glass workshop collection/rewards, Cozmo/Move Relearner/tent.
- [ ] Meteor Falls: Magma/Aqua/Cozmo scene completes without blocked actors; entrances from Routes114/115; all cave floors, Waterfall areas, postgame Steven doorway/battle state.
- [ ] MtChimney: cable animation/arrival/exit, opposing actors, Maxie/Archie paths, meteorite machine/reward state; Jagged Pass → Lavaridge.
- [ ] Lavaridge Gym: every steam-hole direction/landing, trainers, Flannery, badge/TM state. Test all gym warp pairs.
- [ ] Mirage Tower: both native fossils, choice state, collapse and absent-tower Route111 layout; Desert Ruins/Regi doorway remains correctly closed/open; Fossil Maniac and native Desert Underpass.
- [ ] Route114/Lanette/Route115: bridges, trainers, items, shore/cave transitions and native progression/weather hooks.
- [ ] Route118: western approach from Mauville, Good Rod reward/cancel/full-bag paths, Surf crossing, Steven trigger from all three columns, Gabby/Ty states, boundaries toward unmodified Route119/123.
- [ ] Magma Hideout: entrances, all floors, boulders, trainers, Groudon graphics/state, native progression if the appropriate save state is available.
- [ ] Collision/elevation: all route connections and land/water/ledge transitions; animated water/flowers/lava/ash/cave assets.
- [ ] Porymap: reload project, open each new canonical map and every registered special map from registered_special_areas.csv. Check correct tilesets, borders, layers, collision and events; manually clean art if desired.
- [ ] Construction entrances: Timeless Woods (Route102/103), Flower Paradise, western Dewford/coast extras, Champion Island, Devon basement/Dragonspiral and the new northern families show scientists and preserve ordinary Hoenn paths.
- [ ] In a separate working/test copy, remove the construction scientists at one paired portal and rebuild; enter/return through its actual registered special map. Do not treat quarantined foreign/missing/script-positioned exits as completed quests.
- [ ] In that test copy, remove the Dewford west-edge scientists and Route106 construction markers; Surf/walk across the real registered coast in both directions. Confirm ordinary Route106 ↔ Dewford remains usable with blockers present too.
- [ ] Save/reload in every town and selected cave/special map; blackout returns to correct native heal location; no flag/item/trainer/berry reset.
- [ ] Regression visits: Oldale/Mart, Petalburg/Rustboro/Devon, sea Routes105/107/108, Dewford/Granite Cave, Slateport/Museum/Shipyard/Route110/Mauville; validated Unova Nuvema batch and Galar Postwick batch.

Stop after this batch. Report runtime failures with map name, coordinates/warp, player gender and progression state. Do not activate foreign regions or transplant Hyper quest scripts to fix a visual issue.
''')
 print('Published',len(rows),'map inventory rows and',len(queue),'manual-review records.')
if __name__=='__main__':publish()
