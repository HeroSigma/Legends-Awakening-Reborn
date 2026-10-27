HnS_TrainerHill_Roof_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TrainerHill_Roof_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TrainerHill_Roof_Next
 release
 end
HnS_TrainerHill_Roof_Next::
 warp MAP_HNS_REGION_TRAINERHILL_ELEVATOR, 2, 4
 waitstate
 release
 end
