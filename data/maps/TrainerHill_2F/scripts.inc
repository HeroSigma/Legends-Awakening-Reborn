#include "config/free_space.h"
#if !LA_FREE_SPACE
TrainerHill_2F_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, TrainerHill_OnResume
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, TrainerHill_OnWarp
	map_script MAP_SCRIPT_ON_FRAME_TABLE, TrainerHill_OnFrame
	.byte 0


#else
TrainerHill_2F_MapScripts::
	.byte 0
#endif
