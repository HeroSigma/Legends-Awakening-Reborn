HnS_SproutTower_3F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SproutTower_3F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SproutTower_3F_Next
 release
 end
HnS_SproutTower_3F_Next::
 warp MAP_HNS_REGION_RUINSOFALPH_OUTSIDE, 23, 24
 waitstate
 release
 end
