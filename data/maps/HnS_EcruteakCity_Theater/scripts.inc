HnS_EcruteakCity_Theater_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_EcruteakCity_Theater_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_EcruteakCity_Theater_Next
 release
 end
HnS_EcruteakCity_Theater_Next::
 warp MAP_HNS_REGION_ECRUTEAKCITY_HOUSE1, 6, 3
 waitstate
 release
 end
