HnS_PalletTown_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PalletTown_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PalletTown_Next
 release
 end
HnS_PalletTown_Next::
 warp MAP_HNS_REGION_VIRIDIANCITY, 26, 25
 waitstate
 release
 end
