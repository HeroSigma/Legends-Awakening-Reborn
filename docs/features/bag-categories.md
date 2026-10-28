# Bag categories

The bag now presents 13 separate categories: Items, Poke Balls, TMs/HMs, Berries, Key Items, Medicine, Equipment, Training, Evolution, Mega Stones, Z-Crystals, Tera Shards, and Treasures. Categories derive from native item metadata; all item IDs are audited. Berries, including EV-reducing berries, remain in Berries. Fossils and valuables are in Treasures; held evolution items are in Evolution.

This is an organization expansion, not a capacity expansion. The five existing save arrays are unchanged: 30 general item stacks shared by Items and the new subcategories, 16 balls, 64 machines, 46 berries, and 30 key-item stacks. Inventory remains compatible with both normal and compact 60-box saves. No migration, item copying, or inventory reset is required. Native item storage and encryption remain the source of truth. Filters map visible list positions to native slots for selection and removal. Sorting/reordering affects only items in the selected category.

Bag navigation, per-category cursor positions, item selection/context actions, quantities, descriptions, sorting, manual reordering, item use, giving held items, tossing, and native bag artwork are adapted to the categories. Berry/machine special views retain their native IDs. Wally tutorial backup includes every category cursor. Legends Store is not yet a menu/shop: its category policy excludes Key Items and Tera Shards; prices, RTC sales, catalog and purchasing remain the next phase.

Validation: 1,125 native category/UI/inventory assertions, including use/give/toss and save/reload in both storage profiles; 288 Start menu regression checks; 2,196 PC/menu/save integration assertions. Test emulators use isolated battery saves. The player's battery save is never used for testing.
