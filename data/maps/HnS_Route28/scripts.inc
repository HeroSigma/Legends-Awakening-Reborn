HnS_Route28_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route28_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route28_Next
 release
 end
HnS_Route28_Next::
 warp MAP_HNS_REGION_NEWBARKTOWN_LAB, 22, 7
 waitstate
 release
 end
