HnS_Route2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route2_Next
 release
 end
HnS_Route2_Next::
 warp MAP_HNS_REGION_ROUTE3, 42, 10
 waitstate
 release
 end
