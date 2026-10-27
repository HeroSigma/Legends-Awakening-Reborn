HnS_OlivineCity_Cafe_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_OlivineCity_Cafe_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_OlivineCity_Cafe_Next
 release
 end
HnS_OlivineCity_Cafe_Next::
 warp MAP_HNS_REGION_OLIVINECITY_MART, 7, 3
 waitstate
 release
 end
