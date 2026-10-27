HnS_Route39_FarmHouse_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route39_FarmHouse_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route39_FarmHouse_Next
 release
 end
HnS_Route39_FarmHouse_Next::
 warp MAP_HNS_REGION_ROUTE39_BARN, 8, 11
 waitstate
 release
 end
