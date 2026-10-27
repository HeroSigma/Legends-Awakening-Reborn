# Headless Heart & Soul canary runtime checks

Uses the installed mGBA 0.10 core. `runner.c` is a small wrapper, not a replacement emulator. Compile it with mGBA development headers and `-shared -fPIC`, linking libmgba, into `.la_work/amap/hns_runtime/runner.so`.

Run `test_hns.py`, `test_hns_more.py`, `test_hns_warps.py`, then `test_hns_shop.py` in that order. The first test boots the ROM and enters the native new-game callback after the title screen; it does not automate the naming/intro menus. Tests set up destinations using the native warp/map-load callbacks, then exercise normal D-pad/A/B input for entrances, exits, stairs and shop transactions. Local emulator states are build-specific test artifacts, never user saves.

Tests record screenshots and native position/map/VRAM observations under `.la_work/amap/hns_runtime/`. The shop offsets are for the current Reborn save ABI and are checked against the known fresh-game balance before purchase.
