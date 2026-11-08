HnSTest_Route30_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_Route30_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_Route30_Next
 release
 end
HnSTest_Route30_Next::
 warp MAP_HNS_TEST_ROUTE31, 30, 11
 waitstate
 release
 end
