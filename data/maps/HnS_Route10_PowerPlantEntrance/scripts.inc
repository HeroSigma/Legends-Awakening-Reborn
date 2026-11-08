HnS_Route10_PowerPlantEntrance_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route10_PowerPlantEntrance_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route10_PowerPlantEntrance_Next
 release
 end
HnS_Route10_PowerPlantEntrance_Next::
 warp MAP_HNS_REGION_ROUTE10_POWERPLANTBACKROOM, 9, 6
 waitstate
 release
 end
