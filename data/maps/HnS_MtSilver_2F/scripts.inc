HnS_MtSilver_2F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MtSilver_2F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MtSilver_2F_Next
 release
 end
HnS_MtSilver_2F_Next::
 warp MAP_HNS_REGION_MTSILVER_3F, 27, 14
 waitstate
 release
 end
