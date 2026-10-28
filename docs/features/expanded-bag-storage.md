# Full bag storage and debug fills

The bag can hold all 873 registered items at once, in the 13 existing categories, with up to 999 of each item. Fill Bag tops up consumables and equipment to 999; reusable machines and important items are added once. It preserves larger existing quantities of an important item. Running Fill Bag again does not add duplicate stacks. Individual fill commands now follow the displayed categories, including Medicine, Training, Evolution, Equipment, Mega Stones, Z-Crystals, Tera Shards and Treasures.

Location: Debug menu > PC/Bag > Fill > Fill Bag (all items). The normal bag UI, removed indicator dots and fixed list border are retained. This update does not enable the icon grid, graphical Start menu, or Legends Store.

## Save format

Inventory quantities use 10 bits per item ID, with a runtime logical slot map for native bag APIs. There are no heap pointers in saved inventory data. Existing SaveBlock structs, the 60-box Pokemon codec and the legacy collection ABI remain unchanged.

Normal saves store a versioned inventory extension, with CRC, in unused space at the end of the final PC sector. The extension is included in that sector's native checksum. Collection saves use a V3 stream that packs inventory and PC item quantities, excludes genuinely unused SaveBlock2 filler bytes, and keeps all live story fields and all 1,800 PC records. V2 collection saves remain readable. The V3 stream uses 65,129 of 65,152 available payload bytes (23 spare). Future item growth must pass explicit item-bit, quantity-bit and save-capacity assertions.

Existing inventories migrate on load without changing the source battery file. The new format is written only on the next normal in-game save. A legacy inventory with more than 999 total copies of a single item remains in its original layout rather than losing excess items; reduce that oversized stock and reload to migrate. All quantities in the current player's saved inventory were verified in an isolated copy. Item order is rebuilt by item ID on reload; manual ordering applies for the current session.

The native quantity/encryption interfaces, party-menu return, item use, giving, toss, sorting, bag relocation and Wally's temporary tutorial bag are adapted. Per-category lookup caching keeps a fully stocked bag responsive. Runtime test scratch space is moved above the expanded live inventory state.

## PC fill

Both Fast and Slow fill commands scan the PC for owned species, preserve occupied slots, and add missing enabled species once. They stop when the species list ends or storage is full. The list never wraps to the first Pokemon. Repeating the command after a complete fill adds nothing. Normal storage remains limited to 420 slots; collection mode has 1,800.

## Validation

Native mGBA tests exercise full stock, all categories, 999-count persistence, normal and V2-to-V3 migration, the real debug-menu actions, both PC fill paths, deduplication, end-of-list termination, full-pocket navigation, and damaged normal-sector recovery. Additional PC integration, Nurse Joy, training scientist, Start menu and host format tests pass. No tests write the player's actual battery file. The release receipt records counts and ROM/save hashes.
