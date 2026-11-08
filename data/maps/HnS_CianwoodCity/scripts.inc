HnS_CianwoodCity_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CianwoodCity_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CianwoodCity_Next
 release
 end
HnS_CianwoodCity_Next::
 warp MAP_HNS_REGION_SAFARIZONEGATE, 13, 17
 waitstate
 release
 end
