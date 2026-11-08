HnS_Route43_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route43_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route43_Next
 release
 end
HnS_Route43_Next::
 warp MAP_HNS_REGION_ROUTE44, 39, 24
 waitstate
 release
 end
