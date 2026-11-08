HnS_Route48_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route48_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route48_Next
 release
 end
HnS_Route48_Next::
 warp MAP_HNS_REGION_PALLETTOWN, 12, 10
 waitstate
 release
 end
