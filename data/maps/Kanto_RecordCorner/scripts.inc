Kanto_RecordCorner_MapScripts::
	.byte 0

KantoAR_0_2_RecordCorner_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_0_3_BATTLECOLOSSEUM_4P, 7, 4
	goto KantoAR_InspectionFinish
