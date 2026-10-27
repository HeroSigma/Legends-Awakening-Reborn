HnS_FuchsiaCity_PokemonCenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_FuchsiaCity_PokemonCenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_FuchsiaCity_PokemonCenter_Next
 release
 end
HnS_FuchsiaCity_PokemonCenter_Next::
 warp MAP_HNS_REGION_FUCHSIACITY_MART, 5, 4
 waitstate
 release
 end
