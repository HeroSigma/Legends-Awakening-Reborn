Kanto_CeruleanCity_House4_MapScripts::
	.byte 0

KantoAR_7_8_CeruleanCity_House4_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_9_CERULEANCITY_HOUSE5, 5, 4
	goto KantoAR_InspectionFinish
