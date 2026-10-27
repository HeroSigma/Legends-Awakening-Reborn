HnS_Route32_PokemonCenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route32_PokemonCenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route32_PokemonCenter_Next
 release
 end
HnS_Route32_PokemonCenter_Next::
 warp MAP_HNS_REGION_RUINSOFALPH_LAB, 5, 3
 waitstate
 release
 end
