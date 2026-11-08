HnS_EcruteakCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_EcruteakCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_EcruteakCity_Next
 release
 end
HnS_EcruteakCity_Next::
 warp MAP_HNS_REGION_OLIVINECITY, 30, 36
 waitstate
 release
 end
