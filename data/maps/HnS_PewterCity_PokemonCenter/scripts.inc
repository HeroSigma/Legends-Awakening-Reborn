HnS_PewterCity_PokemonCenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PewterCity_PokemonCenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PewterCity_PokemonCenter_Next
 release
 end
HnS_PewterCity_PokemonCenter_Next::
 warp MAP_HNS_REGION_PEWTERCITY_MART, 5, 4
 waitstate
 release
 end
