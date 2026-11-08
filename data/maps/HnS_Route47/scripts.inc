HnS_Route47_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route47_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route47_Next
 release
 end
HnS_Route47_Next::
 warp MAP_HNS_REGION_ROUTE48, 37, 18
 waitstate
 release
 end
