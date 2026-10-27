HnSTest_Gate_Route31_VioletCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_Gate_Route31_VioletCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_Gate_Route31_VioletCity_Next
 release
 end
HnSTest_Gate_Route31_VioletCity_Next::
 warp MAP_HNS_REGION_GATE_RUINSOFALPH_ROUTE32, 6, 5
 waitstate
 release
 end
