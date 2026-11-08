HnS_TohjoFalls_GiovanniRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_TohjoFalls_GiovanniRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_TohjoFalls_GiovanniRoom_Next
 release
 end
HnS_TohjoFalls_GiovanniRoom_Next::
 warp MAP_HNS_REGION_VICTORYROADKANTO_B2F, 19, 25
 waitstate
 release
 end
