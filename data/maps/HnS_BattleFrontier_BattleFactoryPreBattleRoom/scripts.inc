HnS_BattleFrontier_BattleFactoryPreBattleRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattleFactoryPreBattleRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattleFactoryPreBattleRoom_Next
 release
 end
HnS_BattleFrontier_BattleFactoryPreBattleRoom_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_BATTLEFACTORYBATTLEROOM, 6, 6
 waitstate
 release
 end
