HnS_BattleFrontier_BattlePyramidFloor_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattlePyramidFloor_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattlePyramidFloor_Next
 release
 end
HnS_BattleFrontier_BattlePyramidFloor_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPYRAMIDTOP, 15, 11
 waitstate
 release
 end
