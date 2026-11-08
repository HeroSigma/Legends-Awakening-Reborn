HnSTest_VioletCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_VioletCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_VioletCity_Next
 release
 end
HnSTest_VioletCity_Next::
 warp MAP_HNS_REGION_AZALEATOWN, 31, 18
 waitstate
 release
 end
