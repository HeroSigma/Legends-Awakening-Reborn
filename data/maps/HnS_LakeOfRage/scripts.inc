HnS_LakeOfRage_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_LakeOfRage_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_LakeOfRage_Next
 release
 end
HnS_LakeOfRage_Next::
 warp MAP_HNS_REGION_LAKEOFRAGELOWTIDE, 27, 18
 waitstate
 release
 end
