HnS_BlackthornCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BlackthornCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BlackthornCity_Next
 release
 end
HnS_BlackthornCity_Next::
 warp MAP_HNS_TEST_ROUTE29, 35, 16
 waitstate
 release
 end
