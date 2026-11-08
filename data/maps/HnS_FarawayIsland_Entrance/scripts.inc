HnS_FarawayIsland_Entrance_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FarawayIsland_Entrance_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FarawayIsland_Entrance_Next
 release
 end
HnS_FarawayIsland_Entrance_Next::
 warp MAP_HNS_REGION_FARAWAYISLAND_INTERIOR, 15, 17
 waitstate
 release
 end
