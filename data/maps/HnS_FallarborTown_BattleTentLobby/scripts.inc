HnS_FallarborTown_BattleTentLobby_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FallarborTown_BattleTentLobby_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FallarborTown_BattleTentLobby_Next
 release
 end
HnS_FallarborTown_BattleTentLobby_Next::
 warp MAP_HNS_REGION_FALLARBORTOWN_BATTLETENTCORRIDOR, 2, 4
 waitstate
 release
 end
