HnS_BattleFrontier_Lounge6_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_Lounge6_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_Lounge6_Next
 release
 end
HnS_BattleFrontier_Lounge6_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_LOUNGE7, 4, 6
 waitstate
 release
 end
