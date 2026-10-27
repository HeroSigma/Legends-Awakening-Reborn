HnS_MtMortar_B1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MtMortar_B1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MtMortar_B1F_Next
 release
 end
HnS_MtMortar_B1F_Next::
 warp MAP_HNS_REGION_LAKEOFRAGE, 32, 37
 waitstate
 release
 end
