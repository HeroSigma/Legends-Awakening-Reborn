HnS_Route18_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route18_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route18_Next
 release
 end
HnS_Route18_Next::
 warp MAP_HNS_REGION_ROUTE19, 1, 19
 waitstate
 release
 end
