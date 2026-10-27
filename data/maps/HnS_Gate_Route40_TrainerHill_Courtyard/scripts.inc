HnS_Gate_Route40_TrainerHill_Courtyard_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_Route40_TrainerHill_Courtyard_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_Route40_TrainerHill_Courtyard_Next
 release
 end
HnS_Gate_Route40_TrainerHill_Courtyard_Next::
 warp MAP_HNS_REGION_SLATEPORTCITY_BATTLETENTLOBBY, 6, 4
 waitstate
 release
 end
