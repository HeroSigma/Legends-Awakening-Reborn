# Field portraits

Speaker-driven 64x64 field portraits, adapted to the Legends Awakening message/name box system. Reference: Mudskip's field-mugshot branch, commit 61fa4190ff5749c0f75440fc6697f7e4299b2f8e (https://github.com/mudskipper13/pokeemerald/tree/feature/field-mugshot). The reference supplies the display approach and dark-cave OBJ-window technique; this implementation uses a single owned portrait, automatic speaker mapping and the project's existing graphics rather than donor example characters.

Portraits appear above the right side of the message box. Existing dialogue width, speaker names, colors and scripted scenes are preserved. Available art: player (both genders), Birch, Red, Brendan, May, Wally, Norman, Giovanni, Oak, Blue, Green, Shadow Triad and the named Aqua grunt. These are the existing full trainer pictures and Birch introduction art, not newly drawn expressive busts. Other speakers retain ordinary dialogue until suitable art is supplied. No generic substitute is shown for Cyrus or the other professors.

Player colors follow the saved dynamic palette. Rival palettes remain original. The reserved portrait tag is weather-blend immune. Dark maps use a matching OBJ-window mask and restore their prior window bits on close. There are no save format changes or new story gates. Pokenav calls and signs keep their existing layouts.

The portrait is cleared on message close/stop, field reset and window teardown. Ownership checks protect reused sprite IDs. Sprite, tile and palette exhaustion fall back to normal dialogue; palette allocation never evicts a generated overworld encounter. One temporary 2KB decompression buffer is freed immediately after upload. Sprite data is shared with its optional dark-cave mask.

Native tests use disposable saves only: all mapped speakers and missing-art fallbacks, both genders/storage modes, speaker switches, custom player and unchanged rival colors, cave window restoration, sprite/palette exhaustion and resource cleanup. Speaker-color regressions and complete Littleroot/Route 103 chapter runs (Riolu in normal storage; Rockruff in collection storage) are recorded in ROM-hashed reports.
