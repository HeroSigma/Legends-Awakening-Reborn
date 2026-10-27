Kanto_LavenderTown_House1_MapScripts::
	.byte 0

KantoAR_8_3_LavenderTown_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_8_4_LAVENDERTOWN_HOUSE2, 4, 3
	goto KantoAR_InspectionFinish
