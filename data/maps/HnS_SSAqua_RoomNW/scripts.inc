HnS_SSAqua_RoomNW_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SSAqua_RoomNW_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SSAqua_RoomNW_Next
 release
 end
HnS_SSAqua_RoomNW_Next::
 warp MAP_HNS_REGION_SSAQUA_ROOMNE, 3, 5
 waitstate
 release
 end
