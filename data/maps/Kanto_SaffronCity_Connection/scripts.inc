Kanto_SaffronCity_Connection_MapScripts::
	.byte 0

KantoAR_3_11_SaffronCity_Connection_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_12_ONEISLAND, 13, 10
	goto KantoAR_InspectionFinish
