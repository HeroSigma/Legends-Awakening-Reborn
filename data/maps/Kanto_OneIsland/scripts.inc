Kanto_OneIsland_MapScripts::
	.byte 0

KantoAR_3_12_OneIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_13_TWOISLAND, 24, 12
	goto KantoAR_InspectionFinish
