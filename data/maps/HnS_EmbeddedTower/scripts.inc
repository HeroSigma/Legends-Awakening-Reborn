HnS_EmbeddedTower_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_EmbeddedTower_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_EmbeddedTower_Next
 release
 end
HnS_EmbeddedTower_Next::
 warp MAP_HNS_REGION_ROCKETHIDEOUT_B1F, 34, 16
 waitstate
 release
 end
