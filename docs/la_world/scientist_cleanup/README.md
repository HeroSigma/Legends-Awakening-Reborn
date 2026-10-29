# Remove temporary scientist placeholders

Remove scientist objects whose construction scripts only lock, face the player, show a message and release. Also remove Littleroot's explicit LA_TeleportScientist debug shortcut. Functional scripts (items, services, branching travel connections) are excluded even when an old internal label contains Construction. Native story, training and Tera researchers are preserved.

The operation changes object lists only. Map graphics, dimensions, connections, warps, coordinate/background triggers and all surviving object properties are unchanged. Prior user edits are backed up under .la_work/scientist-cleanup. The staged map versions are generated from HEAD with only the matching NPC deletions; unrelated Porymap edits remain in the working tree. Deletions the user had already made to these same placeholders are included in this cleanup commit.

Use tools/la_world/remove_placeholder_scientists.py for an inventory, or --apply to perform the filtered cleanup after closing Porymap. --stage stages the isolated object deletions, rather than unrelated local map edits. Existing importer scripts may reconstruct their historical scaffold; run this cleanup afterward if reimporting those snapshots.

See removals.json for the per-map manifest. Native smoke checks cover the Woods rescue reward, Pokévial use/refill/save handling and Nurse Joy in normal/collection storage. Other regions are checked structurally; every map is not individually playtested.
