HnS_Route10_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route10_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route10_Next
 release
 end
HnS_Route10_Next::
 warp MAP_HNS_REGION_ROUTE11, 37, 20
 waitstate
 release
 end
