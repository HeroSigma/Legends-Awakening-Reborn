HnSTest_CherrygroveCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_CherrygroveCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_CherrygroveCity_Next
 release
 end
HnSTest_CherrygroveCity_Next::
 warp MAP_HNS_TEST_VIOLETCITY, 27, 25
 waitstate
 release
 end
