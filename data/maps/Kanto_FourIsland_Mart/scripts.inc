Kanto_FourIsland_Mart_MapScripts::
	.byte 0

KantoAR_35_7_FourIsland_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_36_0_FIVEISLAND_POKEMONCENTER_1F, 7, 5
	goto KantoAR_InspectionFinish
