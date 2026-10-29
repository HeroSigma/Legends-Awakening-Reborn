# Primary Tera types and summary display

New Pokemon now use their species primary type instead of a personality-selected primary/secondary type. Unassigned TYPE_NONE Tera values resolve to the primary type. Explicit types set by templates or the Devon scientist remain unchanged, and species-forced Tera rules continue to apply.

Fast Fill PC previously initialized one Pokemon and reused it while replacing species and experience. This retained the first species Tera type (normally Bulbasaur / Grass). Both fast and random-IV fills now assign the current species primary Tera type before writing each new box entry. Existing occupied slots remain untouched.

The native summary Tera badge is enabled. On the Pokemon Info page, the rightmost type badge shows the effective Tera type; the left badges show normal typing. Eggs hide this badge to avoid displaying a previous Pokemon Tera type.

Existing saved types cannot reliably be distinguished as accidental Fill PC values versus intentional scientist changes. This patch preserves them. It does not reset existing party/boxed types or replace occupied Fill PC slots. No save layout changes are needed.

Native validation covers new single/dual-type Pokemon with both personality parities, unassigned defaults, both PC storage modes, all Pokemon populated by fast Fill PC, forced species types, a scientist Grass change on Charmander, shard consumption, summary sprite/data and screenshots, and save/reload persistence. Debug Fill and effective-nature summary regressions pass separately.
