# Classic Start menu with L/R lists

The ordinary Start menu uses the original narrow right-side window, border, font, 16-pixel row spacing and cursor. The first list follows the classic order: Pokedex, Pokemon, Bag, PokeNav, player name, Save, Option, Exit. Story unlock flags still control Pokedex, Pokemon and PokeNav.

The second list contains DexNav (when unlocked), Journal, Legends Store and Exit. Debug builds additionally retain their Debug entry. L or R cycles between both lists, with a compact L/R 1/2 or L/R 2/2 hint next to Exit. Existing left/right cycling also remains supported. Switching lists resets the cursor and recreates the appropriately sized window, clearing the previous frame so a shorter list leaves no remnants.

Special-context menus (link/Union Room/Safari/Frontier) keep their previous lists and do not page. No save fields or item/character data change.

Native regressions exercise all unlock combinations in both storage modes, both shoulder buttons, repeated cycling, Exit, B/Start closure, submenu returns without reset, Journal and store access. Both complete lists are captured for visual review.
