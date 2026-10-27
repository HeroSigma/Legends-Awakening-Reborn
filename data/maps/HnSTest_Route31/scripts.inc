HnSTest_Route31_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_Route31_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_Route31_Next
 release
 end
HnSTest_Route31_Next::
 warp MAP_HNS_REGION_ROUTE32, 21, 51
 waitstate
 release
 end
