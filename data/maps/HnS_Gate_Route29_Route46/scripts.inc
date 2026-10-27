HnS_Gate_Route29_Route46_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_Route29_Route46_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_Route29_Route46_Next
 release
 end
HnS_Gate_Route29_Route46_Next::
 warp MAP_HNS_TEST_GATE_ROUTE31_VIOLETCITY, 6, 5
 waitstate
 release
 end
