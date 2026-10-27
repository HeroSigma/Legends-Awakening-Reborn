HnS_DiglettsCave_EntranceNorth_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_DiglettsCave_EntranceNorth_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_DiglettsCave_EntranceNorth_Next
 release
 end
HnS_DiglettsCave_EntranceNorth_Next::
 warp MAP_HNS_REGION_DIGLETTSCAVE_ENTRANCESOUTH, 5, 4
 waitstate
 release
 end
