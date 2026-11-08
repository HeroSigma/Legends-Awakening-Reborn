HnS_Gate_CeladonCity_Route16_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_CeladonCity_Route16_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_CeladonCity_Route16_Next
 release
 end
HnS_Gate_CeladonCity_Route16_Next::
 warp MAP_HNS_REGION_GATE_FUCHSIACITY_ROUTE18, 6, 5
 waitstate
 release
 end
