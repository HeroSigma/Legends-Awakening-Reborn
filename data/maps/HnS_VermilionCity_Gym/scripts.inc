HnS_VermilionCity_Gym_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VermilionCity_Gym_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VermilionCity_Gym_Next
 release
 end
HnS_VermilionCity_Gym_Next::
 warp MAP_HNS_REGION_VERMILIONCITY_FANCLUB, 6, 8
 waitstate
 release
 end
