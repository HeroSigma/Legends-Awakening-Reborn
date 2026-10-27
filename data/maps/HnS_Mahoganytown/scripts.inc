HnS_Mahoganytown_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Mahoganytown_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Mahoganytown_Next
 release
 end
HnS_Mahoganytown_Next::
 warp MAP_HNS_REGION_BLACKTHORNCITY, 28, 30
 waitstate
 release
 end
