HnS_SSAqua_RoomNNE_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SSAqua_RoomNNE_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SSAqua_RoomNNE_Next
 release
 end
HnS_SSAqua_RoomNNE_Next::
 warp MAP_HNS_REGION_SSAQUA_ROOMSSW, 4, 5
 waitstate
 release
 end
