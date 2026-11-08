HnS_Route25_BillsHouse_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route25_BillsHouse_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route25_BillsHouse_Next
 release
 end
HnS_Route25_BillsHouse_Next::
 warp MAP_HNS_REGION_DARKCAVE_SOUTHSIDE, 39, 20
 waitstate
 release
 end
