HnS_Route40_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route40_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route40_Next
 release
 end
HnS_Route40_Next::
 warp MAP_HNS_REGION_ROUTE41, 8, 68
 waitstate
 release
 end
