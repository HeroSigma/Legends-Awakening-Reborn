Kanto_RocketHideout_Elevator_MapScripts::
	.byte 0

KantoAR_1_46_RocketHideout_Elevator_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_47_SILPHCO_1F, 18, 8
	goto KantoAR_InspectionFinish
