HnS_OlivineCity_PokemonCenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_OlivineCity_PokemonCenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_OlivineCity_PokemonCenter_Next
 release
 end
HnS_OlivineCity_PokemonCenter_Next::
 warp MAP_HNS_REGION_OLIVINECITY_GYM, 8, 11
 waitstate
 release
 end
