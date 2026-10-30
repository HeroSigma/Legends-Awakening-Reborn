# Custom in-game Start menu

Vol's icon strip replaces the classic text list during normal play. The overworld remains visible, the selected icon is colored, and the current app name appears in the footer. Up/Down selects apps, A opens, L/R or Left/Right changes pages, and B/Start closes. Exit remains selectable. Adventure has the original unlocked Dex, party, Bag, PokeNav, trainer card, Save and Options actions. Services retains DexNav, Journal, Legends Store and debug when enabled. Existing story unlocks remain authoritative. Some service apps reuse the closest donor icon; their footer labels identify them.

Options > MENU COLOR cycles Teal, Slate, Red and Green. It is stored in the previously unclaimed VAR_UNUSED_0x40F7 (0x40F7), outside DexNav's F8/F9 and follower FA-FF variables. It survives normal saves without changing SaveBlock size, boxed Pokemon format, or the 60-box setting. Options rows are 12 pixels apart so the new choice fits. This port adapts Phantonomy's palette-switching approach to a saved variable instead of adding a packed save option bitfield.

Only normal field menus receive the new design. Link, Union Room, Safari, Pike, Pyramid and partner-room menu construction retain their existing logic and presentation. The custom module reuses native action callbacks and save dialogs. It releases its temporary sprites/windows before field overlays, submenu transitions and save prompts. Allocation failure falls back to the existing list. EWRAM grows by one pointer (4 bytes); temporary menu data is heap allocated. No map JSON or story scenes were changed.

## Credits and references

- Vol / vol8: https://github.com/vol8/pokeemerald/tree/start_menu_1 , commit 54416d4f89d087f856f962a4913cab72d9f825a7. Icon sheet and background used with adapted layout and native action handling.
- Phantonomy / Ddaretrogamer: https://github.com/Ddaretrogamer/Sun-and-Moon-Eclipse/tree/vol_start_menu_pal_switcher , commit fea743e7b918c40c8d827a0723fc63521ffa0cd7. Alternate frame palettes and switching reference. Tilemap palette references are normalized for this engine.
- pret and RHH retain their upstream credits.

Rotom Phone was evaluated but is not installed. Quest icons, new quests and the Rift Research Log remain deferred while the Start menu is addressed.

## Validation

108 native feature checks cover all four colors in both storage modes, actual Options input, theme save/load persistence, save cancellation, Journal handoff and repeated resource cleanup. A further 446 native Start-menu regressions cover unlock combinations, cycling, repeated B input, submenu returns and control release. All 554 pass on the same ROM hash. Screenshots and pinned reports are alongside this file. Player SRAM is never used by tests.

## Footer correction

The footer uses a continuous themed color strip with no white panels or window borders. Clock, L/R page hint and selected app name use white text with a dark shadow. All four themes and all 554 native checks pass on this build.
