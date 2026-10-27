HnS_Route4_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route4_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route4_Next
 release
 end
HnS_Route4_Next::
 warp MAP_HNS_REGION_ROUTE5, 32, 23
 waitstate
 release
 end
