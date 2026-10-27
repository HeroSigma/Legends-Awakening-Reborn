Kanto_FourIsland_House1_MapScripts::
	.byte 0

KantoAR_35_3_FourIsland_House1_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_35_4_FOURISLAND_LORELEISHOUSE, 4, 3
	goto KantoAR_InspectionFinish
