HnS_Route9_PokemonCenter_MapScripts::
 map_script MAP_SCRIPT_ON_TRANSITION, HnsRegion_OnTransition
 .byte 0

HnS_Route9_PokemonCenter_Inspect::
 lock
 faceplayer
 msgbox HnsRegion_InspectText, MSGBOX_YESNO
 goto_if_eq VAR_RESULT, YES, HnS_Route9_PokemonCenter_Next
 release
 end
HnS_Route9_PokemonCenter_Next::
 warp MAP_HNS_REGION_ROUTE10_POWERPLANTENTRANCE, 10, 12
 waitstate
 release
 end
