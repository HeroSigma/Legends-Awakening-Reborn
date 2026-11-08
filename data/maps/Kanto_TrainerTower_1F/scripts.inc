Kanto_TrainerTower_1F_MapScripts::
	.byte 0

KantoAR_2_1_TrainerTower_1F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_2_TRAINERTOWER_2F, 7, 10
	goto KantoAR_InspectionFinish
