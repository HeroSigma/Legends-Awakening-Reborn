Kanto_TrainerTower_7F_MapScripts::
	.byte 0

KantoAR_2_7_TrainerTower_7F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_8_TRAINERTOWER_8F, 7, 10
	goto KantoAR_InspectionFinish
