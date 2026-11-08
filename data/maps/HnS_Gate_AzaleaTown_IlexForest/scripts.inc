HnS_Gate_AzaleaTown_IlexForest_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_AzaleaTown_IlexForest_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_AzaleaTown_IlexForest_Next
 release
 end
HnS_Gate_AzaleaTown_IlexForest_Next::
 warp MAP_HNS_REGION_GATE_ILEXFOREST_ROUTE34, 7, 6
 waitstate
 release
 end
