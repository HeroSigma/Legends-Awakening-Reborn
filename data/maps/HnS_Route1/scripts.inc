HnS_Route1_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route1_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route1_Next
 release
 end
HnS_Route1_Next::
 warp MAP_HNS_REGION_ROUTE2, 16, 39
 waitstate
 release
 end
