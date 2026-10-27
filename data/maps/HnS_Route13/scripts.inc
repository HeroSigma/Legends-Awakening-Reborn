HnS_Route13_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route13_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route13_Next
 release
 end
HnS_Route13_Next::
 warp MAP_HNS_REGION_ROUTE14, 11, 31
 waitstate
 release
 end
