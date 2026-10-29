# Ordinary item pickups in collection mode

Root cause: EventScript_PickUpItem invokes pyramid_getlocation after showing the item description. The generic collection guard blocked CallBattlePyramidFunction, replaced the active script with LaCollection_Blocked, and skipped hideitemdescription.

Allow only BATTLE_PYRAMID_FUNC_CURRENT_LOCATION through the named special guard. The location query is read-only and safe outside the retired facility; all other Pyramid actions remain blocked. The generator emits the same exception so regeneration preserves the fix.

Native tests execute Common_EventScript_FindItem against the actual Petalburg Woods Ether template in isolated normal/collection saves: first, repeated, and full-stack pickups; quantities, header window lifecycle, controls, no warning, and location-only guard behavior. They do not open the player save.
