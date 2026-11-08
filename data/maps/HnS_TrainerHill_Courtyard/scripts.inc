HnS_TrainerHill_Courtyard_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TrainerHill_Courtyard_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TrainerHill_Courtyard_Next
 release
 end
HnS_TrainerHill_Courtyard_Next::
 warp MAP_HNS_REGION_TRAINERHILL_ENTRANCE, 9, 8
 waitstate
 release
 end
