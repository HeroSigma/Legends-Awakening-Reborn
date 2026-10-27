HnS_AzaleaTown_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_AzaleaTown_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_AzaleaTown_Next
 release
 end
HnS_AzaleaTown_Next::
 warp MAP_HNS_REGION_GOLDENRODCITY, 29, 23
 waitstate
 release
 end
