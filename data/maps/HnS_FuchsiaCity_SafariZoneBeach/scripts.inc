HnS_FuchsiaCity_SafariZoneBeach_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FuchsiaCity_SafariZoneBeach_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FuchsiaCity_SafariZoneBeach_Next
 release
 end
HnS_FuchsiaCity_SafariZoneBeach_Next::
 warp MAP_HNS_REGION_FUCHSIACITY_SAFARIZONEBRUSH, 25, 15
 waitstate
 release
 end
