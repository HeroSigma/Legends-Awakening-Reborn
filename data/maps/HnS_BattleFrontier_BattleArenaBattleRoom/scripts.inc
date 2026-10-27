HnS_BattleFrontier_BattleArenaBattleRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattleArenaBattleRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattleArenaBattleRoom_Next
 release
 end
HnS_BattleFrontier_BattleArenaBattleRoom_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_BATTLEFACTORYLOBBY, 9, 6
 waitstate
 release
 end
