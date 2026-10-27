HnS_CianwoodPokecenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CianwoodPokecenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CianwoodPokecenter_Next
 release
 end
HnS_CianwoodPokecenter_Next::
 warp MAP_HNS_REGION_CIANWOODHOUSE1, 6, 3
 waitstate
 release
 end
