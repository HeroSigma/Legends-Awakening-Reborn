HnS_SafariZone2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SafariZone2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SafariZone2_Next
 release
 end
HnS_SafariZone2_Next::
 warp MAP_HNS_REGION_SAFARIZONE3, 23, 18
 waitstate
 release
 end
