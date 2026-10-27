HnS_NewBarkTown_PlayersHouse_1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_NewBarkTown_PlayersHouse_1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_NewBarkTown_PlayersHouse_1F_Next
 release
 end
HnS_NewBarkTown_PlayersHouse_1F_Next::
 warp MAP_HNS_REGION_NEWBARKTOWN_PLAYERSHOUSE_2F, 5, 4
 waitstate
 release
 end
