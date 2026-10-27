HnS_DarkCave_NorthSide_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_DarkCave_NorthSide_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_DarkCave_NorthSide_Next
 release
 end
HnS_DarkCave_NorthSide_Next::
 warp MAP_HNS_REGION_SPROUTTOWER_1F, 12, 13
 waitstate
 release
 end
