HnS_Route23_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route23_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route23_Next
 release
 end
HnS_Route23_Next::
 warp MAP_HNS_REGION_INDIGOPLATEAU, 12, 10
 waitstate
 release
 end
