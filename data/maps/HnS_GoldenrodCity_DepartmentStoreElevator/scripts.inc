HnS_GoldenrodCity_DepartmentStoreElevator_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_GoldenrodCity_DepartmentStoreElevator_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_GoldenrodCity_DepartmentStoreElevator_Next
 release
 end
HnS_GoldenrodCity_DepartmentStoreElevator_Next::
 warp MAP_HNS_REGION_ECRUTEAKCITY_POKEMONCENTER, 8, 5
 waitstate
 release
 end
