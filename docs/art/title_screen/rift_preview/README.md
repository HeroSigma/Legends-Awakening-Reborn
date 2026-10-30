# Legends Awakening title-screen preview

The game title is **Legends Awakening**. Reborn identifies the restarted project/repository, not the displayed game title.

The built-in image generation tool produced `concept-source.png`. Final scene prompt: a pixel-art 3:2 GBA title-screen concept with the exact logo LEGENDS AWAKENING, two trainers and a researcher investigating a fractured spatial rift as Iron Valiant emerges; woodland twilight, violet/gold/white light, PRESS START, no Reborn subtitle, no device frame or watermark. The reference concept was converted to 240x160 with 256 colors and GBA BGR555 palette precision. `title-native.png` is captured from the native emulator, not an artist mockup.

This first playable preview is a still image with native palette fade transitions and title music. Mode 4 displays the indexed image without adding persistent save state or an EWRAM framebuffer. It does not yet animate the rift or Press Start. No new-game or story code changes. A/Start opens the existing main menu; B there returns to this title. Existing reset-RTC, clear-save and berry-update shortcuts retain their callbacks. FireRed mode retains its existing title implementation.

The generated bitmap, palette and editable indexed PNG are in `graphics/title_screen/legends_awakening/`. Native disposable-save tests cover initial title display, no-save navigation and returning/continuing with both 14 and 60 boxes. `validation.json` records the ROM hash and 21 assertions. User saves are never used by these tests.
