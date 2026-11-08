HnS_Route36_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route36_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route36_Next
 release
 end
HnS_Route36_Next::
 warp MAP_HNS_REGION_ROUTE37, 21, 20
 waitstate
 release
 end
