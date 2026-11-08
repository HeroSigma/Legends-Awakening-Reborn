HnS_RocketHideout_B3F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_RocketHideout_B3F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_RocketHideout_B3F_Next
 release
 end
HnS_RocketHideout_B3F_Next::
 warp MAP_HNS_REGION_RUINSOFALPH_WORDSROOM1, 10, 8
 waitstate
 release
 end
