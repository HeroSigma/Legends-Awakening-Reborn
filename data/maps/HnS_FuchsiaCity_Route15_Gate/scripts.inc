HnS_FuchsiaCity_Route15_Gate_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FuchsiaCity_Route15_Gate_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FuchsiaCity_Route15_Gate_Next
 release
 end
HnS_FuchsiaCity_Route15_Gate_Next::
 warp MAP_HNS_REGION_CINNABARISLAND_POKEMONCENTER, 7, 5
 waitstate
 release
 end
