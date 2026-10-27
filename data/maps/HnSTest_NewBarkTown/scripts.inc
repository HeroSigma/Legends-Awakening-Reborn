HnSTest_NewBarkTown_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_NewBarkTown_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_NewBarkTown_Next
 release
 end
HnSTest_NewBarkTown_Next::
 warp MAP_HNS_TEST_CHERRYGROVECITY, 32, 19
 waitstate
 release
 end
