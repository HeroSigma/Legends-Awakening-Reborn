HnS_MtMortar_1F_South_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MtMortar_1F_South_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MtMortar_1F_South_Next
 release
 end
HnS_MtMortar_1F_South_Next::
 warp MAP_HNS_REGION_MTMORTAR_1F_NORTH, 37, 34
 waitstate
 release
 end
