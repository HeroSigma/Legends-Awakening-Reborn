HnS_PalletTown_RedsHouse_1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PalletTown_RedsHouse_1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PalletTown_RedsHouse_1F_Next
 release
 end
HnS_PalletTown_RedsHouse_1F_Next::
 warp MAP_HNS_REGION_PALLETTOWN_REDSHOUSE_2F, 5, 4
 waitstate
 release
 end
