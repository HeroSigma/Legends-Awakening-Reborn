HnS_GoldenrodCity_DepartmentStore_1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_GoldenrodCity_DepartmentStore_1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_GoldenrodCity_DepartmentStore_1F_Next
 release
 end
HnS_GoldenrodCity_DepartmentStore_1F_Next::
 warp MAP_HNS_REGION_GOLDENRODCITY_DEPARTMENTSTORE_2F, 16, 9
 waitstate
 release
 end
