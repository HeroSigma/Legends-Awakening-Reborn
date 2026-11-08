Kanto_Route24_MapScripts::
	.byte 0

KantoAR_3_43_Route24_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_44_ROUTE25, 36, 8
	goto KantoAR_InspectionFinish
