HnS_Route17_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route17_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route17_Next
 release
 end
HnS_Route17_Next::
 warp MAP_HNS_REGION_ROUTE18, 30, 10
 waitstate
 release
 end
