HnS_CianwoodHouse3_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CianwoodHouse3_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CianwoodHouse3_Next
 release
 end
HnS_CianwoodHouse3_Next::
 warp MAP_HNS_REGION_CIANWOODSHOP, 8, 10
 waitstate
 release
 end
