# Badge stock milestones and Devon's Shiny Charm

Mr. Stone now rewards delivery of Steven's letter with a Shiny Charm. His dialogue explains Devon's researchers found it while studying a special stone and noticed unusually colored Pok?mon. Aren/Aria ask about it and promise to report discoveries. Named speaker colors use the existing Stone/player system. Repeat visits use new follow-up dialogue.

The one-time reward uses `FLAG_LA_STONE_SHINY_CHARM` (`FLAG_UNUSED_0x905`), independent of `FLAG_RECEIVED_EXP_SHARE`. Starting with EXP Share therefore cannot skip the letter reward. Older saves that already delivered the letter can claim it on their next visit. Owning a Charm from another source is acknowledged without adding a duplicate, and the claim flag is set only after successful delivery or that acknowledgement.

## Store milestones

| Gym milestone | New stock |
|---|---|
| Roxanne | Small EXP Candy, vitamins/EV mochi, Macho Brace |
| Brawly | Medium EXP Candy, mints, Power items, Ability Capsules, Fresh-Start Mochi |
| Flannery | Rare Candy, large EXP Candy, Dynamax Candy, Ability Patches |
| Winona | XL EXP Candy, Bottle Caps |
| Final Hoenn Badge | Gold Bottle Caps |

Feathers and XS EXP Candy remain early stock. Higher Gym milestones include earlier stock. League completion grants the full training catalog. Stock follows the highest named Hoenn Gym milestone, so notifications stay accurate when earlier Gyms are skipped. Existing prices, daily sales, reusable TM ownership rules, Strange Ball exclusion and Master Ball League gate remain intact.

First-victory badge scripts announce the new services/stock at these milestones. Roxanne's notice explains the scientist unlock; Brawly's explains START on the summary Stats page. Rematches and repeated Gym reward claims do not replay the notices.

Validation: 344 native milestone/reward checks cover locked purchases without money/item changes, all tiers, skipped-Gym ordering, letter prerequisites despite owning EXP Share, repeat/owned-Charm cases, save/load and rendered notices. Existing suites pass 939 Store, 65 progression/capture and 569 TM checks. Tests use isolated batteries, never the player's save.
