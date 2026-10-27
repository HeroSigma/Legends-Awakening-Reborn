HnS_BattleFrontier_BattlePikeRoomNormal_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattlePikeRoomNormal_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattlePikeRoomNormal_Next
 release
 end
HnS_BattleFrontier_BattlePikeRoomNormal_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_BATTLEPIKEROOMFINAL, 1, 5
 waitstate
 release
 end
