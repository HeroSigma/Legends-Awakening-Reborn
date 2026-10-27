Kanto_SevenIsland_MapScripts::
	.byte 0

KantoAR_3_17_SevenIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_18_SIXISLAND, 12, 14
	goto KantoAR_InspectionFinish
