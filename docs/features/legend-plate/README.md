# Blank Plate and Legend Plate foundation

Speak to Birch again after receiving the Rift Tracker to accept the Blank Plate research. Declining leaves the offer available. Both relics remain in the ordinary Plates category, protected from selling, tossing and ordinary shops. Using one in the Bag shows resonance progress.

The seventeen guardian quests require explicit story activation and a recorded victory. A victory creates a pending reward; collecting that reward records completion. Existing Plate ownership does not complete quests. Failed inventory delivery remains retryable, and claiming twice gives no duplicate reward. After all seventeen receipts, return with the Blank Plate to Birch's laboratory to awaken the Legend Plate. The original elemental Plates remain in the Bag.

## Current scope

This is the quest and item foundation. Guardian actors, locations, Totem/SOS battles and the Legend Plate's adaptive Arceus/Judgment battle behavior are not implemented yet. The Legend Plate currently serves as a protected research relic. The next SOS work belongs on its own feature branch in the same main project.

Quest IDs 46?63 use dedicated state flags rather than extending the older two-bit ledger into Gym flags. Active guardian flags occupy 0x8E5?0x8F5; research receipt is 0x907, victory flags 0x908?0x918, awakening is 0x919. Item IDs 877 and 878 are appended; older 877-item Bag saves are migrated with empty new slots.

## Icon

The Legend Plate icon follows the user's supplied silver-gray Arceus tablet reference: beveled tablet, central four-point star and surrounding pointed motifs. An image-generated pixel-art conversion was reduced to 24?24 pixels, a transparent palette entry and twelve opaque RGB555 gray shades. The indexed PNG and matching sixteen-entry palette are under graphics/items. It replaces the temporary gold icon. The Blank Plate keeps its dormant gray Plate icon.

## Validation

Native mGBA checks cover both storage modes, prior Bag-schema loading, activation, loss/flee/capture rejection, reward retries, duplicate prevention, awakening, persistence, quest menu and Bag rendering. A separate scene test exercises Birch's actual offer and awakening scripts. Shop tests verify both relics remain excluded from ordinary sales.

All source work is in /home/allan/projects/Legends-Awakening-Reborn. The retired Saffron worktree was removed after its unique Plate files and local working files were transferred and verified. Unrelated animation research and user map edits are preserved.
