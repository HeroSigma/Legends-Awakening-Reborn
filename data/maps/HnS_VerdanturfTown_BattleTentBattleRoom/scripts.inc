HnS_VerdanturfTown_BattleTentBattleRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VerdanturfTown_BattleTentBattleRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VerdanturfTown_BattleTentBattleRoom_Next
 release
 end
HnS_VerdanturfTown_BattleTentBattleRoom_Next::
 warp MAP_HNS_REGION_FALLARBORTOWN_BATTLETENTLOBBY, 6, 4
 waitstate
 release
 end
