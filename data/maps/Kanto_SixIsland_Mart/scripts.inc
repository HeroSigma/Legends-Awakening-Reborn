Kanto_SixIsland_Mart_MapScripts::
	.byte 0

KantoAR_37_4_SixIsland_Mart_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_38_0_THREEISLAND_HARBOR, 8, 5
	goto KantoAR_InspectionFinish
