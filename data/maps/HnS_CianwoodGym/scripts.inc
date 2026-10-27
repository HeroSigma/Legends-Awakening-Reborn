HnS_CianwoodGym_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CianwoodGym_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CianwoodGym_Next
 release
 end
HnS_CianwoodGym_Next::
 warp MAP_HNS_REGION_MAHOGANYTOWN_POKEMONCENTER, 8, 5
 waitstate
 release
 end
