HnS_SeafoamIslands_B1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SeafoamIslands_B1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SeafoamIslands_B1F_Next
 release
 end
HnS_SeafoamIslands_B1F_Next::
 warp MAP_HNS_REGION_SEAFOAMISLANDS_SECRETCAVE, 17, 14
 waitstate
 release
 end
