Kanto_Route22_NorthEntrance_MapScripts::
	.byte 0

KantoAR_28_0_Route22_NorthEntrance_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_29_0_ROUTE23_UNUSEDHOUSE, 4, 3
	goto KantoAR_InspectionFinish
