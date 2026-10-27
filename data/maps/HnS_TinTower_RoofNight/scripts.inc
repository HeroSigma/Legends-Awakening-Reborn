HnS_TinTower_RoofNight_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TinTower_RoofNight_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TinTower_RoofNight_Next
 release
 end
HnS_TinTower_RoofNight_Next::
 warp MAP_HNS_REGION_TOHJOFALLS_CAVERN, 39, 18
 waitstate
 release
 end
