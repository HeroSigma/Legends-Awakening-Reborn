HnS_MtMortar_1F_North_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MtMortar_1F_North_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MtMortar_1F_North_Next
 release
 end
HnS_MtMortar_1F_North_Next::
 warp MAP_HNS_REGION_MTMORTAR_2F, 28, 20
 waitstate
 release
 end
