HnS_CeladonCity_GameCorner_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CeladonCity_GameCorner_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CeladonCity_GameCorner_Next
 release
 end
HnS_CeladonCity_GameCorner_Next::
 warp MAP_HNS_REGION_CELADONCITY_DEPARTMENTSTORE_1F, 6, 7
 waitstate
 release
 end
