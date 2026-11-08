HnS_IndigoPlateau_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_IndigoPlateau_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_IndigoPlateau_Next
 release
 end
HnS_IndigoPlateau_Next::
 warp MAP_HNS_REGION_ROUTE24, 16, 11
 waitstate
 release
 end
