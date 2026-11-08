HnS_BattleFrontier_BattlePikeRoomWildMons_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattlePikeRoomWildMons_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattlePikeRoomWildMons_Next
 release
 end
HnS_BattleFrontier_BattlePikeRoomWildMons_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_RANKINGHALL, 26, 7
 waitstate
 release
 end
