HnS_VermilionCity_PortOutside_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VermilionCity_PortOutside_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VermilionCity_PortOutside_Next
 release
 end
HnS_VermilionCity_PortOutside_Next::
 warp MAP_HNS_REGION_VERMILIONCITY_PORTINSIDE, 9, 9
 waitstate
 release
 end
