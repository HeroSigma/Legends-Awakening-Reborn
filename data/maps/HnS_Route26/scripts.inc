HnS_Route26_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route26_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route26_Next
 release
 end
HnS_Route26_Next::
 warp MAP_HNS_REGION_ROUTE26NORTH, 18, 16
 waitstate
 release
 end
