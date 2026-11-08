HnS_BellchimeTrail_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BellchimeTrail_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BellchimeTrail_Next
 release
 end
HnS_BellchimeTrail_Next::
 warp MAP_HNS_REGION_ECRUTEAKCITY_GYM, 8, 25
 waitstate
 release
 end
