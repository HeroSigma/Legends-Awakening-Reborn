HnS_Route35_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route35_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route35_Next
 release
 end
HnS_Route35_Next::
 warp MAP_HNS_REGION_ROUTE36, 35, 16
 waitstate
 release
 end
