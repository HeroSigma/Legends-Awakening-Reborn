HnS_Route38_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route38_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route38_Next
 release
 end
HnS_Route38_Next::
 warp MAP_HNS_REGION_ROUTE39, 20, 27
 waitstate
 release
 end
