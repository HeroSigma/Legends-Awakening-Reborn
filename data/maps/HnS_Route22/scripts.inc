HnS_Route22_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route22_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route22_Next
 release
 end
HnS_Route22_Next::
 warp MAP_HNS_REGION_ROUTE23, 12, 69
 waitstate
 release
 end
