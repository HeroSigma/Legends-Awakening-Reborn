# Battle day/night backgrounds

Outdoor battles use the current overworld time blend on battle environment palettes 2–4. Daytime preserves the source colors; dawn, evening and night follow the existing continuous overworld blend. Indoor, underground and other maps without natural lighting retain normal battle lighting. Pokémon, trainer, ball, UI and text palettes remain unchanged.

The initial background load and background restoration path share LoadBattleTimePalette. Each call reloads source colors before tinting and records the tinted background in unfaded storage, so subsequent animation fades and restores retain the right base without accumulating darkness. No save fields, item changes or static memory are added.

Adapted from Kasenn/pokeemerald-expansion-kasen battle-dns, commit 0a3fba5e. The donor sprite-tint and vanilla-UI edge options are intentionally not imported. The outdoor gate uses the existing MapHasNaturalLight predicate and handles indoor maps independently of feature enablement.
Source: https://github.com/Kasenn/pokeemerald-expansion-kasen/tree/battle-dns

Validation: native palette tests across four times and outdoor/indoor/cave map types; untouched UI and sprite palettes; repeated reload stability; actual daytime and nighttime wild battles on Route 102. Tests use isolated saves. Adjacent validation.json pins the tested ROM and screenshots show the battle scene.
