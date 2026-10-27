HnS_Gate_RuinsOfAlph_Route32_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_RuinsOfAlph_Route32_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_RuinsOfAlph_Route32_Next
 release
 end
HnS_Gate_RuinsOfAlph_Route32_Next::
 warp MAP_HNS_REGION_GATE_RUINSOFALPH_ROUTE36, 7, 6
 waitstate
 release
 end
