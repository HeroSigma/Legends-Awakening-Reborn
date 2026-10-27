Kanto_LavenderTown_Mart_MapScripts::
	.byte 0

KantoAR_8_5_LavenderTown_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_9_0_VERMILIONCITY_HOUSE1, 4, 3
	goto KantoAR_InspectionFinish
