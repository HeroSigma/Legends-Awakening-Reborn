HnS_CeladonCity_Apartments_RoofHouse_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CeladonCity_Apartments_RoofHouse_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CeladonCity_Apartments_RoofHouse_Next
 release
 end
HnS_CeladonCity_Apartments_RoofHouse_Next::
 warp MAP_HNS_REGION_CELADONCITY_GAMECORNER, 10, 7
 waitstate
 release
 end
