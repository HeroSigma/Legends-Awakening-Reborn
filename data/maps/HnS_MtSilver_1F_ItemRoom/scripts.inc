HnS_MtSilver_1F_ItemRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MtSilver_1F_ItemRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MtSilver_1F_ItemRoom_Next
 release
 end
HnS_MtSilver_1F_ItemRoom_Next::
 warp MAP_HNS_REGION_MTSILVER_1F_WATERFALLROOM, 28, 25
 waitstate
 release
 end
