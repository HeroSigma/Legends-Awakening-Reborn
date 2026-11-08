HnS_WhirlIslands_1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_WhirlIslands_1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_WhirlIslands_1F_Next
 release
 end
HnS_WhirlIslands_1F_Next::
 warp MAP_HNS_REGION_WHIRLISLANDS_B1F, 43, 45
 waitstate
 release
 end
