Kanto_Route6_NorthEntrance_MapScripts::
	.byte 0

KantoAR_18_0_Route6_NorthEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_18_1_ROUTE6_UNUSEDHOUSE, 4, 3
	goto KantoAR_InspectionFinish
