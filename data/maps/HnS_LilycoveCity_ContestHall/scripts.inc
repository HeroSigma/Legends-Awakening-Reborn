HnS_LilycoveCity_ContestHall_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_LilycoveCity_ContestHall_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_LilycoveCity_ContestHall_Next
 release
 end
HnS_LilycoveCity_ContestHall_Next::
 warp MAP_HNS_REGION_LILYCOVECITY_CONTESTLOBBY, 15, 6
 waitstate
 release
 end
