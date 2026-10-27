HnS_Route45_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route45_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route45_Next
 release
 end
HnS_Route45_Next::
 warp MAP_HNS_REGION_ROUTE46, 13, 23
 waitstate
 release
 end
