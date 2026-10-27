HnS_Route19_Cave_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route19_Cave_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route19_Cave_Next
 release
 end
HnS_Route19_Cave_Next::
 warp MAP_HNS_REGION_UNIONROOM, 7, 6
 waitstate
 release
 end
