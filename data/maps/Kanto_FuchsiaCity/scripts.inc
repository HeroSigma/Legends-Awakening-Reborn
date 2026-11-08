Kanto_FuchsiaCity_MapScripts::
	.byte 0

KantoAR_3_7_FuchsiaCity_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_3_8_CINNABARISLAND, 10, 11
	goto KantoAR_InspectionFinish
