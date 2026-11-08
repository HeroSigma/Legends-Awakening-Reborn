HnS_SafariZone_Low_Left_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SafariZone_Low_Left_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SafariZone_Low_Left_Next
 release
 end
HnS_SafariZone_Low_Left_Next::
 warp MAP_HNS_REGION_SAFARIZONE_LOW_RIGHT, 17, 16
 waitstate
 release
 end
