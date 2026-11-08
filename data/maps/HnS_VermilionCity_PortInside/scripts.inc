HnS_VermilionCity_PortInside_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VermilionCity_PortInside_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VermilionCity_PortInside_Next
 release
 end
HnS_VermilionCity_PortInside_Next::
 warp MAP_HNS_REGION_VERMILIONCITY_GYM, 4, 10
 waitstate
 release
 end
