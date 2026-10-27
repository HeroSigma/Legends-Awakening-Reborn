HnS_BirthIsland_Exterior_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BirthIsland_Exterior_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BirthIsland_Exterior_Next
 release
 end
HnS_BirthIsland_Exterior_Next::
 warp MAP_HNS_REGION_BIRTHISLAND_HARBOR, 8, 4
 waitstate
 release
 end
