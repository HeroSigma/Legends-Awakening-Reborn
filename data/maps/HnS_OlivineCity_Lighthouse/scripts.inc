HnS_OlivineCity_Lighthouse_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_OlivineCity_Lighthouse_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_OlivineCity_Lighthouse_Next
 release
 end
HnS_OlivineCity_Lighthouse_Next::
 warp MAP_HNS_REGION_CIANWOODPOKECENTER, 8, 5
 waitstate
 release
 end
