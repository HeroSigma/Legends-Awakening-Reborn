Kanto_LavenderTown_MapScripts::
	.byte 0

KantoAR_3_4_LavenderTown_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_5_VERMILIONCITY, 24, 20
	goto KantoAR_InspectionFinish
