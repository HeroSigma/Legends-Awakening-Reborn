HnS_Route15_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route15_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route15_Next
 release
 end
HnS_Route15_Next::
 warp MAP_HNS_REGION_ROUTE16, 34, 26
 waitstate
 release
 end
