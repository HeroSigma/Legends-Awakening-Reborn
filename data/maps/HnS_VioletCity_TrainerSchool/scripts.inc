HnS_VioletCity_TrainerSchool_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VioletCity_TrainerSchool_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VioletCity_TrainerSchool_Next
 release
 end
HnS_VioletCity_TrainerSchool_Next::
 warp MAP_HNS_REGION_VIOLETCITY_HOUSE1, 6, 3
 waitstate
 release
 end
