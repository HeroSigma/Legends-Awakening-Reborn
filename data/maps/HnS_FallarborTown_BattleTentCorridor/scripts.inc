HnS_FallarborTown_BattleTentCorridor_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FallarborTown_BattleTentCorridor_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FallarborTown_BattleTentCorridor_Next
 release
 end
HnS_FallarborTown_BattleTentCorridor_Next::
 warp MAP_HNS_REGION_FALLARBORTOWN_BATTLETENTBATTLEROOM, 5, 4
 waitstate
 release
 end
