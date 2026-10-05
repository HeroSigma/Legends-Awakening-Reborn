# Hyper Sinnoh: assets and project travel

Implemented after Hoenn finalization. This is an additive asset/travel migration, not a Sinnoh story implementation. Hyper gameplay scripts, NPC scripts, progression state, flags/variables and save logic were not imported. Existing expansion gameplay and BWA/SWSH imports remain authoritative and protected.

## Registered world

212 new Sinnoh maps plus the already registered Distortion World form 213 regional assets. Three additional actual Hoenn special aliases (two Outer Space scenes and Champion Island harbor) complete outstanding special-area registration without replacing native Birth/Navel Island identities. All 215 newly registered maps are included in the ROM, in Porymap groups, and in the project travel graph with a structural return path.

The regional spine includes Twinleaf, Sandgem, Jubilife, Oreburgh, both Floaroma sectors, Eterna, Hearthome, Solaceon, Veilstone, Celestic, Pastoria, Canalave, Snowpoint, Sunyshore and the Sinnoh League; Routes201–223, split route sectors, lakes, forests, caves, Coronet, Spear Pillar, ruins, Galactic facilities, Safari and other connected interiors are inventoried by donor identity. Duplicate names do not collapse distinct source sectors/floors. `regional_spine.csv` captures group36 surface maps; `full_inventory.csv` includes all additions. `canonical_flag=false` means no existing expansion canonical identity was replaced.

Four previously proven graphics/palette/behavior banks were ported from the earlier Legends Awakening recovery, including the Sinnoh animation callback. Source geometry, borders, tilesets and translated behaviors are retained, with explicit collision/portal corrections in the manifest. 149 surface-water cells use native Surf elevation1; static project portals use private same-art metatiles instead of donor gameplay callbacks.

## Travel and construction

Talk to the annex scientist inside Sootopolis's Mystery Events house and select Yes to arrive in Oreburgh at49,8. Cancel stays in the native house. Oreburgh's scientist at50,8 offers a return to the house at10,6. Native house actors, street door, west stairs, visiting-trainer state and story script prefix are preserved.

Ancient Retreat also links to the inspected Oreburgh street arrival. This arrival is deliberately an ordinary floor cell, not an invisible return teleport. The scientist provides explicit return travel. Active Oreburgh house entrances remain intact; roof/dummy donor metadata is not reused as a door.

Three explicit inspection offers connect the alternative Coronet/Spear Pillar scenes and Champion Island harbor. Construction scientists remain project-owned gates/notices. Actual special maps are registered, not just represented by blocking NPCs. Physical route/door/cave paths still require in-game review; graph reachability does not prove every seam is walkable with construction NPCs present.

Sinnoh's saved met-location uses the existing byte-sized regional section, with individual current-map popup names verified in the linked ROM. No save structure was widened. New regional music/weather are project defaults. Sinnoh trainers, wild encounters, shops, heals/Fly registrations, NPC services, rewards and quests are deferred to project gameplay work; this phase intentionally provides assets and travel only.

## Manual review

27 invalid donor metatile references in Veilstone interiors37.29/37.30/37.31 are replaced with inspected existing solid construction props. Exact original/replacement cells are recorded; raw donor assets remain intact. These three maps have MEDIUM confidence until art cleanup. HIGH confidence describes asset correspondence, not runtime validation.

Four unlinked/obsolete prototypes are quarantined:37.0 duplicate Jubilife interior,37.36 obsolete Safari template,37.50/37.51 Mauville battle templates. The actual linked Pastoria gate37.117 is registered. The manual queue also retains32 source travel references, including foreign/scripted placeholders, missing arrival slots and explicit resolved parent-return decisions. Kanto/Johto travel was not advanced.

## Validation

ROM build passed. Linked assets/events checked across780 Hyper maps and213 linked tileset variants;2,681 objects,2,577 warps and262 connections match current source.30,160 canonical indoor cells retain native collision/elevation/behavior contracts. Animation checks passed21 unique callbacks and29 paired combinations for256 ticks each under AddressSanitizer/UndefinedBehaviorSanitizer, exercising6,252 frame transfers.

32,090 baseline file hashes plus new registered assets are protected by the exact receipt chain. Original map group/order prefixes, canonical IDs, layout IDs, map sections and native gameplay ownership passed. The combined construction-gate audit checked407 scientists, including canonical entrance gates; the additive-map scientist audit checks335 placements. All215 new maps have structural ingress and project return; the inert street arrival is excluded from the return graph. Porymap PNG/palette companions exist for the new banks. Final ROM:32MiB padded; linked30,139,264 bytes. EWRAM226,424 bytes; IWRAM28,384 bytes.

SHA-256:`4164b8c26f3a4a19746c7a7c3f8592ae71ce0b33ac9c46fa7f96456d881521fd`.

This batch has passed source/build/ROM/animation checks. In-game runtime testing remains pending. See `runtime_checklist.md` before approving further regional gameplay work.

## Reproduce

Build with `make BUILD_NAME=emerald-sinnoh-assets -j4`. Run the two verifiers under `tools/la_world/importers/amap/hyper_assets/`: `verify_hyper_region_rom.py --rom-stem pokeemerald-sinnoh-assets`, then `verify_sinnoh_asset_travel.py`. Their receipts check the applied state; do not rerun either migration's apply mode over an existing receipt. Later intentional manual edits should receive an explicit reviewed receipt update rather than bypassing protected hashes.

## Oreburgh exit correction

The initial registry exceeded the signed native map-ID limit. New Sinnoh groups are now consolidated into valid groups0–126 while preserving all existing regional IDs and Oreburgh. All compiled travel references and individual popup names were reverified. A native signed-ID host test passes1,290 map lookups and reproduces the former north/gate invalid promotion. See `oreburgh_exit_fix.md`. This corrected ROM includes your saved house edits.

## Coronet inspection gates

Nine Coronet construction scientists beside actual doors now offer Yes/No inspection travel through the nearest registered static source door. This includes the approach shown in the runtime report and the corridor toward Route216/Snowpoint and the upper Coronet/Spear Pillar path. Cancel stays in place; no donor scripts, flags, progression state or NPC gameplay were introduced. Source/build/ROM/animation/ownership checks passed after the change. Runtime confirmation is pending.

## Confirmed Rock Climb interactions

The previous project-owned traversal stack is ported for eight confirmed source-marker interactions in Route208, Iron Island and Mt.Coronet36.91. Face the rock from its approach cell and press A, then confirm the native Yes/No climb prompt. The proven project ride-gear helper supplies Bibarel when a party member cannot perform the move; no donor progression or persistent flag is required. The handler is restricted to exact new Sinnoh map/coordinate/facing combinations. Native maps and BWA/SWSH interactions are unchanged. No donor NPC markers or donor scripts were transplanted.

Approach cells: Route208 (8,11) facing east and (14,15) west; Iron Island36.64 (10,21) east and (14,19) west; Coronet36.91 (34,13) east, (40,17) west, (40,26) east and (44,24) west. Source marker families098C3593/346C/3622/36AF match all eight occurrences in the registered Sinnoh inventory. Approach/landing geometry is checked; eight exact triggers, incorrect facing/position and native-map exclusions pass a sanitizer host test. Full ROM/assets/animation/ownership checks pass. Retest actual movement, both directions, Cancel, followers and save/reload in game. Eight confirmed points are not a claim that every piece of cliff artwork is a valid climb.

## Vertical climb walls

Acuity Lakefront has a vertical dotted-rock strip at19,35–38 whose translated behavior remains MB_BUMPY_SLOPE. These strips are distinct from the eight prior diagonal marker interactions. Map-scoped project traversal now provides24 A-button approaches covering12 matching vertical strips in Acuity Lakefront, Coronet36.91, Route208, both Route210 strips, Route213, Sunyshore and Veilstone. The original geometry/behaviors remain unchanged; native Hoenn/BWA/SWSH bumpy slopes are unaffected.

Each direction is generated from an inspected continuous strip and clear in-bounds landing, with occupied cells, portal/water landings and edge fragments excluded. One Route213 edge fragment is held without an in-map landing. `vertical_climb_ledger.json` contains all approved cells, landings, steps and the held case. From the lower landing face north; from the upper landing face south; press A and confirm. Acuity approaches are19,39 north and19,34 south, traveling five cells each way. Cancel changes no position. The existing project climb prompt and ride-gear helper are reused without donor story scripts/flags.

All24 vertical approaches, wrong positions/horizontal facing, native-map exclusions and eight diagonal regressions pass sanitizer host tests. ROM/build/asset/animation/ownership checks pass; these new movement routes still need in-game confirmation. The user has already reported reaching Spear Pillar with the previous diagonal support.
