HnS_Route19_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route19_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route19_Next
 release
 end
HnS_Route19_Next::
 warp MAP_HNS_REGION_ROUTE20, 60, 4
 waitstate
 release
 end
