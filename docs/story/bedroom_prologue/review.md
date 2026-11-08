# A Strange Delivery — bedroom prologue

Source: Legends Rewake, current bedroom draft. Mom is ELARA; protagonist uses the selected player name. Creator and Birch intro remain intact.

New games now start in the appropriate canonical Littleroot bedroom, without truck/exploration supplies. Existing saves are not relocated. Existing exploration ROM downloads remain separate.

Flow: black dream → wake in bed → PC chime → free bedroom movement with stairs gated → delivery notice → clock setting → Elara arrives → Tera Orb gift → Elara leaves → stairs unlock. Normal PC use returns after reading the notice; normal clock viewing returns after setting it.

The canonical VAR_LITTLEROOT_INTRO_STATE is authoritative. New semantic stages 10–14 avoid changing the meaning of legacy save states 1–6. Completion returns to native stage 7, allowing the existing Hoenn progression to continue without replaying the moving-in/TV scene.

Reserved persistent flags (verified unused before allocation):
- 0x21 FLAG_LA_INTRO_ACTIVE: identifies new Legends story saves.
- 0x22 FLAG_LA_PC_DELIVERY_MESSAGE_READ.
- 0x23 FLAG_LA_RECEIVED_TERA_ORB.
- 0x24 FLAG_LA_TERA_ORB_ACTIVATED: set by the package scene.
- 0x25 FLAG_LA_ELARA_PACKAGE_SCENE_COMPLETE.
Existing FLAG_SET_WALL_CLOCK remains authoritative. No save-structure changes.

User revision: Tera Orb ownership enables normal Terastallization immediately. The prologue-specific activation gate has been removed, so existing saves with the Orb also work. B_TERA_ORB_ALWAYS_CHARGED is TRUE: no recharge trip is required between battles. Native per-battle gimmick and eligibility rules remain authoritative.

The two Hyper bedrooms retain their layout, tilesets and warp destinations. Two staircase approach triggers per room gate the intro; no regional maps, imported assets or donor gameplay scripts are changed.

The following downstairs story conversation is outside this scene; existing Hoenn dialogue remains available for the next writing pass.

## Validation
- Native ROM build passes.
- 28 native mGBA checks pass across Aren and Aria: proper bedroom/new-game supplies, wake-up, premature clock interaction, both staircase gates, PC notice persistence, clock/package completion, activation flag, exactly one Tera Orb, native save/soft reset/Continue both mid-intro and after delivery, working stairs, no cutscene replay, and restored normal bedroom PC.
- Existing Creator/Birch intro regression: five checks pass (both character choices, name rejection, seven-character custom-name expansion and full handoff).
- Screenshots reviewed for both rooms, protagonist/ELARA nameboxes, native clock, PC and save/reload.
- New states/flags occupy existing save fields; no save ABI extension.
- New-game flow only: existing saves are not forcibly moved or reset.

## Runtime review
Start a NEW GAME in this build. Complete Creator/Birch and choose Aren or Aria. Check the stairs before PC, then after PC/before clock. Set the time (select YES when asked), speak with Elara, inspect the Tera Orb in Key Items, use the normal PC, then walk downstairs. Continue the existing Hoenn story from there. Previous exploration ROMs remain separate.

## RTC-friendly dialogue
The clock reaction now says “Now the clock's set.” Elara greets the player with “Hey, sleepyhead” and refers to “the mail,” removing morning assumptions. Future opening dialogue should remain compatible with afternoon, evening and night starts. RTC mechanics are unchanged.
