HnS_VermilionCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_VermilionCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_VermilionCity_Next
 release
 end
HnS_VermilionCity_Next::
 warp MAP_HNS_REGION_LAVENDERTOWN, 19, 15
 waitstate
 release
 end
