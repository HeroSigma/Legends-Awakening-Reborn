HnS_Route14_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route14_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route14_Next
 release
 end
HnS_Route14_Next::
 warp MAP_HNS_REGION_ROUTE15, 47, 16
 waitstate
 release
 end
