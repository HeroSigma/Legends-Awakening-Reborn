HnS_Route33_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route33_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route33_Next
 release
 end
HnS_Route33_Next::
 warp MAP_HNS_REGION_ROUTE34, 30, 47
 waitstate
 release
 end
