HnS_Route3_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route3_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route3_Next
 release
 end
HnS_Route3_Next::
 warp MAP_HNS_REGION_ROUTE4, 54, 11
 waitstate
 release
 end
