HnS_SaffronCity_Mart_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SaffronCity_Mart_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SaffronCity_Mart_Next
 release
 end
HnS_SaffronCity_Mart_Next::
 warp MAP_HNS_REGION_SAFFRONCITY_TRAINSTATION, 131, 18
 waitstate
 release
 end
