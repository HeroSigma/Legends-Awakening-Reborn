HnS_BattleFrontier_BattleTowerCorridor_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattleTowerCorridor_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattleTowerCorridor_Next
 release
 end
HnS_BattleFrontier_BattleTowerCorridor_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERBATTLEROOM, 5, 4
 waitstate
 release
 end
