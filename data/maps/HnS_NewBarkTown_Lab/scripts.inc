HnS_NewBarkTown_Lab_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_NewBarkTown_Lab_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_NewBarkTown_Lab_Next
 release
 end
HnS_NewBarkTown_Lab_Next::
 warp MAP_HNS_REGION_NEWBARKTOWN_HOUSE2, 6, 3
 waitstate
 release
 end
