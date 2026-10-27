HnS_VermilionCity_Mart_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VermilionCity_Mart_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VermilionCity_Mart_Next
 release
 end
HnS_VermilionCity_Mart_Next::
 warp MAP_HNS_REGION_VERMILIONCITY_PORTOUTSIDE, 24, 6
 waitstate
 release
 end
