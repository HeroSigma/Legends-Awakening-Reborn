# Expansion raid PR review

Reviewed 2026-11-07. Research only; no gameplay changes.

PR 10319 is closed and unmerged, head accda67a250a678db71ced2d8b33e76725f968f2. Its native battle hooks and compact state are useful, but the barrier creation branch is unreachable, Dynamax levels 21-24 fall through to rank 5, Tera initialization is empty, and both added raid test files are empty.

PR 2869 is closed and unmerged, head c8e478e116d2f1d97ad5ea2f602000147a5e7933. It offers a broader older prototype: intro UI, partner selection, 2v1 layout, shields and capture flow. Its source lists partner faint/switch and ability bugs; shield calculations and generation still have TODOs.

Prefer native Expansion integration: newer hooks from 10319, presentation and capture reference from 2869, CFRU as a behavioral reference. Neither PR is a ready-made merge. First prove one isolated Max Raid and test targeting, shields, partner replacement, victory capture, storage and cleanup. Preserve existing story and gimmick controls.

Memory clarification: 660 bytes of static EWRAM headroom is not total free runtime memory. The allocated gHeap is already included in static totals. Measure peak battle heap as well as ROM and global allocation.

Sources:
https://github.com/rh-hideout/pokeemerald-expansion/pull/10319
https://github.com/rh-hideout/pokeemerald-expansion/pull/2869
