HnS_Route6_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route6_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route6_Next
 release
 end
HnS_Route6_Next::
 warp MAP_HNS_REGION_ROUTE7, 10, 14
 waitstate
 release
 end
