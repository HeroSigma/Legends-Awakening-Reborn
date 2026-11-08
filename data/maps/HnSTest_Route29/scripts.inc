HnSTest_Route29_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_Route29_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_Route29_Next
 release
 end
HnSTest_Route29_Next::
 warp MAP_HNS_TEST_ROUTE30, 29, 31
 waitstate
 release
 end
