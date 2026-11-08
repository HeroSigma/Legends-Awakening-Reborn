# Animated Legends Awakening title

Adds a traveling glint across the bright logo lettering and waves of light along the fractured rift. The forest, people and Iron Valiant remain still. The illustration itself retains its current composition; this is localized light animation rather than camera movement or a flashing full-screen filter.

A deterministic asset conversion (`tools/la_world/storage/build_title_animation.py`) allocates 192 static colors and 56 local animation colors to the existing concept source. Logo bands brighten in a left-to-right sweep. Rift bands pulse with staggered sine phases, making the light travel along the tear. The native palette upload runs in VBlank. No extra persistent EWRAM state, background copies per frame or save fields are required. Animation pauses during native fades so Start, A, menu return and save shortcuts keep their existing transitions.

`title-animation.gif` is a nearest-neighbor enlarged recording of actual native emulator frames. `validation.json` includes the tested ROM hash. Tests verify changing logo/rift bands, unchanged static palette/bitmap, distinct native frames and original title transitions in both 14/60-box modes. All testing uses isolated disposable saves.
