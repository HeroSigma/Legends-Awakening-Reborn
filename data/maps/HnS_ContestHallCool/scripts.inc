HnS_ContestHallCool_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_ContestHallCool_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_ContestHallCool_Next
 release
 end
HnS_ContestHallCool_Next::
 warp MAP_HNS_REGION_CONTESTHALLCUTE, 7, 5
 waitstate
 release
 end
