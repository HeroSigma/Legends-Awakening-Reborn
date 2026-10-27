Kanto_CeruleanCity_House5_MapScripts::
	.byte 0

KantoAR_7_9_CeruleanCity_House5_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_8_0_LAVENDERTOWN_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
