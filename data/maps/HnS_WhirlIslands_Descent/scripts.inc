HnS_WhirlIslands_Descent_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_WhirlIslands_Descent_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_WhirlIslands_Descent_Next
 release
 end
HnS_WhirlIslands_Descent_Next::
 warp MAP_HNS_REGION_WHIRLISLANDS_LUGIACHAMBER, 29, 20
 waitstate
 release
 end
