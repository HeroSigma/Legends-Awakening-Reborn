HnS_Route25_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route25_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route25_Next
 release
 end
HnS_Route25_Next::
 warp MAP_HNS_REGION_ROUTE26, 20, 41
 waitstate
 release
 end
