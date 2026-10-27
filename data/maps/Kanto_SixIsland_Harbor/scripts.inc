Kanto_SixIsland_Harbor_MapScripts::
	.byte 0

KantoAR_37_2_SixIsland_Harbor_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_37_3_SIXISLAND_HOUSE, 4, 3
	goto KantoAR_InspectionFinish
