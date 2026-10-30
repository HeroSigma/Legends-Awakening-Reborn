# Dynamic battle move information

Press L while choosing a move in battle to open the existing description panel. Power and accuracy now reflect supported current effects. Increased values are green, decreased values red, and ordinary values retain the normal text color. Guaranteed-accuracy situations use the existing dash display, colored as an improvement when appropriate. Written move descriptions and automatic wrapping are retained.

Adapted from Flash1Lucky/pokeemerald-expansion, dynamic-move-descriptions, commit c32a3d9fb955528980bf5d776bca0800ebd21135. The donor API predates our DamageContext/BattleCalcValues arrays, so its code was adapted to the current engine rather than copied wholesale. Source: https://github.com/Flash1Lucky/pokeemerald-expansion/tree/dynamic-move-descriptions . Credit Flash1Lucky, RHH and pret.

The preview reuses engine base-power and accuracy calculations with scripts/recording disabled and restores the item-effect scratch battler, including Max-move paths. It does not consume randomness or alter battle state. No persistent RAM buffers or save fields were added. The previous three-byte numeric stack buffers are replaced by direct string output, avoiding a terminator overflow for three-digit values.

## Scope and limits

- This is modified base power, not predicted damage. STAB, effectiveness and damage-formula multipliers are not added to the power number.
- Enemy abilities/items are not read into the preview calculation. Accuracy uses the opposite living opponent and visible field/stat-stage conditions; doubles do not show a per-target damage or hit forecast.
- Random, target-dependent, and turn-order-dependent power effects retain their authored base value. This includes Knock Off, Brine, Low Kick, Heat Crash, Electro Ball, Gyro Ball, Magnitude, Present, Payback and similar effects. Analytic/Rivalry power is conservative.
- Max moves use their own power and descriptions. Z-move previews retain the baseline until a dedicated conversion is supported.
- Summary and relearning screens retain their normal written descriptions and base values; battle-only effects are not projected outside battle.

## Validation

Native ARM tests boot a real wild battle and check 65 cases/assertions, including Technician, Iron Fist, Tough Claws, Muscle Band, Wide Lens, Compound Eyes, No Guard, sun/rain Thunder, burned Facade, Acrobatics, status moves, Max Strike/Guard, hidden enemy ability isolation and invalid IDs. Dry-run checks verify battle structures and RNG/scratch values; the idle RNG loop is paused for deterministic observation. The actual Fight/L panel and its positive text palette are checked and captured in facade.png. A further 28 native summary/protagonist/packed-box regression checks pass on the same ROM. Both reports include the ROM hash.
