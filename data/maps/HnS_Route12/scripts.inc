HnS_Route12_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route12_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route12_Next
 release
 end
HnS_Route12_Next::
 warp MAP_HNS_REGION_ROUTE13, 52, 21
 waitstate
 release
 end
