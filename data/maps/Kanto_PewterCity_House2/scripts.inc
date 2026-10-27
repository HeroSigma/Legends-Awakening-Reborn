Kanto_PewterCity_House2_MapScripts::
	.byte 0

KantoAR_6_7_PewterCity_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_0_CERULEANCITY_HOUSE1, 5, 5
	goto KantoAR_InspectionFinish
