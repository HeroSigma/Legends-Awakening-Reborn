Kanto_TrainerTower_Elevator_MapScripts::
	.byte 0

KantoAR_2_11_TrainerTower_Elevator_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_2_12_FIVEISLAND_LOSTCAVE_ENTRANCE, 4, 5
	goto KantoAR_InspectionFinish
