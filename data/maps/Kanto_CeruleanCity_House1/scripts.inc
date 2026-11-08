Kanto_CeruleanCity_House1_MapScripts::
	.byte 0

KantoAR_7_0_CeruleanCity_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_1_CERULEANCITY_HOUSE2, 5, 3
	goto KantoAR_InspectionFinish
