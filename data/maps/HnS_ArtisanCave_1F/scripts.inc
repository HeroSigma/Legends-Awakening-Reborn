HnS_ArtisanCave_1F_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_ArtisanCave_1F_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_ArtisanCave_1F_Next
 release
 end
HnS_ArtisanCave_1F_Next::
 warp MAP_HNS_REGION_ARTISANCAVE_B1F, 23, 27
 waitstate
 release
 end
