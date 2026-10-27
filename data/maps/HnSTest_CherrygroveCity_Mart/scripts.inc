HnSTest_CherrygroveCity_Mart_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_CherrygroveCity_Mart_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_CherrygroveCity_Mart_Next
 release
 end
HnSTest_CherrygroveCity_Mart_Next::
 warp MAP_HNS_REGION_CHERRYGROVECITY_HOUSE1, 6, 3
 waitstate
 release
 end
