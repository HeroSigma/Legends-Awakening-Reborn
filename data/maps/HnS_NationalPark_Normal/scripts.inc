HnS_NationalPark_Normal_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_NationalPark_Normal_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_NationalPark_Normal_Next
 release
 end
HnS_NationalPark_Normal_Next::
 warp MAP_HNS_REGION_NATIONALPARK_BUGCONTEST, 24, 27
 waitstate
 release
 end
