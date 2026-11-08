HnS_UnusedContestHall2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_UnusedContestHall2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_UnusedContestHall2_Next
 release
 end
HnS_UnusedContestHall2_Next::
 warp MAP_HNS_TEST_NEWBARKTOWN, 15, 17
 waitstate
 release
 end
