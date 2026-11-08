HnS_BattleFrontier_Mart_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleFrontier_Mart_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleFrontier_Mart_Next
 release
 end
HnS_BattleFrontier_Mart_Next::
 warp MAP_HNS_REGION_CONTESTHALL, 8, 5
 waitstate
 release
 end
