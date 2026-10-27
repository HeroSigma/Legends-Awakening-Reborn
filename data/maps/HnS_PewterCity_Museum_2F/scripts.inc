HnS_PewterCity_Museum_2F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PewterCity_Museum_2F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PewterCity_Museum_2F_Next
 release
 end
HnS_PewterCity_Museum_2F_Next::
 warp MAP_HNS_REGION_CERULEANCITY_POKEMONCENTER, 7, 5
 waitstate
 release
 end
