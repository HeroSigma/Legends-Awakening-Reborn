HnS_SaffronCity_SilphCo_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SaffronCity_SilphCo_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SaffronCity_SilphCo_Next
 release
 end
HnS_SaffronCity_SilphCo_Next::
 warp MAP_HNS_REGION_SAFFRONCITY_COPYCATSHOUSE_1F, 7, 5
 waitstate
 release
 end
