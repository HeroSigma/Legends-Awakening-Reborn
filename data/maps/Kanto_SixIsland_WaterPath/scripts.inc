Kanto_SixIsland_WaterPath_MapScripts::
	.byte 0

KantoAR_3_60_SixIsland_WaterPath_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_61_SIXISLAND_RUINVALLEY, 24, 26
	goto KantoAR_InspectionFinish
