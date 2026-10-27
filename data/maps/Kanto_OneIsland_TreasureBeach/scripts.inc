Kanto_OneIsland_TreasureBeach_MapScripts::
	.byte 0

KantoAR_3_46_OneIsland_TreasureBeach_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_47_TWOISLAND_CAPEBRINK, 12, 17
	goto KantoAR_InspectionFinish
