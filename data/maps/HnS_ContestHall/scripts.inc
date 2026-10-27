HnS_ContestHall_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_ContestHall_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_ContestHall_Next
 release
 end
HnS_ContestHall_Next::
 warp MAP_HNS_REGION_CONTESTHALLBEAUTY, 7, 5
 waitstate
 release
 end
