HnS_PewterCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PewterCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PewterCity_Next
 release
 end
HnS_PewterCity_Next::
 warp MAP_HNS_REGION_CERULEANCITY, 29, 25
 waitstate
 release
 end
