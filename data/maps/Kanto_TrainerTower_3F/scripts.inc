Kanto_TrainerTower_3F_MapScripts::
	.byte 0

KantoAR_2_3_TrainerTower_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_4_TRAINERTOWER_4F, 7, 10
	goto KantoAR_InspectionFinish
