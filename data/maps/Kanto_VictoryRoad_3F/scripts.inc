Kanto_VictoryRoad_3F_MapScripts::
	.byte 0

KantoAR_1_41_VictoryRoad_3F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_42_ROCKETHIDEOUT_B1F, 14, 17
	goto KantoAR_InspectionFinish
