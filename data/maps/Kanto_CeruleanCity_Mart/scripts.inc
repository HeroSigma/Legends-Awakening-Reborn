Kanto_CeruleanCity_Mart_MapScripts::
	.byte 0

KantoAR_7_7_CeruleanCity_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_8_CERULEANCITY_HOUSE4, 4, 3
	goto KantoAR_InspectionFinish
