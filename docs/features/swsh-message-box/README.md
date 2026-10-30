# Sword & Shield field message box

Adapts Montblanc / montmoguri's swsh_message_box branch at b576dfa57c519f5a070e0562f524d4cdfa9ce14a. Source: https://github.com/montmoguri/pokeemerald-expansion/tree/swsh_message_box . The rounded message and name-frame art and source tilemap retain donor attribution. Frame shadows use our teal shades; white text areas and established character colors remain.

## Integration

The field dialogue window is 26 tiles wide. The new 25-tile message frame moves the standard border graphics start from 0x214 to 0x21A to avoid overlap. Name panels use 15 frame tiles and three window rows. Existing speaker parsing, explicit color overrides, protagonist/rival/professor defaults and evil-team palettes remain intact. Name text stays immediate as before.

PokéNav calls retain the original two-row name panel, six-tile graphics, positioning and text offset. Name drawing/filling/clearing branches by that context. Custom dialogs honor their supplied tile/palette, and shorter description boxes preserve top/bottom bevels instead of stamping a fixed six-row frame. Dialogue clearing uses the actual two-tile side margins and avoids unsigned underflow at the screen edge. Full-sheet streaming synchronization and the custom Start menu are untouched.

No scripts, story flags, maps or save formats changed. The speaker-color test uses unused IWRAM for its temporary explicit-color text instead of overlapping EWRAM window data.

## Validation

969 native checks on the pinned ROM hash: 136 repeated message/name frame geometry and transparent-tile cleanup checks across both storage modes; 212 speaker-color/default/explicit-override checks; 141 spoken-story continuation and line-width checks; 34 actual item-pickup/description cleanup checks; 446 Start-menu lifecycle checks. Story battle outcomes in the story test are injected wins to test continuation, not difficulty. Tests use isolated saves. Screenshots and reports are pinned here.

Build: EWRAM 261364/262144 bytes, IWRAM 28140/32768 bytes, ROM 32693528/33554432 bytes. Release updates the permanent ROM and preserves its paired save.
