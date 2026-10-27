HnSTest_VioletCity_Gym_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnSTest_VioletCity_Gym_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnSTest_VioletCity_Gym_Next
 release
 end
HnSTest_VioletCity_Gym_Next::
 warp MAP_HNS_REGION_AZALEATOWN_POKEMONCENTER, 8, 5
 waitstate
 release
 end
