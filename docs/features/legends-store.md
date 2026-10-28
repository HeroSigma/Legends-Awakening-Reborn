# Legends Store

Available on the Services page of the normal Start menu (and debug Start menu), outside restricted link/Safari/Frontier contexts. The two-page Start menu preserves the existing entries. The shop uses the current field window style and a cached catalog, with no save-format changes.

## Controls

- Left/Right: bag category (Key Items and Tera Shards are skipped).
- Up/Down: item; L/R: five-item pages.
- A: review quantity and total; Left/Right changes quantity; A confirms purchase.
- B: cancel confirmation or exit; Start also cancels/exits.

Delivery goes directly to the correct Bag category. Quantity is 1–99; reusable machines and important items are limited to one and cannot be repurchased while owned. Insufficient funds or bag space never consumes money. Both normal and 60-box collection saves retain purchases and funds.

## Economy

Normal prices include a 25% convenience premium. One eligible category per local RTC day receives a 20% discount on the normal price, removing the premium. Categories rotate through all 11 eligible categories over 11 days. The sale is fixed when opening the store; a new session reads the current day.

Representative normal / sale prices:

| Item | Normal | Sale |
| --- | ---: | ---: |
| Potion | 250 | 200 |
| Ability Capsule | 18,750 | 15,000 |
| Ability Patch | 37,500 | 30,000 |
| Rare Candy | 6,250 | 5,000 |
| Choice items, Life Orb, Leftovers, Focus Sash, Assault Vest | 15,000 | 12,000 |
| Mega Stones | 31,250 | 25,000 |
| Z-Crystals | 25,000 | 20,000 |
| Master Ball | 187,500 | 150,000 |

Other registered items use native prices where reasonable; zero-price items get category-based values. Useful equipment, training items, evolution items, berries and general items have minimum values rather than token native prices. Native shop buy prices are unchanged. Resale is capped at the usual sale fraction of the lowest Legends Store price, preventing sale-day arbitrage while retaining lower native resale values. Key Items and Tera Shards retain their existing behavior.

## Validation

`tools/la_world/storage/test_legends_store.py` checks catalog exclusions, prices and resale safety across all eligible IDs, atomic transactions, quantity limits, full bags, reusable items, persistence in both save modes, real Start-menu entry, confirmation, quantity selection, purchases, every category, and clean exit. See `legends-store-validation.json`. The Start-menu return regression is also run to cover all unlock combinations and existing screens.
