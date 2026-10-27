HnS_FuchsiaCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FuchsiaCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FuchsiaCity_Next
 release
 end
HnS_FuchsiaCity_Next::
 warp MAP_HNS_REGION_CINNABARISLAND, 36, 21
 waitstate
 release
 end
