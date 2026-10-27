Kanto_CeruleanCity_House3_MapScripts::
	.byte 0

KantoAR_7_2_CeruleanCity_House3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_7_3_CERULEANCITY_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
