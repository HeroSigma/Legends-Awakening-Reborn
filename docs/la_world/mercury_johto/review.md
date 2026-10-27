# Mercury Johto replacement — Reborn

The active Johto asset/travel network now uses Mercury geometry. The older Legends-Awakening project is untouched. This work changes Legends-Awakening-Reborn only.

## Installed

- 338 Mercury maps registered with 115 normalized tileset banks.
- 164 existing map identities reused in place; 174 additional donor rooms/sections appended. Every pre-existing numeric map ID remains unchanged.
- New maps are grouped as towns/cities, routes, caves, forests, special areas or interiors. A third Johto interior group was appended without moving existing groups.
- Native three-layer metatiles, palettes, translated baseline behavior, collision/elevation and native static travel. Identical asset payloads are shared.
- Empty project map-script tables and construction inspectors. No Mercury NPC scripts, progression flags, variables, trainers, encounters, quests or save logic were imported.
- Goldenrod's damaged graphics stream was recovered from the other locally supplied Mercury package after verifying identical tileset header, palette, metatile definitions and attributes. The original ROM/patch remain unchanged; see asset_recovery.json.

## Held entries

102 older entries remain registered with their original geometry, but their travel entrances are removed. This count includes surplus duplicate rooms, older placeholders and unresolved functional matches; it does not mean 102 whole locations are missing. Route 28, Mt. Silver and Sinjoh Ruins are included, as requested. Their inspectors offer travel to the new hub if an existing save is already there. Full list: held_original_maps.csv.

The donor's forest border filler 47.7 is registered for editor/reference use, with its two incoming visual connections disabled. Nine water-only sectors remain connected and retain Surf water; they are not discarded for lacking dry land on which to place scientists.

## Validation and limits

The ROM build and linked-map checks are recorded in validation.json. Those checks cover map IDs, source geometry, every normalized metatile cell's art, tile/palette/attribute pointers, warp destination indices, construction object coordinates, native water elevation and preservation of other regions' source files. All registered regions' layouts are also checked after the linker optimization.

Travel connectivity is a map-level graph check, not movement-level proof. Ten one-way areas have project inspectors that can return the player to Littleroot or advance the inspection tour. The full inspection tour has 328 safe land arrivals; normal travel also includes the nine water-only sectors. See travel_connectivity.json.

Mercury animations and custom graphical callbacks are not yet ported: new tileset callbacks are NULL. Unrecognized Mercury-specific behavior extensions retain their reference values in the extraction and need runtime/semantic review; baseline conversion currently falls back to normal native behavior for unknown IDs. In particular, do not assume a custom climbing surface or scripted puzzle works solely because the layout is present. No field-move progression was transplanted.

Indoor correspondence confidence is MEDIUM where rooms were matched by location, role and geometry. These are construction-only destinations; building-specific gameplay must be deliberately designed later. Display names retain existing save/map-section IDs and only override Johto layout presentation.

Porymap definitions and PNG/JASC companion files are installed, but opening every map in the Porymap GUI has not been verified. Close/reopen the project to load the new registry.

## Build capacity

The existing linker already used section garbage collection. Native compilation now emits separate function/data sections so unused declarations can be removed. This avoids cutting referenced maps, artwork or gameplay systems. Makefile before/after is backed up; compare only this task's added section flags because the checkout already contained unrelated work.

## Source tools

1. extract_mercury.py
2. replace_johto_mercury.py --apply (one-shot; refuses to overwrite the baseline)
3. reconcile_mercury_behaviors.py
4. finalize_mercury_johto.py
5. gate_mercury_stubs.py
6. make -j6
7. verify_mercury_johto.py

Tools live under tools/la_world/importers/amap/. Source extraction is under .la_work/amap/mercury_full_v11. Exact pre-change edited files and protected-file hashes are under .la_work/amap/mercury_johto_backup. Existing GS asset files were not deleted or rewritten.

Final checks: 346,825 normalized visual cells preserved; 1,763 active layouts across the registered regions checked against source. Legacy groups configured as NULL in the existing build remain inactive. The normal directed Johto travel graph reaches 327 maps; the construction tour supplies 328 safe land arrivals. Mercury source border filler 47.7 is the only new reference-only map.

Porymap compatibility repair: all 115 declarations and shared graphics/palette/metatile symbols are exposed directly in the standard root source files. Graphics use per-payload folders containing tiles.png. Declaration/path checks pass for 338 maps; the rebuilt ROM SHA-256 is unchanged. Run fix_mercury_porymap.py after changing helper declarations to refresh the managed editor-visible blocks.
