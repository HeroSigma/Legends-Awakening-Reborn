HnS_ViridianCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_ViridianCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_ViridianCity_Next
 release
 end
HnS_ViridianCity_Next::
 warp MAP_HNS_REGION_PEWTERCITY, 26, 22
 waitstate
 release
 end
