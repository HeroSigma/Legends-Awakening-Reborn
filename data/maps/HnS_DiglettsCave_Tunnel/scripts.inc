HnS_DiglettsCave_Tunnel_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_DiglettsCave_Tunnel_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_DiglettsCave_Tunnel_Next
 release
 end
HnS_DiglettsCave_Tunnel_Next::
 warp MAP_HNS_REGION_SEAFOAMISLANDS_1F, 33, 28
 waitstate
 release
 end
