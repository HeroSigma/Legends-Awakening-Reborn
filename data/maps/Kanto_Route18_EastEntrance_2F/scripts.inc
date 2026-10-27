Kanto_Route18_EastEntrance_2F_MapScripts::
	.byte 0

KantoAR_26_1_Route18_EastEntrance_2F_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_27_0_ROUTE19_UNUSEDHOUSE, 4, 3
	goto KantoAR_InspectionFinish
