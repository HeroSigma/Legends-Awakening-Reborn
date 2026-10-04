# Proven Hyper asset stack in Reborn

Hyper supplies world/assets. Expansion supplies the gameplay brain.
This ports the previously proven Legends-Awakening asset stack; it does not
rediscover donor maps, import story scripts, or replace canonical maps.

```sh
python3 tools/la_world/importers/amap/hyper_assets/port_hyper_assets.py --repo .
python3 tools/la_world/importers/amap/hyper_assets/port_hyper_assets.py --repo . --apply
python3 tools/la_world/importers/amap/hyper_assets/test_hyper_assets.py
make -j4
```

The default prior repository is the sibling `Legends-Awakening`; the default
export is `.la_work/amap/HypEm_v5.7_EN_QoL_amap_export`. Override those with
`--prior-repo` and `--donor`. Reports are in `.la_work/amap/hyper_asset_integration`.
The recovered behavior catalog is vendored under `reference/`, pinned to the
identified recovery package. Source ROM identity is guarded.

Ported infrastructure:
- 74 Hoenn-referenced recovered tilesets, 13 palette banks per tileset,
  metatiles and semantic behavior attributes, under disjoint `Hyper` symbols.
- 20 proven generic animation callbacks and the existing expansion Battle Dome
  callback; source frame payloads and descriptor semantics are reused.
- 194 recovered object graphics and 16 deduplicated palettes at tags D800-D80F.
- 518 source blockdata/border assets staged outside canonical map/layout tables.
- A visual-only canonical graphics binding mechanism, empty by default.

Canonical graphics bindings use current `MAP_*` and `OBJ_EVENT_GFX_*` symbols
and pointers to reviewed visual structs. They must preserve canonical player,
berry, animation and reflection contracts. Source IDs are visual-bank lookup
keys, not new gameplay graphics IDs. The expansion dynamic-GFX resolver runs
before the opt-in renderer override; all eleven prior verified canonical
initializer families are already present. No imported-map wrappers are added.
The common recovered graphics bank is not a blanket replacement for native
player/berry controls; those need explicit visual adapters in the later canary.

Behaviors are rebound by recovered source semantic names. High attribute bits
remain unchanged. The proven 1F/2D facade overrides are regenerated with their
actual source-use collision guard. One unreferenced custom attribute slot is
neutralized and recorded; future scripted substitutions must be reviewed.
Known prior visual edits of source sprites 205/206 are retained and pinned.
The recovered sprite's VRAM allocation size and actual image stride are
recorded separately.

The plan JSON/Markdown covers prior components, what existed, direct reuse,
regeneration, dependencies and validation. The flag bridge is reference-only;
no save layout, flags, donor vars, NPC gameplay, story warps or script ownership
are ported. Existing BWA/SWSH source files are protected by hash. Normal builds
may refresh ignored generated events/local-ID headers from the user's existing
map JSON; these derived artifacts are logged separately from source changes.

Current validation: normal ROM build and eleven checks, including ASan/UBSan
animation DMA/frame simulation. Asset declarations can be garbage-collected
while unused; the later canonical canary is the runtime activation test.
Recommended batch: OldaleTown 0.10, Route102 0.17, OldaleTown_Mart 2.4, with
reviewed event/door coordinates and expansion-owned gameplay retained.

## Canonical Hoenn Canary #1

Only OldaleTown, Route102 and OldaleTown_Mart are activated. `hoenn_canary1.py` applies a reviewed, hash-guarded three-map batch; a second apply refuses to overwrite changed inputs. `test_hoenn_canary1.py` verifies coordinate/ownership/protection contracts, and `verify_hoenn_canary1_rom.py` inspects the linked ROM. The original asset-stage receipt remains historical; asset tests accept only exact superseding hashes from the explicit canary receipt. Reports, originals, ledger, checklist and frozen ROM are in `.la_work/amap/hyper_hoenn_canary1/`. The shared Mart layout is unchanged. No donor gameplay scripts or saved-position migration are introduced. Runtime success was subsequently confirmed by the user.

## Opening spine Canary #2

User confirmed Canary #1 runtime success. `hoenn_canary2.py` adds only LittlerootTown, Route101, Route103 and PetalburgCity, retaining the confirmed three destinations. `test_hoenn_canary2.py` audits all native events, scene paths, movement-only reconciliation, receipt protection and the one-cell Route101 accommodation. `verify_hoenn_canary2_rom.py` reads all seven activated destinations from the linked ROM. Reports/manifest/ledger/checklist/originals/frozen ROM: `.la_work/amap/hyper_hoenn_canary2/`. Native gameplay commands remain authoritative; no donor story/save/quest logic is imported. Canonical/layout IDs are unchanged. Asset/Canary #1 checks recognize only exact superseding receipt hashes. Runtime success was subsequently confirmed by the user. Do not rerun asset staging over activated canary bindings.

## Rustboro progression Canary #3

`hoenn_canary3.py` activates the 16 explicitly listed canonical corridor/progression/service maps. Route102 and Route103 receive only fixed, project-owned construction scientists at Timeless Woods mouths; their validated native events/layouts remain intact. Fifteen scientists reserve donor-only entrances without registering donor maps or importing donor logic. Shared Center, Mart and Flower Shop layouts are cloned so unrelated maps keep native assets.

The coordinate ledger covers every original event, native story movement paths and connection geometry. Three compatibility cells are recorded: one Rustboro hedge cell for native Devon approaches and two Rusturf collision/elevation corrections preventing a Rock Smash bypass. Native map identities, story states, script rewards, encounters, warp destinations, connection metadata, save structures and dynamic graphics remain authoritative. Rustboro's existing Fly coordinate follows the relocated Center; its heal ID, respawn map and nurse are unchanged.

Use `python3 tools/la_world/importers/amap/hyper_assets/hoenn_canary3.py --validate` after application. Reapplying refuses changed inputs. `test_hoenn_canary3.py` checks ownership, reachability/gates, shared-layout isolation, graphics ABI and native counters/weather. `verify_hoenn_canary3_rom.py` inspects all 23 activated destinations and linked object-script/warp pointers. Historical suites follow exact, scoped receipt hashes and retain assertions over every native event. Reports, inventory, originals, receipts, runtime checklist and frozen ROM are under `.la_work/amap/hyper_hoenn_canary3/`. Canary #3 runtime success was confirmed by the user. Do not rerun asset staging over activated bindings.

## Canonical Hoenn Canary #4 — Dewford to Mauville

`hoenn_canary4.py` replaces 28 canonical asset/layout destinations while retaining every native gameplay field except reviewed event x/y and one Scott movement-data step. Ten shared layouts are isolated, 110 map-local art adapters retain native rendering/animation fields, and five project-only scientists reserve extra entrances. Private collision/elevation compatibility copies leave the staged source bank unchanged. Canonical sea/cave geometry, reciprocal warp slots, native rival land gate and Mauville puzzle ownership are checked explicitly.

Run `hoenn_canary4.py --validate`, the `test_*.py` suite, and `verify_hoenn_canary4_rom.py` after a successful build. Reapplication refuses changed inputs. Historical receipts remain intact and follow a strict fourth-stage hash chain; independently changed project settings/generated headers are pinned separately in the fourth receipt, not silently ignored. Reports and the pending runtime checklist are under `.la_work/amap/hyper_hoenn_canary4/`. Stop after this batch until user runtime confirmation. Do not rerun asset staging over activated bindings.

## Porymap editing

Hyper definitions are directly exposed in the standard tileset declaration files for the installed editor. Separate generated Hyper headers remain reference. `verify_porymap_hyper.py` validates 75 tilesets and 54 activated canonical map references. Reopen the project to clear cached labels on WSL. See `.la_work/amap/porymap_hyper_compat/README.md`. Manual cleanup requires a fresh build and updated reconciliation ledgers; frozen test ROMs remain untouched.

## Western Hoenn sea corridor correction

`hoenn_corridor_correction.py` fills canonical Route105/107/108 and reserves the previously missed western Dewford connection family and Champion Island mouth. `--validate` preserves the strict receipt chain and regenerates the cumulative entrance audit. Six new project-owned scientists, no donor gameplay/new map registrations. A local Route105 primary attribute derivative keeps expansion abnormal-weather Dive semantics; only Regi closed-door art/coordinate operands are remapped. Connected-map transitions reload primary assets when the primary pointer changes. Shared-primary native loading remains unchanged.

Run the `test_*.py` suite, `verify_porymap_hyper.py` and `verify_hoenn_corridor_rom.py` after building. The current linked verifier replaces earlier frozen-batch verifiers for current ROM checks; earlier ROMs/receipts remain historical. Outputs and pending runtime checklist: `.la_work/amap/hyper_hoenn_corridor_correction/`. Do not reapply over manual editor cleanup; inspect and reconcile changes first. No next town/region batch before runtime confirmation.

## Northwest Hoenn / real construction-area registration (Canary #5)

`hoenn_canary5.py` reconciles 67 canonical maps and registers 63 actual special layouts/maps from `hoenn_canary5_scope.json`, retaining five generated Trainer Hill layouts. It requires the staged Hyper bank, full export, correspondence inventory and earlier canary/corridor receipts. Preflight/apply is for a reviewed fresh baseline; do not reapply over the completed batch or manual Porymap edits.

`special_portal_assets.py` gives script-dependent special portals native static warp behavior with map-local copies of identical metatile artwork, leaving shared banks untouched. `verify_hoenn_canary5.py` checks the current source contract and isolated `pokeemerald-canary5` linked ROM; `test_hoenn_canary5_guard.py` exercises the actual construction connection guard. `report_hoenn_canary5.py` publishes the authoritative current registry/review/checklist and manual queue under `.la_work/amap/hyper_hoenn_canary5/`.

Build in a separate cache: `make BUILD_NAME=emerald-canary5 -j4`. The normal project source remains Porymap editable; existing canonical map/group/layout/mapsec IDs are preserved. Actual special destinations replace the earlier entrance-only reservations. Foreign or nonreciprocal donor edges remain reference-only. Native story/weather map ownership, save ABI, encounters, heal/Fly destinations and BWA/SWSH imports stay authoritative. This batch awaits user runtime confirmation.


## Hoenn Canary #6: earlier dungeon closure

`hoenn_canary6.py` and its canonical/special scope files stage New Mauville (2), Abandoned Ship (13), Island Cave (1), and 25 actual construction-only special maps. Expansion owns native progression and events; the Scanner moves to inspected floor (21,10), and the first ship underwater layout expands to 25×8 with native Dive semantics retained. Regice retains its native graphic contract.

Build separately with `make BUILD_NAME=emerald-canary6 -j4`, then run `verify_hoenn_canary6.py`, `verify_porymap_hyper.py`, and `report_hoenn_canary6.py` from the project root. Reports live in `.la_work/amap/hyper_hoenn_canary6/`. The verifier audits linked assets and ownership, animation, append-only IDs, native Regice perimeter, and static special-map entry/return paths. Runtime collision/progression remains a user checklist.

The final receipt records three user editor changes (Rustboro blockdata, Rustboro/Route104 events) separately from migration edits. `editor_merge_review.json` documents restoring stale editor registry saves while preserving those user files byte-for-byte. Close/reload Porymap after external registry updates before saving.


## Route114 water correction

`fix_route114_water.py` restores the donor elevation1 on 119 surfable water cells mistakenly assigned old native land elevations by Canary5. It retains artwork, behaviors and collision bits, and remaps Claude to the actual donor bridge (20,27) and the Fossil Maniac house sign to its sign tile (30,6), preserving expansion gameplay fields. Canary5 generation now excludes surfable cells from land-elevation reconciliation. Frozen earlier batch receipts remain intact; the current verifier recognizes this separate two-file correction receipt.

After the isolated Canary6 build, run `verify_route114_water.py` and `verify_hoenn_canary6.py`. Reports are in `.la_work/amap/hyper_hoenn_route114_water_fix/`. In game, check shore boundaries on foot, Surf entry/travel/exit, the bridge fisherman battle, and the relocated house sign. Reload Porymap after this external event/layout edit before saving.

Route114 shoreline follow-up: `.la_work/amap/hyper_hoenn_route114_shore_fix/receipt.json` chains the first water repair without rewriting its history. It restores 74 donor land elevations incorrectly converted to wildcard0, including the screenshot's (29,16)/(30,16) shore. `verify_route114_water.py` validates both repairs and all 186 land/water boundaries. Canary5 generation no longer copies native wildcard0 onto donor elevation3 land.


## Hoenn Canary #7: Fortree corridor

`hoenn_canary7.py` and its scopes replace 18 canonical maps (Route119 and Institute/house, Fortree and interiors/Gym, Route120, Ancient Tomb, Scorched Slab) and register 11 actual associated construction-only maps. No donor gameplay scripts are copied. Native Route120 visual tile operands are rebound to inspected Hyper bridge/water/wall assets; all story branching remains native. Twenty source-matched event coordinate changes are recorded in the ledger.

Run `test_hoenn_canary7_geometry.py` before apply; it proves both Route119 rival/Scott scene branches, source water levels and native Gym geometry. Apply with `hoenn_canary7.py --apply`, then build separately using `make BUILD_NAME=emerald-canary7 -j4`. Run `verify_hoenn_canary7.py`, `verify_porymap_hyper.py` and `report_hoenn_canary7.py` after generated registry hashes are recorded in the receipt. The final verifier protects all earlier files/imports and checks linked assets, numeric IDs, native script ownership, animation and new static entry/return paths. The preflight generator is for the baseline stage; do not rerun it on an applied checkout.

Artifacts are in `.la_work/amap/hyper_hoenn_canary7/`. Runtime checklist covers rival genders, Aqua/Castform, Devon Scope/Kecleon, Winona rotating gates, weather, bridges, Registeel, actual special maps and prior imports. No later batch is advanced until runtime confirmation.


Route110 follow-up: `fix_route110_water.py` restores 160 donor water elevations without changing any Cycling Road bridge/nonwater cells. Run `--verify` after the isolated Canary7 build to check all 1,258 water cells, unchanged bridge geometry and linked blockdata. The Canary7 verifier accepts the exact one-file correction receipt in `.la_work/amap/hyper_hoenn_route110_water_fix/`. Canary4 generation now excludes Route110 water from its native ocean-elevation normalization.


Route119 access follow-up: `.la_work/amap/hyper_hoenn_route119_access_fix/receipt.json` records 267 surface-elevation restorations and four object elevation remaps, retaining all gameplay fields. The Canary7 generator now retains source elevations on Route119, and the current verifier accepts the exact reviewed correction chain. `verify_route119_access.py` checks donor levels, event ownership and linked blockdata. The geometry report validates the south-to-Institute land approach and valid door at (7,32). Runtime conditional objects/bridges remain checklist items.


## Hoenn Canary #8: Lilycove/Safari/Mt. Pyre corridor

`hoenn_canary8.py` and its scope files map 44 canonical entries: Routes121/122/123, Lilycove and interiors, Safari sectors/entrance/Rest House, Berry Master's house and Mt. Pyre floors/exterior/summit. Two real construction maps (Temple of the End and Mountain Top) are registered; MtPyre6F reuses the existing Ultra Space arrival/static return. An unused Mart stays unused. Source surface levels are retained; the lone inspected Lilycove surfable cell (53,2) is corrected from land3 to water1. Native events may receive audited geometry coordinates/elevations, retaining gameplay fields.

`test_hoenn_canary8_geometry.py` is a pre-apply baseline review of native warp cells, donor water levels, exact native/donor Wailmer visual operands and heal/Fly arrival. Apply with `hoenn_canary8.py --apply`; build with `make BUILD_NAME=emerald-canary8 -j4`. Record generated registry output hashes in the receipt, then run `verify_hoenn_canary8.py`, `verify_porymap_hyper.py` and `report_hoenn_canary8.py`. Do not rerun the baseline generator on an applied checkout. The verifier checks 300 linked Hyper maps, preserves 566 native event gameplay records and 44 script owners, validates sparse MtPyre warp correspondence and native department-store dynamic warp constants, and checks animation and new static entry/return paths.

Reports live in `.la_work/amap/hyper_hoenn_canary8/`, including coordinate ledger, geometry/boundary proofs, registry/manifest CSVs and runtime checklist. Temple→Rainbow Castle arrival remains deferred; the pre-existing off-map DepartmentStore1F sign remains a manual-review entry. Fortree Gym runtime confirmation remains pending separately. No later replacement batch is advanced. Reload Porymap after external registry updates before saving.


## Hoenn Canary #9: eastern sea / main-story League closure

Canary #8 runtime success was confirmed by the user. `hoenn_canary9.py` and scopes activate116 canonical maps and register22 actual construction-only maps. Eight canonical story-switched layouts (Sootopolis, Route131, clean Sky Pillar floors/top) also use Hyper geometry. Existing Mystery Events House maps remain native; two related actual special maps are registered/editor-visible with deferred ingress because their donor entrance conflicts with an authoritative canonical door. Foreign Sinnoh exits stay closed.

`hoenn_canary9_support.py` reuses the prior recovered08305DE0 graphics/palettes bank and extracts only referenced alternate geometry from the hash-pinned source ZIP. No donor script command bodies, flags, save data or gameplay wrappers are installed. Source scripts are inspected solely to identify graphical layout references/unlocked artwork. Private identical-art behaviors reconcile unsafe Dive/Surface pairs, the dormant Aqua pad and the native Sky Pillar stair. Expansion owns all native progression, puzzles, tide switching and warp destination semantics.

Run `test_hoenn_canary9_geometry.py` only before apply on the baseline. After apply, use isolated `make BUILD_NAME=emerald-canary9 -j4`, record generated registry hashes in the receipt, then run `verify_hoenn_canary9.py`, `check_hoenn_canary9_boundaries.py`, `verify_porymap_hyper.py` and `report_hoenn_canary9.py`. Reapplying/preflight over an applied checkout is refused. The final verifier protects31,591 baseline files and checks438 active Hyper maps plus eight alternate layouts, native event/script ownership, numeric IDs, animation and static return paths. Construction notices and all-room paths still require runtime tests.

Reports are under `.la_work/amap/hyper_hoenn_canary9/`; reload Porymap before saving. The main story route is mapped through the League; Canary #9 runtime success was confirmed by the user on2026-10-04. Versioned review, inventory, static validation and runtime confirmation are in `docs/la_world/hyper_hoenn/canary9/`. Battle Frontier/foreign regions/unused maps are not advanced. Stop after this batch for user feedback.
