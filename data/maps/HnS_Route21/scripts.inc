HnS_Route21_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route21_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route21_Next
 release
 end
HnS_Route21_Next::
 warp MAP_HNS_REGION_ROUTE22, 26, 11
 waitstate
 release
 end
