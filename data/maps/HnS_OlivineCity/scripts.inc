HnS_OlivineCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_OlivineCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_OlivineCity_Next
 release
 end
HnS_OlivineCity_Next::
 warp MAP_HNS_REGION_CIANWOODCITY, 14, 30
 waitstate
 release
 end
