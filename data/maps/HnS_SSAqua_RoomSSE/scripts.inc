HnS_SSAqua_RoomSSE_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SSAqua_RoomSSE_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SSAqua_RoomSSE_Next
 release
 end
HnS_SSAqua_RoomSSE_Next::
 warp MAP_HNS_REGION_SSAQUA_ROOMSE, 3, 5
 waitstate
 release
 end
