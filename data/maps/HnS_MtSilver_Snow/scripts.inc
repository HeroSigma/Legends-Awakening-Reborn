HnS_MtSilver_Snow_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MtSilver_Snow_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MtSilver_Snow_Next
 release
 end
HnS_MtSilver_Snow_Next::
 warp MAP_HNS_REGION_MTSILVER_SUMMITDAY, 10, 13
 waitstate
 release
 end
