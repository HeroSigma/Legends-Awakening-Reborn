HnS_SlowpokeWell_B2F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_SlowpokeWell_B2F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_SlowpokeWell_B2F_Next
 release
 end
HnS_SlowpokeWell_B2F_Next::
 warp MAP_HNS_REGION_ILEXFOREST, 41, 35
 waitstate
 release
 end
