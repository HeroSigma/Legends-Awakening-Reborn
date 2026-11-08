#include "config/free_space.h"
#if !LA_FREE_SPACE
BattleFrontier_PokemonCenter_2F_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, CableClub_OnFrame
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, CableClub_OnWarp
	map_script MAP_SCRIPT_ON_LOAD, CableClub_OnLoad
	map_script MAP_SCRIPT_ON_TRANSITION, CableClub_OnTransition
	.byte 0

@ The below 3 are unused and leftover from RS
BattleFrontier_PokemonCenter_2F_EventScript_Colosseum::
	call CableClub_EventScript_Colosseum
	end

BattleFrontier_PokemonCenter_2F_EventScript_TradeCenter::
	call CableClub_EventScript_TradeCenter
	end

BattleFrontier_PokemonCenter_2F_EventScript_RecordCorner::
	call CableClub_EventScript_RecordCorner
	end


#else
BattleFrontier_PokemonCenter_2F_MapScripts::
	.byte 0
BattleFrontier_PokemonCenter_2F_EventScript_Colosseum::
	goto EventScript_LegacyFeatureDisabled
BattleFrontier_PokemonCenter_2F_EventScript_TradeCenter::
	goto EventScript_LegacyFeatureDisabled
BattleFrontier_PokemonCenter_2F_EventScript_RecordCorner::
	goto EventScript_LegacyFeatureDisabled
#endif
