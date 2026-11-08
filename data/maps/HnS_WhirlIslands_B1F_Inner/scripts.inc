HnS_WhirlIslands_B1F_Inner_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_WhirlIslands_B1F_Inner_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_WhirlIslands_B1F_Inner_Next
 release
 end
HnS_WhirlIslands_B1F_Inner_Next::
 warp MAP_HNS_REGION_WHIRLISLANDS_B2F, 35, 15
 waitstate
 release
 end
