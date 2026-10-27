HnS_BlackthornCity_Mart_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BlackthornCity_Mart_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BlackthornCity_Mart_Next
 release
 end
HnS_BlackthornCity_Mart_Next::
 warp MAP_HNS_REGION_BLACKTHORNCITY_GYM, 19, 33
 waitstate
 release
 end
