# Timeless Woods: the item and the rifts

The main Hoenn_Timeless_Woods map (78.0) remains in its existing group with its original layout, warps and connections. This is project-owned dialogue and state; no donor gameplay scripts are transplanted.

On first entry the player thinks: “This place… It feels familiar. But why?”

Walking onto (16,13) starts the meeting. Giovanni stands at (25,12), Cyrus at (23,12), and the regular item-ball object at (24,12). The camera moves eight cells right and one up, centering on (24,12). Both men face each other. Giovanni removes the ball and steps into its cell. They discuss using the item to stabilize rifts, gain reliable travel between worlds, and control the crossings while keeping the professors and children away. This leaves the item's nature and the wider plan open for later chapters.

Both men walk right to x33 and disappear beyond the camera edge. No warp or destination is invented for their departure. The camera returns to the stationary player. The player recognizes them without recalling where, intends to inform Professor Birch, and wants more information. This does not yet add a follow-up Birch conversation.

## Saved state

- FLAG_LA_TIMELESS_WOODS_ENTERED / 0x3A: first-entry thought finished.
- FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN / 0x3B: meeting completed; hides both men on future visits.
- FLAG_LA_TIMELESS_WOODS_ORB_TAKEN / 0x3C: item taken; hides the ball.
- VAR_TEMP_1 and VAR_TEMP_2 are map-local scene gates initialized from these flags. No save structure changes.

A saved game that has already heard the Route 102 call can still see this new scene; its state is independent. Saving during the locked scene is unavailable. No physical player movement is forced.

## Graphics

The two new native graphics IDs are appended before NUM_OBJ_EVENT_GFX, preserving every existing graphics ID. Their indexed PNGs and shared palette are copied from Hyper 081 / 096. The nine used frame payloads match the previously validated Hyper asset bank byte-for-byte. Native graphics definitions make these actors editable in Porymap. All other donor-library candidates remain staged only.

## Runtime review

Re-enter Timeless Woods from your current save. Check the arrival thought, then walk onto (16,13). Watch the facing, item pickup and departures; revisit and save/reload to confirm the event remains completed. Automated native checks exercise both player genders using disposable saves only.
