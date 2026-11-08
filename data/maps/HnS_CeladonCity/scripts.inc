HnS_CeladonCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CeladonCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CeladonCity_Next
 release
 end
HnS_CeladonCity_Next::
 warp MAP_HNS_REGION_SAFFRONCITY, 33, 32
 waitstate
 release
 end
