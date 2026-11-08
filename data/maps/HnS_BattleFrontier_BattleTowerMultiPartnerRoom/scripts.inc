HnS_BattleFrontier_BattleTowerMultiPartnerRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_BattleTowerMultiPartnerRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_BattleTowerMultiPartnerRoom_Next
 release
 end
HnS_BattleFrontier_BattleTowerMultiPartnerRoom_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_BATTLETOWERMULTICORRIDOR, 8, 3
 waitstate
 release
 end
