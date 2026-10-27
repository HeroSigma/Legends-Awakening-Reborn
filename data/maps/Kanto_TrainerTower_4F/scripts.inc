Kanto_TrainerTower_4F_MapScripts::
	.byte 0

KantoAR_2_4_TrainerTower_4F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_5_TRAINERTOWER_5F, 7, 10
	goto KantoAR_InspectionFinish
