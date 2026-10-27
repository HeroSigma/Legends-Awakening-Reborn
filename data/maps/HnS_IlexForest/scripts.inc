HnS_IlexForest_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_IlexForest_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_IlexForest_Next
 release
 end
HnS_IlexForest_Next::
 warp MAP_HNS_REGION_NATIONALPARK_NORMAL, 24, 27
 waitstate
 release
 end
