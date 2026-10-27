HnS_TohjoFalls_Cavern_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TohjoFalls_Cavern_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TohjoFalls_Cavern_Next
 release
 end
HnS_TohjoFalls_Cavern_Next::
 warp MAP_HNS_REGION_TOHJOFALLS_GIOVANNIROOM, 4, 5
 waitstate
 release
 end
