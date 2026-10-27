Kanto_FuchsiaCity_House3_MapScripts::
	.byte 0

KantoAR_11_9_FuchsiaCity_House3_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_12_0_CINNABARISLAND_GYM, 15, 12
	goto KantoAR_InspectionFinish
