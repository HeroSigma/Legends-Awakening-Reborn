HnS_ContestHallCute_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_ContestHallCute_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_ContestHallCute_Next
 release
 end
HnS_ContestHallCute_Next::
 warp MAP_HNS_REGION_CONTESTHALLSMART, 7, 5
 waitstate
 release
 end
