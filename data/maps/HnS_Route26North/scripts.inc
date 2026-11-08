HnS_Route26North_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route26North_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route26North_Next
 release
 end
HnS_Route26North_Next::
 warp MAP_HNS_REGION_ROUTE27, 80, 19
 waitstate
 release
 end
