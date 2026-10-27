HnS_Route24_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route24_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route24_Next
 release
 end
HnS_Route24_Next::
 warp MAP_HNS_REGION_ROUTE25, 57, 17
 waitstate
 release
 end
