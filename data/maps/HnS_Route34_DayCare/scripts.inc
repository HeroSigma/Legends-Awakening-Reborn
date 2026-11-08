HnS_Route34_DayCare_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route34_DayCare_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route34_DayCare_Next
 release
 end
HnS_Route34_DayCare_Next::
 warp MAP_HNS_REGION_ROUTE28_HOUSE, 6, 3
 waitstate
 release
 end
