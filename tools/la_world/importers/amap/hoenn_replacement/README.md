# Hyper Hoenn canonical replacement planner

Planning only: this tool writes reports and never edits gameplay or donor files.
It accounts for all 518 canonical Emerald slots, examines the full 922-map
Hyper export, and selects one corroborated relocated Hoenn room (37.118).
Other-region candidates are reference material; no additive destinations are created.

Run from the repository root:

```sh
python3 tools/la_world/importers/amap/hoenn_replacement/build_hyper_hoenn_plan.py --repo .
python3 tools/la_world/importers/amap/hoenn_replacement/test_hyper_hoenn_plan.py
```

Defaults:
- Donor: `.la_work/amap/HypEm_v5.7_EN_QoL_amap_export`
- Reports: `.la_work/amap/hyper_hoenn_replacement`
- Recovery evidence: `/mnt/c/Users/aadair/Downloads/tools`

Override with `--donor`, `--output`, and `--evidence-root`. The recovered
behavior catalog is required. Different ROM identity or Emerald group shape
requires review rather than silently continuing with slot matching.

The manifest preserves canonical identities and gameplay metadata. Confidence
measures counterpart identity; replacement mode describes proposed strategy.
Every import/replacement permission remains false. The high-confidence CSV
is not an import list. Manual review, keep-original and static-candidate CSVs
partition all 518 destinations. The event ledger records every current
expansion event with coordinate/terrain comparisons, not automatic bindings.

Declared header counts and actual exported records are separate. Filtered
records and invalid 255-count headers are quarantined. Donor scripts/NPCs,
raw flags/vars/specials/natives and callback addresses remain reference-only.
Prior recovery reports from Legends-Awakening do not establish application
or runtime validation in Legends-Awakening-Reborn.

Validation covers current source/donor hashes, complete coverage, CSV
partitions, repurposed/relocated destinations, dynamic returns, custom
behavior guards and preservation of the current Littleroot scientist.
No ROM build or runtime replacement is performed. Later implementation needs
isolated source-hash-guarded patches, event/path/routing ledgers, rollback
assets and ordinary gameplay/save/blackout tests.
