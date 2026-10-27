HnS_ReceptionGate_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_ReceptionGate_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_ReceptionGate_Next
 release
 end
HnS_ReceptionGate_Next::
 warp MAP_HNS_REGION_ROUTE39_FARMHOUSE, 6, 3
 waitstate
 release
 end
