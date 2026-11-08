HnS_Route46_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route46_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route46_Next
 release
 end
HnS_Route46_Next::
 warp MAP_HNS_REGION_ROUTE47, 67, 30
 waitstate
 release
 end
