HnS_PewterCity_House2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PewterCity_House2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PewterCity_House2_Next
 release
 end
HnS_PewterCity_House2_Next::
 warp MAP_HNS_REGION_PEWTERCITY_GYM, 6, 8
 waitstate
 release
 end
