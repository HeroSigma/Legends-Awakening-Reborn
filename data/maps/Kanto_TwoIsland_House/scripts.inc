Kanto_TwoIsland_House_MapScripts::
	.byte 0

KantoAR_33_1_TwoIsland_House_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_33_2_TWOISLAND_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
