HnS_VioletCity_House1_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VioletCity_House1_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VioletCity_House1_Next
 release
 end
HnS_VioletCity_House1_Next::
 warp MAP_HNS_REGION_VIOLETCITY_HOUSE2, 4, 5
 waitstate
 release
 end
