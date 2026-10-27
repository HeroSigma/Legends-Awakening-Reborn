HnS_MtSilver_SummitNight_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MtSilver_SummitNight_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MtSilver_SummitNight_Next
 release
 end
HnS_MtSilver_SummitNight_Next::
 warp MAP_HNS_REGION_CLIFFEDGECAVE, 22, 14
 waitstate
 release
 end
