HnS_DragonsDen_Shrine_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_DragonsDen_Shrine_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_DragonsDen_Shrine_Next
 release
 end
HnS_DragonsDen_Shrine_Next::
 warp MAP_HNS_REGION_WHIRLISLANDS_1F, 34, 18
 waitstate
 release
 end
