HnS_AzaleaTown_KurtsHouse_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_AzaleaTown_KurtsHouse_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_AzaleaTown_KurtsHouse_Next
 release
 end
HnS_AzaleaTown_KurtsHouse_Next::
 warp MAP_HNS_REGION_AZALEATOWN_HOUSE1, 5, 5
 waitstate
 release
 end
