HnS_SafariZone_Top_Right_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SafariZone_Top_Right_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SafariZone_Top_Right_Next
 release
 end
HnS_SafariZone_Top_Right_Next::
 warp MAP_HNS_REGION_SAFARIZONE1, 25, 17
 waitstate
 release
 end
