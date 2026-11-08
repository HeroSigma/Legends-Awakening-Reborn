HnS_Route37_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route37_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route37_Next
 release
 end
HnS_Route37_Next::
 warp MAP_HNS_REGION_ROUTE38, 25, 25
 waitstate
 release
 end
