# Hoenn interior polish batch 3

Reviewed 28 non-gym interiors: Verdanturf, Fallarbor, Lavaridge, Route 111 support houses, Route 113 Glass Workshop, and Route 114 Fossil Maniac house/tunnel and Lanette house.

All 28 use Hyper-derived layouts and tilesets. 22 blockdata files match the recovered donor exactly; 6 retain existing gameplay/collision reconciliation. 28/28 dimensions match their donor. Correspondence files retain donor IDs, pointers, hashes, dimensions and tileset identities.

Visual review found coherent furniture, doors, stairs and floors, with no invalid used palette references. Static checks passed for 58 warp arrivals and 76 active actors; background events are in bounds. Verdanturf's outdoor Battle Tent arena is intentional Hyper art. Native virtual actors and script-controlled facility positions remain intact.

No corrective map edits were needed. Expansion scripts, event ownership, service logic, flags and save semantics remain unchanged. No new ROM was built; use the existing validated ROM. Static review does not validate scripted movement, conditional story states or facility mechanics; complete the runtime checklist.

Lavaridge Gym and other gym mechanics are excluded. Reproduce with `--batch 3` on the interior renderer and access auditor under `tools/la_world/importers/amap/hyper_assets/`.

Next interior batch: Fortree and Route 119 Weather Institute, followed by Lilycove and surrounding support interiors.
