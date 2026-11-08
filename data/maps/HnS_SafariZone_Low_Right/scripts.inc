HnS_SafariZone_Low_Right_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SafariZone_Low_Right_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SafariZone_Low_Right_Next
 release
 end
HnS_SafariZone_Low_Right_Next::
 warp MAP_HNS_REGION_SAFARIZONE_TOP_MID, 18, 19
 waitstate
 release
 end
