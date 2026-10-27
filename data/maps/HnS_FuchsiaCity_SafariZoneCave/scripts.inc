HnS_FuchsiaCity_SafariZoneCave_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FuchsiaCity_SafariZoneCave_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FuchsiaCity_SafariZoneCave_Next
 release
 end
HnS_FuchsiaCity_SafariZoneCave_Next::
 warp MAP_HNS_REGION_ARTISANCAVE_1F, 6, 11
 waitstate
 release
 end
