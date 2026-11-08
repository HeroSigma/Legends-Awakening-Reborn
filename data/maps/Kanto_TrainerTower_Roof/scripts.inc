Kanto_TrainerTower_Roof_MapScripts::
	.byte 0

KantoAR_2_9_TrainerTower_Roof_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_10_TRAINERTOWER_LOBBY, 9, 11
	goto KantoAR_InspectionFinish
