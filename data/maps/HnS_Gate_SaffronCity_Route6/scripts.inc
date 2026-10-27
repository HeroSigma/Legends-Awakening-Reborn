HnS_Gate_SaffronCity_Route6_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_SaffronCity_Route6_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_SaffronCity_Route6_Next
 release
 end
HnS_Gate_SaffronCity_Route6_Next::
 warp MAP_HNS_REGION_GATE_SAFFRONCITY_ROUTE7, 6, 5
 waitstate
 release
 end
