Kanto_UndergroundPath_EastWestTunnel_MapScripts::
	.byte 0

KantoAR_1_34_UndergroundPath_EastWestTunnel_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_35_UNDERGROUNDPATH_EASTENTRANCE, 8, 5
	goto KantoAR_InspectionFinish
