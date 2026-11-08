HnS_CeruleanCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CeruleanCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CeruleanCity_Next
 release
 end
HnS_CeruleanCity_Next::
 warp MAP_HNS_REGION_VERMILIONCITY, 35, 24
 waitstate
 release
 end
