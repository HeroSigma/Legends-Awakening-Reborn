HnS_Route26_House2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route26_House2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route26_House2_Next
 release
 end
HnS_Route26_House2_Next::
 warp MAP_HNS_REGION_GATE_ROUTE2_VIRIDIANFOREST, 7, 6
 waitstate
 release
 end
