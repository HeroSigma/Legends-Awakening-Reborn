HnS_CianwoodShop_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CianwoodShop_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CianwoodShop_Next
 release
 end
HnS_CianwoodShop_Next::
 warp MAP_HNS_REGION_CIANWOODGYM, 10, 14
 waitstate
 release
 end
