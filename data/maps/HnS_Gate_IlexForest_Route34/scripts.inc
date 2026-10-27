HnS_Gate_IlexForest_Route34_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_IlexForest_Route34_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_IlexForest_Route34_Next
 release
 end
HnS_Gate_IlexForest_Route34_Next::
 warp MAP_HNS_REGION_GATE_GOLDENRODCITY_ROUTE35, 7, 6
 waitstate
 release
 end
