# Hoenn interior polish2: Dewford, Slateport and Mauville

All26 reviewed non-gym interiors use Hyper-derived layouts and recovered Hyper tilesets.15 blockdata files exactly match their donor export;11 are reconciled versions that preserve expansion event/collision contracts and visual portal adapters. Donor pointers, hashes, source identities, dimensions, tilesets and reconciliation counts are in `donor_correspondence.csv/json`. All room dimensions match their corresponding donor layout.

Scope:5 Dewford rooms,14 Slateport rooms and7 Mauville rooms. This includes houses, Hall, Marts/Centers, Oceanic Museum1F/2F, Stern's Shipyard1F/2F, Harbor, Name Rater, Fan Club, Bike Shop, Game Corner and the three Slateport Battle Tent rooms. Native expansion gameplay remains authoritative in every room. Battle Tent art/access is reviewed here; facility mechanics require their own runtime checks. Dewford/Mauville gyms and Granite Cave dungeon mechanics are outside this interior batch.

Four contact sheets show current furniture, walls, floors and event positions. No invalid used palette references were found.57 static door/stair arrivals resolve valid slots with clear neighboring floor;106 active actors have a floor/counter interaction approach. Background events are in bounds. No corrective map edits were indicated by visual/static QA. Current Porymap edits and native story actors, shop inventories, healing, fossil/boat/contest/coin state and save semantics are untouched.

Use the existing validated ROM; no new ROM is necessary. Static reachability does not prove all flag-dependent story states or scripted services. See `runtime_checklist.md` for Museum fee/Aqua/Stern scenes, Harbor travel, Bike Shop swapping, Game Corner coin/reward interactions and Battle Tent review.

Reproduce the visual and access review using the `--batch 2` option on `hoenn_interior_polish.py` and `audit_hoenn_interiors.py` under `tools/la_world/importers/amap/hyper_assets/`.

Next normal-progression interior batch: Verdanturf, Fallarbor and Lavaridge, including Route111/113/114 support houses and relevant service rooms. Gyms and puzzle-driven interiors remain explicit mechanics batches.
