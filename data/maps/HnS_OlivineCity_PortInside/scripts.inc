HnS_OlivineCity_PortInside_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_OlivineCity_PortInside_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_OlivineCity_PortInside_Next
 release
 end
HnS_OlivineCity_PortInside_Next::
 warp MAP_HNS_REGION_OLIVINECITY_LIGHTHOUSE, 89, 10
 waitstate
 release
 end
