HnS_PalletTown_House2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PalletTown_House2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PalletTown_House2_Next
 release
 end
HnS_PalletTown_House2_Next::
 warp MAP_HNS_REGION_PALLETTOWN_HOUSE3, 6, 3
 waitstate
 release
 end
