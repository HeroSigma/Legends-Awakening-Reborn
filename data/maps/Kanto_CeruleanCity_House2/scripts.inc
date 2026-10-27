Kanto_CeruleanCity_House2_MapScripts::
	.byte 0

KantoAR_7_1_CeruleanCity_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_2_CERULEANCITY_HOUSE3, 4, 3
	goto KantoAR_InspectionFinish
