HnS_SaffronCity_Tunnel_SW_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SaffronCity_Tunnel_SW_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SaffronCity_Tunnel_SW_Next
 release
 end
HnS_SaffronCity_Tunnel_SW_Next::
 warp MAP_HNS_REGION_ROUTE8_TUNNELENTRANCE, 11, 9
 waitstate
 release
 end
