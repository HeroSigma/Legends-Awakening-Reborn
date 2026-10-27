HnS_PokemonLeague_WillsRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PokemonLeague_WillsRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PokemonLeague_WillsRoom_Next
 release
 end
HnS_PokemonLeague_WillsRoom_Next::
 warp MAP_HNS_REGION_POKEMONLEAGUE_KOGASROOM, 5, 6
 waitstate
 release
 end
