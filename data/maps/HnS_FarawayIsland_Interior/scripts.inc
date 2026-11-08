HnS_FarawayIsland_Interior_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FarawayIsland_Interior_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FarawayIsland_Interior_Next
 release
 end
HnS_FarawayIsland_Interior_Next::
 warp MAP_HNS_REGION_BIRTHISLAND_EXTERIOR, 15, 15
 waitstate
 release
 end
