HnS_CianwoodHouse1_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CianwoodHouse1_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CianwoodHouse1_Next
 release
 end
HnS_CianwoodHouse1_Next::
 warp MAP_HNS_REGION_CIANWOODHOUSE2, 4, 5
 waitstate
 release
 end
