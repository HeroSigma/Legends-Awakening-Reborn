HnS_CinnabarIsland_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CinnabarIsland_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CinnabarIsland_Next
 release
 end
HnS_CinnabarIsland_Next::
 warp MAP_HNS_REGION_ROUTE1, 25, 19
 waitstate
 release
 end
