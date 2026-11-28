# Reviewed Galar recovery / Unova retirement

## Scope

Recovered 56 visually reviewed maps from the user's Sword & Shield Ultimate+
v1.2.1.2 donor (SHA-256 recorded in source-receipt.json). This is a restored map
asset/travel foundation, not a completed Galar campaign. The donor's other 428
non-excluded candidates remain outside the build; 197 inherited legacy maps and
20 superseded revisions are also excluded. Hoenn story progression is unchanged.

The selected set includes Postwick, Wedgehurst, Motostoke, Turffield, Hulbury,
Hammerlocke, Stow-on-Side, Ballonlea, Circhester, Spikemuth, Wyndon, several routes,
Wild Area sections, mines and selected interiors/special areas. Not every room,
route or destination in the donor is restored. No story gate or public portal to
Galar has been invented. The maps are available in Porymap's Galar Recovery group
for story planning; runtime QA uses isolated native warps.

## Unova

Archived 33 old Unova map wrappers and 31 orphaned Unova layout registrations.
The active wrappers were already redirecting to Littleroot; they were not a
working Unova region. Original map JSON/scripts and original layout records live
under archives/unova-retired-20261128. Original source graphics and the user's
Nuvema map/border files remain intact.

Retired numeric map/layout slots are kept as inert records. Removing or reusing
those numbers would shift unrelated maps and saved references. The existing
retired-region redirect in overworld.c now names the explicit tombstone maps.
No non-Unova map number changes. Gen 5 species distribution is a separate system.

## Asset and travel repair

- Reused the exact-build extraction in the canonical checkout's
  .la_work/amap/swsh_full_v11 after checking donor and selected source hashes.
- Imported only SELECTED_ASSET/PRESERVE_CANARY records from the existing reviewed
  manifest. No donor NPC, trainer, cutscene or event script pointers execute.
- Converted all 24 recovered tileset banks from two-layer to the current
  three-layer format, using the project's existing layer conversion mapping.
- Packed referenced metatile definitions, saving 234,624 bytes. Every map/border
  cell was checked for identical tile words, behavior, collision and elevation.
  Full pre-packed metatiles/attributes remain under archives/galar-reviewed-source.
  pack_galar_metatiles.py is guarded against a second renumbering.
- Repaired real doorway links and one reciprocal Wild Area warp index. Donor
  story transitions on ordinary floor and unresolved destinations are disabled.
- Corrected the selected Postwick/Route 1 seam to reciprocal offsets +1/-1.
- New map labels use the donor location names; unnamed donor rooms display Galar.
- No inspection scientists or visible inspection tour is included. Files named
  inspection_arrivals are historical tool coordinates, superseded for runtime QA
  by runtime_arrivals.json; all 56 maps have safe arrival coordinates.

The previous full-import scripts target older two-layer data. Do not rerun them
on packed assets. Re-extract from the donor, convert, repair and repack deliberately
when expanding this set. Additional Galar maps require more ROM space and review.

## Validation

The isolated native emulator test loads every recovered map, checks walkable
arrivals and location names, enters every enabled doorway destination, verifies
retired Unova bank redirects, saves/reloads in Galar, and checks every unrelated
map bank/index against the pre-change commit. No user battery save is loaded.

See runtime-validation.json for exact checks and ROM hash. The source receipts
and intermediate repair reports document each phase; summary.json records the
final state. Native screenshots show selected major locations.

Final native validation: 853 checks passed, including both directions of the
Postwick/Route 1 seam. The linked ROM uses 33,379,804 bytes of 33,554,432, leaving
174,628 bytes. Further donor-map expansion requires additional space work.
