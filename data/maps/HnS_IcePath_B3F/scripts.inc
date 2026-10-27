HnS_IcePath_B3F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_IcePath_B3F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_IcePath_B3F_Next
 release
 end
HnS_IcePath_B3F_Next::
 warp MAP_HNS_REGION_ICEPATH_B4F, 16, 14
 waitstate
 release
 end
