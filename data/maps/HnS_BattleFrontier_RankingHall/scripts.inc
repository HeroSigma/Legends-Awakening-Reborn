HnS_BattleFrontier_RankingHall_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_RankingHall_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_RankingHall_Next
 release
 end
HnS_BattleFrontier_RankingHall_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE1, 5, 4
 waitstate
 release
 end
