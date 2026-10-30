# Sword & Shield Bag menu

Ports Montblanc / montmoguri swsh_bag_menu at 73aa2c1d2f94ad81d562007d2706d64b5c282f7e. Source: https://github.com/montmoguri/pokeemerald-expansion/wiki/Sword-%26-Shield-Bag-Menu . Upstream credits include ShantyTown, Archie, Kasen, Zatsu and PCG; retain shared SwSh asset credits.

## Integration

The SwSh scrolling list, item preview, quantity controls and move/berry information use teal accents matching our other SwSh interfaces. The original expanded Bag storage remains authoritative. All 13 category views stay available: Items, Poke Balls, TMs/HMs, Berries, Key Items, Medicine, Held Items, Training, Evolution, Mega Stones, Z-Crystals, Tera Shards and Treasures. Ability Patch/Capsule remain in Training; X Items remain in Items. Store exclusion rules for HMs, Key Items and Tera Shards remain unchanged.

The donor's five-pocket indices were adapted to category views for navigation, item reads, quantities, sorting, moving and tossing. A per-category native-slot cache avoids repeated scans of the expanded physical Items pocket. It is invalidated on list updates. The current item-table audit finds a maximum of 190 items in a category, within the 256-entry buffers. Wally's temporary tutorial inventory suspends/resumes the expanded Bag and restores all category cursor positions.

Item Use/Give retains our installed SwSh party selector and its bulk training/cap handling. The donor inline-party item engine, alternate battle pocket scheme and Pyramid skin are disabled. Battle uses the same 13 categories. Existing Pyramid handling remains available where permitted by storage mode. No SaveBlock, packed inventory, PC format or map changes.

## Validation

9765 native checks on one pinned ROM hash: 1162 category/routing/real Use/Give/Toss and save checks; 7124 full-inventory/legacy migration/checksum recovery/debug fill checks; 934 Legends Store checks; 79 bulk training checks; 20 real wild-battle healing/capture checks; 446 Start-menu lifecycle checks. Both 14-box and 60-box profiles are covered with isolated emulator saves. Screenshots and reports are pinned here.

Existing UI tests now allow the donor text callbacks to finish, wait for the actual Bag input task on a full inventory, and account for the donor list omitting the classic Close Bag row. Temporary test HP buffers use unused IWRAM instead of overlapping gWindows.

Build: EWRAM 261364/262144 bytes, IWRAM 28140/32768 bytes, ROM 32692596/33554432 bytes. Release updates the permanent ROM while preserving its paired save.
