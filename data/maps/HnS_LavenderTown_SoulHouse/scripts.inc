HnS_LavenderTown_SoulHouse_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_LavenderTown_SoulHouse_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_LavenderTown_SoulHouse_Next
 release
 end
HnS_LavenderTown_SoulHouse_Next::
 warp MAP_HNS_REGION_CELADONCITY_POKEMONCENTER, 7, 5
 waitstate
 release
 end
