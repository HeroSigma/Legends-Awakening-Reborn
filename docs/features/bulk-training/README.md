# Bulk training items

Using Rare Candies, EXP candies, vitamins or feathers on a party Pokémon offers a quantity prompt when more than one useful item is available. Use the D-Pad to adjust the count, A to use it and B to cancel. Battle item use remains unchanged. EV-reducing berries are not included in this pass.

The maximum respects bag quantity, the current badge level cap, the per-stat EV item limit and the total EV limit. The last item may contribute only the remaining EVs or EXP needed. Items beyond those actually applied are not consumed. Existing stat screens, level-up move learning, evolution and single Rare Candy evolution-only handling remain in the original flow. EXP text reports actual awarded experience.

Implementation adapts the quantity-selection idea from Kasenn/pokeemerald-expansion-kasen multiuse-candies-evitems, commit 0ab471f6. Reborn uses the current native single-item effect engine repeatedly, rather than importing the donor's incompatible multi-argument item engine. State lives in the existing allocated party menu object, with no SaveBlock or static EWRAM expansion.
Source: https://github.com/Kasenn/pokeemerald-expansion-kasen/tree/multiuse-candies-evitems

Native tests check all six vitamins, partial total EV room, Rare/EXP Candy caps, cancel behavior and confirmed item consumption in the real quantity menu. Test batteries are isolated from the user's save.
