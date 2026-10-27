HnS_EcruteakCity_SageOffice1_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_EcruteakCity_SageOffice1_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_EcruteakCity_SageOffice1_Next
 release
 end
HnS_EcruteakCity_SageOffice1_Next::
 warp MAP_HNS_REGION_ECRUTEAKCITY_SAGEOFFICE2, 5, 8
 waitstate
 release
 end
