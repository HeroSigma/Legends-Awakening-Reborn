HnS_Route7_TunnelEntrance_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route7_TunnelEntrance_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route7_TunnelEntrance_Next
 release
 end
HnS_Route7_TunnelEntrance_Next::
 warp MAP_HNS_REGION_SAFFRONCITY_TUNNEL_SW, 40, 3
 waitstate
 release
 end
