HnS_TinTower_9F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TinTower_9F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TinTower_9F_Next
 release
 end
HnS_TinTower_9F_Next::
 warp MAP_HNS_REGION_TINTOWER_ROOFDAY, 11, 10
 waitstate
 release
 end
