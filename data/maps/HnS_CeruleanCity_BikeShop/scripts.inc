HnS_CeruleanCity_BikeShop_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CeruleanCity_BikeShop_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CeruleanCity_BikeShop_Next
 release
 end
HnS_CeruleanCity_BikeShop_Next::
 warp MAP_HNS_REGION_CERULEANCITY_GYM, 8, 11
 waitstate
 release
 end
