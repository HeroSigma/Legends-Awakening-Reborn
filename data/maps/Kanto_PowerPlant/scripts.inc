Kanto_PowerPlant_MapScripts::
	.byte 0

KantoAR_1_95_PowerPlant_Inspect::
	call KantoAR_InspectionPrompt
	warp MAP_KANTOAR_1_96_MTEMBER_RUBYPATH_B4F, 10, 8
	goto KantoAR_InspectionFinish
