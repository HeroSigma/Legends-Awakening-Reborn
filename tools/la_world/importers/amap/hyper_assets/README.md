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

Only OldaleTown, Route102 and OldaleTown_Mart are activated. `hoenn_canary1.py` applies a reviewed, hash-guarded three-map batch; a second apply refuses to overwrite changed inputs. `test_hoenn_canary1.py` verifies coordinate/ownership/protection contracts, and `verify_hoenn_canary1_rom.py` inspects the linked ROM. The original asset-stage receipt remains historical; asset tests accept only exact superseding hashes from the explicit canary receipt. Reports, originals, ledger, checklist and frozen ROM are in `.la_work/amap/hyper_hoenn_canary1/`. The shared Mart layout is unchanged. No donor gameplay scripts or saved-position migration are introduced. Runtime validation is pending; stop after this batch.

## Opening spine Canary #2

User confirmed Canary #1 runtime success. `hoenn_canary2.py` adds only LittlerootTown, Route101, Route103 and PetalburgCity, retaining the confirmed three destinations. `test_hoenn_canary2.py` audits all native events, scene paths, movement-only reconciliation, receipt protection and the one-cell Route101 accommodation. `verify_hoenn_canary2_rom.py` reads all seven activated destinations from the linked ROM. Reports/manifest/ledger/checklist/originals/frozen ROM: `.la_work/amap/hyper_hoenn_canary2/`. Native gameplay commands remain authoritative; no donor story/save/quest logic is imported. Canonical/layout IDs are unchanged. Asset/Canary #1 checks recognize only exact superseding receipt hashes. New runtime testing is pending; stop after this batch. Do not rerun asset staging over activated canary bindings.
