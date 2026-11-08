Kanto_TrainerTower_2F_MapScripts::
	.byte 0

KantoAR_2_2_TrainerTower_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_3_TRAINERTOWER_3F, 7, 10
	goto KantoAR_InspectionFinish
