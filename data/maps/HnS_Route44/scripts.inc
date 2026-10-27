HnS_Route44_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route44_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route44_Next
 release
 end
HnS_Route44_Next::
 warp MAP_HNS_REGION_ROUTE45, 19, 51
 waitstate
 release
 end
