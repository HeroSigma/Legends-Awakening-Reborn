Kanto_VermilionCity_House1_MapScripts::
	.byte 0

KantoAR_9_0_VermilionCity_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_9_1_VERMILIONCITY_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
