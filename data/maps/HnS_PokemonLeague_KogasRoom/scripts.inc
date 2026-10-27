HnS_PokemonLeague_KogasRoom_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_PokemonLeague_KogasRoom_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_PokemonLeague_KogasRoom_Next
 release
 end
HnS_PokemonLeague_KogasRoom_Next::
 warp MAP_HNS_REGION_POKEMONLEAGUE_BRUNOSROOM, 5, 6
 waitstate
 release
 end
