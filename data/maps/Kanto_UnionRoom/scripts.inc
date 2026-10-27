Kanto_UnionRoom_MapScripts::
	.byte 0

KantoAR_0_4_UnionRoom_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_0_VIRIDIANFOREST, 22, 34
	goto KantoAR_InspectionFinish
