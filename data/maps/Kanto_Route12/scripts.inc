Kanto_Route12_MapScripts::
	.byte 0

KantoAR_3_30_Route12_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_31_ROUTE13, 36, 10
	goto KantoAR_InspectionFinish
