HnS_Route27_House_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route27_House_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route27_House_Next
 release
 end
HnS_Route27_House_Next::
 warp MAP_HNS_REGION_MTSILVER_POKEMONCENTER, 8, 5
 waitstate
 release
 end
