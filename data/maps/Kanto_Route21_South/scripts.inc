Kanto_Route21_South_MapScripts::
	.byte 0

KantoAR_3_40_Route21_South_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_41_ROUTE22, 24, 13
	goto KantoAR_InspectionFinish
