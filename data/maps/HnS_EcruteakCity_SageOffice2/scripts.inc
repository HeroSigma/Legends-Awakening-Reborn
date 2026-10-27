HnS_EcruteakCity_SageOffice2_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_EcruteakCity_SageOffice2_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_EcruteakCity_SageOffice2_Next
 release
 end
HnS_EcruteakCity_SageOffice2_Next::
 warp MAP_HNS_REGION_BELLCHIMETRAIL, 35, 34
 waitstate
 release
 end
