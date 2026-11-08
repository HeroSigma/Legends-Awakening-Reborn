HnS_Gate_Route2_ViridianForest_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_Route2_ViridianForest_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_Route2_ViridianForest_Next
 release
 end
HnS_Gate_Route2_ViridianForest_Next::
 warp MAP_HNS_REGION_GATE_VIRIDIANFOREST_ROUTE2, 7, 6
 waitstate
 release
 end
