Kanto_SixIsland_OutcastIsland_MapScripts::
	.byte 0

KantoAR_3_58_SixIsland_OutcastIsland_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_59_SIXISLAND_GREENPATH, 38, 14
	goto KantoAR_InspectionFinish
