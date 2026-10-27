HnS_SeafoamIslands_1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SeafoamIslands_1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SeafoamIslands_1F_Next
 release
 end
HnS_SeafoamIslands_1F_Next::
 warp MAP_HNS_REGION_SEAFOAMISLANDS_GYM, 18, 19
 waitstate
 release
 end
