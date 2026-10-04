# Hyper Hoenn Canary #9 — eastern sea and League

Previous Canary #8 runtime success was confirmed by the user. This batch passed build/static validation and the user confirmed Canary #9 runtime success on2026-10-04.

## Scope

**116 canonical maps**: Routes124–134, Mossdeep/all interiors and Space Center, Shoal Cave both tide layouts/ice room, Sootopolis and normal services/gyms, Ever Grande/League/Hall of Fame, Victory Road, Pacifidlog/all interiors, Aqua Hideout, Seafloor Cavern, Cave of Origin, Sky Pillar, connected underwater sectors, Sealed Chamber, Marine/Terra cave state destinations and Route124 treasure hunter house.

**22 actual construction-only special maps**: Outer Space, Basement, extra Victory Road rooms, Test of Heart, Ultra Alliance, Steven’s Island family, Distortion World, Sootopolis extra rooms and Ancient Retreat. Geometry/assets, append-only groups/mapsecs, static links and 38 notices are present. Existing special destinations are reused where their reviewed arrival is known. Foreign Sinnoh exits remain closed; no foreign canonical migration is performed.

Canonical MAP_* constants, existing layout IDs, native scripts/progression/flags/vars/encounters, native dynamic graphics initializers, original warp destinations/connections and save ABI are authoritative. All earlier core source files, user cleanup, BWA/SWSH imports and the Route110/114/119 repairs are protected by the current baseline. Native story objects receive only ledger-reviewed position/elevation changes.

## Reconciliation

- 897 original event records and 116 native script owners checked. No donor gameplay scripts, quest flags, save bridge or imported-map wrappers are added.
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

ROM build passed. Linked verification checked **438 active Hyper maps**, 102 banks, 1962 objects, 1462 warps and 156 connections. Eight alternate layouts are linked correctly. Animation host checks passed under address/undefined sanitizers. Porymap declaration/path checks passed for438 maps and127 tilesets.

MAPSEC_NONE remains218; MAPSEC_COUNT is247. Existing numeric map/group/layout/section positions are preserved. The original map-group maximum remains within the native ABI. ROM SHA256: `1cf46c162fc335de6a1db9996b92bd5f6e15a353c7da3b620bd63438781d4800`.

See runtime_checklist.md, maps_inventory.csv, canonical_replacements.csv, registered_special_areas.csv, manual_review.csv, keep_expansion_original.csv, eastern_hoenn_manifest.json, coordinate_remap_ledger.json and validation.json. Reload Porymap before saving. Canary #9 runtime success is user-confirmed; the two deferred special ingresses remain documented holds.
