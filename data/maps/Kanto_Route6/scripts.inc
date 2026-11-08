Kanto_Route6_MapScripts::
	.byte 0

KantoAR_3_24_Route6_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_25_ROUTE7, 12, 10
	goto KantoAR_InspectionFinish
