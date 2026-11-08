HnS_Gate_SaffronCity_Route8_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_SaffronCity_Route8_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_SaffronCity_Route8_Next
 release
 end
HnS_Gate_SaffronCity_Route8_Next::
 warp MAP_HNS_REGION_ROUTE9_POKEMONCENTER, 8, 5
 waitstate
 release
 end
