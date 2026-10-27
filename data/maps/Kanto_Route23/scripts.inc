Kanto_Route23_MapScripts::
	.byte 0

KantoAR_3_42_Route23_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_43_ROUTE24, 11, 20
	goto KantoAR_InspectionFinish
