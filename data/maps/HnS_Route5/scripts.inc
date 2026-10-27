HnS_Route5_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route5_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route5_Next
 release
 end
HnS_Route5_Next::
 warp MAP_HNS_REGION_ROUTE6, 31, 18
 waitstate
 release
 end
