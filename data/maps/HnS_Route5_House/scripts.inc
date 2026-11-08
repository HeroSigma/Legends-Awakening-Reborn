HnS_Route5_House_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route5_House_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route5_House_Next
 release
 end
HnS_Route5_House_Next::
 warp MAP_HNS_REGION_ROUTE5_TUNNELENTRANCE, 11, 9
 waitstate
 release
 end
