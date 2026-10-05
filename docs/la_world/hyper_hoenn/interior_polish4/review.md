# Hoenn interior polish batch 4

Reviewed 37 non-gym rooms: Fortree houses, decoration shop, Mart and Center; Route 119 house and Weather Institute; Lilycove services, Contest rooms, Cove Lily Motel, department store, Museum, Harbor and houses; Route 121 Safari entrance and Route 123 Berry Master's house.

All use Hyper-derived geometry and tilesets. 37 blockdata files match their donor exactly; 0 preserve existing reconciliation. 37/37 dimensions match donor layouts. Donor correspondence includes IDs, pointers, dimensions, tilesets and source/current hashes.

Five contact sheets were visually reviewed. No invalid used palette references. One concrete defect was corrected: the first-floor department store directory interaction moved from out-of-bounds (0,8) to its visible Hyper sign at (2,2), with clear approach at (2,3). Native script and facing requirement are unchanged. No layout, object, warp or map-ID changes were made.

After correction, 88 static warp arrivals and 193 active actor approaches pass. Native dynamic elevator destinations remain owned by expansion runtime. Hidden and facility-controlled actors remain intact. The unused Mart remains a registry-only room; no entrance was invented.

Fortree Gym mechanics are excluded. Static access and visual review cannot prove story-dependent Weather Institute scenes, Contest movement, elevator selection, Lottery state or travel menus. See runtime checklist. Build status is recorded in validation.md.

Reproduce with `--batch 4` on the interior renderer and access auditor under `tools/la_world/importers/amap/hyper_assets/`.
