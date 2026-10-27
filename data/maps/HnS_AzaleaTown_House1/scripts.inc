HnS_AzaleaTown_House1_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_AzaleaTown_House1_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_AzaleaTown_House1_Next
 release
 end
HnS_AzaleaTown_House1_Next::
 warp MAP_HNS_REGION_AZALEATOWN_GYM, 12, 30
 waitstate
 release
 end
