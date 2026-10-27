HnS_BattleFrontier_Lounge7_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_Lounge7_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_Lounge7_Next
 release
 end
HnS_BattleFrontier_Lounge7_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_RECEPTIONGATE, 4, 7
 waitstate
 release
 end
