HnS_OlivineCity_PortOutside_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_OlivineCity_PortOutside_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_OlivineCity_PortOutside_Next
 release
 end
HnS_OlivineCity_PortOutside_Next::
 warp MAP_HNS_REGION_OLIVINECITY_PORTINSIDE, 9, 14
 waitstate
 release
 end
