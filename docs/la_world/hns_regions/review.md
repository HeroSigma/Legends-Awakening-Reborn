# Heart & Soul Kanto/Johto placeholder exploration

505 maps are registered with native Reborn layouts and Porymap declarations. New Game starts in New Bark Town. The project's Kanto travel option leads to Pallet Town. Each active map has inspection travel to the next preserved map.

## Coverage

| Category | Maps |
|---|---:|
| Johto towns/routes | 31 |
| Kanto towns/routes | 40 |
| Johto interiors | 122 |
| Kanto interiors | 110 |
| Dungeons, including associated Artisan Cave floors | 93 |
| Side areas/facilities | 99 |
| Quarantined reference layouts | 10 |
| Total | 505 |

Alola and Sinjoh stay outside this migration. Reference maps remain registered and editable; normal travel and the inspection circuit skip them.

## Objects and ownership

4,093 donor object records are preserved in object_event_ledger.json: 3,909 visible placeholders and 184 dormant overlapping, unresolved dynamic or off-map actors. Overlapping positions show one actor; alternatives remain editable in Porymap. Original positions, artwork, scripts, flags and complete event records remain in the reference ledger.

NPCs, trainers, leaders, item objects and berry objects use project construction dialogue. Battles, rewards, donor flags/variables, progression and donor map scripts are disabled. Static facing replaces donor movement routines. 975 BG markers use harmless interactions; 524 coordinate markers remain dormant.

504 dedicated scientists supply inspection travel. One map at the native 64-object limit reuses an existing placeholder for inspection travel. All prior map/group/layout numeric positions remain unchanged.

## Assets and travel

150 normalized tileset combinations preserve graphics, palettes, metatiles, borders and translated attributes. Source 640/384 banks are normalized to Reborn's 512/512 format without changing global tile/metatile IDs. Three-layer definitions use the existing native format. Animation callbacks use the native queue and counters. 134 static art selectors are recovered; Pokemon use Reborn's species bridge.

1,345 static warp records and 199 connections stay within the new region. Artisan Cave and shared-facility returns use HnS copies, preserving canonical Hoenn destinations.

Nine source travel records remain held in blocked_travel.json:
- Three prototype entrances and one deferred Sinjoh entrance.
- Two multiplayer-room dynamic exits without a normal incoming parent.
- Two obsolete Fuchsia/Route 19 gate exits referencing missing destination indices.
- One S.S. Aqua exit referencing a nonexistent Olivine port warp.

Their maps remain preserved and inspectable; destination indices were not invented. Facilities are placeholders: elevators, ship schedules, multiplayer, contests, Safari admission, Frontier rules and story-dependent Gym puzzles require later project gameplay work.

Bellchime Trail's donor-only falling-leaf weather is deferred. League rooms use native battle-scene presentation. Hall of Fame retains the donor's unusual ice/button floor attributes for manual review; its progression script is absent.

Documented behavior equivalents remain in behavior_translation.json: headbutt trees use normal terrain; special bookshelves/shelves use native interactions; north-restricted grass/cave use native terrain; water north-arrow uses the native north-arrow warp; ice bridge uses the native low pond bridge. Custom donor mechanics are inactive.

## Validation

- ROM build and native three-layer asset checks pass.
- 15,591 preexisting map/layout/asset files remain unchanged. Six normal generated map/layout tables are regenerated.
- All existing map/group/layout numeric positions are retained.
- Native mGBA load/render sweep: 505/505 maps pass.
- Actual outdoor Mart/Gym entry movement, both genders: 56/56 pass.
- Hidden variants, harmless interactions, stairs and animation checks: 111/111 pass.
- Compiled Kanto travel branch reaches Pallet Town.
- RAM remains 230,364 bytes EWRAM and 28,140 bytes IWRAM. Linked ROM usage: 32,136,208 bytes.

This establishes placeholder exploration. It does not claim every stair, puzzle or cell has been manually played. Runtime JSON and per-map screenshots provide the exact coverage.

## Editing and follow-up

Reopen Porymap to refresh the new declarations. Inspect dormant alternatives and held links before assigning gameplay. Start a new game for the configured New Bark exploration start. Existing saves keep their saved location.

Staging refuses to overwrite an existing manifest, protecting subsequent Porymap edits. The pre-change archive and protected-file hashes are under .la_work/amap/hns_regions_backup. Reusable tools are under tools/la_world/importers/amap: stage_hns_regions.py, hns_region_assets.py, hns_region_objects.py and verify_hns_regions.py.
