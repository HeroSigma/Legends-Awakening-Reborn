HnS_Route41_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route41_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route41_Next
 release
 end
HnS_Route41_Next::
 warp MAP_HNS_REGION_ROUTE42, 47, 15
 waitstate
 release
 end
