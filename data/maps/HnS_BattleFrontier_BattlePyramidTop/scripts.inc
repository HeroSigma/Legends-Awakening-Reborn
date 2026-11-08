HnS_BattleFrontier_BattlePyramidTop_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattlePyramidTop_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattlePyramidTop_Next
 release
 end
HnS_BattleFrontier_BattlePyramidTop_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_BATTLEARENALOBBY, 8, 9
 waitstate
 release
 end
