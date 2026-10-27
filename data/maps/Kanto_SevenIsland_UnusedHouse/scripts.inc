Kanto_SevenIsland_UnusedHouse_MapScripts::
	.byte 0

KantoAR_31_5_SevenIsland_UnusedHouse_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_31_6_SEVENISLAND_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
