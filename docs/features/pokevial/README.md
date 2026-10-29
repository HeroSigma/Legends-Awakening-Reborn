# Three-charge Pokévial

A reusable KEY ITEM awarded after protecting the Devon and Silph researchers in Petalburg Woods, alongside the existing Great Ball. For already-completed saves, Devon's first-floor receptionist grants the reward once. If the item cannot fit, the receptionist can retry. No repeated free refills from the reward conversation.

Use from the bag or registered shortcut outside battle. A confirmation shows remaining charges. One charge fully restores the party's HP, fainted partners, status and PP. Eggs are unchanged. Already-healthy or empty parties do not spend charges. The vial refills on HealPlayerParty, including Pokémon Centers and scripted full-party rest stops. Vial healing calls HealPokemon directly so it neither refills itself nor heals boxed Pokémon. Battle use and shop sales are unavailable.

The icon shows full/two/one/empty charge stages. Persistent charges use VAR_LA_POKEVIAL_CHARGES (unused 0x40E5); reward uses FLAG_LA_POKEVIAL_RECEIVED (unused 0x45). Existing item IDs remain stable; new item 874 is appended. No change to the native save-block layout. Packed normal/collection inventory readers accept prior item counts, zero-extend old inventories and write the current count. Collection payload transfers use the saved inventory length rather than shifting the old box payload by one byte.

## Attribution

Feature inspiration and original implementation: [Pokémon San Fran Pokévial branch](https://github.com/PokemonSanFran/pokeemerald/tree/pokevial) and [documentation](https://github.com/PokemonSanFran/pokeemerald/wiki/pokevial). Original concept credited there to BuffelSaft; implementation contributions include Karathan. Pokévial icons and palette by Horo, retrieved unchanged from that branch (pokevial0, 3, 6, 9 and pokevial.pal). Native item/healing and save integration were adapted for this project's expansion and compact collection storage rather than merging vanilla save-block changes.

## Validation

Native isolated-emulator tests exercise all charges, healing, no-op/empty use, icon stages, egg preservation, actual registered/bag entry points, cancellation, reception catch-up, once-only rewards and save/reload in both storage modes. Migration fixtures are generated from the archived pre-feature ROM, not player saves. Forest regression uses injected native battle outcomes to test scene flow; it does not measure combat difficulty.
