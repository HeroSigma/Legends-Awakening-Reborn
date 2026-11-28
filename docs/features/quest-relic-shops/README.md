# Quest relic shop exclusions

Implemented as a shared ordinary-shop acquisition policy, without save migration.

- 83 items are reserved, including 17 Plates, 17 Memories and four Genesect Drives.
- Explicit relics cover Red/Blue Orbs, Soul Dew, Adamant/Lustrous/Griseous item
  families, Rusted weapons, Ogerpon Masks, Urshifu Scrolls, form keys and encounter
  tickets, and the existing Legendary/Mythical Mega Stones and Z-Crystals.
- Meteorite is included because the native Deoxys form tables use it. Generic
  type Z-Crystals remain ordinary even though Arceus can use them for forms.
- Life Orb, Flame Orb, Toxic Orb, Adrenaline Orb and Adamant Mint remain ordinary.
  Fossils and general treasures are not blanket-banned.
- Normal Mart list construction filters relics alongside existing stock criteria.
  The payment handler checks again before adding inventory or subtracting money.
  Decorations keep their separate purchasing path.
- Legends Store uses the same policy for catalog, price and purchase validation.
- Existing inventory, item use, script gifts and manual save behavior are unchanged.
  Owned relics do not bypass an encounter or story gate.

The Devon Memory vendor and Plate placements are later parts. A dedicated
Memory vendor must explicitly allow its intended stock after the Type: Null
unlock instead of using the ordinary Mart path unchanged.

## Validation

`test_quest_relic_shops.py` uses an independent relic manifest, compiled native
item metadata and an isolated mGBA battery. It checks pre-badge, all-badge and
Champion policies; blocked purchase quantities/prices/money; all reserved items'
script awards and save/reload ownership; mixed and empty native Mart lists;
and a live native Mart with an injected forbidden payment selection.

The form-table review covers the current Legendary/Mythical Mega items, primal
Orbs, Sinnoh form relics, Zygarde Cube, Silvally Memories, Genesect Drives,
Ogerpon Masks, Necrozma's crystal, Deoxys's Meteorite and Shaymin/Hoopa keys.
Form-key fusions and old held orbs remain explicitly covered too.

1,213 relic-shop checks and 1,241 existing gimmick Store/Wattson checks passed.
No user save is loaded by these tests. `ordinary-mart.png` shows a test catalog
with Red Orb removed while Potion and Life Orb remain.
