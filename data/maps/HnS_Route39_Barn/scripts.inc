HnS_Route39_Barn_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route39_Barn_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route39_Barn_Next
 release
 end
HnS_Route39_Barn_Next::
 warp MAP_HNS_REGION_ROUTE30_HOUSE, 3, 5
 waitstate
 release
 end
