# Hoenn interior polish batch 10: registered Hyper specials

Reviewed all 126 existing HyperHoenn maps across 16 contact sheets. This includes 61 indoor, 32 underground, 15 underwater, 14 route, one ocean-route, one city and two MAP_TYPE_NONE records. Maps retain their actual registered canonical names, numeric group/map positions, map sections, layouts, tilesets, event counts, donor identities/pointers and relationships in the inventory files. No new maps or Hyper gameplay scripts were imported.

Zero invalid used palette references. All 490 reviewed warp records point to existing destinations and slots. The structural network audit confirms all 126 specials are recorded as reachable and have canonical return paths. This is graph reachability, not proof that a player can walk each route.

The raw access scan retains 20 OPEN warnings: ten arrivals without an adjacent clear floor cell and ten scientist approaches not established by warp-root BFS. These are not silently treated as passed. Some rooms use connections or project travel; each warning needs source geometry and runtime-state review. See manual_review.csv/json, including Distortion/Solaceon links, Ultra Alliance, Test of Heart/Ever Grande, Champion Island, Rainbow Castle and Ruins of Decision/Meteor Falls returns.

Two MAP_TYPE_NONE headers also remain open for intended-semantics review: HyperHoenn_35_35_Temple_of_the_End and HyperHoenn_35_42_Steven_s_Island. Do not infer a header change solely from room appearance.

Construction scientists and all project-owned travel remain intact. The gate inventory lists 408 project-wide construction/relevant scientist records; the dedicated construction audit counts 407 Construction-script blockers, plus the inventory includes an inspection/travel scientist. This is not 408 NPCs inside the specials: the batch has 120 active actor candidates. No gate was removed, actor moved, warp destination changed or encounter logic transplanted.

Split-room layouts, void backgrounds, platform worlds and underwater artwork were preserved as source intent rather than filled automatically. No additional visual defect was confirmed by the overview sheets, but full-size renders and in-game inspection remain necessary for detailed cleanup.

Use the existing Batch 5 ROM. No map/asset/runtime edits or rebuild were performed for this batch. Faraway Island entrance and Navel Rock exterior art findings from Batch 9 remain open. This completes the special-map review inventory, not construction-area gameplay readiness.

Reproduce with --batch 10 on hoenn_interior_polish.py and audit_hoenn_interiors.py, then run review_hoenn_specials.py. Next work should resolve the open arrival/approach and island-art queues before opening any of these construction areas.
