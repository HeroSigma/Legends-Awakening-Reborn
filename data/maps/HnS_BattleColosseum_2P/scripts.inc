HnS_BattleColosseum_2P_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BattleColosseum_2P_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BattleColosseum_2P_Next
 release
 end
HnS_BattleColosseum_2P_Next::
 warp MAP_HNS_REGION_FUCHSIACITY_SAFARIZONEENTRANCE, 6, 7
 waitstate
 release
 end
