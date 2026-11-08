HnS_UnionRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_UnionRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_UnionRoom_Next
 release
 end
HnS_UnionRoom_Next::
 warp MAP_HNS_REGION_TRAINERHILL_COURTYARD, 24, 23
 waitstate
 release
 end
