HnS_CinnabarIsland_PokemonCenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_CinnabarIsland_PokemonCenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_CinnabarIsland_PokemonCenter_Next
 release
 end
HnS_CinnabarIsland_PokemonCenter_Next::
 warp MAP_HNS_REGION_INDIGOPLATEAU_POKEMONCENTER, 15, 11
 waitstate
 release
 end
