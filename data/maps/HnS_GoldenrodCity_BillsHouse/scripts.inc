HnS_GoldenrodCity_BillsHouse_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_GoldenrodCity_BillsHouse_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_GoldenrodCity_BillsHouse_Next
 release
 end
HnS_GoldenrodCity_BillsHouse_Next::
 warp MAP_HNS_REGION_GOLDENRODCITY_BIKESHOP, 5, 5
 waitstate
 release
 end
