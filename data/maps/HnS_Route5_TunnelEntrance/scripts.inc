HnS_Route5_TunnelEntrance_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route5_TunnelEntrance_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route5_TunnelEntrance_Next
 release
 end
HnS_Route5_TunnelEntrance_Next::
 warp MAP_HNS_REGION_GATE_SAFFRONCITY_ROUTE5, 7, 6
 waitstate
 release
 end
