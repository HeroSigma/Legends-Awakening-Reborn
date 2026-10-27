HnS_VioletCity_Mart_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VioletCity_Mart_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VioletCity_Mart_Next
 release
 end
HnS_VioletCity_Mart_Next::
 warp MAP_HNS_REGION_VIOLETCITY_TRAINERSCHOOL, 5, 11
 waitstate
 release
 end
