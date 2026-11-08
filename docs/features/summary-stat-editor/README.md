# Summary stat editor

Open the Stats page of a party or PC Pokémon's Sword/Shield summary and press Start. The editor displays calculated stats, six EVs and IVs, effective nature and available ability. Select a stat and press A, then use Left/Right for single steps, Up/Down for ten, or L/R to clear/max the selected stat. The editor enforces 31 IVs, 252 EVs per stat and 510 total EVs. Start in the editor sets all six IVs to 31. Changes apply immediately; B returns to the same Pokémon's Stats page. L/R on the main editor screen cycles eligible party Pokémon. Return to the PC to choose a different boxed Pokémon.

No level, Tera type, move or nickname editing is available here. The existing summary move relearning and rename features remain. Tera changes still require the Devon scientist and shards. The training scientist's two remaining services are level catch-up and EV presets, both free. Edits are unavailable in battles, restricted previews and for eggs. Party edits preserve identity, damage, and fainted state; boxed edits write through the project's storage APIs and persist with the normal save.

Adapted from [PCG06's Stat Editor](https://github.com/PCG06/pokeemerald/tree/feat/stat_editor), revision cae26d8d50bbc52a7ba9d0acb23767e272498185, based on pokeemerald-expansion. Graphics use the project teal palette. The scrolling tilemap is allocated on entry and freed on exit. No save layout or existing item IDs changed.

Native test: tools/la_world/storage/test_summary_stat_editor.py, 36 checks with isolated saves. Covers both storage modes, real summary entry/return, 31 All, EV budget, abilities, effective nature, damage/fainting, 60-box writeback/save reload, and both retained scientist services. See validation.json for the exact tested ROM hash.
