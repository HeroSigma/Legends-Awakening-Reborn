HnS_CeladonCity_Apartments_RoofDay_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CeladonCity_Apartments_RoofDay_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CeladonCity_Apartments_RoofDay_Next
 release
 end
HnS_CeladonCity_Apartments_RoofDay_Next::
 warp MAP_HNS_REGION_CELADONCITY_APARTMENTS_ROOFNIGHT, 6, 11
 waitstate
 release
 end
