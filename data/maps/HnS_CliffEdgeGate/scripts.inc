HnS_CliffEdgeGate_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CliffEdgeGate_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CliffEdgeGate_Next
 release
 end
HnS_CliffEdgeGate_Next::
 warp MAP_HNS_REGION_MTMORTAR_1F_SOUTH, 52, 28
 waitstate
 release
 end
