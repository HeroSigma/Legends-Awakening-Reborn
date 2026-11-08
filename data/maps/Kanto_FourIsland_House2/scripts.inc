Kanto_FourIsland_House2_MapScripts::
	.byte 0

KantoAR_35_6_FourIsland_House2_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_35_7_FOURISLAND_MART, 5, 4
	goto KantoAR_InspectionFinish
