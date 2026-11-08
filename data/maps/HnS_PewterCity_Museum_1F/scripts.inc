HnS_PewterCity_Museum_1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PewterCity_Museum_1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PewterCity_Museum_1F_Next
 release
 end
HnS_PewterCity_Museum_1F_Next::
 warp MAP_HNS_REGION_PEWTERCITY_MUSEUM_2F, 9, 5
 waitstate
 release
 end
