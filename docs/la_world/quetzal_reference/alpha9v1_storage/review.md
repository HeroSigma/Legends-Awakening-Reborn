# Quetzal English Alpha 9v1: storage inspection

The supplied 32 MiB ROM has SHA256 `74bd8f7be7647c3a5088e5df300d8144b93dff624c98e0a4a0b6d19bd25179a5`. This differs from the earlier Quetzal 0.9.0 reference. It contains the FLASH1M library marker; this alone is not an end-to-end save-capacity test.

## Confirmed binary and native results

| Selector | Metadata predicate | Record bytes | Boxes | Slots |
|---|---:|---:|---:|---:|
| 0 | 1 | 38 | 37 | 1,110 |
| 0 | 0 | 31 | 45 | 1,350 |
| 1 | 1 | 28 | 50 | 1,500 |
| 1 | 0 | 21 | 67 | 2,010 |

Record strides and clear lengths occur in `0x0813857C`. Count getter `0x08137F00` reads selector `0x08137ED4` and predicate `0x08137898`. Calls to the actual count routine in an isolated mGBA core verified all four results. Synthetic RAM was used: this is not full-save or normal-UI-access validation. See runtime_results.json and the bounded disassembly files.

The menu contains “CHANGE NUMBER OF BOXES”. Format conversion warns: “All pokémon nicknames will be erased. Are you sure?”. Reducing capacity warns: “The last [number] boxes will be deleted. Are you sure?”. These do not say that expanding storage erases every Pokémon.

The ten-byte difference between formats is consistent with nickname removal. The other seven-byte difference has not been assigned a definitive meaning. Do not assume that dropping those fields is safe for Reborn.

## Reborn implications

Reborn's compiled BoxPokemon size is 80 bytes; current PokemonStorage is 34,144 bytes for 14 boxes. Sixty boxes would require 144,000 bytes for Pokémon records alone at that size. Removing unrelated features does not shrink these records.

Quetzal provides a concrete compact-storage reference exceeding the 60-box target. This is a design reference, not a drop-in binary port. Reborn requires its own versioned codec, field-by-field encode/decode rules, PC consumer integration, save-layout design and capacity testing.

The inspected selector does not establish a dependency on disabling Frontier, Contests or Trainer Hill. Retiring their gameplay and retaining their maps for repurposing is a separate design choice.

## Recommended implementation sequence

1. Specify exact retention requirements: species/forms, moves/PP, held items, experience, IVs/EVs, nature, ability, gender/shiny state, personality, OT identity, ribbons, origin and custom fields. Decide nickname policy explicitly.
2. Build a 60-box codec prototype and measure guaranteed worst-case save/RAM capacity for 1,800 occupied slots.
3. Test deposit/withdrawal, swapping, summaries, forms/evolution, breeding, trades where supported, DexNav/custom data, full save/reload, interrupted writes and corrupt records with disposable saves.
4. Add the in-game storage option after the backend is proven. Preserve existing Pokémon when expanding where possible, and block shrinking while overflow boxes contain Pokémon instead of silently deleting them.

The permanent Reborn ROM still matches the last release. This inspection wrote neither that ROM nor its battery save. The isolated experiment never opened a user battery save. No donor executable code was imported into Reborn.
