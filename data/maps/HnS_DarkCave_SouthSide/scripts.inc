HnS_DarkCave_SouthSide_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_DarkCave_SouthSide_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_DarkCave_SouthSide_Next
 release
 end
HnS_DarkCave_SouthSide_Next::
 warp MAP_HNS_REGION_DARKCAVE_NORTHSIDE, 29, 21
 waitstate
 release
 end
