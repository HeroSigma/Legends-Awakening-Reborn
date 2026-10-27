Kanto_ThreeIsland_House5_MapScripts::
	.byte 0

KantoAR_34_7_ThreeIsland_House5_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_35_0_FOURISLAND_POKEMONDAYCARE, 6, 4
	goto KantoAR_InspectionFinish
