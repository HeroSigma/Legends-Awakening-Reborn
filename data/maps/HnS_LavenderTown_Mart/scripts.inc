HnS_LavenderTown_Mart_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_LavenderTown_Mart_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_LavenderTown_Mart_Next
 release
 end
HnS_LavenderTown_Mart_Next::
 warp MAP_HNS_REGION_LAVENDERTOWN_HOUSE1, 7, 4
 waitstate
 release
 end
