HnS_PokemonLeague_BrunosRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PokemonLeague_BrunosRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PokemonLeague_BrunosRoom_Next
 release
 end
HnS_PokemonLeague_BrunosRoom_Next::
 warp MAP_HNS_REGION_POKEMONLEAGUE_KARENSROOM, 11, 6
 waitstate
 release
 end
