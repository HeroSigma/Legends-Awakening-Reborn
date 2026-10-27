HnS_MahoganyTown_Shop_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_MahoganyTown_Shop_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_MahoganyTown_Shop_Next
 release
 end
HnS_MahoganyTown_Shop_Next::
 warp MAP_HNS_REGION_MAHOGANYTOWN_HOUSE1, 6, 3
 waitstate
 release
 end
