HnS_Trees_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Trees_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Trees_Next
 release
 end
HnS_Trees_Next::
 warp MAP_HNS_TEST_NEWBARKTOWN, 15, 17
 waitstate
 release
 end
