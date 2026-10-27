HnS_TradeCenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TradeCenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TradeCenter_Next
 release
 end
HnS_TradeCenter_Next::
 warp MAP_HNS_REGION_BATTLECOLOSSEUM_2P, 7, 4
 waitstate
 release
 end
