HnS_SeafoamIslands_SecretCave_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SeafoamIslands_SecretCave_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SeafoamIslands_SecretCave_Next
 release
 end
HnS_SeafoamIslands_SecretCave_Next::
 warp MAP_HNS_REGION_MTSILVER_OUTSIDE, 22, 17
 waitstate
 release
 end
