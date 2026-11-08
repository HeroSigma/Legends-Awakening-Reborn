HnS_VioletCity_House2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VioletCity_House2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VioletCity_House2_Next
 release
 end
HnS_VioletCity_House2_Next::
 warp MAP_HNS_TEST_VIOLETCITY_GYM, 9, 9
 waitstate
 release
 end
