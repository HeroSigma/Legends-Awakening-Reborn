HnS_SSAqua_RoomSW_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SSAqua_RoomSW_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SSAqua_RoomSW_Next
 release
 end
HnS_SSAqua_RoomSW_Next::
 warp MAP_HNS_REGION_SAFARIZONE_TOP_LEFT, 15, 15
 waitstate
 release
 end
