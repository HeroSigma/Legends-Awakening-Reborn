Kanto_TrainerTower_8F_MapScripts::
	.byte 0

KantoAR_2_8_TrainerTower_8F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_9_TRAINERTOWER_ROOF, 9, 8
	goto KantoAR_InspectionFinish
