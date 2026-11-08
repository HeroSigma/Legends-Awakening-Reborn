Kanto_TrainerTower_5F_MapScripts::
	.byte 0

KantoAR_2_5_TrainerTower_5F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_6_TRAINERTOWER_6F, 7, 10
	goto KantoAR_InspectionFinish
