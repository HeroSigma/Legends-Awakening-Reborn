Kanto_BirthIsland_Exterior_MapScripts::
	.byte 0

KantoAR_2_56_BirthIsland_Exterior_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_57_ONEISLAND_KINDLEROAD_EMBERSPA, 13, 20
	goto KantoAR_InspectionFinish
