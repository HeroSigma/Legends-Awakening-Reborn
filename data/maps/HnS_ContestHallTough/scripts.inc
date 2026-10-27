HnS_ContestHallTough_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_ContestHallTough_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_ContestHallTough_Next
 release
 end
HnS_ContestHallTough_Next::
 warp MAP_HNS_REGION_LILYCOVECITY_CONTESTHALL, 25, 16
 waitstate
 release
 end
