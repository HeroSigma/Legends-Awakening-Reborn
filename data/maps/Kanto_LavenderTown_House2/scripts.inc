Kanto_LavenderTown_House2_MapScripts::
	.byte 0

KantoAR_8_4_LavenderTown_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_8_5_LAVENDERTOWN_MART, 5, 4
	goto KantoAR_InspectionFinish
