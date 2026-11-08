Kanto_SevenIsland_TrainerTower_MapScripts::
	.byte 0

KantoAR_3_62_SevenIsland_TrainerTower_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_63_SEVENISLAND_SEVAULTCANYON_ENTRANCE, 15, 20
	goto KantoAR_InspectionFinish
