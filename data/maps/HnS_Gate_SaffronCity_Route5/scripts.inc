HnS_Gate_SaffronCity_Route5_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Gate_SaffronCity_Route5_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Gate_SaffronCity_Route5_Next
 release
 end
HnS_Gate_SaffronCity_Route5_Next::
 warp MAP_HNS_REGION_SAFFRONCITY_TUNNEL_NS, 4, 20
 waitstate
 release
 end
