# Devon Tera economy

## Progression

Automatic shard rewards and the Devon basement laboratory unlock when both native `FLAG_RETURNED_DEVON_GOODS` and `FLAG_RECEIVED_POKENAV` are set. This is after recovering Devon Goods and meeting Mr. Stone. Existing saves with those milestones qualify automatically. No new save fields or story dialogue were added.

## Wild rewards

- Each defeated wild Pokémon gives one shard matching its species' primary type. Battle transformations and its Tera Type do not change the reward.
- Each successful catch gives the same reward during ownership transfer, including when the Pokémon is sent to storage.
- Each rewarded Pokémon independently has a 1% chance of an additional Stellar Shard.
- Shards go directly to the Bag without reward messages, sounds or pickup objects. Full Bag/stack capacity follows native `AddBagItem` failure behavior; there is no overflow queue.
- Trainer, tutorial, first rescue, link, recorded, Frontier and ghost battles do not award shards. Escaping from a live Pokémon gives none. Defeated opponents in a wild double battle still count; a caught opponent is not paid twice at cleanup.

## Held equipment

Random wild held items use one 5% roll per Pokémon. This is separate from shard rewards and is available before the Devon milestone. Explicit scripted or DexNav held items are preserved and bypass the random roll. Native species items remain candidates, rather than retaining their old higher default rates. Compound Eyes does not increase the agreed 5% rate.

For a successful roll, the pool considers:

- Item-based Mega Evolutions available to that species or a later evolution, up to three forward evolutionary steps. This includes both Charizardites on Charmander/Charmeleon/Charizard. Branches and enabled form-change tables are used directly.
- A generic Z-Crystal matching the primary type.
- Native species items, Choice Band/Specs based on attacking stats, Choice Scarf, Leftovers, Focus Sash, Life Orb, Eviolite for evolving species, or Assault Vest.

For Mega families, half of successful held-item rolls choose a compatible stone; one quarter choose the matching Z-Crystal; the remainder choose native or battle equipment. Non-Mega families use Z-Crystals/native items/battle equipment. The existing Altering Cave special-item table remains available within the same 5% roll.

There are no automatic equipment drops. Catch the Pokémon or use the native theft mechanics to recover its item. Player theft against wild opponents may take Mega Stones and Z-Crystals; native empty-hand, damage, Sticky Hold and other move/ability requirements still apply. Trainer theft, Knock Off, Trick and form-item rules otherwise remain native.

## Scientist

The existing Hoenn_Basement map remains canonical `MAP_HYPERHOENN_34_10_BASEMENT` and is entered from Devon Corp 1F's basement stairs. The entrance scientist moves aside after the native milestones. The service scientist is at (4,2), with a clear interaction cell (4,3). A construction scientist continues blocking the separate Ultra Space entrance at (6,9).

Choose from three pages covering all 18 regular types and Stellar, choose a party Pokémon, then confirm the quoted item/count. Normal treatments cost 50 shards of the selected type; Stellar costs 150 Stellar Shards. Cancellation, insufficient shards, Eggs, invalid selections and choosing the existing Tera Type consume nothing. The commit operation revalidates before spending. HP, levels, species, held items, trainer ownership and moves are preserved. The native Tera Type field and Bag storage are used; no save ABI changes.

## Validation

Native mGBA tests are in `tools/la_world/importers/amap/hns_runtime/test_legends_tera*.py`. They use disposable saves, exercise linked ARM functions, complete real wild battles/capture/theft flows, drive the scientist UI, and perform a native battery save/continue. The capture fixture enters the native ball-throw battle script directly to make the catch deterministic.
