HnS_LavenderTown_RadioStation_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_LavenderTown_RadioStation_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_LavenderTown_RadioStation_Next
 release
 end
HnS_LavenderTown_RadioStation_Next::
 warp MAP_HNS_REGION_LAVENDERTOWN_SOULHOUSE, 12, 10
 waitstate
 release
 end
