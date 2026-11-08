HnS_VerdanturfTown_BattleTentLobby_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VerdanturfTown_BattleTentLobby_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VerdanturfTown_BattleTentLobby_Next
 release
 end
HnS_VerdanturfTown_BattleTentLobby_Next::
 warp MAP_HNS_REGION_VERDANTURFTOWN_BATTLETENTCORRIDOR, 2, 4
 waitstate
 release
 end
