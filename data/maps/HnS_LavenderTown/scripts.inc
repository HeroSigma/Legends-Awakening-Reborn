HnS_LavenderTown_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_LavenderTown_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_LavenderTown_Next
 release
 end
HnS_LavenderTown_Next::
 warp MAP_HNS_REGION_CELADONCITY, 31, 21
 waitstate
 release
 end
