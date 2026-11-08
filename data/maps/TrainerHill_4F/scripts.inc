#include "config/free_space.h"
#if !LA_FREE_SPACE
TrainerHill_4F_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, TrainerHill_OnResume
	map_script MAP_SCRIPT_ON_FRAME_TABLE, TrainerHill_OnFrame
	.byte 0


#else
TrainerHill_4F_MapScripts::
	.byte 0
#endif
