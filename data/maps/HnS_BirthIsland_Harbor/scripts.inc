HnS_BirthIsland_Harbor_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_BirthIsland_Harbor_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_BirthIsland_Harbor_Next
 release
 end
HnS_BirthIsland_Harbor_Next::
 warp MAP_HNS_REGION_BATTLEFRONTIER_OUTSIDEWEST, 28, 36
 waitstate
 release
 end
