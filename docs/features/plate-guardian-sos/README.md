# Plate guardian SOS: first playable encounter

The Meadow resonance is the first playable guardian. Accept Birch's Blank Plate research, or speak to him again on an older save with research already started, to receive the Petalburg Woods lead. Breloom appears at (17,19), beside the western clearing, only while its quest is active or its reward is pending. No map geometry, exits, other actors or pickups were changed.

Challenge Breloom at level 30 with two battle-ready Pok?mon. This implementation uses player-controlled doubles: Breloom starts alone with +1 Defense and Special Defense, then calls a level-25 Shroomish after the first surviving turn. Only one ally can be present. If that ally falls, a second may arrive after a two-turn interval. There are at most two calls, and no call after Breloom faints. The player must defeat every present opponent to win; capture is blocked in this quest battle. Fleeing and losing leave the quest retryable.

The battle return records victory before the field script delivers the Meadow Plate and collects its resonance. Inventory delivery failure leaves the reward pending. A prior owned Meadow Plate does not grant victory and is not duplicated. Once collected, Breloom disappears and stays hidden on subsequent visits.

The remaining sixteen guardian species/ally pairs are defined for future scripts, but their locations and activation scenes are not placed. They remain locked. The Legend Plate's adaptive Judgment behavior remains future work.

## Implementation and state

The SOS session occupies eight bytes of temporary EWRAM and is cleared on scripted battle return. It does not change save structure or consume additional persistent flags. Existing Plate flags are used for receipts; Petalburg Woods uses TEMP_13 for per-load guardian visibility. This temporary flag must not be reused by another actor in that map.

SOS is opt-in through LegendsSOS_StartGuardian (8004 = activated quest index, 8005 = level). It refuses invalid levels, inactive/completed/pending quests, another active session or insufficient battle-ready party members before changing enemies. Normal wild and trainer battles do not activate SOS.

Reinforcements enter through the native controller/switch-in script, including hazards and abilities. Fresh party slots prevent repeated EXP receipts and stale party-state reuse. The arrival hook runs after ordinary end-turn effects and checks both guardian and ally state. Existing story capture blocks remain intact.

## Validation

Native mGBA tests exercise actual introductions, aura boosts, ally arrivals, repeat-call limits, victory, fleeing, losing, cleanup and an ordinary subsequent wild battle. Separate field tests cover visibility gates, walkable approach, decline, party checks, actual battle return/reward, removal and return visits. Existing Plate save/schema and Birch scene tests are retained.

The final build passed 373 native checks: 36 SOS battle checks, 13 guardian field checks, 292 Plate/save checks, 20 Birch scene/catch-up checks and 12 live Wattson Mega checks. Native test saves are isolated; no user battery save is loaded.
