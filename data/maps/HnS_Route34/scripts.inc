HnS_Route34_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route34_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route34_Next
 release
 end
HnS_Route34_Next::
 warp MAP_HNS_REGION_ROUTE35, 20, 24
 waitstate
 release
 end
