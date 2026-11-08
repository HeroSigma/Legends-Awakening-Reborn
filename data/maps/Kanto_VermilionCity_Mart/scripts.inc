Kanto_VermilionCity_Mart_MapScripts::
	.byte 0

KantoAR_9_5_VermilionCity_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_9_6_VERMILIONCITY_GYM, 5, 8
	goto KantoAR_InspectionFinish
