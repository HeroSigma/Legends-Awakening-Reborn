HnS_DragonsDen_Cavern_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_DragonsDen_Cavern_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_DragonsDen_Cavern_Next
 release
 end
HnS_DragonsDen_Cavern_Next::
 warp MAP_HNS_REGION_DRAGONSDEN_SHRINE, 7, 9
 waitstate
 release
 end
