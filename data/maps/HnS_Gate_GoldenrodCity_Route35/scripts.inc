HnS_Gate_GoldenrodCity_Route35_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_GoldenrodCity_Route35_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_GoldenrodCity_Route35_Next
 release
 end
HnS_Gate_GoldenrodCity_Route35_Next::
 warp MAP_HNS_REGION_GATE_NATIONALPARK, 34, 9
 waitstate
 release
 end
