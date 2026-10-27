HnS_Route10_PowerPlantBackRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route10_PowerPlantBackRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route10_PowerPlantBackRoom_Next
 release
 end
HnS_Route10_PowerPlantBackRoom_Next::
 warp MAP_HNS_REGION_ROUTE16_HOUSE, 6, 3
 waitstate
 release
 end
