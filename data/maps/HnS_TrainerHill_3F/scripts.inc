HnS_TrainerHill_3F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TrainerHill_3F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TrainerHill_3F_Next
 release
 end
HnS_TrainerHill_3F_Next::
 warp MAP_HNS_REGION_TRAINERHILL_4F, 8, 10
 waitstate
 release
 end
