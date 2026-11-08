Kanto_VermilionCity_House2_MapScripts::
	.byte 0

KantoAR_9_4_VermilionCity_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_9_5_VERMILIONCITY_MART, 5, 4
	goto KantoAR_InspectionFinish
