HnS_ViridianForest_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_ViridianForest_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_ViridianForest_Next
 release
 end
HnS_ViridianForest_Next::
 warp MAP_HNS_REGION_MTMOON_CAVE, 25, 20
 waitstate
 release
 end
