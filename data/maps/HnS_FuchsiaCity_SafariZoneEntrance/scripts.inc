HnS_FuchsiaCity_SafariZoneEntrance_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FuchsiaCity_SafariZoneEntrance_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FuchsiaCity_SafariZoneEntrance_Next
 release
 end
HnS_FuchsiaCity_SafariZoneEntrance_Next::
 warp MAP_HNS_REGION_FUCHSIACITY_SAFARIZONEBEACH, 25, 22
 waitstate
 release
 end
