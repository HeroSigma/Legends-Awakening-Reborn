HnS_Route2_House_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route2_House_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route2_House_Next
 release
 end
HnS_Route2_House_Next::
 warp MAP_HNS_REGION_MTMOON_SHOP, 5, 6
 waitstate
 release
 end
