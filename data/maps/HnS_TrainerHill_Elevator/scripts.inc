HnS_TrainerHill_Elevator_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TrainerHill_Elevator_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TrainerHill_Elevator_Next
 release
 end
HnS_TrainerHill_Elevator_Next::
 warp MAP_HNS_REGION_SSAQUA_1F, 18, 9
 waitstate
 release
 end
