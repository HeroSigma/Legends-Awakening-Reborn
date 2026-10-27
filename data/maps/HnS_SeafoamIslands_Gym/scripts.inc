HnS_SeafoamIslands_Gym_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SeafoamIslands_Gym_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SeafoamIslands_Gym_Next
 release
 end
HnS_SeafoamIslands_Gym_Next::
 warp MAP_HNS_REGION_SEAFOAMISLANDS_B1F, 33, 31
 waitstate
 release
 end
