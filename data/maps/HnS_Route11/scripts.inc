HnS_Route11_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route11_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route11_Next
 release
 end
HnS_Route11_Next::
 warp MAP_HNS_REGION_ROUTE12, 17, 45
 waitstate
 release
 end
