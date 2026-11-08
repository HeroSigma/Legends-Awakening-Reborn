HnS_GoldenrodCity_GameCorner_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_GoldenrodCity_GameCorner_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_GoldenrodCity_GameCorner_Next
 release
 end
HnS_GoldenrodCity_GameCorner_Next::
 warp MAP_HNS_REGION_GOLDENRODCITY_TRAINSTATION, 22, 18
 waitstate
 release
 end
