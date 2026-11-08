HnS_VerdanturfTown_BattleTentCorridor_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VerdanturfTown_BattleTentCorridor_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VerdanturfTown_BattleTentCorridor_Next
 release
 end
HnS_VerdanturfTown_BattleTentCorridor_Next::
 warp MAP_HNS_REGION_VERDANTURFTOWN_BATTLETENTBATTLEROOM, 6, 4
 waitstate
 release
 end
