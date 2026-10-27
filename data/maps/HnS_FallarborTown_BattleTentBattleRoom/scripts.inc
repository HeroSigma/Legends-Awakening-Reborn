HnS_FallarborTown_BattleTentBattleRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FallarborTown_BattleTentBattleRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FallarborTown_BattleTentBattleRoom_Next
 release
 end
HnS_FallarborTown_BattleTentBattleRoom_Next::
 warp MAP_HNS_REGION_RECEPTIONGATE, 11, 10
 waitstate
 release
 end
