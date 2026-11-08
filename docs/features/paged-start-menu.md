# Two-page Start menu

The normal Start menu uses two themed pages, with a title, page number, separator, 18-pixel row spacing, and control hints.

- **Adventure:** Pokemon, Bag, Pokedex, DexNav, PokeNav. Story unlocks still control visibility.
- **Services:** trainer card, Journal, Legends Store, Save, Options.
- Debug builds add Debug to Services; six rows fit and omit the footer.

Left/Right or L/R changes pages and resets the cursor to the first row. Up/Down wraps within the current page. A opens a selection; B or Start closes. Returning from a submenu retains its page and selection. The current page is session-only and does not alter save data. Restricted link, Safari, and Frontier menus retain their existing actions and behavior.

The wider window uses base tile 0x100 so its 270 tiles end below the standard frame graphics at 0x214. This prevents the larger menu from overwriting its own border artwork.

Validation uses native mGBA with isolated saves: all 16 combinations of four story unlocks, both storage modes, both close buttons, both page directions, shoulder-button wrapping, repeated submenu visits and rapid B presses, Journal, and actual Legends Store purchases. Screenshots show both fully unlocked pages.
