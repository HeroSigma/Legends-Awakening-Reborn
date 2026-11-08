HnS_SaffronCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SaffronCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SaffronCity_Next
 release
 end
HnS_SaffronCity_Next::
 warp MAP_HNS_REGION_FUCHSIACITY, 23, 20
 waitstate
 release
 end
