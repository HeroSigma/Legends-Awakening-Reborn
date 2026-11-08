Kanto_CeruleanCity_MapScripts::
	.byte 0

KantoAR_3_3_CeruleanCity_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_4_LAVENDERTOWN, 14, 10
	goto KantoAR_InspectionFinish
