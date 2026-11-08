HnS_MtSilver_MountainSide_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MtSilver_MountainSide_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MtSilver_MountainSide_Next
 release
 end
HnS_MtSilver_MountainSide_Next::
 warp MAP_HNS_REGION_MTSILVER_2F, 25, 25
 waitstate
 release
 end
