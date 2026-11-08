HnS_WhirlIslands_B3F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_WhirlIslands_B3F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_WhirlIslands_B3F_Next
 release
 end
HnS_WhirlIslands_B3F_Next::
 warp MAP_HNS_REGION_WHIRLISLANDS_DESCENT, 46, 50
 waitstate
 release
 end
