# Starter briefcase

Case, text-background and ball/hand artwork: Mudskip. Original UI design/code: Archie, using ghoulslash's UI shell, with Grunt Lucas credited in the original guide. Reference: https://github.com/TeamAquasHideout/pokeemerald/tree/birch_case at e79c3166c4f10bffb865f0c35c61af1cfec6fc69. Guide: https://github.com/pret/pokeemerald/wiki/New-Birch%27s-Briefcase-With-Fully-Custom-Starters-by-Archie-and-Mudskip.

This presentation-only adaptation replaces the original ChooseStarter screen while keeping its native callback contract. The current three species come from GetStarterPokemon: Treecko, Torchic, Mudkip in the Hoenn build. Names, typing and full-color previews follow those species. Left/right browses and wraps; the selected ball rocks and the hand floats. A opens confirmation, A again accepts, and B backs out of confirmation. B cannot bypass the required starter choice.

No donor sample parties, custom give-mon commands, forced moves, perfect stats, held items or extra starter species are imported. The UI returns the original index through gSpecialVar_Result and invokes the existing saved callback. CB2_GiveStarter sets VAR_STARTER_MON, awards one level-5 starter and starts the native first battle, including the project's existing rescue story rules. Lab nickname and rival progression remain owned by the current scripts. GetStarterPokemon also safely rejects the first out-of-range index.

Resources are released before the callback. The safe VBlank transfer callback remains installed through the native battle transition so its palette fade can complete. BG scroll coordinates are reset rather than inherited from the map. Both storage formats keep their current count; no save layout changes.

The ROM-hashed native report records 88 checks: all three choices in both storage modes, wrapping and repeated preview swaps, confirmation/decline, required selection, correct result, no gift from the UI itself, resource cleanup, correct native award species/level/starter variable, and actual first-battle readiness. Tests use disposable saves. Choice and confirmation screenshots are included.
