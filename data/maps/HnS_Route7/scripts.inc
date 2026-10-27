HnS_Route7_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route7_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route7_Next
 release
 end
HnS_Route7_Next::
 warp MAP_HNS_REGION_ROUTE8, 32, 20
 waitstate
 release
 end
