HnS_SafariZone1_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SafariZone1_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SafariZone1_Next
 release
 end
HnS_SafariZone1_Next::
 warp MAP_HNS_REGION_SAFARIZONE2, 28, 17
 waitstate
 release
 end
