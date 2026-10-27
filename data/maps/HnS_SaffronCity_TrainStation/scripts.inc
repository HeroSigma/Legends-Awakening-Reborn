HnS_SaffronCity_TrainStation_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SaffronCity_TrainStation_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SaffronCity_TrainStation_Next
 release
 end
HnS_SaffronCity_TrainStation_Next::
 warp MAP_HNS_REGION_SAFFRONCITY_FIGHTINGDOJO, 14, 8
 waitstate
 release
 end
