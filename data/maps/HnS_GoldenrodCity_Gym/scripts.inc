HnS_GoldenrodCity_Gym_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_GoldenrodCity_Gym_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_GoldenrodCity_Gym_Next
 release
 end
HnS_GoldenrodCity_Gym_Next::
 warp MAP_HNS_REGION_GOLDENRODCITY_FLOWERSHOP, 6, 5
 waitstate
 release
 end
