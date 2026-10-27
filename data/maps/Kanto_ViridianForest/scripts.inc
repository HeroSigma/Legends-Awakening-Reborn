Kanto_ViridianForest_MapScripts::
	.byte 0

KantoAR_1_0_ViridianForest_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_1_MTMOON_1F, 24, 20
	goto KantoAR_InspectionFinish
