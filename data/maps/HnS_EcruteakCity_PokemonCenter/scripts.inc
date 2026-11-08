HnS_EcruteakCity_PokemonCenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_EcruteakCity_PokemonCenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_EcruteakCity_PokemonCenter_Next
 release
 end
HnS_EcruteakCity_PokemonCenter_Next::
 warp MAP_HNS_REGION_ECRUTEAKCITY_MART, 7, 3
 waitstate
 release
 end
