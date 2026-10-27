HnS_RuinsOfAlph_Lab_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_RuinsOfAlph_Lab_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_RuinsOfAlph_Lab_Next
 release
 end
HnS_RuinsOfAlph_Lab_Next::
 warp MAP_HNS_REGION_ROUTE34_DAYCARE, 7, 5
 waitstate
 release
 end
