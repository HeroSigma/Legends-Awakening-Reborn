HnS_Route9_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route9_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route9_Next
 release
 end
HnS_Route9_Next::
 warp MAP_HNS_REGION_ROUTE10, 18, 45
 waitstate
 release
 end
