HnS_NationalPark_BugContest_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_NationalPark_BugContest_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_NationalPark_BugContest_Next
 release
 end
HnS_NationalPark_BugContest_Next::
 warp MAP_HNS_REGION_BURNEDTOWER_1F, 15, 12
 waitstate
 release
 end
