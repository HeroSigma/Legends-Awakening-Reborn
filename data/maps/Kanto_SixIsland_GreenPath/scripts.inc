Kanto_SixIsland_GreenPath_MapScripts::
	.byte 0

KantoAR_3_59_SixIsland_GreenPath_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_60_SIXISLAND_WATERPATH, 8, 51
	goto KantoAR_InspectionFinish
