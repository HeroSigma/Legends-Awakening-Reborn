HnS_GoldenrodCity_UndergroundEntrance_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_GoldenrodCity_UndergroundEntrance_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_GoldenrodCity_UndergroundEntrance_Next
 release
 end
HnS_GoldenrodCity_UndergroundEntrance_Next::
 warp MAP_HNS_REGION_GOLDENRODCITY_UNDERGROUNDTUNNEL, 4, 18
 waitstate
 release
 end
