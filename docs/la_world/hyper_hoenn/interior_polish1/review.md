# Hoenn interior polish: opening towns

Reviewed32 non-gym interiors in Littleroot, Oldale, Petalburg and Rustboro, including Birch's lab, both player/rival houses, Wally's house, all three Devon floors, Cutter's house, flats, school, Marts and both Pokémon Center floors. Current source was clean before this audit; existing Porymap edits are retained.

Four contact sheets show current tile art, orange active-event markers, gray virtual/hidden-event markers and cyan warp cells. All32 rooms have valid used palette references and coherent furniture/wall/floor arrangements.71 outgoing warp arrivals resolve valid destination slots with a free adjacent floor cell.98 active NPCs have reachable floor or counter interaction approaches. Static checks found no access defects needing map edits.

Native virtual clock/PC/rival proxies in Littleroot's upstairs rooms, the invisible Mr.Stone interaction proxy in Devon3F, and Walda's bed interaction cell are intentional. They must not be cleared or relocated as stray blockers. Native reward-ball flags and conditional actor overlap are retained. Fixed NPCs beside chairs, lab furniture, counter staff and school pupils remain at their authoritative expansion coordinates.

No map geometry, events, scripts, graphics, warps, progression flags, saves or validated donor imports were changed in this batch. No new ROM is necessary. This report is visual/static QA; actual story/service behavior still needs the runtime checklist. Petalburg/Rustboro gyms are explicitly excluded for their separate puzzle/story batch.

Recommended next interior batch after runtime sign-off: Dewford/Granite Cave support rooms, Slateport Museum/Shipyard/Mart/Center, then Mauville. Furniture restyling should use a stated visual preference; current opening interiors need no corrective tile churn.

Artifacts: `inventory.csv`, full cell/event inventory, `access_audit.json`, four visual contact sheets and `runtime_checklist.md`. Re-render with `tools/la_world/importers/amap/hyper_assets/hoenn_interior_polish.py` after any manual cleanup.
