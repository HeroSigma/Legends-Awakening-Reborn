HnS_BattleFrontier_BattleDomePreBattleRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattleDomePreBattleRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattleDomePreBattleRoom_Next
 release
 end
HnS_BattleFrontier_BattleDomePreBattleRoom_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_BATTLEDOMEBATTLEROOM, 10, 5
 waitstate
 release
 end
