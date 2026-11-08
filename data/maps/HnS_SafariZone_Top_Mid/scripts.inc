HnS_SafariZone_Top_Mid_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SafariZone_Top_Mid_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SafariZone_Top_Mid_Next
 release
 end
HnS_SafariZone_Top_Mid_Next::
 warp MAP_HNS_REGION_SAFARIZONE_TOP_RIGHT, 19, 16
 waitstate
 release
 end
