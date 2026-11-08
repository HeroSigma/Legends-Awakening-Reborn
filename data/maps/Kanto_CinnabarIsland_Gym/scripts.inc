Kanto_CinnabarIsland_Gym_MapScripts::
	.byte 0

KantoAR_12_0_CinnabarIsland_Gym_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_12_1_CINNABARISLAND_POKEMONLAB_ENTRANCE, 14, 7
	goto KantoAR_InspectionFinish
