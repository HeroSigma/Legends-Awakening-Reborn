HnS_PokemonLeague_KarensRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PokemonLeague_KarensRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PokemonLeague_KarensRoom_Next
 release
 end
HnS_PokemonLeague_KarensRoom_Next::
 warp MAP_HNS_REGION_POKEMONLEAGUE_CHAMPIONSROOM, 6, 10
 waitstate
 release
 end
